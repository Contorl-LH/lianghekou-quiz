file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改renderQuestion函数，添加题干文字和答案文字的显示
old_render = '''  document.getElementById('qid').textContent = q.id;
  const badge = document.getElementById('typeBadge');
  badge.textContent = typeNames[q.type] || q.type;
  badge.className = 'type-badge type-' + q.type;

  const qImg = document.getElementById('qImg');
  qImg.src = q.q_img;
  qImg.classList.remove('zoomed');
  qImg.style.display = 'block';

  const aImg = document.getElementById('aImg');
  aImg.src = q.a_img;
  aImg.classList.remove('zoomed');'''

new_render = '''  document.getElementById('qid').textContent = q.id;
  const badge = document.getElementById('typeBadge');
  badge.textContent = typeNames[q.type] || q.type;
  badge.className = 'type-badge type-' + q.type;

  // 显示题干文字
  const qText = document.getElementById('questionText');
  if (qText) {
    qText.textContent = q.q || '';
    qText.style.display = q.q ? 'block' : 'none';
  }

  const qImg = document.getElementById('qImg');
  qImg.src = q.q_img;
  qImg.classList.remove('zoomed');
  qImg.style.display = 'block';

  const aImg = document.getElementById('aImg');
  aImg.src = q.a_img;
  aImg.classList.remove('zoomed');

  // 显示答案文字
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

if old_render in content:
    content = content.replace(old_render, new_render)
    print("renderQuestion函数已修改，添加了题干文字和答案文字显示")
else:
    print("找不到renderQuestion函数的代码")
    idx = content.find("document.getElementById('qid').textContent = q.id;")
    if idx != -1:
        print(f"找到代码在位置: {idx}")
        print(content[idx:idx+400])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
