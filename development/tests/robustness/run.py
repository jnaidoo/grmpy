"""This script replicates the estimation results from Cainero 2011 via the grmpy estimation method.
Additionally it returns a figure of the Marginal treatment effect based on the estimation results.
"""
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd
import numpy as np
import json

from grmpy.estimate.estimate_auxiliary import calculate_mte
from grmpy.estimate.estimate import estimate


def plot_est_mte(rslt, data_frame):
    """This function calculates the marginal treatment effect for different quartiles of the
    unobservable V. ased on the calculation results."""

    # Define the Quantiles and read in the original results
    quantiles = [0.0001] + np.arange(0.01, 1., 0.01).tolist() + [0.9999]
    mte_ = json.load(open('mte_original.json', 'r'))
    mte_original = mte_[1]
    mte_original_d = mte_[0]
    mte_original_u = mte_[2]

    # Calculate the MTE and confidence intervals
    mte = calculate_mte(rslt, data_frame, quantiles)
    mte = [i / 4 for i in mte]
    mte_up, mte_d = calculate_cof_int(rslt, data_frame, mte, quantiles)
    # Plot both curves
    ax = plt.figure().add_subplot(111)

    ax.set_ylabel(r"$B^{MTE}$")
    ax.set_xlabel("$u_S$")
    ax.plot(quantiles, mte, label='grmpy MTE', color='blue')
    ax.plot(quantiles, mte_up, color='blue', linestyle=':')
    ax.plot(quantiles, mte_d, color='blue', linestyle=':')
    ax.plot(quantiles, mte_original, label='original MTE', color='red')
    ax.plot(quantiles, mte_original_d, color='red', linestyle=':')
    ax.plot(quantiles, mte_original_u, color='red', linestyle=':')

    ax.set_ylim([-0.4, 0.5])

    plt.legend()

    plt.tight_layout()
    plt.savefig('fig-marginal-benefit-parametric-replication.png')
    return mte


def calculate_cof_int(rslt, data_frame, mte, quantiles):
    """This function calculates the confidence interval of the marginal treatment effect."""

    # Import parameters and inverse hessian matrix
    hess_inv = rslt['AUX']['hess_inv'] / data_frame.shape[0]
    params = rslt['AUX']['x_internal']

    # Distribute parameters
    dist_cov = hess_inv[-4:, -4:]
    param_cov = hess_inv[:46, :46]
    dist_gradients = np.array([params[-4], params[-6], params[-2], params[-3]])

    # Process data
    covariates = [rslt['varnames'][j - 1] for j in rslt['TREATED']['order']]
    x = np.mean(data_frame[covariates]).tolist()
    x_neg = [-i for i in x]
    x += x_neg
    x = np.array(x)

    # Create auxiliary parameters
    part1 = np.dot(x, np.dot(param_cov, x))
    part2 = np.dot(dist_gradients, np.dot(dist_cov, dist_gradients))

    # Prepare two lists for storing the values
    mte_up = []
    mte_d = []

    # Combine all auxiliary parameters and calculate the confidence intervals
    for counter, i in enumerate(quantiles):
        value = part2 * (norm.ppf(i)) ** 2
        aux = np.sqrt(part1 + value) / 4
        mte_up += [mte[counter] + norm.ppf(0.95) * aux]
        mte_d += [mte[counter] - norm.ppf(0.95) * aux]
    print(mte_up, mte_d)

    return mte_up, mte_d


if __name__ == '__main__':

    filename = 'fig-marginal-benefit-parametric-replication.png'

    # Estimate the coefficients
    rslt = estimate('replication.grmpy.ini')

    # Calculate and plot the marginal treatment effect
    data = pd.read_pickle('aer-replication-mock.pkl')
    mte = plot_est_mte(rslt, data)
