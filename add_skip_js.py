file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在localStorage数据部分添加不考题列表
old_storage = '''// localStorage 数据
let wrongBook = JSON.parse(localStorage.getItem('quiz_wrong_book') || '[]');
let favorites = JSON.parse(localStorage.getItem('quiz_favorites') || '[]');
let doneBook = JSON.parse(localStorage.getItem('quiz_done_book') || '[]');
let planData = JSON.parse(localStorage.getItem('quiz_10day_plan') || 'null');
let quizProgress = JSON.parse(localStorage.getItem('quiz_progress') || 'null');'''

new_storage = '''// localStorage 数据
let wrongBook = JSON.parse(localStorage.getItem('quiz_wrong_book') || '[]');
let favorites = JSON.parse(localStorage.getItem('quiz_favorites') || '[]');
let doneBook = JSON.parse(localStorage.getItem('quiz_done_book') || '[]');
let planData = JSON.parse(localStorage.getItem('quiz_10day_plan') || 'null');
let quizProgress = JSON.parse(localStorage.getItem('quiz_progress') || 'null');
let skipBook = JSON.parse(localStorage.getItem('quiz_skip_book') || '[]');
let skipFilterType = 'all';'''

if old_storage in content:
    content = content.replace(old_storage, new_storage)
    print("localStorage数据部分已添加不考题列表")
else:
    print("找不到localStorage数据部分")

# 在updateBadges函数中添加不考题数量更新
old_badges = '''function updateBadges() {
  document.getElementById('wrongBadge').textContent = wrongBook.length;
  document.getElementById('favBadge').textContent = favorites.length;
  document.getElementById('wrongBadge').style.display = wrongBook.length ? 'inline-block' : 'none';
  document.getElementById('favBadge').style.display = favorites.length ? 'inline-block' : 'none';
}'''

new_badges = '''function updateBadges() {
  document.getElementById('wrongBadge').textContent = wrongBook.length;
  document.getElementById('favBadge').textContent = favorites.length;
  document.getElementById('wrongBadge').style.display = wrongBook.length ? 'inline-block' : 'none';
  document.getElementById('favBadge').style.display = favorites.length ? 'inline-block' : 'none';
  const skipBadge = document.getElementById('skipBadge');
  if (skipBadge) {
    skipBadge.textContent = skipBook.length;
    skipBadge.style.display = skipBook.length ? 'inline-block' : 'none';
  }
}'''

if old_badges in content:
    content = content.replace(old_badges, new_badges)
    print("updateBadges函数已添加不考题数量更新")
else:
    print("找不到updateBadges函数")

# 在switchMode函数中添加不考题模式
old_switch = '''function switchMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(tab => {
    tab.classList.toggle('active', tab.dataset.mode === mode);
  });
  document.getElementById('quizMode').style.display = mode === 'quiz' ? 'block' : 'none';
  document.getElementById('planMode').style.display = mode === 'plan' ? 'block' : 'none';
  document.getElementById('wrongMode').style.display = mode === 'wrong' ? 'block' : 'none';
  document.getElementById('favMode').style.display = mode === 'fav' ? 'block' : 'none';
  
  if (mode === 'wrong') renderWrongList();
  if (mode === 'fav') renderFavList();
  if (mode === 'quiz') { restoreQuizProgress(); }
}'''

new_switch = '''function switchMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(tab => {
    tab.classList.toggle('active', tab.dataset.mode === mode);
  });
  document.getElementById('quizMode').style.display = mode === 'quiz' ? 'block' : 'none';
  document.getElementById('planMode').style.display = mode === 'plan' ? 'block' : 'none';
  document.getElementById('wrongMode').style.display = mode === 'wrong' ? 'block' : 'none';
  document.getElementById('favMode').style.display = mode === 'fav' ? 'block' : 'none';
  const skipMode = document.getElementById('skipMode');
  if (skipMode) skipMode.style.display = mode === 'skip' ? 'block' : 'none';
  
  if (mode === 'wrong') renderWrongList();
  if (mode === 'fav') renderFavList();
  if (mode === 'skip') renderSkipList();
  if (mode === 'quiz') { restoreQuizProgress(); }
}'''

