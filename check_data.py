import json
import re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 提取JSON数组
match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
if match:
    data = json.loads(match.group(1))
else:
    # 尝试找到第一个[和最后一个]
    start = content.find('[')
    end = content.rfind(']') + 1
    data = json.loads(content[start:end])

print(f'总题目数: {len(data)}')

# 查看选择题示例
choice_questions = [q for q in data if q['type'] == 'A'][:2]
print('\n=== 选择题示例 ===')
for q in choice_questions:
    print(f"ID: {q['id']}")
    print(f"题干: {q['q'][:150]}")
    print(f"答案: {q.get('a', '无')[:150]}")
    print(f"选项: {q.get('options', '无')}")
    print(f"图片: {q.get('img', '无')}")
    print()

# 查看判断题示例
judge_questions = [q for q in data if q['type'] == 'B'][:3]
print('=== 判断题示例 ===')
for q in judge_questions:
    print(f"ID: {q['id']}")
    print(f"题干: {q['q'][:150]}")
    print(f"答案: {q.get('a', '无')[:150]}")
    print(f"选项: {q.get('options', '无')}")
    print(f"图片: {q.get('img', '无')}")
    print()

# 统计各题型数量
type_counts = {}
for q in data:
    t = q['type']
    type_counts[t] = type_counts.get(t, 0) + 1
print('=== 题型统计 ===')
for t, c in type_counts.items():
    print(f"{t}: {c}题")
