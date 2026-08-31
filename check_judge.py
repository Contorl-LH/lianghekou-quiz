import json
import re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

# 查找La5B1003
for q in data:
    if q['id'] == 'La5B1003':
        print(f"ID: {q['id']}")
        print(f"题干: {q['q']}")
        print(f"答案: {q['a']}")
        print(f"包含（³）: {'（³）' in q['q']}")
        print(f"包含（3）: {'（3）' in q['q']}")
        break

# 检查所有判断题是否还有（3）或（³）
judge_questions = [q for q in data if q['type'] == 'B']
suffix_pattern = re.compile(r'[（(]\s*[3³]\s*[）)]')
still_has = [q for q in judge_questions if suffix_pattern.search(q['q'])]
print(f"\n仍有（3）或（³）的判断题: {len(still_has)}题")
for q in still_has[:10]:
    print(f"  {q['id']}: {q['q'][-60:]}")

# 检查是否有其他特殊字符
print("\n=== 检查其他特殊字符 ===")
special_chars = ['³', '²', '¹', '⁰', '⁴', '⁵']
for char in special_chars:
    count = sum(1 for q in judge_questions if char in q['q'])
    if count > 0:
        print(f"包含 '{char}' 的判断题: {count}题")
