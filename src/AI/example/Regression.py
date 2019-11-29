# -*- utf-8 -*-
import numpy as np

from src.AI.tools.plot import plotTask

x = np.zeros((100, 2), dtype=np.float16, order='C')


# ["12.23", "23.34"] => [12.23, 23.34]
def trans_list_str_data_to_float(data) -> list:
    result = []
    for i in data:
        result.append(float(i))
    return result


def line_clean(_line) -> str:
    result = _line.replace("\r\n", '')
    return result


with open('ex1data1.txt', 'rb') as file:
    line = file.readline()
    pos = 0
    while line is not None and line is not "" and line.__len__() != 0:
        line_data = str(line, encoding="utf8")
        line_data = line_clean(line_data)
        x[pos] = trans_list_str_data_to_float(line_data.split(","))
        line = file.readline()
        pos += 1
    # slice array
    x = x[0:pos]


def normalization(data):
    result = data
    for i in range(pos):
        for j in range(2):
            result[i][j] = (data[i][j] - data[:, j].min()) / (data[:, j].max() - data[:, j].min())
    return result


unnormalized = np.copy(x)
x = normalization(x)
plot = plotTask().init()
plot.draw(points=x)

# theta
# h(theta) = theta(0) + theta(1) * x
theta = np.ones((2, 1), dtype=np.float16, order='C')
# theta.shape = (2, 1)


# m = pos
m = pos

# learning rate
alpha = 0.01

# gradient times 100
for i in range(5000):
    # simultaneously upgrade theta vector
    theta_tmp = np.zeros((2, 1), dtype=np.float16, order='C')
    # J(theta)
    # j = h = np.dot(theta.T, x_tmp)
    x_1 = x[:, 0]
    ones = np.ones(pos, dtype=np.float16, order='C')
    x_tmp = np.asarray([ones, x_1])
    h = np.dot(theta.T, x_tmp)
    print(theta)
    for j in range(2):
        sum = 0
        for count in range(pos):
            t = h[0][count] - x[:, 1][count]
            sum += t * x_tmp.T[count][j]
        theta_tmp[j][0] = theta[j][0] - (alpha * sum / m)
    # last_j_theta =
    theta = theta_tmp
    h = np.dot(theta.T, x_tmp)
    for count in range(pos):
        t = h[0][count] - x[:, 1][count]
        sum += t * t
    J = (1 / (2 * m)) * sum
    print(J)

_x = np.arange(0, 1, 0.01)
_y = theta[0][0] + _x * theta[1][0]
plot.draw(points=x, lines=[(_x, _y)])
