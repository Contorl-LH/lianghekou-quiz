file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改buildPlan函数，排除不考题
old_build = '''function buildPlan() {
  // 按题型分组
  const byType = {};
  allQuestions.forEach(q => {
    if (!byType[q.type]) byType[q.type] = [];
    byType[q.type].push(q.id);
  });'''

new_build = '''function buildPlan() {
  // 按题型分组（排除不考题）
  const byType = {};
  allQuestions.forEach(q => {
    if (skipBook.includes(q.id)) return; // 排除不考题
    if (!byType[q.type]) byType[q.type] = [];
    byType[q.type].push(q.id);
  });'''

if old_build in content:
    content = content.replace(old_build, new_build)
    print("buildPlan函数已修改，排除不考题")
else:
    print("找不到buildPlan函数")

# 2. 修改renderWrongList函数，排除不考题
old_wrong_list = '''function renderWrongList() {
  const list = document.getElementById('wrongList');
  const empty = document.getElementById('wrongEmpty');
  list.innerHTML = '';
  const filtered = wrongListFilterType === 'all' ? wrongBook : wrongBook.filter(qid => {
    const q = allQuestions.find(x => x.id === qid);
    return q && q.type === wrongListFilterType;
  });'''

new_wrong_list = '''function renderWrongList() {
  const list = document.getElementById('wrongList');
  const empty = document.getElementById('wrongEmpty');
  list.innerHTML = '';
  const filtered = wrongListFilterType === 'all' ? wrongBook : wrongBook.filter(qid => {
    const q = allQuestions.find(x => x.id === qid);
    return q && q.type === wrongListFilterType;
  }).filter(qid => !skipBook.includes(qid)); // 排除不考题'''

if old_wrong_list in content:
    content = content.replace(old_wrong_list, new_wrong_list)
    print("renderWrongList函数已修改，排除不考题")
else:
    print("找不到renderWrongList函数")

# 3. 修改getFilteredWrongBook函数，排除不考题
old_wrong_train = '''function getFilteredWrongBook() {
  if (wrongTrainFilterType === 'all') return [...wrongBook];
  return wrongBook.filter(qid => {
    const q = allQuestions.find(x => x.id === qid);
    return q && q.type === wrongTrainFilterType;
  });
}'''

new_wrong_train = '''function getFilteredWrongBook() {
  let result = wrongBook.filter(qid => !skipBook.includes(qid)); // 排除不考题
  if (wrongTrainFilterType === 'all') return result;
  return result.filter(qid => {
    const q = allQuestions.find(x => x.id === qid);
    return q && q.type === wrongTrainFilterType;
  });
}'''

if old_wrong_train in content:
    content = content.replace(old_wrong_train, new_wrong_train)
    print("getFilteredWrongBook函数已修改，排除不考题")
else:
    print("找不到getFilteredWrongBook函数")

# 4. 修改renderFavList函数，排除不考题
old_fav_list = '''function renderFavList() {
  const list = document.getElementById('favList');
  const empty = document.getElementById('favEmpty');
  list.innerHTML = '';
  const filtered = favFilterType === 'all' ? favorites : favorites.filter(qid => {
    const q = allQuestions.find(x => x.id === qid);
    return q && q.type === favFilterType;
  });'''

new_fav_list = '''function renderFavList() {
  const list = document.getElementById('favList');
  const empty = document.getElementById('favEmpty');
  list.innerHTML = '';
  const filtered = favFilterType === 'all' ? favorites : favorites.filter(qid => {
    const q = allQuestions.find(x => x.id === qid);
    return q && q.type === favFilterType;
  }).filter(qid => !skipBook.includes(qid)); // 排除不考题'''

if old_fav_list in content:
    content = content.replace(old_fav_list, new_fav_list)
    print("renderFavList函数已修改，排除不考题")
else:
    print("找不到renderFavList函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("所有修改完成")
