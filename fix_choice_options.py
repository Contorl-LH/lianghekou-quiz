import json
import re
import os

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'总题目数: {len(data)}')

# 修复选择题选项
choice_questions = [q for q in data if q['type'] == 'A']
print(f'选择题总数: {len(choice_questions)}')

fixed_format = 0
fixed_incomplete = 0
need_image_in_question = []

for q in choice_questions:
    qid = q['id']
    options = q.get('o', {})
    
    if not options:
        need_image_in_question.append(qid)
        continue
    
    # 1. 修复选项格式：移除换行符、多余空格、清理内容
    new_options = {}
    for key, value in options.items():
        # 移除换行符，替换为空格
        cleaned = re.sub(r'\s+', ' ', str(value)).strip()
        # 移除开头的句号或点号
        cleaned = re.sub(r'^[。.、，,]+', '', cleaned).strip()
        # 移除结尾的"图X-X"等图片引用
        cleaned = re.sub(r'图[A-Z]-\d+.*$', '', cleaned).strip()
        new_options[key] = cleaned
    
    q['o'] = new_options
    
    # 检查是否有变化
    if new_options != options:
        fixed_format += 1
    
    # 2. 检查选项是否完整（4个选项，且内容不为空）
    valid_options = {k: v for k, v in new_options.items() if v and len(v) > 1}
    if len(valid_options) < 4:
        need_image_in_question.append(qid)
        fixed_incomplete += 1

print(f'\n修复选项格式: {fixed_format}题')
print(f'选项不完整（需要题干显示图片）: {len(need_image_in_question)}题')
print(f'  示例: {need_image_in_question[:10]}')

# 3. 为选项不完整的题目添加标记，在题干部分显示图片
for q in data:
    if q['id'] in need_image_in_question:
        q['show_q_img_in_question'] = True
    else:
        q['show_q_img_in_question'] = False

# 4. 修复答案不在选项中的问题
for q in choice_questions:
    answer = q.get('a', '').strip()
    options = q.get('o', {})
    if answer and answer not in options and options:
        # 如果答案不在选项中，尝试从选项中找到最接近的
        # 或者添加答案到选项中
        if answer not in options:
            options[answer] = options.get(answer, '')
            q['o'] = dict(sorted(options.items()))

# 保存修复后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'\n修复完成，已保存到 quiz_data_final.js')

# 验证
print('\n=== 验证 ===')
choice_after = [q for q in data if q['type'] == 'A']
incomplete_after = [q for q in choice_after if len({k:v for k,v in q.get('o',{}).items() if v and len(v)>1}) < 4]
show_img = [q for q in choice_after if q.get('show_q_img_in_question')]
print(f'选择题总数: {len(choice_after)}')
print(f'选项不完整: {len(incomplete_after)}题')
print(f'题干显示图片标记: {len(show_img)}题')

# 显示几道修复后的题目
print('\n=== 修复后示例 ===')
for qid in ['La5A1002', 'E_La5A1002', 'Lb1A2106', 'E_Lb4A1095']:
    for q in data:
        if q['id'] == qid:
            print(f"\n{qid}:")
            print(f"  题干: {q['q'][:60]}...")
            print(f"  答案: {q['a']}")
            print(f"  选项: {q.get('o', {})}")
            print(f"  题干显示图片: {q.get('show_q_img_in_question', False)}")
            break
