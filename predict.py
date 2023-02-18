import json
import pandas as pd
import os.path

def extract_values():
    with open('data/args.json', 'r') as json_file:
        data = json.load(json_file)
    theta0 = data['theta0']
    theta1 = data['theta1']

    return theta0, theta1

if __name__ == "__main__":
    try:
        mileage = float(input('Enter mileage to predict: '))
    except KeyboardInterrupt:
        print('Interrupted by user')
        exit(0)
    if (os.path.exists('data/args.json')):
        theta0, theta1 = extract_values()
    else:
        theta0 = 0
        theta1 = 0
    print(f'price prediction: {theta0 + (theta1 * mileage)}')
