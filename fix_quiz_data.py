import json
import re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

print(f'原始题目数: {len(data)}')

# 统计修复前的问题
choice_with_answer = 0
judge_no_options = 0
empty_answer = 0

for q in data:
    if q['type'] == 'A':
        # 检查题干是否包含答案（如（B）、(B)、（b）等）
        if re.search(r'[（(][A-Da-d][）)]', q['q']):
            choice_with_answer += 1
    elif q['type'] == 'B':
        if not q.get('o'):
            judge_no_options += 1
        if not q.get('a') or q['a'].strip() == '':
            empty_answer += 1

print(f'选择题题干包含答案: {choice_with_answer}题')
print(f'判断题无选项: {judge_no_options}题')
print(f'判断题答案为空: {empty_answer}题')

# 修复数据
fixed_choice = 0
fixed_judge = 0

for q in data:
    if q['type'] == 'A':
        # 移除题干中的答案，如（B）、(B)、（b）等
        original_q = q['q']
        # 移除括号中的答案字母
        q['q'] = re.sub(r'[（(]\s*[A-Da-d]\s*[）)]', '', q['q'])
        # 移除多余的空格和换行
        q['q'] = re.sub(r'\s+', ' ', q['q']).strip()
        if original_q != q['q']:
            fixed_choice += 1
        
        # 确保选项存在
        if not q.get('o'):
            q['o'] = {'A': '', 'B': '', 'C': '', 'D': ''}
    
    elif q['type'] == 'B':
        # 为判断题添加选项
        q['o'] = {'正确': '正确', '错误': '错误'}
        fixed_judge += 1
        
        # 标准化答案
        if q.get('a'):
            answer = q['a'].strip()
            if answer in ['对', '正确', '√', 'T', 't', 'true', 'True']:
                q['a'] = '正确'
            elif answer in ['错', '错误', '×', 'F', 'f', 'false', 'False']:
                q['a'] = '错误'

print(f'\n修复选择题题干: {fixed_choice}题')
print(f'修复判断题选项: {fixed_judge}题')

# 验证修复结果
print('\n=== 修复后验证 ===')
choice_questions = [q for q in data if q['type'] == 'A'][:2]
for q in choice_questions:
    print(f"选择题 {q['id']}:")
    print(f"  题干: {q['q'][:100]}")
    print(f"  答案: {q['a']}")
    print(f"  选项: {q.get('o')}")
    print()

judge_questions = [q for q in data if q['type'] == 'B'][:2]
for q in judge_questions:
    print(f"判断题 {q['id']}:")
    print(f"  题干: {q['q'][:100]}")
    print(f"  答案: {q['a']}")
    print(f"  选项: {q.get('o')}")
    print()

# 保存修复后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'\n修复完成，已保存到 quiz_data_final.js')
print(f'总题目数: {len(data)}')
