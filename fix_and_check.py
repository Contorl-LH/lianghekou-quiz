import json
import re
import os

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'总题目数: {len(data)}')

# 1. 检查判断题末尾的（3）或（³）
judge_questions = [q for q in data if q['type'] == 'B']
print(f'\n判断题总数: {len(judge_questions)}')

# 找出末尾有（3）或（³）的判断题
suffix_pattern = re.compile(r'[（(]\s*[3³]\s*[）)]\s*$')
problems = []
for q in judge_questions:
    if suffix_pattern.search(q['q'].strip()):
        problems.append(q)

print(f'末尾有（3）或（³）的判断题: {len(problems)}题')
for q in problems[:10]:
    print(f"  {q['id']}: {q['q'][-50:]}")

# 修复：移除末尾的（3）或（³）
fixed_count = 0
for q in data:
    if q['type'] == 'B':
        original = q['q']
        # 移除末尾的（3）、(3)、（³）、(³)
        q['q'] = suffix_pattern.sub('', q['q'].strip()).strip()
        # 也移除中间可能存在的（3）等
        q['q'] = re.sub(r'[（(]\s*[3³]\s*[）)]', '', q['q'])
        if original != q['q']:
            fixed_count += 1

print(f'\n已修复判断题: {fixed_count}题')

# 2. 复核题干图片对应情况
print('\n=== 题干图片复核 ===')
missing_q_img = []
missing_a_img = []
q_img_not_exist = []
a_img_not_exist = []
mismatch = []

for q in data:
    qid = q['id']
    
    # 检查题干图片字段
    if not q.get('q_img'):
        missing_q_img.append(qid)
    else:
        # 检查图片文件是否存在
        q_img_path = os.path.join(r'C:\temp\deploy', q['q_img'])
        if not os.path.exists(q_img_path):
            q_img_not_exist.append(qid)
    
    # 检查答案图片字段
    if not q.get('a_img'):
        missing_a_img.append(qid)
    else:
        a_img_path = os.path.join(r'C:\temp\deploy', q['a_img'])
        if not os.path.exists(a_img_path):
            a_img_not_exist.append(qid)
    
    # 检查图片文件名是否与题目ID对应
    if q.get('q_img'):
        q_img_filename = os.path.basename(q['q_img'])
        expected_q_img = f"{qid}_q.png"
        if q_img_filename != expected_q_img:
            mismatch.append(f"{qid}: q_img={q_img_filename}, expected={expected_q_img}")
    
    if q.get('a_img'):
        a_img_filename = os.path.basename(q['a_img'])
        expected_a_img = f"{qid}_a.png"
        if a_img_filename != expected_a_img:
            mismatch.append(f"{qid}: a_img={a_img_filename}, expected={expected_a_img}")

print(f'缺少题干图片字段: {len(missing_q_img)}题')
if missing_q_img[:5]:
    print(f'  示例: {missing_q_img[:5]}')

print(f'缺少答案图片字段: {len(missing_a_img)}题')
if missing_a_img[:5]:
    print(f'  示例: {missing_a_img[:5]}')

print(f'题干图片文件不存在: {len(q_img_not_exist)}题')
if q_img_not_exist[:5]:
    print(f'  示例: {q_img_not_exist[:5]}')

print(f'答案图片文件不存在: {len(a_img_not_exist)}题')
if a_img_not_exist[:5]:
    print(f'  示例: {a_img_not_exist[:5]}')

print(f'图片文件名与题目ID不匹配: {len(mismatch)}题')
for m in mismatch[:10]:
    print(f'  {m}')

# 保存修复后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'\n修复完成，已保存到 quiz_data_final.js')

# 验证修复结果
print('\n=== 修复验证 ===')
judge_after = [q for q in data if q['type'] == 'B']
still_has_suffix = [q for q in judge_after if suffix_pattern.search(q['q'].strip())]
print(f'修复后仍有（3）后缀的判断题: {len(still_has_suffix)}题')

# 显示几道修复后的判断题
for q in judge_after[:3]:
    print(f"  {q['id']}: {q['q'][:80]}...")
