#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/22 19:55:00 by darodrig          #+#    #+#              #
#    Updated: 2020/10/22 19:55:01 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import numpy as np
import pandas as pd

def estimate_price(theta, mileage):
    price = theta[0] + theta[1] * mileage
    return price

def predict(theta, x):
    xx = np.ones([x.shape[0], 2])
    xx[:,-1] = x
    y = xx.dot(theta)
    return y

def fit(theta, X, Y, learning_rate, n_cycle):
    price = X
    if type(theta) != np.ndarray or theta.size == 0:
        print("mismatching types")
        print(type(theta) + " != np.ndarray")
        return None
    if type(X) != np.ndarray or X.size == 0:
        print(type(X))
        print("Incorrect X array")
        return None
    if type(Y) != np.ndarray or Y.size == 0:
        print("Incorrect Y array")
        return None
    ones = np.ones((X.shape[0], 2))
    ones[:,-1] = X
    m = theta.size
    
    theta0 = theta[0]
    theta1 = theta[1]
    for i in range(0, n_cycle):
        hypothesis = estimate_price(theta, X)
        tmp_theta0 = learning_rate * 1/m * sum(hypothesis - price)
        tmp_theta1 = learning_rate * 1/m * sum((hypothesis - price) * X)
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    theta[0] = theta0
    theta[1] = theta1
    return theta

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    km = np.array(df['km'])
    price = np.array(df['price'])
    try:
        filename = "theta.txt"
        f = open(filename, "r")
        theta = np.zeros(2)
        theta[0] = float(f.readline())
        theta[1] = float(f.readline())
        f.close()
    except:
        print(f"Error: \"{filename}\" file not found or wrong format.")
        exit(0)
    print(km.shape)
    y = predict(theta, km)
    print(km)
    print(y)
    lr = 0.2 #learning rate = alpha
    theta = fit(theta, km, y, lr, 1)
    print(theta)
    #WIP
