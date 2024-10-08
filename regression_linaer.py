import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.linear_model import LinearRegression


bedrooms = np.array([1,1,2,2,3,4,4,5,5,5,])
bedrooms = bedrooms.reshape(-1,1)

house_price = np.array([15000,20000,27000, 34000,50000, 68000, 65000, 81000, 85000,90000])

linreg = LinearRegression()
linreg.fit(bedrooms, house_price)


plt.scatter(bedrooms, house_price )
plt.plot(bedrooms, linreg.predict(bedrooms))

plt.show()

