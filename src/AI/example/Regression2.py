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


plot = plotTask().init()
x = normalization(x)
plot.draw(points=x)

d = 11

# theta
# h(theta) = theta(0) + theta(1) * x
theta = np.ones((d + 1, 1), dtype=np.float16, order='C')
# theta.shape = (2, 1)


# m = pos
m = pos

# learning rate
alpha = 0.3

J = 999999
# gradient times 100
for i in range(10000):
    # simultaneously upgrade theta vector
    theta_tmp = np.zeros((d + 1, 1), dtype=np.float16, order='C')
    # J(theta)
    # j = h = np.dot(theta.T, x_tmp)
    x_1 = x[:, 0]
    ones = np.ones(pos, dtype=np.float16, order='C')
    new_x = []
    new_x.append(ones)
    for d_p in range(d):
        new_x.append(x[:, 0] ** (d_p + 1))
    x_tmp = np.asarray(new_x)
    h = np.dot(theta.T, x_tmp)
    for j in range(d + 1):
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
    J_last = J
    J = (1 / (2 * m)) * sum
    if abs(J_last - J) < 0.0000001:
        print("finish")
        break

_x = np.arange(0, 1, 0.01)
_y = theta[0][0]
for d_p in range(d):
    print(theta[d_p + 1][0])
    print(d_p + 1)
    _y += theta[d_p + 1][0] * (_x ** (d_p + 1))
plot.draw(points=x, lines=[(_x, _y)])
