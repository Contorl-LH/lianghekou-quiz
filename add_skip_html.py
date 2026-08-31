file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在首页导航栏添加"不考题"入口
old_nav = '''    <div class="nav-tabs">
      <button class="nav-tab active" data-mode="quiz" onclick="switchMode('quiz')">答题</button>
      <button class="nav-tab" data-mode="plan" onclick="switchMode('plan')">10天计划</button>
      <button class="nav-tab" data-mode="wrong" onclick="switchMode('wrong')">错题本<span class="badge" id="wrongBadge">0</span></button>
      <button class="nav-tab" data-mode="fav" onclick="switchMode('fav')">收藏夹<span class="badge" id="favBadge">0</span></button>
    </div>'''

new_nav = '''    <div class="nav-tabs">
      <button class="nav-tab active" data-mode="quiz" onclick="switchMode('quiz')">答题</button>
      <button class="nav-tab" data-mode="plan" onclick="switchMode('plan')">10天计划</button>
      <button class="nav-tab" data-mode="wrong" onclick="switchMode('wrong')">错题本<span class="badge" id="wrongBadge">0</span></button>
      <button class="nav-tab" data-mode="fav" onclick="switchMode('fav')">收藏夹<span class="badge" id="favBadge">0</span></button>
      <button class="nav-tab" data-mode="skip" onclick="switchMode('skip')">不考题<span class="badge" id="skipBadge">0</span></button>
    </div>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("首页导航栏已添加不考题入口")
else:
    print("找不到首页导航栏")

# 2. 在做题界面的操作按钮中添加"标记为不考题"按钮
old_actions = '''        <div class="action-row">
          <button class="action-btn done-mark" id="doneBtn" onclick="toggleDoneMark()">✅ 标记已做</button>
          <button class="action-btn fav" id="favBtn" onclick="toggleFavorite()">⭐ 收藏</button>
          <button class="action-btn wrong-mark" id="wrongBtn" onclick="toggleWrongMark()">❌ 标记错题</button>
        </div>'''

new_actions = '''        <div class="action-row">
          <button class="action-btn done-mark" id="doneBtn" onclick="toggleDoneMark()">✅ 标记已做</button>
          <button class="action-btn fav" id="favBtn" onclick="toggleFavorite()">⭐ 收藏</button>
          <button class="action-btn wrong-mark" id="wrongBtn" onclick="toggleWrongMark()">❌ 标记错题</button>
          <button class="action-btn skip-mark" id="skipBtn" onclick="toggleSkipMark()">🚫 不考题</button>
        </div>'''

if old_actions in content:
    content = content.replace(old_actions, new_actions)
    print("做题界面已添加不考题按钮")
else:
    print("找不到做题界面操作按钮")

# 3. 添加不考题列表页面（在收藏夹列表后面）
old_fav_list_end = '''    </div>
  </div>

  <!-- 10天计划模式 -->'''

new_skip_list = '''    </div>

    <!-- 不考题列表 -->
    <div class="list-mode" id="skipMode" style="display:none">
      <div class="list-header">
        <h2>🚫 不考题</h2>
        <p style="color:#666;font-size:14px">已标记为不考的题目，不会出现在答题和10天计划中</p>
        <button class="btn-danger" onclick="clearAllSkipConfirm()">清空不考题</button>
      </div>
      <div class="list-filter">
        <button class="type-filter-btn active" data-type="all" onclick="setSkipFilter('all')">全部</button>
        <button class="type-filter-btn" data-type="A" onclick="setSkipFilter('A')">选择</button>
        <button class="type-filter-btn" data-type="B" onclick="setSkipFilter('B')">判断</button>
        <button class="type-filter-btn" data-type="C" onclick="setSkipFilter('C')">简答</button>
        <button class="type-filter-btn" data-type="D" onclick="setSkipFilter('D')">计算</button>
        <button class="type-filter-btn" data-type="E" onclick="setSkipFilter('E')">绘图</button>
        <button class="type-filter-btn" data-type="F" onclick="setSkipFilter('F')">论述</button>
      </div>
      <div class="question-list" id="skipList"></div>
    </div>
  </div>

  <!-- 10天计划模式 -->'''

if old_fav_list_end in content:
    content = content.replace(old_fav_list_end, new_skip_list)
    print("不考题列表页面已添加")
else:
    print("找不到收藏夹列表结束位置")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML修改完成")
