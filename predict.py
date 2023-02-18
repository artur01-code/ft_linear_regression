import json
import pandas as pd
import os.path
import matplotlib.pyplot as plt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def extract_values():
    with open('data/args.json', 'r') as json_file:
        data = json.load(json_file)
    theta0 = data['theta0']
    theta1 = data['theta1']

    return theta0, theta1

if __name__ == "__main__":
    print(bcolors.HEADER + "----------------------------------------------------------------")
    print("Welcome to the price prediction program")
    print("----------------------------------------------------------------" + bcolors.ENDC)
    try:
        mileage = float(input('Enter mileage to predict: '))
    except KeyboardInterrupt:
        print('Interrupted by user')
        exit(0)
    if (mileage <= 0):
        print('Mileage must be a positive number')
        exit(0)
    if (os.path.exists('data/args.json')):
        theta0, theta1 = extract_values()
    else:
        theta0 = 0
        theta1 = 0
    print(f'price prediction: {theta0 + (theta1 * mileage)}')
    print("\n\n")
