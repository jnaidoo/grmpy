"""The module provides a random dictionary generating process for test purposes."""
import uuid

from scipy.stats import wishart
import numpy as np


def constraints(probability=0.1, is_zero=True, agents=None, seed=None, maxfun=None, sample=None):
    """The constraints function returns an dictionary that provides specific characteristics for the
    random dictionary generating process.
    """
    constraints_dict = dict()
    constraints_dict['DETERMINISTIC'] = np.random.random_sample() < probability
    if not constraints_dict['DETERMINISTIC'] and is_zero:
        constraints_dict['IS_ZERO'] = np.random.random_sample() < probability / (1 - probability)
    else:
        constraints_dict['IS_ZERO'] = False
    if agents is None:
        constraints_dict['AGENTS'] = np.random.randint(1, 1000)
    else:
        constraints_dict['AGENTS'] = agents
    if seed is None:
        constraints_dict['SEED'] = np.random.randint(1, 10000)
    else:
        constraints_dict['SEED'] = seed
    if maxfun is None:
        constraints_dict['MAXFUN'] = np.random.randint(0, 100)
    else:
        constraints_dict['MAXFUN'] = maxfun
    if sample is None:
        if constraints_dict['AGENTS'] != 1:
            constraints_dict['SAMPLE_SIZE'] = np.random.randint(1, constraints_dict['AGENTS'])
        else:
            constraints_dict['SAMPLE_SIZE'] = 1
    else:
        constraints_dict['SAMPLE_SIZE'] = sample

    return constraints_dict


def generate_random_dict(constraints_dict=None):
    """The function generates a random initialization dictionary."""

    if constraints_dict is not None:
        assert isinstance(constraints_dict, dict)
    else:
        constraints_dict = constraints()

    is_deterministic = constraints_dict['DETERMINISTIC']

    is_zero = constraints_dict['IS_ZERO']

    agents = constraints_dict['AGENTS']

    seed = constraints_dict['SEED']

    maxfun = constraints_dict['MAXFUN']

    agents_sample = constraints_dict['SAMPLE_SIZE']

    source = my_random_string(8)

    dict_ = {}
    treated_num = np.random.randint(1, 10)
    cost_num = np.random.randint(1, 10)
    # Coefficients
    for key_ in ['UNTREATED', 'TREATED', 'COST']:

        dict_[key_] = {}

        if key_ in ['UNTREATED', 'TREATED']:
            dict_[key_]['coeff'], dict_[key_]['types'] = generate_coeff(treated_num, key_, is_zero)
            if key_ == 'TREATED':
                dict_[key_]['types'] = dict_['UNTREATED']['types']
        else:
            dict_[key_]['coeff'], dict_[key_]['types'] = generate_coeff(cost_num, key_, is_zero)

    # Simulation parameters
    dict_['SIMULATION'] = {}
    for key_ in ['agents', 'source', 'seed']:
        if key_ == 'seed':
            dict_['SIMULATION'][key_] = seed
        elif key_ == 'agents':
            dict_['SIMULATION'][key_] = agents
        else:
            dict_['SIMULATION'][key_] = source
    # Estimation parameters
    dict_['ESTIMATION'] = {}
    for key_ in ['agents', 'file', 'maxfun', 'optimizer', 'gtol']:
        if key_ == 'agents':
            dict_['ESTIMATION'][key_] = agents_sample
        elif key_ == 'file':
            dict_['ESTIMATION'][key_] = source + '.grmpy.txt'
        elif key_ == 'maxfun':
            dict_['ESTIMATION'][key_] = maxfun
        elif key_ == 'gtol':
            dict_['ESTIMATION'][key_] = np.random.uniform(0.001, 0.002)
        else:
            dict_['ESTIMATION'][key_] = 'SCIPY-BFGS'

    # Variance and covariance parameters
    dict_['DIST'] = {}
    if not is_deterministic:
        x = np.identity(3)
        b = wishart.rvs(df=10, scale=x, size=1, random_state=seed)
    else:
        b = np.zeros((3, 3))
    dict_['DIST']['coeff'] = []
    dict_['DIST']['coeff'].append(b[0, 0] ** 0.5)
    dict_['DIST']['coeff'].append(b[0, 1])
    dict_['DIST']['coeff'].append(b[0, 2])
    dict_['DIST']['coeff'].append(b[1, 1] ** 0.5)
    dict_['DIST']['coeff'].append(b[2, 1])
    dict_['DIST']['coeff'].append(b[2, 2] ** 0.5)
    print_dict(dict_)
    return dict_


def print_dict(dict_, file_name='test'):
    """The function creates an init file from a given dictionary."""
    labels = ['SIMULATION', 'ESTIMATION', 'TREATED', 'UNTREATED', 'COST', 'DIST']
    write_nonbinary = np.random.random_sample() < 0.5
    with open(file_name + '.grmpy.ini', 'w') as file_:

        for label in labels:

            file_.write(label + '\n\n')

            if label in ['SIMULATION', 'ESTIMATION']:
                if label == 'SIMULATION':
                    structure = ['agents', 'seed', 'source']
                else:
                    structure = ['agents', 'optimizer', 'maxfun', 'gtol', 'file']

                for key_ in structure:
                    if key_ in ['source', 'file', 'optimizer']:
                        str_ = '{0:<25} {1:20}\n'
                        file_.write(str_.format(key_, dict_[label][key_]))
                    elif key_ == 'gtol':
                        str_ = '{0:<13} {1:20.6f}\n'
                        file_.write(str_.format(key_, dict_[label][key_]))
                    else:
                        str_ = '{0:<10} {1:20}\n'
                        file_.write(str_.format(key_, dict_[label][key_]))

            elif label in ['TREATED', 'UNTREATED', 'COST', 'DIST']:
                for i in range(len(dict_[label]['coeff'])):
                    if 'types' in dict_[label].keys():
                        if isinstance(dict_[label]['types'][i], list):
                            str_ = '{0:<10} {1:20.4f} {2:>18} {3:5.4f}\n'
                            file_.write(
                                str_.format(
                                    'coeff', dict_[label]['coeff'][i], dict_[label]['types'][i][0],
                                    dict_[label]['types'][i][1])
                            )

                        else:
                            if write_nonbinary:
                                str_ = '{0:<10} {1:20.4f} {2:>18}\n'
                                file_.write(str_.format('coeff', dict_[label]['coeff'][i],
                                                        dict_[label]['types'][i]))
                            else:
                                str_ = '{0:<10} {1:20.4f}\n'
                                file_.write(str_.format('coeff', dict_[label]['coeff'][i]))

                    else:
                        str_ = '{0:<10} {1:20.4f}\n'
                        file_.write(str_.format('coeff', dict_[label]['coeff'][i]))
            file_.write('\n')


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]


def generate_coeff(num, key_, is_zero):
    """The function generates random coefficients for creating the random init dictionary."""
    if not is_zero:
        list_ = np.random.normal(0., 2., [num]).tolist()
        if key_ in ['UNTREATED', 'COST']:
            binary_list = ['nonbinary'] * num
            for i in range(len(binary_list)):
                if np.random.random_sample() < 0.1:
                    if i is not 0:
                        frac = np.random.uniform(0, 1)
                        binary_list[i] = ['binary', frac]
        else:
            binary_list = []
    else:
        binary_list = ['nonbinary'] * num
        list_ = np.array([0] * num).tolist()

    return list_, binary_list
