file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改renderQuestion函数，添加讲解内容的设置
old_render = '''  // 显示答案文字
  const aText = document.getElementById('answerText');
  if (aText) {
    let answerText = q.a || '';
    // 如果是选择题，显示选项内容
    if (q.type === 'A' && q.o && q.o[q.a]) {
      answerText = q.a + '. ' + q.o[q.a];
    }
    aText.textContent = answerText;
    aText.style.display = answerText ? 'block' : 'none';
  }'''

new_render = '''  // 显示答案文字
  const aText = document.getElementById('answerText');
  if (aText) {
    let answerText = q.a || '';
    // 如果是选择题，显示选项内容
    if (q.type === 'A' && q.o && q.o[q.a]) {
      answerText = q.a + '. ' + q.o[q.a];
    }
    aText.textContent = answerText;
    aText.style.display = answerText ? 'block' : 'none';
  }

  // 显示题目讲解
  const expText = document.getElementById('explanationText');
  const expSection = document.getElementById('explanationSection');
  if (expText && expSection) {
    const explain = q.explain || q.explanation || q.analysis || '';
    expText.textContent = explain;
    expSection.style.display = explain ? 'block' : 'none';
  }'''

if old_render in content:
    content = content.replace(old_render, new_render)
    print("renderQuestion函数已添加讲解设置")
else:
    print("找不到renderQuestion函数的代码")

# 修改renderPlanQuestion函数，添加讲解内容的设置
old_plan_render = '''  // 显示答案文字
  const planAText = document.getElementById('planAnswerText');
  if (planAText) {
    let answerText = q.a || '';
    if (q.type === 'A' && q.o && q.o[q.a]) {
      answerText = q.a + '. ' + q.o[q.a];
    }
    planAText.textContent = answerText;
    planAText.style.display = answerText ? 'block' : 'none';
  }'''

new_plan_render = '''  // 显示答案文字
  const planAText = document.getElementById('planAnswerText');
  if (planAText) {
    let answerText = q.a || '';
    if (q.type === 'A' && q.o && q.o[q.a]) {
      answerText = q.a + '. ' + q.o[q.a];
    }
    planAText.textContent = answerText;
    planAText.style.display = answerText ? 'block' : 'none';
  }

  // 显示题目讲解
  const planExpText = document.getElementById('planExplanationText');
  const planExpSection = document.getElementById('planExplanationSection');
  if (planExpText && planExpSection) {
    const explain = q.explain || q.explanation || q.analysis || '';
    planExpText.textContent = explain;
    planExpSection.style.display = explain ? 'block' : 'none';
  }'''

if old_plan_render in content:
    content = content.replace(old_plan_render, new_plan_render)
    print("renderPlanQuestion函数已添加讲解设置")
else:
    print("找不到renderPlanQuestion函数的代码")

# 添加讲解的CSS样式
old_css = '''  /* 答案图片组 */
  .answer-image-group {'''

new_css = '''  /* 题目讲解 */
  .explanation-section {
    margin-top: 12px;
    margin-bottom: 12px;
    padding: 12px 14px;
    background: linear-gradient(135deg, #fffbeb, #fef3c7);
    border-radius: 10px;
    border-left: 4px solid #f59e0b;
  }
  .explanation-label {
    display: inline-block;
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 8px;
  }
  .explanation-text {
    font-size: 14px;
    line-height: 1.8;
    color: #78350f;
    white-space: pre-wrap;
    word-break: break-word;
  }

  /* 答案图片组 */
  .answer-image-group {'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("讲解CSS样式已添加")
else:
    print("找不到答案图片组CSS样式")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
