file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改switchMode函数，添加不考题模式
old_switch = '''function switchMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.toggle('active', t.dataset.mode === mode));
  document.getElementById('quizMode').classList.toggle('hidden', mode !== 'quiz');
  document.getElementById('planMode').classList.toggle('active', mode === 'plan');
  document.getElementById('wrongMode').classList.toggle('active', mode === 'wrong');
  document.getElementById('favMode').classList.toggle('active', mode === 'fav');

  const showBottomNav = (mode === 'quiz' || (mode === 'plan' && document.getElementById('planQuiz').style.display === 'block'));
  document.getElementById('bottomNav').style.display = showBottomNav ? 'flex' : 'none';
  document.querySelector('.toolbar-toggle').style.display = mode === 'quiz' ? 'flex' : 'none';
  document.getElementById('toolbar').classList.remove('open');
  document.querySelector('.toolbar-toggle').classList.remove('open');

  if (mode === 'plan') {
    document.getElementById('planOverview').style.display = 'block';
    document.getElementById('planQuiz').style.display = 'none';
    renderPlanOverview();
  }
  if (mode === 'wrong') {
    const trainMode = document.getElementById('wrongTrainMode');
    const listMode = document.getElementById('wrongListMode');
    if (trainMode) trainMode.style.display = 'none';
    if (listMode) listMode.style.display = 'block';
    renderWrongList();
  }
  if (mode === 'fav') renderFavList();
}'''

new_switch = '''function switchMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.toggle('active', t.dataset.mode === mode));
  document.getElementById('quizMode').classList.toggle('hidden', mode !== 'quiz');
  document.getElementById('planMode').classList.toggle('active', mode === 'plan');
  document.getElementById('wrongMode').classList.toggle('active', mode === 'wrong');
  document.getElementById('favMode').classList.toggle('active', mode === 'fav');
  const skipMode = document.getElementById('skipMode');
  if (skipMode) skipMode.classList.toggle('active', mode === 'skip');

  const showBottomNav = (mode === 'quiz' || (mode === 'plan' && document.getElementById('planQuiz').style.display === 'block'));
  document.getElementById('bottomNav').style.display = showBottomNav ? 'flex' : 'none';
  document.querySelector('.toolbar-toggle').style.display = mode === 'quiz' ? 'flex' : 'none';
  document.getElementById('toolbar').classList.remove('open');
  document.querySelector('.toolbar-toggle').classList.remove('open');

  if (mode === 'plan') {
    document.getElementById('planOverview').style.display = 'block';
    document.getElementById('planQuiz').style.display = 'none';
    renderPlanOverview();
  }
  if (mode === 'wrong') {
    const trainMode = document.getElementById('wrongTrainMode');
    const listMode = document.getElementById('wrongListMode');
    if (trainMode) trainMode.style.display = 'none';
    if (listMode) listMode.style.display = 'block';
    renderWrongList();
  }
  if (mode === 'fav') renderFavList();
  if (mode === 'skip') renderSkipList();
}'''

if old_switch in content:
    content = content.replace(old_switch, new_switch)
    print("switchMode函数已修改，添加不考题模式")
else:
    print("找不到switchMode函数")

# 修改筛选逻辑，排除不考题
old_filter = '''let filteredQuestions = [...allQuestions];'''

new_filter = '''let filteredQuestions = allQuestions.filter(q => !skipBook.includes(q.id));'''

if old_filter in content:
    content = content.replace(old_filter, new_filter)
    print("筛选逻辑已修改，排除不考题")
else:
    print("找不到筛选逻辑")

# 在renderQuestion函数中调用updateSkipButton()
old_render_end = '''  document.getElementById('prevBtn').disabled = currentIndex === 0;
  document.getElementById('nextBtn').disabled = currentIndex === filteredQuestions.length - 1;

  const progress = ((currentIndex + 1) / filteredQuestions.length) * 100;
  document.getElementById('progressFill').style.width = progress + '%';
  saveQuizProgress(); // 保存当前做题位置
}'''

new_render_end = '''  document.getElementById('prevBtn').disabled = currentIndex === 0;
  document.getElementById('nextBtn').disabled = currentIndex === filteredQuestions.length - 1;

  const progress = ((currentIndex + 1) / filteredQuestions.length) * 100;
  document.getElementById('progressFill').style.width = progress + '%';
  saveQuizProgress(); // 保存当前做题位置
  updateSkipButton(); // 更新不考题按钮状态
}'''

if old_render_end in content:
    content = content.replace(old_render_end, new_render_end)
    print("renderQuestion函数已添加updateSkipButton调用")
else:
    print("找不到renderQuestion函数结束位置")

# 添加不考题按钮的CSS样式
old_css = '''  .action-btn.wrong-mark {
    background: linear-gradient(135deg, #fc8181, #f56565);
  }'''

new_css = '''  .action-btn.wrong-mark {
    background: linear-gradient(135deg, #fc8181, #f56565);
  }
  .action-btn.skip-mark {
    background: linear-gradient(135deg, #ed8936, #dd6b20);
    color: white;
  }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("不考题按钮CSS样式已添加")
else:
    print("找不到wrong-mark CSS样式")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JavaScript和CSS修改完成")
