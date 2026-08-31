import json, re

with open(r'C:\temp\deploy\quiz_data_final.js', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'window\.QUIZ_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

# 修复Lb1A5117
for q in data:
    if q['id'] == 'Lb1A5117':
        print(f"修复Lb1A5117:")
        print(f"  原选项: {q.get('o', {})}")
        print(f"  原答案: {q.get('a', '')}")
        q['o'] = {
            'A': 'U1＞U2，I1＞I2',
            'B': 'U1＞U2，I1＜I2',
            'C': 'U1＜U2，I1＞I2',
            'D': 'U1＜U2，I1＜I2'
        }
        q['a'] = 'D'
        print(f"  新选项: {q['o']}")
        print(f"  新答案: {q['a']}")
        break

# 修复E_La3A5044
for q in data:
    if q['id'] == 'E_La3A5044':
        print(f"\n修复E_La3A5044:")
        print(f"  原题目: {q['q']}")
        print(f"  原选项: {q.get('o', {})}")
        print(f"  原答案: {q.get('a', '')}")
        q['q'] = '一个电容器C和一个电容量为2μF的电容器串联后，总电容量为电容器C的电容量1/3，那么电容器C的电容量是多少μF？'
        q['o'] = {
            'A': '3',
            'B': '4',
            'C': '6',
            'D': '8'
        }
        q['a'] = 'B'
        print(f"  新题目: {q['q']}")
        print(f"  新选项: {q['o']}")
        print(f"  新答案: {q['a']}")
        break

# 保存修改后的数据
new_content = 'window.QUIZ_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
with open(r'C:\temp\deploy\quiz_data_final.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n数据异常题目已修复")
