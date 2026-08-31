file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 为.list-mode添加默认样式display: none，与.plan-mode一致
old_css = '''  /* 隐藏类 */
  .hidden { display: none !important; }
  .list-mode.hidden { display: none !important; }
  .list-mode.active { display: block; }
  .plan-mode { display: none; }
  .plan-mode.active { display: block; }'''

new_css = '''  /* 隐藏类 */
  .hidden { display: none !important; }
  .list-mode { display: none; }
  .list-mode.hidden { display: none !important; }
  .list-mode.active { display: block; }
  .plan-mode { display: none; }
  .plan-mode.active { display: block; }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("CSS样式已修复，为.list-mode添加默认display: none")
else:
    print("找不到CSS样式")

# 2. 修改switchMode函数，统一所有窗口的显示控制
old_switch = '''function switchMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.toggle('active', t.dataset.mode === mode));
  document.getElementById('quizMode').classList.toggle('hidden', mode !== 'quiz');
  document.getElementById('planMode').classList.toggle('active', mode === 'plan');
  document.getElementById('wrongMode').classList.toggle('active', mode === 'wrong');
  document.getElementById('favMode').classList.toggle('active', mode === 'fav');
  const skipMode = document.getElementById('skipMode');
  if (skipMode) {
    skipMode.classList.toggle('active', mode === 'skip');
    skipMode.style.display = mode === 'skip' ? 'block' : 'none';
  }

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

new_switch = '''function switchMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.toggle('active', t.dataset.mode === mode));

  // 统一控制所有窗口的显示
  const quizMode = document.getElementById('quizMode');
  const planMode = document.getElementById('planMode');
  const wrongMode = document.getElementById('wrongMode');
  const favMode = document.getElementById('favMode');
  const skipMode = document.getElementById('skipMode');

  // quizMode使用hidden类控制
  if (quizMode) quizMode.classList.toggle('hidden', mode !== 'quiz');

  // 其他模式使用active类控制（默认display:none，有active才显示）
  if (planMode) planMode.classList.toggle('active', mode === 'plan');
  if (wrongMode) wrongMode.classList.toggle('active', mode === 'wrong');
  if (favMode) favMode.classList.toggle('active', mode === 'fav');
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
    print("switchMode函数已修复，统一所有窗口的显示控制")
else:
    print("找不到switchMode函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
