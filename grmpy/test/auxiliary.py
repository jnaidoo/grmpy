"""The module provides basic auxiliary functions for the test modules."""
import shlex
import glob
import os


def cleanup(options=None):
    """The function deletes package related output files."""
    fnames = glob.glob("*.grmpy.*")

    if options is None:
        for f in fnames:
            os.remove(f)
    elif options == 'regression':
        for f in fnames:
            if f.startswith('regression'):
                pass
            else:
                os.remove(f)
    elif options == 'init_file':
        for f in fnames:
            if f.startswith('test.grmpy'):
                pass
            else:
                os.remove(f)


def read_desc(fname):
    """The function reads the descriptives output file and returns a dictionary that contains the
    relevant parameters for test6 in test_integration.py.
    """
    dict_ = {}
    with open(fname, 'r') as handle:
        for i, line in enumerate(handle):
            list_ = shlex.split(line)
            if 7 <= i < 10:
                if list_[0] in ['All', 'Treated', 'Untreated']:
                    dict_[list_[0]] = {}
                    dict_[list_[0]]['Number'] = list_[1:]
            elif 20 <= i < 23:
                if list_[0] == 'Observed':
                    dict_['All'][list_[0] + ' ' + list_[1]] = list_[2:]
                else:
                    dict_['All'][list_[0] + ' ' + list_[1] + ' ' + list_[2]] = list_[3:]
            elif 29 <= i < 32:
                if list_[0] == 'Observed':
                    dict_['Treated'][list_[0] + ' ' + list_[1]] = list_[2:]
                else:
                    dict_['Treated'][list_[0] + ' ' + list_[1] + ' ' + list_[2]] = list_[3:]
            elif 38 <= i < 41:
                if list_[0] == 'Observed':
                    dict_['Untreated'][list_[0] + ' ' + list_[1]] = list_[2:]
                else:
                    dict_['Untreated'][list_[0] + ' ' + list_[1] + ' ' + list_[2]] = list_[3:]

        # Process the string in int and float values
        for key_ in dict_.keys():

            dict_[key_]['Number'] = [int(i) for i in dict_[key_]['Number']]
            for subkey \
                    in ['Observed Sample', 'Simulated Sample (finish)', 'Simulated Sample (start)']:
                dict_[key_][subkey] = [float(j) for j in dict_[key_][subkey]]

    return dict_
