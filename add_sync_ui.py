file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在head中添加Supabase SDK引用
old_head = '<title>两河口二次专业理论题库</title>'
new_head = '''<title>两河口二次专业理论题库</title>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'''

content = content.replace(old_head, new_head)

# 2. 在body末尾添加同步功能UI（在</body>之前）
sync_ui = '''
<!-- 数据同步弹窗 -->
<div class="sync-modal" id="syncModal" style="display:none">
  <div class="sync-modal-overlay" onclick="closeSyncModal()"></div>
  <div class="sync-modal-content">
    <div class="sync-modal-header">
      <h3>📊 数据同步</h3>
      <button class="sync-close-btn" onclick="closeSyncModal()">✕</button>
    </div>
    <div class="sync-modal-body">
      <!-- 同步码方式 -->
      <div class="sync-section">
        <h4>🔑 同步码方式（无需注册）</h4>
        <p class="sync-desc">将当前设备的所有答题数据生成同步码，在其他设备粘贴即可恢复</p>
        <div class="sync-actions">
          <button class="sync-btn sync-btn-primary" onclick="generateSyncCode()">📋 复制同步码</button>
        </div>
        <div class="sync-input-group">
          <textarea class="sync-textarea" id="syncCodeInput" placeholder="粘贴同步码..."></textarea>
          <button class="sync-btn sync-btn-success" onclick="importSyncCode()">✅ 导入同步码</button>
        </div>
      </div>
      
      <!-- Supabase云端同步 -->
      <div class="sync-section">
        <h4>☁️ 云端同步（Supabase）</h4>
        <p class="sync-desc">注册账号后实现多设备自动同步</p>
        <div id="supabaseLoginSection" style="display:none">
          <div class="sync-input-group">
            <input type="email" id="supabaseEmail" placeholder="邮箱" class="sync-input">
            <input type="password" id="supabasePassword" placeholder="密码" class="sync-input">
          </div>
          <div class="sync-actions">
            <button class="sync-btn sync-btn-primary" onclick="supabaseLogin()">🔐 登录</button>
            <button class="sync-btn sync-btn-secondary" onclick="supabaseRegister()">📝 注册</button>
          </div>
        </div>
        <div id="supabaseUserSection" style="display:none">
          <p class="sync-user-info">当前用户：<span id="supabaseUserEmail"></span></p>
          <div class="sync-actions">
            <button class="sync-btn sync-btn-primary" onclick="uploadToSupabase()">⬆️ 上传数据</button>
            <button class="sync-btn sync-btn-success" onclick="downloadFromSupabase()">⬇️ 下载数据</button>
            <button class="sync-btn sync-btn-danger" onclick="supabaseLogout()">🚪 退出登录</button>
          </div>
        </div>
        <div class="sync-config-section">
          <details>
            <summary>⚙️ Supabase配置（首次使用需配置）</summary>
            <div class="sync-input-group">
              <input type="text" id="supabaseUrl" placeholder="Supabase项目URL" class="sync-input">
              <input type="text" id="supabaseAnonKey" placeholder="Supabase anon key" class="sync-input">
              <button class="sync-btn sync-btn-secondary" onclick="saveSupabaseConfig()">💾 保存配置</button>
            </div>
            <p class="sync-hint">配置保存在本地，不会上传到任何服务器</p>
          </details>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 确认操作弹窗 -->
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
</div>
'''

# 在</body>之前插入
content = content.replace('</body>', sync_ui + '</body>')

