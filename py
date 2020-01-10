import panda as pd
from sklearn.preprecessing import LabelEncoder, OneHotEncoder, StandardScaler
data = pd.read_csv('listA.csv')
data.iloc[:,:]
le = LabelEncoder()
data[:, 8] = le.fit_transform(data[:, 8])
