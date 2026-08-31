import json
import re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'总题目数: {len(data)}')

# 检查判断题答案
judge_questions = [q for q in data if q['type'] == 'B']
print(f'\n判断题总数: {len(judge_questions)}')

# 统计答案分布
answer_counts = {}
for q in judge_questions:
    ans = q.get('a', '').strip()
    answer_counts[ans] = answer_counts.get(ans, 0) + 1

print('\n=== 判断题答案分布 ===')
for ans, count in sorted(answer_counts.items(), key=lambda x: -x[1]):
    print(f"  '{ans}': {count}题")

# 检查答案为空或非标准化的题目
empty_answer = [q for q in judge_questions if not q.get('a') or q['a'].strip() == '']
non_standard = [q for q in judge_questions if q.get('a', '').strip() not in ['正确', '错误']]

print(f'\n答案为空: {len(empty_answer)}题')
print(f'答案非标准化: {len(non_standard)}题')

# 检查是否有"讲解"字段
has_explain = sum(1 for q in data if q.get('explain') or q.get('explanation') or q.get('analysis'))
print(f'\n已有讲解字段的题目: {has_explain}题')

# 为所有题目添加"讲解"字段（如果没有）
added_count = 0
for q in data:
    if not q.get('explain'):
        q['explain'] = ''
        added_count += 1

print(f'已添加讲解字段: {added_count}题')

# 为判断题生成简单的讲解模板
# 对于答案为"正确"的题目，讲解为"该说法正确。"
# 对于答案为"错误"的题目，讲解为"该说法错误。"
generated_count = 0
for q in judge_questions:
    if not q.get('explain') or q['explain'].strip() == '':
        ans = q.get('a', '').strip()
        if ans == '正确':
            q['explain'] = '该说法正确。'
            generated_count += 1
        elif ans == '错误':
            q['explain'] = '该说法错误。'
            generated_count += 1

print(f'已生成判断题讲解: {generated_count}题')

# 保存修复后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'\n修复完成，已保存到 quiz_data_final.js')

# 验证
print('\n=== 验证 ===')
judge_after = [q for q in data if q['type'] == 'B']
empty_after = [q for q in judge_after if not q.get('a') or q['a'].strip() == '']
has_explain_after = sum(1 for q in data if q.get('explain'))
print(f'判断题总数: {len(judge_after)}')
print(f'答案为空: {len(empty_after)}')
print(f'有讲解字段: {has_explain_after}')

# 显示几道题的示例
print('\n=== 示例 ===')
for q in judge_after[:3]:
    print(f"{q['id']}:")
    print(f"  题干: {q['q'][:60]}...")
    print(f"  答案: {q['a']}")
    print(f"  讲解: {q.get('explain', '无')}")
    print()