# 3. 添加同步功能的CSS样式（在</style>之前）
sync_css = '''
  /* 数据同步弹窗 */
  .sync-modal {
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    z-index: 2000; display: flex; align-items: center; justify-content: center;
  }
  .sync-modal-overlay {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6); backdrop-filter: blur(5px);
  }
  .sync-modal-content {
    position: relative; background: white; border-radius: 20px;
    width: 90%; max-width: 500px; max-height: 85vh; overflow-y: auto;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    animation: syncModalIn 0.3s ease;
  }
  @keyframes syncModalIn {
    from { opacity: 0; transform: scale(0.9) translateY(20px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
  }
  .sync-modal-header {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 24px; border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 20px 20px 0 0;
  }
  .sync-modal-header h3 { color: white; font-size: 18px; font-weight: 700; }
  .sync-close-btn {
    background: rgba(255,255,255,0.2); border: none; color: white;
    width: 32px; height: 32px; border-radius: 50%; cursor: pointer;
    font-size: 16px; transition: all 0.2s;
  }
  .sync-close-btn:hover { background: rgba(255,255,255,0.3); transform: rotate(90deg); }
  .sync-modal-body { padding: 20px 24px; }
  .sync-section { margin-bottom: 24px; }
  .sync-section h4 {
    font-size: 15px; font-weight: 700; color: #2d3748;
    margin-bottom: 8px;
  }
  .sync-desc {
    font-size: 12px; color: #718096; margin-bottom: 12px; line-height: 1.5;
  }
  .sync-actions {
    display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 12px;
  }
  .sync-btn {
    padding: 10px 16px; border: none; border-radius: 10px;
    font-size: 13px; font-weight: 600; cursor: pointer;
    transition: all 0.2s; flex: 1; min-width: 100px;
  }
  .sync-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
  .sync-btn:active { transform: translateY(0); }
  .sync-btn-primary { background: linear-gradient(135deg, #4299e1, #2b6cb0); color: white; }
  .sync-btn-success { background: linear-gradient(135deg, #48bb78, #2f855a); color: white; }
  .sync-btn-secondary { background: #edf2f7; color: #4a5568; }
  .sync-btn-danger { background: linear-gradient(135deg, #f56565, #c53030); color: white; }
  .sync-input-group {
    display: flex; flex-direction: column; gap: 10px; margin-top: 10px;
  }
  .sync-input {
    padding: 10px 14px; border: 1.5px solid #e2e8f0; border-radius: 10px;
    font-size: 13px; transition: all 0.2s;
  }
  .sync-input:focus {
    outline: none; border-color: #4299e1;
    box-shadow: 0 0 0 3px rgba(66,153,225,0.15);
  }
  .sync-textarea {
    padding: 10px 14px; border: 1.5px solid #e2e8f0; border-radius: 10px;
    font-size: 12px; min-height: 80px; resize: vertical;
    font-family: monospace; word-break: break-all;
  }
  .sync-textarea:focus {
    outline: none; border-color: #4299e1;
    box-shadow: 0 0 0 3px rgba(66,153,225,0.15);
  }
  .sync-user-info {
    font-size: 13px; color: #2d3748; margin-bottom: 10px;
    padding: 8px 12px; background: #f7fafc; border-radius: 8px;
  }
  .sync-config-section { margin-top: 12px; }
  .sync-config-section details {
    background: #f7fafc; padding: 10px 14px; border-radius: 10px;
  }
  .sync-config-section summary {
    cursor: pointer; font-size: 13px; font-weight: 600; color: #4a5568;
  }
  .sync-hint { font-size: 11px; color: #a0aec0; margin-top: 6px; }

  /* 确认弹窗 */
  .confirm-modal {
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    z-index: 3000; display: flex; align-items: center; justify-content: center;
  }
  .confirm-modal-overlay {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
  }
  .confirm-modal-content {
    position: relative; background: white; border-radius: 16px;
    padding: 24px; width: 85%; max-width: 350px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    text-align: center;
  }
  .confirm-modal-content h4 {
    font-size: 16px; font-weight: 700; color: #2d3748; margin-bottom: 12px;
  }
  .confirm-modal-content p {
    font-size: 14px; color: #4a5568; margin-bottom: 20px; line-height: 1.5;
  }
  .confirm-actions { display: flex; gap: 12px; }
  .confirm-btn {
    flex: 1; padding: 10px; border: none; border-radius: 10px;
    font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.2s;
  }
  .confirm-btn-cancel { background: #edf2f7; color: #4a5568; }
  .confirm-btn-ok { background: linear-gradient(135deg, #4299e1, #2b6cb0); color: white; }
  .confirm-btn:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
'''

content = content.replace('</style>', sync_css + '</style>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("同步功能UI和CSS已添加")
