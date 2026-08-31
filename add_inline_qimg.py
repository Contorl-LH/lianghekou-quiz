file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改普通答题部分的HTML，在题干部分添加条件显示的图片
old_question = '''      <div class="card-body">
        <div class="question-text" id="questionText"></div>
        <div class="answer-options" id="answerOptions"></div>'''

new_question = '''      <div class="card-body">
        <div class="question-text" id="questionText"></div>
        <img id="qImgInline" src="" alt="题干" onclick="toggleZoom(this)" style="display:none;margin-bottom:16px;border-radius:10px;max-width:100%;cursor:pointer;">
        <div class="answer-options" id="answerOptions"></div>'''

if old_question in content:
    content = content.replace(old_question, new_question)
    print("普通答题部分HTML已添加条件显示图片")
else:
    print("找不到普通答题部分HTML")

# 修改renderQuestion函数，添加条件显示题干图片的逻辑
old_render = '''  // 显示题干文字
  const qText = document.getElementById('questionText');
  if (qText) {
    qText.textContent = q.q || '';
    qText.style.display = q.q ? 'block' : 'none';
  }

  const qImg = document.getElementById('qImg');
  qImg.src = q.q_img;
  qImg.classList.remove('zoomed');
  qImg.style.display = 'block';'''

new_render = '''  // 显示题干文字
  const qText = document.getElementById('questionText');
  if (qText) {
    qText.textContent = q.q || '';
    qText.style.display = q.q ? 'block' : 'none';
  }

  // 答案部分的题干图片
  const qImg = document.getElementById('qImg');
  qImg.src = q.q_img;
  qImg.classList.remove('zoomed');
  qImg.style.display = 'block';

  // 题干部分的条件显示图片（仅对选项不完整的题目显示）
  const qImgInline = document.getElementById('qImgInline');
  if (qImgInline) {
    if (q.show_q_img_in_question) {
      qImgInline.src = q.q_img;
      qImgInline.style.display = 'block';
    } else {
      qImgInline.style.display = 'none';
    }
  }'''

if old_render in content:
    content = content.replace(old_render, new_render)
    print("renderQuestion函数已添加条件显示图片逻辑")
else:
    print("找不到renderQuestion函数的代码")

# 修改计划答题部分的HTML，在题干部分添加条件显示的图片
old_plan_question = '''        <div class="card-body">
          <div class="question-text" id="planQuestionText"></div>
          <div class="answer-options" id="planAnswerOptions"></div>'''

new_plan_question = '''        <div class="card-body">
          <div class="question-text" id="planQuestionText"></div>
          <img id="planQImgInline" src="" alt="题干" onclick="toggleZoom(this)" style="display:none;margin-bottom:16px;border-radius:10px;max-width:100%;cursor:pointer;">
          <div class="answer-options" id="planAnswerOptions"></div>'''

if old_plan_question in content:
    content = content.replace(old_plan_question, new_plan_question)
    print("计划答题部分HTML已添加条件显示图片")
else:
    print("找不到计划答题部分HTML")

# 修改renderPlanQuestion函数，添加条件显示题干图片的逻辑
old_plan_render = '''  // 显示题干文字
  const planQText = document.getElementById('planQuestionText');
  if (planQText) {
    planQText.textContent = q.q || '';
    planQText.style.display = q.q ? 'block' : 'none';
  }

  document.getElementById('planQImg').src = q.q_img;
  document.getElementById('planAImg').src = q.a_img;'''

new_plan_render = '''  // 显示题干文字
  const planQText = document.getElementById('planQuestionText');
  if (planQText) {
    planQText.textContent = q.q || '';
    planQText.style.display = q.q ? 'block' : 'none';
  }

  // 答案部分的题干图片和答案图片
  document.getElementById('planQImg').src = q.q_img;
  document.getElementById('planAImg').src = q.a_img;

  // 题干部分的条件显示图片（仅对选项不完整的题目显示）
  const planQImgInline = document.getElementById('planQImgInline');
  if (planQImgInline) {
    if (q.show_q_img_in_question) {
      planQImgInline.src = q.q_img;
      planQImgInline.style.display = 'block';
    } else {
      planQImgInline.style.display = 'none';
    }
  }'''

if old_plan_render in content:
    content = content.replace(old_plan_render, new_plan_render)
    print("renderPlanQuestion函数已添加条件显示图片逻辑")
else:
    print("找不到renderPlanQuestion函数的代码")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
