#! /usr/bin/env python3 
import numpy as np

if __name__ == "__main__":
	theta = np.zeros(2)
	mileage = float(input("Please enter mileage: "))
	price = theta[0] + theta[1] * mileage
	print(price)
