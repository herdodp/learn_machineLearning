import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


#baca data csv
data = pd.read_csv('C:/Users/herdodp/Documents/learn_python/gigi.csv')

#menghapus id
data.drop('nomor', axis=1, inplace=True)

#memisahkan label dan attribute
x = [['tinggi', 'lebar', 'panjang_akar']]
y = [['label']]

#membagi menjadi data train dan data test
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.1, random_state=123)


#membuat decision tree
tree = DecisionTreeClassifier()
tree = tree.fit(x_train, y_train)

predict = tree.predict(x_test)

score = round(accuracy_score(predict,y_test),3)

print(score)





data.info()
data.head()