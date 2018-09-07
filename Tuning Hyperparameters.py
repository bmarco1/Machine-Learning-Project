#Fine tune hyperparameters

#Create a confusion matrix by first calling for a cross_val_predict()

>>>y_train_pred = cross_val_predict(sgd_clf, x_train_scaled, y_train, cv=3)
>>>conf_mx = confusion_matrix(y_train, y_train_pred)
>>>conf_mx

#use matshow() to display an easier to read model

plt.matshow(conf_mx, cmap=plt.cm.gray)
plt.show()

#compare error rates instead fo absolute error by dividing each value in the matrix by the number of images

row_sums = conf_mx.sum(axis=1, keepdims=True)
norm_conf_mx = conf_mx / row_sums

#Use this to fill zeros and keep only errors

np.fill_diagonal(norm_conf_mx, 0)
plt.matshow(norm_conf_mx, cmap=plt.cm.gray)
plt.show()

cl_a, cl_b = 3, 5
x_aa = x_train[(y_train == cl_a) & (y_train_pred ==cl_a)]
x_ab = x_train[(y_train == cl_a) & (y_train_pred ==cl_b)]
x_ba = x_train[(y_train == cl_b) & (y_train_pred ==cl_a)]
x_bb = x_train[(y_train == cl_b) & (y_train_pred ==cl_b)]

plt.subplot(221); plot_digits(x_aa[:25], images_per_row)
plt.subplot(222); plot_digits(x_ab[:25], images_per_row)
plt.subplot(223); plot_digits(x_ba[:25], images_per_row)
plt.subplot(224); plot_digits(x_bb[:25], images_per_row)
plt.show()

#Break
