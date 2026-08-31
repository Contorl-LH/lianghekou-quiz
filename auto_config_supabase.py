file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改initSupabase函数，添加默认配置
old_init = '''// 初始化Supabase
function initSupabase() {
  const config = JSON.parse(localStorage.getItem('supabase_config') || '{}');
  if (config.url && config.anonKey && typeof supabase !== 'undefined') {'''

new_init = '''// 初始化Supabase
function initSupabase() {
  // 默认配置（已自动配置）
  const defaultConfig = {
    url: 'https://rwpfamzutiqwkhyfswbd.supabase.co',
    anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ3cGZhbXp1dGlxd2toeWZzd2JkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODgwNjQxMzQsImV4cCI6MjEwMzY0MDEzNH0._Duid4aBRhXbjoKUXWbSm1fvibF0hCjK6E781izXpFo'
  };
  // 优先使用localStorage中的配置，否则使用默认配置
  let config = JSON.parse(localStorage.getItem('supabase_config') || '{}');
  if (!config.url || !config.anonKey) {
    config = defaultConfig;
    localStorage.setItem('supabase_config', JSON.stringify(config));
  }
  if (config.url && config.anonKey && typeof supabase !== 'undefined') {'''

if old_init in content:
    content = content.replace(old_init, new_init)
    print("initSupabase函数已修改，添加了默认配置")
else:
    print("找不到initSupabase函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
