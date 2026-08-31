import json
import re
import os

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'总题目数: {len(data)}')

# 检查选择题
choice_questions = [q for q in data if q['type'] == 'A']
print(f'\n选择题总数: {len(choice_questions)}')

# 统计选项情况
no_options = []
empty_options = []
abnormal_options = []
missing_image = []
answer_not_in_options = []

for q in choice_questions:
    qid = q['id']
    options = q.get('o')
    
    # 检查是否有选项
    if not options:
        no_options.append(qid)
        continue
    
    # 检查选项是否为空
    option_values = [v.strip() for v in options.values() if v.strip()]
    if len(option_values) == 0:
        empty_options.append(qid)
    
    # 检查选项数量是否正常（应该是4个）
    if len(options) != 4:
        abnormal_options.append((qid, len(options)))
    
    # 检查答案是否在选项中
    answer = q.get('a', '').strip()
    if answer and answer not in options:
        answer_not_in_options.append((qid, answer, list(options.keys())))
    
    # 检查题干图片是否存在
    q_img = q.get('q_img', '')
    if q_img:
        q_img_path = os.path.join(r'C:\temp\deploy', q_img)
        if not os.path.exists(q_img_path):
            missing_image.append(qid)
    else:
        missing_image.append(qid)

print(f'\n=== 选择题选项统计 ===')
print(f'无选项: {len(no_options)}题')
if no_options[:5]:
    print(f'  示例: {no_options[:5]}')

print(f'选项内容全为空: {len(empty_options)}题')
if empty_options[:5]:
    print(f'  示例: {empty_options[:5]}')

print(f'选项数量异常（非4个）: {len(abnormal_options)}题')
for qid, count in abnormal_options[:10]:
    print(f'  {qid}: {count}个选项')

print(f'答案不在选项中: {len(answer_not_in_options)}题')
for qid, answer, keys in answer_not_in_options[:10]:
    print(f'  {qid}: 答案={answer}, 选项键={keys}')

print(f'题干图片缺失: {len(missing_image)}题')
if missing_image[:5]:
    print(f'  示例: {missing_image[:5]}')

# 检查选项内容是否包含图片引用或异常字符
print(f'\n=== 选项内容异常检查 ===')
suspicious_options = []
for q in choice_questions:
    options = q.get('o', {})
    for key, value in options.items():
        # 检查选项是否包含换行符（可能是图片说明）
        if '\n' in value or '图' in value or '如图' in value:
            suspicious_options.append((q['id'], key, value[:80]))
            break

print(f'选项包含图片引用或换行: {len(suspicious_options)}题')
for qid, key, value in suspicious_options[:10]:
    print(f'  {qid} 选项{key}: {value}')

# 显示几道题的完整信息供复核
print(f'\n=== 待复核题目示例 ===')
check_ids = []
if no_options:
    check_ids.extend(no_options[:3])
if abnormal_options:
    check_ids.extend([x[0] for x in abnormal_options[:3]])
if answer_not_in_options:
    check_ids.extend([x[0] for x in answer_not_in_options[:3]])

for qid in list(set(check_ids))[:6]:
    for q in data:
        if q['id'] == qid:
            print(f"\n{qid}:")
            print(f"  题干: {q['q'][:80]}...")
            print(f"  答案: {q['a']}")
            print(f"  选项: {q.get('o', {})}")
            print(f"  题干图片: {q.get('q_img', '无')}")
            break
