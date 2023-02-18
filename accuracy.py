import numpy as np

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

#https://en.wikipedia.org/wiki/Root-mean-square_deviation

if __name__ == "__main__":
    print(bcolors.HEADER + "----------------------------------------------------------------")
    print("Welcome to the RMSE program")
    print("----------------------------------------------------------------" + bcolors.ENDC)

    # Define the estimatePrice function
    def estimatePrice(theta0, theta1, mileage):
        return theta0 + theta1 * mileage

    # Load the trained theta values from the file
    theta = np.loadtxt('theta_values.txt', delimiter=',')

    # Load the test data
    test_data = np.genfromtxt('data/data.csv', delimiter=',', skip_header=1)

    # Separate the test mileage and price data into separate arrays
    test_mileage = test_data[:, 0]
    test_price = test_data[:, 1]

    # Calculate the predicted prices using the trained theta values
    predicted_prices = estimatePrice(theta[0], theta[1], test_mileage)

    # Calculate the root mean squared error (RMSE)
    rmse = np.sqrt(np.mean((predicted_prices - test_price) ** 2))

    # Print the RMSE
    print('The root mean squared error (RMSE) is:', rmse)
    print("\n\n")
