
import pandas as pd
import numpy as np
from numpy import random, vstack, empty



# Monte Carlo Function
def MC(data):
    """
    Build a new performance matrix from the distribution
    with m : mean value and v : variance per criterion

    PARAMETERS
    ----------
    data: Data Frame 
    Table with input data and parameters

    RETURNS
    ---------
    ndata: Data frame 
    Table with the new performance Data Frame with random value picked
    in the distribution
    """
    ndata = data.copy()
    variance = ndata['VAR'].values  # general variance located in the column "VAR"
    m = ndata.iloc[:, 0:28].values  # for each scenario : columns 0 to 27
    v = np.abs(m * variance[:, np.newaxis])  # variance v of the performance matrix
    perf = np.random.normal(m, v)  # random value in the normal distribution
    ndata.iloc[:, 0:28] = perf
    return ndata


# Reference profiles matrix
def refIntervals(data):
    """
    Build a reference matrix from the reference profiles of the input data

    PARAMETERS
    ----------
    data : Data Fram
        Table with input data and parameters

    RETURNS
    -------
    nref : Data Frame
        Table with the reference Data Frame
    """
    nref_intermediate = pd.DataFrame(index=['g1.1', 'g1.2', 'g1.3', 'g1.4', 'g1.5',
                                'g2.1', 'g2.2', 'g2.3', 'g2.4',
                                'g3.1', 'g3.2', 'g3.3', 'g3.4',
                                'g4.1', 'g4.2', 'g4.3'],
                         columns=['b0_min', 'b0_max',
                                  'b1_min', 'b1_max',
                                  'b2_min', 'b2_max',
                                  'b3_min', 'b3_max',
                                  'b4_min', 'b4_max',
                                  'b5_min', 'b5_max'])
    
    nref = pd.DataFrame(index=['g1.1', 'g1.2', 'g1.3', 'g1.4', 'g1.5',
                                'g2.1', 'g2.2', 'g2.3', 'g2.4',
                                'g3.1', 'g3.2', 'g3.3', 'g3.4',
                                'g4.1', 'g4.2', 'g4.3'],
                         columns=['b0_max',
                                  'b1_min', 'b1_max',
                                  'b2_min', 'b2_max',
                                  'b3_min', 'b3_max',
                                  'b4_min', 'b4_max',
                                  'b5_min'])
    P = data['P'].values  # general interval located in the column "P"
    bk = data.iloc[:, 30:36].values  # for each reference profile : columns 30 to 35
    bk_min = bk - bk*P[:, np.newaxis]
    bk_max = bk + bk*P[:, np.newaxis]

    # new reference matrix of bk_min and bk_max
    for k in range(bk_min.shape[1]):
            nref_intermediate.iloc[:,  2*k] = bk_min[:, k]
            nref_intermediate.iloc[:,  2*k+1] = bk_max[:, k]
    nref_intermediate.iloc[6, 6:12] = 1  # g2.2 is a YES/NO criterion, the interval cannot be applied --> à faire + proprement avec original ref.
    columns_to_delete = ['b0_min', 'b5_max']
    nref = nref_intermediate.drop(columns=columns_to_delete)
    nref.to_csv('new_ref_matrix.csv')
    return nref
