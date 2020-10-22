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

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    km = np.array(df['km'])
    price = np.array(df['price'])
    print("KM:")
    print(km)
    print("Price:")
    m = km.size
    lr = 0.2 #learning rate
    theta = np.zeros(2)
    phi = 0
    for i in range(m):
        phi += estimate_price(theta, km[i] - price[i])
    print(phi)
        
    print(m)
