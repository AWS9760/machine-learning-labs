x = [1, 2, 3]
y = [3, 5, 7]

theta0 = 0
theta1 = 0
alpha = 0.1
m = len(x)

predictions = [theta0 + theta1 * xi for xi in x]

errors = [predictions[i] - y[i] for i in range(m)]

cost = sum(e ** 2 for e in errors) / (2 * m)

grad_theta0 = sum(errors) / m
grad_theta1 = sum(errors[i] * x[i] for i in range(m)) / m

theta0_new = theta0 - alpha * grad_theta0
theta1_new = theta1 - alpha * grad_theta1

print("Predictions:", predictions)
print("Errors:", errors)
print("Cost:", cost)
print("Gradient theta0:", grad_theta0)
print("Gradient theta1:", grad_theta1)
print("Updated theta0:", theta0_new)
print("Updated theta1:", theta1_new)