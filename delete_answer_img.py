import json
import re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'总题目数: {len(data)}')

# 删除答案图片字段（a_img）
deleted_count = 0
for q in data:
    if 'a_img' in q:
        del q['a_img']
        deleted_count += 1

print(f'已删除答案图片字段: {deleted_count}题')

# 保存修改后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('数据修改完成，已保存到 quiz_data_final.js')

# 验证
print('\n=== 验证 ===')
has_a_img = sum(1 for q in data if 'a_img' in q)
print(f'仍包含a_img字段的题目: {has_a_img}题')
print(f'题目字段示例: {list(data[0].keys())}')
