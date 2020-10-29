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

def estimate_price(mileage, theta0, theta1):
    price = theta0 + (theta1 * mileage)
    return price

def predict(theta, x):
    xx = np.ones([x.shape[0], 2])
    xx[:,-1] = x
    y = xx.dot(theta)
    return y

def linear_regression(mileage, price, m, theta0, theta1, learning_rate, ntimes):
    m = float(m)
    x = mileage
    y = price
    mileage = (mileage-min(mileage))/(max(mileage)-min(mileage))
    price = (price-min(price))/(max(price)-min(price))
    for i in range(ntimes):
        yp = estimate_price(mileage, theta0, theta1)
        tmp_theta0 = learning_rate * 1/m * sum(yp - price)
        tmp_theta1 = learning_rate * 1/m * sum((yp - price) * mileage)
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    theta0 = theta0*(max(y)-min(y)) + min(y) + (theta1*min(x)*(min(y)-max(y)))/(max(x)-min(x))
    theta1 = theta1*(max(y)-min(y)) / (max(x)-min(x))
    return theta0, theta1

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
    yp = predict(theta, km)
    print(km)
    print(yp)
    
    lr = 0.2 #learning rate = alpha
    theta = linear_regression(km, price, km.size, theta[0], theta[1], 0.1, 10000)
    print(theta)

