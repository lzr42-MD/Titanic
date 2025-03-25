

import pandas as pd


train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

age_median=train['Age'].median()
train['Age']=train['Age'].fillna(age_median)
test['Age']=test['Age'].fillna(age_median)


def extract_cabin(cabin):
    if pd.isnull(cabin):
        return 'Unknown'
    else:
        return cabin[0]

train['Cabin'] = train['Cabin'].apply(extract_cabin)
test['Cabin'] = test['Cabin'].apply(extract_cabin)


embarked_mode=train['Embarked'].mode()[0]
train['Embarked']=train['Embarked'].fillna(embarked_mode)


drop_columns=['PassengerId','Ticket']
train=train.drop(drop_columns,axis=1)
test=test.drop(drop_columns,axis=1)


train.to_csv('cleaned_train.csv',index=False)
test.to_csv('cleaned_test.csv',index=False)





