file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改renderPlanQuestion函数
old_plan_render = '''  document.getElementById('planQid').textContent = q.id;
  const badge = document.getElementById('planTypeBadge');
  badge.textContent = typeNames[q.type] || q.type;
  badge.className = 'type-badge type-' + q.type;

  document.getElementById('planQImg').src = q.q_img;
  document.getElementById('planAImg').src = q.a_img;

  // 选择题选项
  const optsDiv = document.getElementById('planAnswerOptions');
  optsDiv.innerHTML = '';
  if (q.type === 'A' && q.o) {
    Object.keys(q.o).sort().forEach(key => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.opt = key;
      btn.innerHTML = `<span class="opt-letter">${key}</span><span>${q.o[key]}</span>`;
      btn.onclick = () => planSelectOption(key);
      optsDiv.appendChild(btn);
    });
  }'''

new_plan_render = '''  document.getElementById('planQid').textContent = q.id;
  const badge = document.getElementById('planTypeBadge');
  badge.textContent = typeNames[q.type] || q.type;
  badge.className = 'type-badge type-' + q.type;

  // 显示题干文字
  const planQText = document.getElementById('planQuestionText');
  if (planQText) {
    planQText.textContent = q.q || '';
    planQText.style.display = q.q ? 'block' : 'none';
  }

  document.getElementById('planQImg').src = q.q_img;
  document.getElementById('planAImg').src = q.a_img;

  // 显示答案文字
  const planAText = document.getElementById('planAnswerText');
  if (planAText) {
    let answerText = q.a || '';
    if (q.type === 'A' && q.o && q.o[q.a]) {
      answerText = q.a + '. ' + q.o[q.a];
    }
    planAText.textContent = answerText;
    planAText.style.display = answerText ? 'block' : 'none';
  }

  // 选择题和判断题选项
  const optsDiv = document.getElementById('planAnswerOptions');
  optsDiv.innerHTML = '';
  if ((q.type === 'A' || q.type === 'B') && q.o) {
    Object.keys(q.o).sort().forEach(key => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.opt = key;
      if (q.type === 'B') {
        btn.innerHTML = `<span class="opt-letter">${key === '正确' ? '✓' : '✗'}</span><span>${q.o[key]}</span>`;
      } else {
        btn.innerHTML = `<span class="opt-letter">${key}</span><span>${q.o[key]}</span>`;
      }
      btn.onclick = () => planSelectOption(key);
      optsDiv.appendChild(btn);
    });
  }'''

if old_plan_render in content:
    content = content.replace(old_plan_render, new_plan_render)
    print("renderPlanQuestion函数已修改")
else:
    print("找不到renderPlanQuestion函数的代码")
    idx = content.find("document.getElementById('planQid').textContent = q.id;")
    if idx != -1:
        print(f"找到代码在位置: {idx}")
        print(content[idx:idx+500])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
