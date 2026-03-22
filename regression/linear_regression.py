import numpy as np

X=np.array([1,2,3,4])

y=np.array([2,4,6,8])

w=0
b=0

learning_rate = 0.01
epochs = 1000

n = len(X)

for i in range(epochs):
    y_pred = w * X + b
    dw = (-2/n) * np.sum(X*(y-y_pred))
    db = (-2/n) * np.sum(y-y_pred)

    w = w - learning_rate * dw
    b = b - learning_rate * db

print("Weight:",w)
print("Bias:",b)

x_new = 5

prediction = w * x_new + b

print("Prediction:",prediction)


