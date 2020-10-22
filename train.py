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
    xx = np.zeros([x.shape[0], 2])
    xx[:,-1] = x
    y = xx.dot(theta)
    return y

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
    y = predict(theta, km)
    m = km.size
    lr = 0.2 #learning rate
    #WIP
