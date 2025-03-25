import pandas as pd
from sklearn.model_selection import train_test_split

train=pd.read_csv('featured_train.csv')
X=train.drop('Survived',axis=1)
y=train['Survived']
X_train, X_val, y_train, y_val=train_test_split(X,y,test_size=0.2,random_state=42)



from sklearn.ensemble import RandomForestClassifier
# model_rf=RandomForestClassifier(random_state=42)
# model_rf.fit(X_train,y_train)
# y_predict_rf = model_rf.predict(X_val)
# accuracy_rf = (y_predict_rf == y_val).mean()
# print(f'随机森林验证准确率为：{accuracy_rf:.2%}')

from sklearn.model_selection import GridSearchCV
param_grid={'n_estimators':[50,100],'max_depth':[5,10]}
model_rf=RandomForestClassifier(random_state=42)
grid_search=GridSearchCV(model_rf,param_grid,cv=3)
grid_search.fit(X_train,y_train)
print('最佳参数：',grid_search.best_params_)
print('最佳模型准确率：',grid_search.best_score_.round(2))
best_model=grid_search.best_estimator_
y_predict=best_model.predict(X_val)



from sklearn.linear_model import LogisticRegression
model_lr = LogisticRegression(max_iter=1000)
model_lr.fit(X_train,y_train)
y_predict_lr = model_lr.predict(X_val)
accuracy_lr = (y_predict_lr == y_val).mean()
print(f'逻辑回归验证集准确率为：{accuracy_lr:.2%}')



from xgboost import XGBClassifier
model_xgb=XGBClassifier(random_state=42)
model_xgb.fit(X_train,y_train)
y_predict_xgb=model_xgb.predict(X_val)
accuracy_xgb=(y_predict_xgb == y_val).mean()
print(f'xgb的验证集准确率为：{accuracy_xgb:.2%}')



from sklearn.model_selection import cross_val_score
scores=cross_val_score(model_rf,X,y,cv=5)
print(f'交叉验证集准确率为：{scores.mean():.2%}(±{scores.std():.2%})')



# 加载处理后的测试集数据
test = pd.read_csv('featured_test.csv')

# 查看列名
print("测试集列名:", test.columns.tolist())

# 如果存在Survived列，删除它
if 'Survived' in test.columns:
    test = test.drop('Survived', axis=1)



# 用随机森林预测测试集
test_predict= best_model.predict(test)

# 生成提交文件（需保留PassengerId，这里假设之前删除了，建议从原始数据读取）
submission = pd.read_csv('test.csv')[['PassengerId']].copy()
submission['Survived'] = test_predict
submission.to_csv('submission.csv', index=False)


















