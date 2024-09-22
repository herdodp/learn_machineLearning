import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import linear_model


#membaca data csv
df  = pd.read_csv('C:/Users/herdodp/Documents/learn_python/Social_Network_Ads.csv')

#menghilangkan Id karena tidak diperlukan
data = df.drop(columns=['User ID'])

#proses one-hot ecnoding dengna pd.get_dummies()
data  = pd.get_dummies(data, dtype='int')
data

#pisahkan atribut dan label
predictions = ['Age', 'EstimatedSalary', 'Gender_Female', 'Gender_Male']
x = data[predictions]
y = data['Purchased']

#lakukan normalisasi terhadap data yang kita miliki
scaler = StandardScaler()
scaler.fit(x)
scaled_data = scaler.transform(x)
scaled_data = pd.DataFrame(scaled_data, columns = x.columns)
scaled_data.head()

#bagi data menjadi data train dan data test untuk setiap atribut dan label
x_train, x_test, y_train, y_test = train_test_split(scaled_data, y, test_size=0.2, random_state=123)

#latih model dengan fungsi fit
model = linear_model.LogisticRegression()
model.fit(x_train, y_train)

#uji akurasi model
print(model.score(x_test, y_test))




#df.info()
#df.head()