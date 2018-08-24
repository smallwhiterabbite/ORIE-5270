from scipy.optimize import minimize
import random
import numpy as np


def rosenbrock_fun(x):
    """
    Compute Rosenbrick function with n=3 given x
    :param x: input vector
    :return: f(x) where f is the Rosenbrock function
    """
    return 100 * (x[2] - x[1] ** 2) ** 2 + (1 - x[1]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def rosenbrock_jac(x):
    """
    Calculate the gradient of Rosenbrock function
    :param x: input vector
    :return: gradient
    """
    return np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0]),
                     -400 * x[1] * (x[2] - x[1] ** 2) - 2 * (1 - x[1]) + 200 * (x[1] - x[0]**2),
                     200 * (x[2] - x[1] ** 2)])


if __name__ == '__main__':
    res = np.zeros(100)
    for i in range(100):
        x1 = random.randrange(-100, 100)
        x2 = random.randrange(-100, 100)
        x3 = random.randrange(-100, 100)
        x = np.array([x1, x2, x3])
        res[i] = minimize(rosenbrock_fun, x, method='BFGS', jac=rosenbrock_jac).fun
    print(min(res))
