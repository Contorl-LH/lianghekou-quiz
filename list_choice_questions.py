import json, re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

# 获取所有选择题
choice_questions = [q for q in data if q['type'] == 'A']
print(f"选择题总数: {len(choice_questions)}")

# 输出前100道选择题的ID和答案，用于核对
print("\n=== 前100道选择题 ===")
for i, q in enumerate(choice_questions[:100]):
    print(f"{i+1}. {q['id']}: 答案={q.get('a', '空')}, 图片={q.get('q_img', 'none')}")
