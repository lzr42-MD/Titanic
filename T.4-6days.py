# 一次性完成所有特征工程
import pandas as pd

# 读取清洗后的数据（第1-3天生成的文件）
train = pd.read_csv('cleaned_train.csv')
test = pd.read_csv('cleaned_test.csv')



train['Title']=train['Name'].str.split(', ',expand=True)[1].str.split('.',expand=True)[0]
test['Title']=test['Name'].str.split(', ',expand=True)[1].str.split('.',expand=True)[0]
common_titles=['Mr','Miss','Mrs','Master']
train['Title']=train['Title'].apply(lambda x:x if x in common_titles else 'Others')
test['Title']=test['Title'].apply(lambda x:x if x in common_titles else 'Others')

train = train.drop('Name', axis=1)  # 添加这行到特征工程代码中
test = test.drop('Name', axis=1)



train['FamilySize']=train['SibSp']+train['Parch']+1
test['FamilySize']=test['SibSp']+test['Parch']+1



fare_bins=pd.qcut(train['Fare'],q=3,retbins=True)[1]
train['FareCategory']=pd.cut(train['Fare'],bins=fare_bins,labels=['Low','Medium','High'])
test['FareCategory']=pd.cut(test['Fare'],bins=fare_bins,labels=['Low','Medium','High'])



categorical_cols=['Sex','Embarked','Title','Cabin','FareCategory']
train_encoded=pd.get_dummies(train,columns=categorical_cols)
test_encoded=pd.get_dummies(test,columns=categorical_cols)

all_columns=set(train_encoded.columns).union(set(test_encoded.columns))
train_encoded=train_encoded.reindex(columns=all_columns,fill_value=0)
test_encoded=test_encoded.reindex(columns=all_columns,fill_value=0)



bins=[0,12,30,50,100]
labels=['Child','Youth','Middle','Elder']
train['AgeGroup']=pd.cut(train['Age'],bins=bins,labels=labels)
test['AgeGroup']=pd.cut(test['Age'],bins=bins,labels=labels)



train_encoded.to_csv('featured_train.csv',index=False)
test_encoded.to_csv('featured_test.csv',index=False)

