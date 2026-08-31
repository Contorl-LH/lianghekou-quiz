file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 删除我添加的重复HTML弹窗（从<!-- 数据同步弹窗 -->到</div>\n</body>之前）
old_html_start = '<!-- 数据同步弹窗 -->'
old_html_end = '</div>\n</body>'

start_idx = content.find(old_html_start)
end_idx = content.find(old_html_end, start_idx)

if start_idx != -1 and end_idx != -1:
    # 找到确认弹窗的结束位置（第二个</div>）
    confirm_end = content.find('</div>\n</div>', start_idx)
    if confirm_end != -1:
        end_idx = confirm_end + len('</div>\n</div>')
    
    content = content[:start_idx] + content[end_idx:]
    print("重复的HTML弹窗已删除")
else:
    print(f"找不到重复HTML: start={start_idx}, end={end_idx}")

# 2. 在现有的</script>之前添加Supabase功能代码
# 找到最后一个</script>（在init();之后）
script_end = content.rfind('init();\n</script>')

if script_end != -1:
    supabase_js = '''
init();

// ============ Supabase云端同步 ============
let supabaseClient = null;
let supabaseUser = null;

// 初始化Supabase
function initSupabase() {
  const config = JSON.parse(localStorage.getItem('supabase_config') || '{}');
  if (config.url && config.anonKey && typeof supabase !== 'undefined') {
    try {
      supabaseClient = supabase.createClient(config.url, config.anonKey);
      supabaseClient.auth.getUser().then(({ data }) => {
        if (data && data.user) {
          supabaseUser = data.user;
        }
      });
      return true;
    } catch (e) {
      console.error('Supabase初始化失败:', e);
    }
  }
  return false;
}

// 打开Supabase配置弹窗
function openSupabaseConfig() {
  const config = JSON.parse(localStorage.getItem('supabase_config') || '{}');
  const url = prompt('请输入Supabase项目URL（在Supabase项目Settings > API中获取）:', config.url || '');
  if (url === null) return;
  const anonKey = prompt('请输入Supabase anon key（在Supabase项目Settings > API中获取）:', config.anonKey || '');
  if (anonKey === null) return;
  
  localStorage.setItem('supabase_config', JSON.stringify({ url: url.trim(), anonKey: anonKey.trim() }));
  
  if (initSupabase()) {
    alert('Supabase配置成功！\\n\\n请在Supabase中创建user_data表后使用云端同步。\\n\\n建表SQL：\\nCREATE TABLE user_data (\\n  user_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,\\n  data JSONB NOT NULL,\\n  updated_at TIMESTAMPTZ DEFAULT NOW()\\n);');
  } else {
    alert('配置已保存，但初始化失败，请检查URL和key是否正确');
  }
}

// Supabase登录
async function supabaseLogin() {
  if (!supabaseClient) {
    openSupabaseConfig();
    return;
  }
  const email = prompt('请输入邮箱:');
  if (!email) return;
  const password = prompt('请输入密码:');
  if (!password) return;
  
  try {
    const { data, error } = await supabaseClient.auth.signInWithPassword({ email, password });
    if (error) throw error;
    supabaseUser = data.user;
    alert('登录成功！当前用户: ' + supabaseUser.email);
  } catch (e) {
    alert('登录失败: ' + e.message);
  }
}

// Supabase注册
async function supabaseRegister() {
  if (!supabaseClient) {
    openSupabaseConfig();
    return;
  }
  const email = prompt('请输入邮箱:');
  if (!email) return;
  const password = prompt('请输入密码（至少6位）:');
  if (!password || password.length < 6) {
    alert('密码至少6位');
    return;
  }
  
  try {
    const { data, error } = await supabaseClient.auth.signUp({ email, password });
    if (error) throw error;
    if (data.user) {
      supabaseUser = data.user;
      alert('注册成功！已自动登录');
    } else {
      alert('注册成功！请检查邮箱验证后登录');
    }
  } catch (e) {
    alert('注册失败: ' + e.message);
  }
}

// 上传数据到Supabase
async function uploadToSupabase() {
  if (!supabaseClient || !supabaseUser) {
    alert('请先登录Supabase');
    return;
  }
  if (!confirm('确定要上传数据到云端吗？这将覆盖云端数据。')) return;
  
  try {
    const data = {
      v: 1,
      t: Date.now(),
      wrong: localStorage.getItem('quiz_wrong_book') || '[]',
      fav: localStorage.getItem('quiz_favorites') || '[]',
      done: localStorage.getItem('quiz_done_book') || '[]',
      plan: localStorage.getItem('quiz_10day_plan') || 'null',
      prog: localStorage.getItem('quiz_progress') || 'null'
    };
    
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
    alert('上传失败: ' + e.message + '\\n\\n请确保已在Supabase创建user_data表');
  }
}

// 从Supabase下载数据
async function downloadFromSupabase() {
  if (!supabaseClient || !supabaseUser) {
    alert('请先登录Supabase');
    return;
  }
  if (!confirm('确定要从云端下载数据吗？这将覆盖本地数据。')) return;
  
  try {
    const { data, error } = await supabaseClient
      .from('user_data')
      .select('data')
      .eq('user_id', supabaseUser.id)
      .single();
    
    if (error) throw error;
    
    if (data && data.data) {
      const d = data.data;
      if (d.wrong) localStorage.setItem('quiz_wrong_book', d.wrong);
      if (d.fav) localStorage.setItem('quiz_favorites', d.fav);
      if (d.done) localStorage.setItem('quiz_done_book', d.done);
      if (d.plan) localStorage.setItem('quiz_10day_plan', d.plan);
      if (d.prog) localStorage.setItem('quiz_progress', d.prog);
      
      // 重新加载内存数据
      wrongBook = JSON.parse(localStorage.getItem('quiz_wrong_book') || '[]');
      favorites = JSON.parse(localStorage.getItem('quiz_favorites') || '[]');
      doneBook = JSON.parse(localStorage.getItem('quiz_done_book') || '[]');
      planData = JSON.parse(localStorage.getItem('quiz_10day_plan') || 'null');
      quizProgress = JSON.parse(localStorage.getItem('quiz_progress') || 'null');
      
      updateBadges();
      renderQuestion();
      alert('数据下载成功！已覆盖本地数据');
    } else {
      alert('云端没有数据');
    }
  } catch (e) {
    alert('下载失败: ' + e.message);
  }
}

// Supabase退出登录
async function supabaseLogout() {
  if (!supabaseClient) return;
  await supabaseClient.auth.signOut();
  supabaseUser = null;
  alert('已退出登录');
}

// 打开云端同步菜单
function openCloudSync() {
  if (!supabaseClient) {
    if (confirm('尚未配置Supabase，是否现在配置？')) {
      openSupabaseConfig();
    }
    return;
  }
  
  const options = [];
  if (supabaseUser) {
    options.push('当前用户: ' + supabaseUser.email);
    options.push('1. 上传数据到云端');
    options.push('2. 从云端下载数据');
    options.push('3. 退出登录');
    options.push('4. 重新配置Supabase');
  } else {
    options.push('1. 登录');
    options.push('2. 注册');
    options.push('3. 重新配置Supabase');
  }
  
  const choice = prompt('☁️ 云端同步（Supabase）\\n\\n' + options.join('\\n') + '\\n\\n请输入选项数字:');
  
  if (supabaseUser) {
    if (choice === '1') uploadToSupabase();
    else if (choice === '2') downloadFromSupabase();
    else if (choice === '3') supabaseLogout();
    else if (choice === '4') openSupabaseConfig();
  } else {
    if (choice === '1') supabaseLogin();
    else if (choice === '2') supabaseRegister();
    else if (choice === '3') openSupabaseConfig();
  }
}

// 页面加载时初始化Supabase
if (typeof supabase !== 'undefined') {
  initSupabase();
}
'''
    
    content = content[:script_end] + supabase_js + content[script_end + len('init();\n</script>'):]
    print("Supabase功能代码已添加")
else:
    print("找不到init();\n</script>位置")

# 3. 在工具栏添加云端同步按钮
# 找到现有的同步按钮或工具栏
toolbar_pattern = 'onclick="openSyncModal(\'export\')"'
if toolbar_pattern in content:
    # 在导出按钮后面添加云端同步按钮
    old_btn = 'onclick="openSyncModal(\'export\')">📤 导出数据</button>'
    new_btn = '''onclick="openSyncModal('export')">📤 导出数据</button>
      <button class="btn-secondary" onclick="openCloudSync()" style="background:linear-gradient(135deg,#667eea,#764ba2);color:white">☁️ 云端同步</button>'''
    content = content.replace(old_btn, new_btn)
    print("云端同步按钮已添加")
else:
    print("找不到导出按钮位置")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSupabase云端同步功能添加完成！")
