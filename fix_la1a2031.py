import json, re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

# 1. 修正La1A2031的答案：A -> B
for q in data:
    if q['id'] == 'La1A2031':
        print(f"修正La1A2031: {q['a']} -> B")
        q['a'] = 'B'
        break

# 2. 查看答案为空的2道选择题的详细信息
print("\n=== 答案为空的选择题详细信息 ===")
for q in data:
    if q['type'] == 'A' and (not q.get('a') or q['a'].strip() == ''):
        print(f"\n题目ID: {q['id']}")
        print(f"题目: {q['q']}")
        print(f"选项: {q.get('o', {})}")
        print(f"题干图片: {q.get('q_img', 'none')}")

# 保存修改后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n已保存修改（La1A2031答案修正为B）")
