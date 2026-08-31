file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在首页导航栏添加"不考题"入口
old_nav = '''  <div class="mode-tabs">
    <button class="mode-tab active" data-mode="quiz" onclick="switchMode('quiz')">答题</button>
    <button class="mode-tab" data-mode="plan" onclick="switchMode('plan')">10天计划</button>
    <button class="mode-tab" data-mode="wrong" onclick="switchMode('wrong')">错题本<span class="badge" id="wrongBadge">0</span></button>
    <button class="mode-tab" data-mode="fav" onclick="switchMode('fav')">收藏夹<span class="badge" id="favBadge">0</span></button>
  </div>'''

new_nav = '''  <div class="mode-tabs">
    <button class="mode-tab active" data-mode="quiz" onclick="switchMode('quiz')">答题</button>
    <button class="mode-tab" data-mode="plan" onclick="switchMode('plan')">10天计划</button>
    <button class="mode-tab" data-mode="wrong" onclick="switchMode('wrong')">错题本<span class="badge" id="wrongBadge">0</span></button>
    <button class="mode-tab" data-mode="fav" onclick="switchMode('fav')">收藏夹<span class="badge" id="favBadge">0</span></button>
    <button class="mode-tab" data-mode="skip" onclick="switchMode('skip')">不考题<span class="badge" id="skipBadge">0</span></button>
  </div>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("首页导航栏已添加不考题入口")
else:
    print("找不到首页导航栏")

# 2. 找到收藏夹列表的结束位置，添加不考题列表
# 先找到收藏夹列表的开始
fav_start = content.find('id="favMode"')
if fav_start != -1:
    # 找到收藏夹列表的结束（下一个</div>）
    # 找到10天计划模式的开始
    plan_start = content.find('<!-- 10天计划模式 -->', fav_start)
    if plan_start != -1:
        # 在10天计划模式之前插入不考题列表
        skip_list = '''
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
'''
        content = content[:plan_start] + skip_list + '\n' + content[plan_start:]
        print("不考题列表页面已添加")
    else:
        print("找不到10天计划模式开始位置")
else:
    print("找不到收藏夹列表")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML修改完成")