if old_switch in content:
    content = content.replace(old_switch, new_switch)
    print("switchMode函数已添加不考题模式")
else:
    print("找不到switchMode函数")

# 在</script>之前添加不考题相关的函数
skip_functions = '''
// ============ 不考题功能 ============
function saveSkip() {
  localStorage.setItem('quiz_skip_book', JSON.stringify(skipBook));
  updateBadges();
}

function toggleSkipMark() {
  const q = filteredQuestions[currentIndex];
  const idx = skipBook.indexOf(q.id);
  if (idx > -1) {
    skipBook.splice(idx, 1);
  } else {
    skipBook.push(q.id);
  }
  saveSkip();
  updateSkipButton();
  // 如果标记为不考题，自动跳转到下一题
  if (idx === -1 && currentIndex < filteredQuestions.length - 1) {
    setTimeout(() => nextQuestion(), 300);
  }
}

function updateSkipButton() {
  const q = filteredQuestions[currentIndex];
  const btn = document.getElementById('skipBtn');
  if (btn) {
    const isSkipped = skipBook.includes(q.id);
    btn.textContent = isSkipped ? '✅ 恢复考题' : '🚫 不考题';
    btn.style.background = isSkipped ? 'linear-gradient(135deg,#48bb78,#38a169)' : 'linear-gradient(135deg,#ed8936,#dd6b20)';
  }
}

function isSkipped(qid) {
  return skipBook.includes(qid);
}

function renderSkipList() {
  const list = document.getElementById('skipList');
  if (!list) return;
  let skipped = allQuestions.filter(q => skipBook.includes(q.id));
  if (skipFilterType !== 'all') {
    skipped = skipped.filter(q => q.type === skipFilterType);
  }
  if (skipped.length === 0) {
    list.innerHTML = '<div class="empty-state">暂无不考题</div>';
    return;
  }
  list.innerHTML = skipped.map(q => `
    <div class="list-item" onclick="jumpToQuestion('${q.id}')">
      <span class="list-qid">${q.id}</span>
      <span class="list-type type-${q.type}">${typeNames[q.type]}</span>
      <span class="list-text">${q.q.substring(0, 60)}...</span>
      <button class="action-btn skip-mark" onclick="event.stopPropagation();restoreSkipQuestion('${q.id}')">恢复</button>
    </div>
  `).join('');
}

function setSkipFilter(type) {
  skipFilterType = type;
  document.querySelectorAll('#skipMode .type-filter-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.type === type);
  });
  renderSkipList();
}

function restoreSkipQuestion(qid) {
  const idx = skipBook.indexOf(qid);
  if (idx > -1) {
    skipBook.splice(idx, 1);
    saveSkip();
    renderSkipList();
  }
}

function clearAllSkipConfirm() {
  if (confirm('确定要清空所有不考题吗？')) {
    skipBook = [];
    saveSkip();
    renderSkipList();
  }
}

function jumpToQuestion(qid) {
  const idx = allQuestions.findIndex(q => q.id === qid);
  if (idx > -1) {
    // 先从skip中恢复
    const skipIdx = skipBook.indexOf(qid);
    if (skipIdx > -1) {
      skipBook.splice(skipIdx, 1);
      saveSkip();
    }
    currentIndex = idx;
    switchMode('quiz');
    renderQuestion();
  }
}
'''

# 在</script>之前插入
old_script_end = '\n</script>'
if old_script_end in content:
    # 找到最后一个</script>
    last_idx = content.rfind('</script>')
    content = content[:last_idx] + skip_functions + '\n' + content[last_idx:]
    print("不考题相关函数已添加")
else:
    print("找不到</script>结束标签")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JavaScript修改完成")
