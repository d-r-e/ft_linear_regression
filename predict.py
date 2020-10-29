#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/22 19:04:55 by darodrig          #+#    #+#              #
#    Updated: 2020/10/22 19:54:59 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import numpy as np

def estimate_price(theta, mileage):
    price = theta[0] + theta[1] * mileage
    return price

if __name__ == "__main__":
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
        
    mileage = float(input("Please enter mileage: "))
    price = estimate_price(theta, mileage)
    print(f'Predicted price: {price}')
