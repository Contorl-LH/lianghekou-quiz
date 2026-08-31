file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 移除工具栏中的导出和导入按钮
old_buttons = '''  <button class="btn-success" onclick="openSyncModal('export')">📤导出数据</button>
  <button class="btn-secondary" onclick="openCloudSync()" style="background:linear-gradient(135deg,#667eea,#764ba2);color:white">☁️云端同步</button>
  <button class="btn-primary" onclick="openSyncModal('import')">📥导入数据</button>'''

new_buttons = '''  <button class="btn-secondary" onclick="openCloudSync()" style="background:linear-gradient(135deg,#667eea,#764ba2);color:white">☁️云端同步</button>'''

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons)
    print("导出/导入按钮已移除")
else:
    print("找不到导出/导入按钮")
    # 尝试分别移除
    content = content.replace('  <button class="btn-success" onclick="openSyncModal(\'export\')">📤导出数据</button>\n', '')
    content = content.replace('  <button class="btn-primary" onclick="openSyncModal(\'import\')">📥导入数据</button>\n', '')
    print("已分别移除导出/导入按钮")

# 2. 移除同步码弹窗UI
old_modal = '''<!-- 数据同步模态框 -->
<div class="modal-overlay" id="syncModal">
  <div class="modal-box" style="max-width:420px">
    <h3 id="syncModalTitle">数据同步</h3>
    <p id="syncModalText" style="font-size:13px;color:#666;margin-bottom:10px"></p>
    <textarea id="syncDataText" style="width:100%;min-height:120px;padding:10px;border:1px solid #ccc;border-radius:8px;font-size:12px;font-family:monospace;resize:vertical;box-sizing:border-box" placeholder="粘贴同步码..."></textarea>
    <div id="syncStats" style="font-size:12px;color:#888;margin-top:8px;text-align:left"></div>
    <div class="modal-buttons" style="margin-top:14px">
      <button class="cancel" onclick="closeSyncModal()">关闭</button>
      <button class="confirm" id="syncActionBtn" style="background:#2980b9" onclick="doSyncAction()">复制同步码</button>
    </div>
  </div>
</div>'''

if old_modal in content:
    content = content.replace(old_modal, '')
    print("同步码弹窗UI已移除")
else:
    print("找不到同步码弹窗UI")

# 3. 移除确认操作弹窗（如果存在）
old_confirm = '''<!-- 确认操作弹窗 -->
<div class="confirm-modal" id="confirmModal" style="display:none">
  <div class="confirm-modal-overlay" onclick="closeConfirmModal()"></div>
  <div class="confirm-modal-content">
    <h4>确认操作</h4>
    <p id="confirmMessage">确定要执行此操作吗？</p>
    <div class="confirm-actions">
      <button class="confirm-btn confirm-btn-cancel" onclick="closeConfirmModal()">取消</button>
      <button class="confirm-btn confirm-btn-ok" id="confirmOkBtn">确定</button>
    </div>
  </div>
</div>'''

if old_confirm in content:
    content = content.replace(old_confirm, '')
    print("确认操作弹窗已移除")
else:
    print("找不到确认操作弹窗")

# 4. 移除同步码相关的JavaScript函数
# 找到同步码函数的开始和结束
sync_start = content.find('// ============ 数据同步（导出/导入） ============')
sync_end = content.find('// ============ Supabase云端同步 ============')

if sync_start != -1 and sync_end != -1:
    content = content[:sync_start] + content[sync_end:]
    print("同步码JavaScript函数已移除")
else:
    print(f"找不到同步码函数范围: start={sync_start}, end={sync_end}")

# 5. 移除同步码相关的CSS
# 找到.modal-overlay和.modal-box相关的CSS
css_patterns = [
    '  .modal-overlay {',
    '  .modal-box {',
    '  .modal-buttons {',
]

# 简单处理：移除.modal相关的CSS块
import re
# 移除.modal-overlay, .modal-box, .modal-buttons的CSS定义
content = re.sub(r'  \.modal-overlay \{[^}]+\}\n', '', content)
content = re.sub(r'  \.modal-box \{[^}]+\}\n', '', content)
content = re.sub(r'  \.modal-buttons \{[^}]+\}\n', '', content)

# 移除.confirm-modal相关的CSS
content = re.sub(r'  /\* 确认弹窗 \*/\n', '', content)
content = re.sub(r'  \.confirm-modal \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-modal-overlay \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-modal-content \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-modal-content h4 \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-modal-content p \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-actions \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-btn \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-btn-cancel \{[^}]+\}\n', '', content)
content = re.sub(r'  \.confirm-btn-ok \{[^}]+\}\n', '', content)

print("同步码相关CSS已移除")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n同步码功能已全部移除，只保留云端同步功能")
