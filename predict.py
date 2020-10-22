#! /usr/bin/env python3
import numpy as np

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
    price = theta[0] + theta[1] * mileage
    print(f'Predicted price: {price}')
