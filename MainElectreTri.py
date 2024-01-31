
import pandas as pd
import numpy as np
from numpy import random, vstack, empty
import PreProcess
import Process


# Import of data from csv file as a Pandas Dataframe
d = pd.read_csv('Input_data.csv')
P = 0 # trial and error
d['P'] = P
λ = 0.75
repetition = 1



# ELECTRE Tri application function
def Elec_tri(data, rep):
    """
    Function which capitalises ELECTRE_Tri calculations and repeats them
    a rep number of times

    PARAMETERS
    ----------
    data: Data Frame 
        Table with the input data and parameters
    rep: int
        Repetition of the method

    RETURNS
    ---------
    mopti: DataFrame
        Table with the percentage of the optimistic sorting of each alternative in each category
    mpessi: DataFrame
        Table with the percentage of the pessimistic sorting of each alternative in each category
    """

    pessi = np.zeros((9, 28))
    opti = np.zeros((9, 28))
    pessi_sort = pd.DataFrame(pessi, index=['C1', 'C1/C2', 'C2',
                                            'C2/C3', 'C3', 'C3/C4',
                                            'C4', 'C4/C5', 'C5'],
                              columns=['S1.1', 'S1.2', 'S1.3', 'S1.4',
                                       'S2.1', 'S2.2', 'S2.3', 'S2.4',
                                       'S3.1', 'S3.2', 'S3.3', 'S3.4',
                                       'S4.1', 'S4.2', 'S4.3', 'S4.4',
                                       'S5.1', 'S5.2', 'S5.3', 'S5.4',
                                       'S6.1', 'S6.2', 'S6.3', 'S6.4',
                                       'S7.1', 'S7.2', 'S7.3', 'S7.4'])
    opti_sort = pd.DataFrame(opti, index=['C1', 'C1/C2', 'C2',
                                          'C2/C3', 'C3', 'C3/C4',
                                          'C4', 'C4/C5', 'C5'],
                             columns=['S1.1', 'S1.2', 'S1.3', 'S1.4',
                                      'S2.1', 'S2.2', 'S2.3', 'S2.4',
                                      'S3.1', 'S3.2', 'S3.3', 'S3.4',
                                      'S4.1', 'S4.2', 'S4.3', 'S4.4',
                                      'S5.1', 'S5.2', 'S5.3', 'S5.4',
                                      'S6.1', 'S6.2', 'S6.3', 'S6.4',
                                      'S7.1', 'S7.2', 'S7.3', 'S7.4'])
    # repetitions
    for i in range(rep):
        newdata = PreProcess.MC(data)
        newdata.to_csv('newdata.csv')
        
        newref = PreProcess.refIntervals(data)
        
        dconca, dconcb = Process.conc(newdata, newref)
        dconca.to_csv('dconca.csv')
        dconcb.to_csv('dconcb.csv')
        
        ddisca, ddiscb = Process.disco(newdata, newref)
        ddisca.to_csv('ddisca.csv')
        ddiscb.to_csv('ddiscb.csv')
        
        dgconca = Process.gconc(newdata, dconca)
        dgconca.to_csv('dgconca.csv')
        
        dgconcb = Process.gconc(newdata, dconcb)
        dgconcb.to_csv('dgconcb.csv')
        
        dcreda = Process.credibility(dgconca, ddisca)
        dcreda.to_csv('dcreda.csv')
        
        dcredb = Process.credibility(dgconcb, ddiscb)
        dcredb.to_csv('dcredb.csv')
        
        dranking = Process.over_ranking_relations(dcreda, dcredb, λ)
        dranking.to_csv('dranking.csv')
        
        opti_sort = Process.optimistic_sort(dranking, opti_sort)
        pessi_sort = Process.pessimistic_sort(dranking, pessi_sort)
    pessi_sort = pessi_sort.apply(lambda x: (x / rep) * 100)  # %
    opti_sort = opti_sort.apply(lambda x: x / rep * 100)  # %
    return opti_sort, pessi_sort


o_sorting, p_sorting = Elec_tri(d, repetition)
o_sorting_transposed = o_sorting.transpose()
o_sorting_transposed['Total'] = 100
p_sorting_transposed = p_sorting.transpose()
p_sorting_transposed['Total'] = 100

# Creation of csv files containing the repartition of the scenarios
# in the categories as percentages
# p_sorting.to_csv('pessimistic_sorting.csv')
# o_sorting.to_csv('optimistic_sorting.csv')

"""
# Printing of the optimistic and pessimistic sorting
print("The optimistic sorting of the scenarios is:")
print(o_sorting_transposed)

print("The pessimistic sorting of the scenarios is:")
print(p_sorting_transposed)
"""
