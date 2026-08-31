file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在10天计划的操作按钮区域添加"不考题"按钮
old_plan_actions = '''          <div class="action-row">
            <button class="action-btn done-mark" id="planDoneBtn" onclick="togglePlanDone()">✅ 标记已做</button>
            <button class="action-btn fav" id="planFavBtn" onclick="togglePlanFavorite()">⭐ 收藏</button>
            <button class="action-btn wrong-mark" id="planWrongBtn" onclick="togglePlanWrongMark()">❌ 标记错题</button>
          </div>'''

new_plan_actions = '''          <div class="action-row">
            <button class="action-btn done-mark" id="planDoneBtn" onclick="togglePlanDone()">✅ 标记已做</button>
            <button class="action-btn fav" id="planFavBtn" onclick="togglePlanFavorite()">⭐ 收藏</button>
            <button class="action-btn wrong-mark" id="planWrongBtn" onclick="togglePlanWrongMark()">❌ 标记错题</button>
            <button class="action-btn skip-mark" id="planSkipBtn" onclick="togglePlanSkipMark()">🚫 不考题</button>
          </div>'''

if old_plan_actions in content:
    content = content.replace(old_plan_actions, new_plan_actions)
    print("10天计划操作按钮已添加不考题按钮")
else:
    print("找不到10天计划操作按钮区域")

# 2. 添加togglePlanSkipMark函数
# 找到togglePlanWrongMark函数，在它后面添加togglePlanSkipMark函数
old_plan_wrong = '''function togglePlanWrongMark() {
  const dayIds = planDays[planCurrentDay];
  const qid = dayIds[planQuizIndex];
  const idx = wrongBook.indexOf(qid);
  if (idx > -1) wrongBook.splice(idx, 1);
  else wrongBook.push(qid);
  saveWrong();
  updatePlanActionButtons();
}'''

new_plan_wrong_skip = '''function togglePlanWrongMark() {
  const dayIds = planDays[planCurrentDay];
  const qid = dayIds[planQuizIndex];
  const idx = wrongBook.indexOf(qid);
  if (idx > -1) wrongBook.splice(idx, 1);
  else wrongBook.push(qid);
  saveWrong();
  updatePlanActionButtons();
}

function togglePlanSkipMark() {
  const dayIds = planDays[planCurrentDay];
  const qid = dayIds[planQuizIndex];
  const wasSkipped = skipBook.includes(qid);
  
  if (wasSkipped) {
    // 恢复考题
    const idx = skipBook.indexOf(qid);
    if (idx > -1) skipBook.splice(idx, 1);
  } else {
    // 标记为不考题
    skipBook.push(qid);
  }
  saveSkip();
  
  // 从当天的题目列表中移除/恢复不考题
  if (!wasSkipped) {
    // 标记为不考题：从当天列表中移除
    const dayIdx = dayIds.indexOf(qid);
    if (dayIdx > -1) dayIds.splice(dayIdx, 1);
    // 调整当前索引
    if (planQuizIndex >= dayIds.length) planQuizIndex = dayIds.length - 1;
    if (planQuizIndex < 0) planQuizIndex = 0;
  }
  
  updatePlanActionButtons();
  renderPlanQuestion();
  updateStats();
}'''

if old_plan_wrong in content:
    content = content.replace(old_plan_wrong, new_plan_wrong_skip)
    print("已添加togglePlanSkipMark函数")
else:
    print("找不到togglePlanWrongMark函数")

# 3. 修改updatePlanActionButtons函数，更新不考题按钮状态
old_update_plan = '''function updatePlanActionButtons() {
  const dayIds = planDays[planCurrentDay];
  const qid = dayIds[planQuizIndex];
  document.getElementById('planDoneBtn').textContent = isPlanDone(qid) ? '✅ 已完成' : '✅ 标记已做';
  document.getElementById('planFavBtn').textContent = favorites.includes(qid) ? '⭐ 已收藏' : '⭐ 收藏';
  document.getElementById('planWrongBtn').textContent = wrongBook.includes(qid) ? '❌ 已标记错题' : '❌ 标记错题';
}'''

new_update_plan = '''function updatePlanActionButtons() {
  const dayIds = planDays[planCurrentDay];
  const qid = dayIds[planQuizIndex];
  document.getElementById('planDoneBtn').textContent = isPlanDone(qid) ? '✅ 已完成' : '✅ 标记已做';
  document.getElementById('planFavBtn').textContent = favorites.includes(qid) ? '⭐ 已收藏' : '⭐ 收藏';
  document.getElementById('planWrongBtn').textContent = wrongBook.includes(qid) ? '❌ 已标记错题' : '❌ 标记错题';
  const planSkipBtn = document.getElementById('planSkipBtn');
  if (planSkipBtn) {
    const isSkipped = skipBook.includes(qid);
    planSkipBtn.textContent = isSkipped ? '✅ 恢复考题' : '🚫 不考题';
  }
}'''

if old_update_plan in content:
    content = content.replace(old_update_plan, new_update_plan)
    print("updatePlanActionButtons函数已更新不考题按钮状态")
else:
    print("找不到updatePlanActionButtons函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("所有修改完成")
