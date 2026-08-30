file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到CSS开始和结束的位置
css_start = content.find('<style>') + len('<style>')
css_end = content.find('</style>')

old_css = content[css_start:css_end]

# 新的美化CSS
new_css = '''
  * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body {
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-attachment: fixed;
    color: #2d3748;
    min-height: 100vh;
    overflow-x: hidden;
  }
  body { padding-bottom: 90px; }

  /* 头部 */
  .header {
    background: linear-gradient(135deg, #1a365d 0%, #2b6cb0 50%, #4299e1 100%);
    color: white;
    padding: 16px 18px 14px;
    box-shadow: 0 8px 32px rgba(26, 54, 93, 0.4);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
  }
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }
  .header h1 {
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }
  .header .stats {
    font-size: 12px;
    opacity: 0.9;
    background: rgba(255,255,255,0.15);
    padding: 4px 10px;
    border-radius: 12px;
    backdrop-filter: blur(5px);
  }

  /* 模式标签 */
  .mode-tabs {
    display: flex;
    gap: 4px;
    background: rgba(255,255,255,0.12);
    border-radius: 12px;
    padding: 4px;
    backdrop-filter: blur(10px);
  }
  .mode-tab {
    flex: 1;
    padding: 8px 4px;
    text-align: center;
    font-size: 13px;
    border-radius: 9px;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    color: rgba(255,255,255,0.85);
    border: none;
    background: none;
    font-weight: 500;
  }
  .mode-tab:hover {
    background: rgba(255,255,255,0.1);
    color: white;
  }
  .mode-tab.active {
    background: white;
    color: #1a365d;
    font-weight: 700;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }
  .mode-tab .badge {
    display: inline-block;
    background: linear-gradient(135deg, #f56565, #c53030);
    color: white;
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 10px;
    margin-left: 3px;
    min-width: 16px;
    font-weight: 600;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  }

  /* 工具栏 */
  .toolbar-toggle {
    background: rgba(255,255,255,0.95);
    padding: 10px 18px;
    border-bottom: 1px solid rgba(26, 54, 93, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    user-select: none;
    backdrop-filter: blur(10px);
  }
  .toolbar-toggle span { font-size: 14px; color: #4a5568; font-weight: 500; }
  .toolbar-toggle .arrow { transition: transform 0.3s; font-size: 12px; color: #718096; }
  .toolbar-toggle.open .arrow { transform: rotate(180deg); }
  .toolbar {
    background: rgba(255,255,255,0.98);
    padding: 14px 18px;
    border-bottom: 1px solid rgba(26, 54, 93, 0.1);
    display: none;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    backdrop-filter: blur(10px);
  }
  .toolbar.open { display: flex; }
  .toolbar label { font-size: 13px; color: #4a5568; display: flex; align-items: center; gap: 6px; font-weight: 500; }
  .toolbar select, .toolbar input {
    padding: 8px 12px; border: 1.5px solid #e2e8f0; border-radius: 10px; font-size: 14px; min-height: 38px;
    background: white; transition: all 0.2s; color: #2d3748;
  }
  .toolbar select:focus, .toolbar input:focus {
    outline: none; border-color: #4299e1; box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.15);
  }
  .toolbar select { min-width: 100px; }
  .toolbar input { flex: 1; min-width: 120px; }
  .toolbar button {
    padding: 8px 16px; border: none; border-radius: 10px; cursor: pointer;
    font-size: 13px; min-height: 38px; font-weight: 600; transition: all 0.2s;
  }
  .toolbar button:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
  .btn-primary { background: linear-gradient(135deg, #4299e1, #2b6cb0); color: white; }
  .btn-secondary { background: #edf2f7; color: #4a5568; }
  .btn-danger { background: linear-gradient(135deg, #f56565, #c53030); color: white; }
  .btn-success { background: linear-gradient(135deg, #48bb78, #2f855a); color: white; }

  /* 主内容区 */
  .main { max-width: 100%; margin: 0 auto; padding: 14px; }

  /* 进度条 */
  .progress-bar {
    width: 100%; height: 8px; background: rgba(255,255,255,0.3);
    border-radius: 4px; margin-bottom: 14px; overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #4299e1, #667eea, #764ba2);
    transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 0 10px rgba(102, 126, 234, 0.5);
    border-radius: 4px;
  }

  /* 卡片 */
  .card {
    background: rgba(255,255,255,0.98);
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(26, 54, 93, 0.15);
    overflow: hidden;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.5);
    backdrop-filter: blur(10px);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .card:hover {
    box-shadow: 0 15px 50px rgba(26, 54, 93, 0.2);
  }
  .card-header {
    padding: 16px 20px;
    border-bottom: 1px solid rgba(26, 54, 93, 0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(90deg, #f7fafc 0%, #ffffff 100%);
  }
  .card-header .qid {
    font-size: 16px;
    font-weight: 700;
    color: #1a365d;
    letter-spacing: 0.3px;
  }
  .card-header .type-badge {
    padding: 5px 14px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  .type-A { background: linear-gradient(135deg, #bee3f8, #90cdf4); color: #2a4365; }
  .type-B { background: linear-gradient(135deg, #c6f6d5, #9ae6b4); color: #22543d; }
  .type-C { background: linear-gradient(135deg, #fefcbf, #faf089); color: #744210; }
  .type-D { background: linear-gradient(135deg, #e9d8fd, #d6bcfa); color: #44337a; }
  .type-E { background: linear-gradient(135deg, #fed7d7, #feb2b2); color: #742a2a; }
  .type-F { background: linear-gradient(135deg, #b2f5ea, #81e6d9); color: #234e52; }

  /* 卡片内容 */
  .card-body { padding: 16px; text-align: center; }
  .card-body img {
    max-width: 100%;
    height: auto;
    border: 2px solid #e2e8f0;
    border-radius: 14px;
    cursor: zoom-in;
    transition: all 0.25s;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }
  .card-body img:hover {
    border-color: #4299e1;
    box-shadow: 0 6px 20px rgba(66, 153, 225, 0.2);
  }
  .card-body img.zoomed {
    cursor: zoom-out;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 95vw;
    max-height: 90vh;
    z-index: 1000;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    border: 3px solid white;
  }
  .zoom-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.8);
    z-index: 999;
    backdrop-filter: blur(5px);
  }
  .zoom-overlay.show { display: block; }

  /* 选择题选项 */
  .answer-options {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 16px;
    padding: 0 4px;
  }
  .option-btn {
    padding: 14px 18px;
    border: 2px solid #e2e8f0;
    border-radius: 14px;
    background: white;
    font-size: 15px;
    text-align: left;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    align-items: center;
    gap: 12px;
    color: #2d3748;
  }
  .option-btn:hover {
    border-color: #4299e1;
    background: #ebf8ff;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(66, 153, 225, 0.15);
  }
  .option-btn:active { transform: scale(0.98); }
  .option-btn .opt-letter {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: linear-gradient(135deg, #edf2f7, #e2e8f0);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 14px;
    color: #4a5568;
    flex-shrink: 0;
    transition: all 0.2s;
  }
  .option-btn:hover .opt-letter {
    background: linear-gradient(135deg, #4299e1, #2b6cb0);
    color: white;
  }
  .option-btn.correct {
    border-color: #48bb78;
    background: linear-gradient(135deg, #f0fff4, #c6f6d5);
  }
  .option-btn.correct .opt-letter {
    background: linear-gradient(135deg, #48bb78, #2f855a);
    color: white;
  }
  .option-btn.wrong {
    border-color: #f56565;
    background: linear-gradient(135deg, #fff5f5, #fed7d7);
  }
  .option-btn.wrong .opt-letter {
    background: linear-gradient(135deg, #f56565, #c53030);
    color: white;
  }
  .option-btn.disabled {
    opacity: 0.7;
    cursor: not-allowed;
    pointer-events: none;
  }

  /* 结果提示 */
  .result-tip {
    margin-top: 14px;
    padding: 12px 16px;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    display: none;
  }
  .result-tip.show { display: block; animation: fadeIn 0.3s; }
  .result-tip.correct {
    background: linear-gradient(135deg, #c6f6d5, #9ae6b4);
    color: #22543d;
  }
  .result-tip.wrong {
    background: linear-gradient(135deg, #fed7d7, #feb2b2);
    color: #742a2a;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* 操作按钮 */
  .action-row {
    display: flex;
    gap: 10px;
    margin-top: 16px;
    flex-wrap: wrap;
  }
  .action-btn {
    flex: 1;
    min-width: 100px;
    padding: 12px 16px;
    border: none;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  .action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.15);
  }
  .action-btn:active {
    transform: translateY(0);
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  .action-btn.done-mark {
    background: linear-gradient(135deg, #48bb78, #2f855a);
    color: white;
  }
  .action-btn.fav-mark {
    background: linear-gradient(135deg, #ed8936, #dd6b20);
    color: white;
  }
  .action-btn.wrong-mark {
    background: linear-gradient(135deg, #f56565, #c53030);
    color: white;
  }

  /* 答案区域 */
  .answer-section {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 2px dashed #e2e8f0;
    display: none;
  }
  .answer-section.show { display: block; animation: fadeIn 0.3s; }
  .answer-label {
    display: inline-block;
    background: linear-gradient(135deg, #4299e1, #2b6cb0);
    color: white;
    padding: 6px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(66, 153, 225, 0.3);
  }

  /* 提示文字 */
  .hint {
    text-align: center;
    font-size: 12px;
    color: rgba(255,255,255,0.8);
    margin-top: 8px;
    padding: 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 8px;
    backdrop-filter: blur(5px);
  }

  /* 底部导航 */
  .bottom-nav {
    position: fixed;
    bottom: 12px;
    left: 12px;
    right: 12px;
    background: rgba(255,255,255,0.98);
    border-top: 1px solid rgba(26, 54, 93, 0.1);
    box-shadow: 0 -8px 32px rgba(26, 54, 93, 0.2);
    display: flex;
    z-index: 100;
    padding-bottom: env(safe-area-inset-bottom, 0);
    border-radius: 18px;
    overflow: hidden;
    backdrop-filter: blur(20px);
  }
  .bottom-nav button {
    flex: 1;
    padding: 10px 4px;
    border: none;
    background: none;
    cursor: pointer;
    font-size: 11px;
    font-weight: 600;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 3px;
    transition: all 0.2s;
    min-height: 56px;
    white-space: nowrap;
    color: #718096;
  }
  .bottom-nav button:hover {
    background: rgba(66, 153, 225, 0.08);
  }
  .bottom-nav button:active {
    transform: scale(0.95);
  }
  .bottom-nav .nav-icon {
    font-size: 18px;
    filter: drop-shadow(0 1px 2px rgba(0,0,0,0.1));
  }
  .bottom-nav .nav-text { font-size: 10px; font-weight: 600; }
  .bottom-nav .btn-prev { color: #4a5568; }
  .bottom-nav .btn-prev-undo { color: #718096; }
  .bottom-nav .btn-answer { color: #2f855a; }
  .bottom-nav .btn-answer.active { color: #dd6b20; }
  .bottom-nav .btn-next-undo { color: #718096; }
  .bottom-nav .btn-next { color: #2b6cb0; }

  /* 题型筛选 */
  .plan-type-filter {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 4px 0;
    margin-bottom: 12px;
    scrollbar-width: none;
  }
  .plan-type-filter::-webkit-scrollbar { display: none; }
  .type-filter-btn {
    padding: 8px 16px;
    border: 1.5px solid rgba(255,255,255,0.3);
    border-radius: 20px;
    background: rgba(255,255,255,0.15);
    color: white;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.25s;
    backdrop-filter: blur(10px);
  }
  .type-filter-btn:hover {
    background: rgba(255,255,255,0.25);
    transform: translateY(-1px);
  }
  .type-filter-btn.active {
    background: white;
    color: #1a365d;
    border-color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }

  /* 列表项 */
  .question-list { display: flex; flex-direction: column; gap: 10px; }
  .list-item {
    background: rgba(255,255,255,0.95);
    border-radius: 14px;
    padding: 14px 16px;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.5);
  }
  .list-item:hover {
    transform: translateX(4px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    background: white;
  }
  .list-item .item-info { flex: 1; }
  .list-item .item-qid { font-size: 14px; font-weight: 600; color: #1a365d; }
  .list-item .item-type { font-size: 11px; color: #718096; margin-top: 2px; }
  .list-item .item-actions { display: flex; gap: 8px; }
  .list-item .item-btn {
    padding: 6px 10px;
    border: none;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
  }
  .list-item .item-btn:hover { transform: scale(1.05); }

  /* 空状态 */
  .empty-state, .empty-list {
    text-align: center;
    padding: 40px 20px;
    color: rgba(255,255,255,0.8);
  }
  .empty-state .icon, .empty-list .icon {
    font-size: 48px;
    margin-bottom: 12px;
    opacity: 0.6;
  }

  /* 计划页面 */
  .plan-header {
    background: rgba(255,255,255,0.15);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 14px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
  }
  .plan-header h2 {
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
  }
  .plan-day-card {
    background: rgba(255,255,255,0.95);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
    cursor: pointer;
    transition: all 0.25s;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
  .plan-day-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  }
  .plan-day-title {
    font-size: 16px;
    font-weight: 700;
    color: #1a365d;
    margin-bottom: 8px;
  }
  .plan-day-progress {
    height: 8px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
    margin: 8px 0;
  }
  .plan-day-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #4299e1, #667eea);
    border-radius: 4px;
    transition: width 0.4s;
  }

  /* 计划答题头部 */
  .plan-quiz-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    background: rgba(255,255,255,0.15);
    padding: 12px 16px;
    border-radius: 14px;
    backdrop-filter: blur(10px);
  }
  .plan-back-btn {
    background: rgba(255,255,255,0.2);
    color: white;
    border: none;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
  }
  .plan-back-btn:hover { background: rgba(255,255,255,0.3); }
  .plan-quiz-title {
    color: white;
    font-size: 16px;
    font-weight: 700;
  }
  .plan-quiz-progress {
    color: rgba(255,255,255,0.9);
    font-size: 13px;
    font-weight: 600;
    background: rgba(255,255,255,0.15);
    padding: 4px 10px;
    border-radius: 10px;
  }

  /* 隐藏类 */
  .hidden { display: none !important; }
  .list-mode.hidden { display: none !important; }
  .list-mode.active { display: block; }
  .plan-mode { display: none; }
  .plan-mode.active { display: block; }
'''

new_content = content[:css_start] + new_css + content[css_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS全面美化完成！")
print(f"新CSS长度: {len(new_css)} 字符")
