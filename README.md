# 🚢 泰坦尼克号生存预测 | Titanic Survival Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)

![Kaggle Score](https://img.shields.io/badge/Kaggle-0.78708-yellow)

一个基于机器学习的泰坦尼克号乘客生存预测项目，使用Python实现数据清洗、特征工程和随机森林建模。

**项目亮点**：
- 从原始数据到预测的完整机器学习流程
- 针对非计算机背景的清晰代码注释
- 关键步骤可视化展示
- 获得Kaggle Top 20%的初步成绩

[👉 **点击查看Kaggle提交结果**](https://www.kaggle.com/competitions/titanic/submissions)  

**核心代码文件**：
- [🧹 数据清洗](https://raw.githubusercontent.com/lzr42-MD/Titanic/refs/heads/master/T.1-3days.py)
- [🔧 特征工程](https://github.com/lzr42-MD/Titanic/blob/master/T.4-6days.py)
- [🤖 模型训练](https://raw.githubusercontent.com/lzr42-MD/Titanic/refs/heads/master/T.7-9days.py)

---

## 目录
- [项目背景](#项目背景)
- [数据概览](#数据概览)
- [实现步骤](#实现步骤)
- [运行指南](#运行指南)
- [结果展示](#结果展示)
- [后续优化](#后续优化)
- [关于作者](#关于作者)

---

## 🎯 项目背景
根据泰坦尼克号乘客数据（如年龄、性别、船票等级等），构建机器学习模型预测乘客生存概率。这是Kaggle入门经典项目，适合机器学习初学者练手。

**解决的问题**：
- 如何处理缺失值和异常数据？
- 如何从原始特征（如姓名、船舱）提取有效信息？
- 如何选择适合的分类模型？

---

## 📊 数据概览
数据集包含以下关键字段：
| 字段 | 说明 | 示例 |
|------|------|------|
| Survived | 是否幸存（0=否，1=是） | 1 |
| Pclass | 船票等级（1/2/3等舱） | 3 |
| Sex | 性别 | male |
| Age | 年龄 | 22.0 |
| Fare | 票价 | 7.25 |

**数据集来源**：  
[Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)

---

## 🛠 实现步骤
1. **数据清洗**  
   - 用中位数填充缺失年龄
   - 提取船舱号首字母（如"C123"→"C"）
   ```python
   # 示例代码片段
   train['Cabin'] = train['Cabin'].apply(lambda x: x[0] if pd.notnull(x) else 'Unknown')
2.**特征工程**

从姓名提取称呼（Mr/Mrs/Miss）

合并亲属数量为家庭规模

对分类变量进行独热编码

3.**模型构建**

|模型|  验证集准确率|  特点|
|------|------|------|
|随机森林| 82.12%	| 处理复杂特征|
|逻辑回归| 81.56%	| 可解释性强|

---

## 💻 运行指南
环境要求：

Python 3.9+

主要库：pandas, scikit-learn, matplotlib

---

## 📈 结果展示
Kaggle提交成绩：
当前最佳分数：0.78708（Top 78%）

---

## 🔮 后续优化
尝试神经网络模型

添加更多交互特征

优化年龄分箱策略

---

## 👦 关于作者
你好！我是[LZR]，一名Python爱好者。这是我在机器学习领域的第一个实践项目，欢迎交流建议！


