file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 将skipBook的声明移到filteredQuestions之前
old_code = '''// ============ 数据与状态 ============
const allQuestions = window.QUIZ_DATA || [];
let filteredQuestions = allQuestions.filter(q => !skipBook.includes(q.id));
let currentIndex = 0;
let answerVisible = false;
let currentMode = 'quiz'; // quiz / plan / wrong / fav
let answered = false;
let selectedOption = null;

// localStorage 数据
let wrongBook = JSON.parse(localStorage.getItem('quiz_wrong_book') || '[]');
let favorites = JSON.parse(localStorage.getItem('quiz_favorites') || '[]');
let doneBook = JSON.parse(localStorage.getItem('quiz_done_book') || '[]');
let planData = JSON.parse(localStorage.getItem('quiz_10day_plan') || 'null');
let quizProgress = JSON.parse(localStorage.getItem('quiz_progress') || 'null');
let skipBook = JSON.parse(localStorage.getItem('quiz_skip_book') || '[]');
let skipFilterType = 'all';'''

new_code = '''// ============ 数据与状态 ============
const allQuestions = window.QUIZ_DATA || [];

// localStorage 数据（必须在filteredQuestions之前声明）
let wrongBook = JSON.parse(localStorage.getItem('quiz_wrong_book') || '[]');
let favorites = JSON.parse(localStorage.getItem('quiz_favorites') || '[]');
let doneBook = JSON.parse(localStorage.getItem('quiz_done_book') || '[]');
let planData = JSON.parse(localStorage.getItem('quiz_10day_plan') || 'null');
let quizProgress = JSON.parse(localStorage.getItem('quiz_progress') || 'null');
let skipBook = JSON.parse(localStorage.getItem('quiz_skip_book') || '[]');
let skipFilterType = 'all';

let filteredQuestions = allQuestions.filter(q => !skipBook.includes(q.id));
let currentIndex = 0;
let answerVisible = false;
let currentMode = 'quiz'; // quiz / plan / wrong / fav
let answered = false;
let selectedOption = null;'''

if old_code in content:
    content = content.replace(old_code, new_code)
    print("变量声明顺序已修复")
else:
    print("找不到目标代码")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
