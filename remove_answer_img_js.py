file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改renderQuestion函数，移除设置aImg.src的代码
old_render = '''  // 答案部分的题干图片
  const qImg = document.getElementById('qImg');
  qImg.src = q.q_img;
  qImg.classList.remove('zoomed');
  qImg.style.display = 'block';

  // 题干部分的条件显示图片（仅对选项不完整的题目显示）
  const qImgInline = document.getElementById('qImgInline');'''

new_render = '''  // 答案部分的题干图片
  const qImg = document.getElementById('qImg');
  qImg.src = q.q_img;
  qImg.classList.remove('zoomed');
  qImg.style.display = 'block';

  // 题干部分的条件显示图片（仅对选项不完整的题目显示）
  const qImgInline = document.getElementById('qImgInline');'''

# 实际上上面的代码没有aImg，让我查找包含aImg的代码
old_a_img = '''  const aImg = document.getElementById('aImg');
  aImg.src = q.a_img;
  aImg.classList.remove('zoomed');'''

if old_a_img in content:
    content = content.replace(old_a_img, '')
    print("renderQuestion函数中的aImg代码已移除")
else:
    print("找不到renderQuestion函数中的aImg代码")
    # 查找包含aImg的代码
    idx = content.find("document.getElementById('aImg')")
    if idx != -1:
        print(f"找到aImg在位置: {idx}")
        print(content[idx-50:idx+200])

# 修改renderPlanQuestion函数，移除设置planAImg.src的代码
old_plan_a_img = '''  // 答案部分的题干图片和答案图片
  document.getElementById('planQImg').src = q.q_img;
  document.getElementById('planAImg').src = q.a_img;'''

new_plan_a_img = '''  // 答案部分的题干图片
  document.getElementById('planQImg').src = q.q_img;'''

if old_plan_a_img in content:
    content = content.replace(old_plan_a_img, new_plan_a_img)
    print("renderPlanQuestion函数中的planAImg代码已移除")
else:
    print("找不到renderPlanQuestion函数中的planAImg代码")
    idx = content.find("planAImg")
    if idx != -1:
        print(f"找到planAImg在位置: {idx}")
        print(content[idx-50:idx+200])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JavaScript修改完成")
