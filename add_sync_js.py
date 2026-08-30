file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到</script>标签的位置（最后一个script标签）
script_end = content.rfind('</script>')

if script_end == -1:
    print("找不到</script>标签")
else:
    # 在最后一个</script>之前插入同步功能代码
    sync_js = '''
// ============ 数据同步功能 ============
let supabaseClient = null;
let supabaseUser = null;

// 初始化Supabase配置
function initSupabase() {
  const config = JSON.parse(localStorage.getItem('supabase_config') || '{}');
  if (config.url && config.anonKey) {
    try {
      supabaseClient = supabase.createClient(config.url, config.anonKey);
      // 检查登录状态
      supabaseClient.auth.getUser().then(({ data }) => {
        if (data.user) {
          supabaseUser = data.user;
          updateSupabaseUI();
        }
      });
      return true;
    } catch (e) {
      console.error('Supabase初始化失败:', e);
      return false;
    }
  }
  return false;
}

// 保存Supabase配置
function saveSupabaseConfig() {
  const url = document.getElementById('supabaseUrl').value.trim();
  const anonKey = document.getElementById('supabaseAnonKey').value.trim();
  if (!url || !anonKey) {
    alert('请填写Supabase项目URL和anon key');
    return;
  }
  localStorage.setItem('supabase_config', JSON.stringify({ url, anonKey }));
  if (initSupabase()) {
    alert('Supabase配置保存成功！');
    updateSupabaseUI();
  } else {
    alert('配置保存成功，但初始化失败，请检查URL和key是否正确');
  }
}

// 更新Supabase UI
function updateSupabaseUI() {
  const loginSection = document.getElementById('supabaseLoginSection');
  const userSection = document.getElementById('supabaseUserSection');
  if (supabaseUser) {
    loginSection.style.display = 'none';
    userSection.style.display = 'block';
    document.getElementById('supabaseUserEmail').textContent = supabaseUser.email;
  } else {
    loginSection.style.display = 'block';
    userSection.style.display = 'none';
  }
}

// Supabase登录
async function supabaseLogin() {
  if (!supabaseClient) {
    alert('请先配置Supabase');
    return;
  }
  const email = document.getElementById('supabaseEmail').value.trim();
  const password = document.getElementById('supabasePassword').value;
  if (!email || !password) {
    alert('请填写邮箱和密码');
    return;
  }
  try {
    const { data, error } = await supabaseClient.auth.signInWithPassword({ email, password });
    if (error) throw error;
    supabaseUser = data.user;
    updateSupabaseUI();
    alert('登录成功！');
  } catch (e) {
    alert('登录失败: ' + e.message);
  }
}

// Supabase注册
async function supabaseRegister() {
  if (!supabaseClient) {
    alert('请先配置Supabase');
    return;
  }
  const email = document.getElementById('supabaseEmail').value.trim();
  const password = document.getElementById('supabasePassword').value;
  if (!email || !password) {
    alert('请填写邮箱和密码');
    return;
  }
  if (password.length < 6) {
    alert('密码至少6位');
    return;
  }
  try {
    const { data, error } = await supabaseClient.auth.signUp({ email, password });
    if (error) throw error;
    if (data.user) {
      supabaseUser = data.user;
      updateSupabaseUI();
      alert('注册成功！已自动登录');
    } else {
      alert('注册成功！请检查邮箱验证');
    }
  } catch (e) {
    alert('注册失败: ' + e.message);
  }
}

// Supabase退出登录
async function supabaseLogout() {
  if (!supabaseClient) return;
  await supabaseClient.auth.signOut();
  supabaseUser = null;
  updateSupabaseUI();
  alert('已退出登录');
}

// 获取所有数据
function getAllData() {
  return {
    wrongBook: wrongBook,
    favorites: favorites,
    doneBook: doneBook,
    planData: planData,
    quizProgress: quizProgress,
    timestamp: Date.now()
  };
}

// 上传数据到Supabase
async function uploadToSupabase() {
  if (!supabaseClient || !supabaseUser) {
    alert('请先登录Supabase');
    return;
  }
  showConfirm('确定要上传数据到云端吗？这将覆盖云端数据。', async () => {
    try {
      const data = getAllData();
      const { error } = await supabaseClient
        .from('user_data')
        .upsert({
          user_id: supabaseUser.id,
          data: data,
          updated_at: new Date().toISOString()
        }, { onConflict: 'user_id' });
      if (error) throw error;
      alert('数据上传成功！');
    } catch (e) {
      alert('上传失败: ' + e.message + '\\n请确保已在Supabase创建user_data表');
    }
  });
}

// 从Supabase下载数据
async function downloadFromSupabase() {
  if (!supabaseClient || !supabaseUser) {
    alert('请先登录Supabase');
    return;
  }
  showConfirm('确定要从云端下载数据吗？这将合并到本地数据。', async () => {
    try {
      const { data, error } = await supabaseClient
        .from('user_data')
        .select('data')
        .eq('user_id', supabaseUser.id)
        .single();
      if (error) throw error;
      if (data && data.data) {
        mergeData(data.data);
        alert('数据下载成功！已合并到本地');
      } else {
        alert('云端没有数据');
      }
    } catch (e) {
      alert('下载失败: ' + e.message);
    }
  });
}

// 合并数据
function mergeData(cloudData) {
  // 错题本合并（取并集）
  if (cloudData.wrongBook) {
    wrongBook = [...new Set([...wrongBook, ...cloudData.wrongBook])];
    saveWrong();
  }
  // 收藏夹合并
  if (cloudData.favorites) {
    favorites = [...new Set([...favorites, ...cloudData.favorites])];
    saveFav();
  }
  // 已做题目合并
  if (cloudData.doneBook) {
    doneBook = [...new Set([...doneBook, ...cloudData.doneBook])];
    saveDone();
  }
  // 10天计划数据（取时间较新的）
  if (cloudData.planData && (!planData || (cloudData.timestamp > (quizProgress?.timestamp || 0)))) {
    planData = cloudData.planData;
    localStorage.setItem('quiz_10day_plan', JSON.stringify(planData));
  }
  // 答题进度（取时间较新的）
  if (cloudData.quizProgress) {
    quizProgress = cloudData.quizProgress;
    localStorage.setItem('quiz_progress', JSON.stringify(quizProgress));
    restoreQuizProgress();
  }
  updateBadges();
  renderQuestion();
}

// ============ 同步码功能 ============
// 生成同步码
function generateSyncCode() {
  const data = getAllData();
  const jsonStr = JSON.stringify(data);
  // Base64编码
  const base64 = btoa(unescape(encodeURIComponent(jsonStr)));
  // 复制到剪贴板
  navigator.clipboard.writeText(base64).then(() => {
    alert('同步码已复制到剪贴板！\\n\\n请在其他设备的"数据同步"中粘贴此同步码。\\n\\n同步码长度: ' + base64.length + ' 字符');
  }).catch(() => {
    // 如果剪贴板不可用，显示在输入框中
    document.getElementById('syncCodeInput').value = base64;
    alert('同步码已生成，请手动复制下方输入框中的内容');
  });
}

// 导入同步码
function importSyncCode() {
  const code = document.getElementById('syncCodeInput').value.trim();
  if (!code) {
    alert('请先粘贴同步码');
    return;
  }
  showConfirm('确定要导入同步码吗？数据将合并到本地。', () => {
    try {
      // Base64解码
      const jsonStr = decodeURIComponent(escape(atob(code)));
      const data = JSON.parse(jsonStr);
      mergeData(data);
      document.getElementById('syncCodeInput').value = '';
      alert('同步码导入成功！');
    } catch (e) {
      alert('同步码无效，请检查是否完整复制');
    }
  });
}

// ============ 弹窗控制 ============
function openSyncModal() {
  document.getElementById('syncModal').style.display = 'flex';
  // 加载已保存的配置
  const config = JSON.parse(localStorage.getItem('supabase_config') || '{}');
  if (config.url) document.getElementById('supabaseUrl').value = config.url;
  if (config.anonKey) document.getElementById('supabaseAnonKey').value = config.anonKey;
  updateSupabaseUI();
}

function closeSyncModal() {
  document.getElementById('syncModal').style.display = 'none';
}

// 确认弹窗
let confirmCallback = null;
function showConfirm(message, callback) {
  document.getElementById('confirmMessage').textContent = message;
  confirmCallback = callback;
  document.getElementById('confirmModal').style.display = 'flex';
  document.getElementById('confirmOkBtn').onclick = () => {
    closeConfirmModal();
    if (confirmCallback) confirmCallback();
  };
}

function closeConfirmModal() {
  document.getElementById('confirmModal').style.display = 'none';
  confirmCallback = null;
}

// 页面加载时初始化Supabase
window.addEventListener('load', () => {
  initSupabase();
});
'''

    new_content = content[:script_end] + sync_js + content[script_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("同步功能JavaScript代码已添加")

# 4. 在工具栏添加"数据同步"按钮
# 找到toolbar-toggle或toolbar区域
toolbar_pattern = '<div class="toolbar-toggle"'
if toolbar_pattern in content:
    # 在toolbar-toggle之前添加同步按钮（或者修改现有的）
    pass

# 让我在筛选工具栏中添加同步按钮
# 找到.toolbar的结束标签
toolbar_end = content.find('</div>\n\n  .main')
if toolbar_end > 0:
    # 在toolbar中添加同步按钮
    old_toolbar_end = '</div>\n\n  .main'
    new_toolbar_end = '''  <button class="btn-secondary" onclick="openSyncModal()" style="background:linear-gradient(135deg,#667eea,#764ba2);color:white">📊 数据同步</button>
</div>

  .main'''
    content = content.replace(old_toolbar_end, new_toolbar_end)
    print("数据同步按钮已添加到工具栏")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n所有同步功能代码添加完成！")
