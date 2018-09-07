#Linear Data

import numpy as np

x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

#Break

#Compute the same linear model using matrix multiplication

x_b = np.c_[np.ones((100, 1)), x]     #add x0 = 1 ro each instance
theta_best = np.linalg.inv(x_b.t.dot(x_b)).dot(x_b.t).dot(y)

>>>theta_best

#Break

#Make predictions using ^0

>>>x_new =np.array([[0], [2]])
>>>x_new_b = np.c_[np.ones((2, 1)), x_new]      #add x0 = 1 ro each instance
>>>y_predict = x_new_b.dot(theta_best)
>>>y_predict

#Plot the predictions

plt.plot(x_new, y_predict, "r-")
plt.plot(x, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

#The scikit-learn code for the same model

>>>from sklearn.linear_model import Linear_Regression
>>>lin_reg=Linear_Regression
>>>lin_reg.fit(x, y)
>>>lin_reg.intercept_, lin_reg.coef_

>>>lin_reg.predict(x_new)

#Break
