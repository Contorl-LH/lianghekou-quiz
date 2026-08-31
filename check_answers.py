import json, re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'总题目数: {len(data)}')

# 1. 查找答案为空的选择题
print('\n=== 答案为空的选择题 ===')
for q in data:
    if q['type'] == 'A' and (not q.get('a') or q['a'].strip() == ''):
        print(f"  {q['id']}: {q['q'][:50]}...")

# 2. 查找答案不在A/B/C/D范围内的选择题
print('\n=== 答案不在A/B/C/D范围内的选择题 ===')
for q in data:
    if q['type'] == 'A' and q.get('a', '').strip() not in ['A', 'B', 'C', 'D']:
        print(f"  {q['id']}: 答案='{q.get('a', '')}'")

# 3. 查找答案不在正确/错误范围内的判断题
print('\n=== 答案不在正确/错误范围内的判断题 ===')
for q in data:
    if q['type'] == 'B' and q.get('a', '').strip() not in ['正确', '错误']:
        print(f"  {q['id']}: 答案='{q.get('a', '')}'")

# 4. 查找La1A2031
print('\n=== La1A2031 ===')
for q in data:
    if q['id'] == 'La1A2031':
        print(f"  题目: {q['q']}")
        print(f"  选项: {q.get('o', {})}")
        print(f"  当前答案: {q.get('a', '')}")
