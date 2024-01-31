
import pandas as pd
import numpy as np
from numpy import random, vstack, empty

# Partial concordance
def conc(data, ref):
    """
    Calculates the concordance coefficient between a performance and a profile

    PARAMETERS
    ----------
    data: Data Frame 
        Table with input data and parameters
    ref: Data Frame 
        Table with reference profiles

    RETURNS
    ---------
    Cab: DataFrame 
        Table with concordance Cj(ai,bk) of each alternative ai
        regarding each profile bk for each criterion j
    Cba: DataFrame 
        Table with concordance Cj(bk,ai) of each profile bk
        regarding each alternative ai for each criterion j
    """
    Cab = pd.DataFrame()
    Cba = pd.DataFrame()
    for sc in data.iloc[:, 0:28]:  # for each scenario : columns 0 to 27
        for pr in range(ref.shape[1]):  # for each reference profile
            alpha = (data[sc] - ref.iloc[:, pr] + data.iloc[:, 37]) \
                / (data.iloc[:, 37] - data.iloc[:, 36])
            beta = (ref.iloc[:, pr] - data[sc] + data.iloc[:, 37]) \
                / (data.iloc[:, 37] - data.iloc[:, 36])
            Cab = pd.concat([Cab, alpha], axis=1, ignore_index=True)
            Cba = pd.concat([Cba, beta], axis=1, ignore_index=True)
    Cab[Cab < 0] = 0
    Cab[Cab > 1] = 1
    Cba[Cba < 0] = 0
    Cba[Cba > 1] = 1
    return Cab, Cba


# Discordance
def disco(data, ref):
    """
    Calculates the discordance coefficient between a performance and a profile

     PARAMETERS
    ----------
    data: Data Frame 
        Table with input data and parameters
    ref: Data Frame 
        Table with reference profiles

    RETURNS
    ---------
    Dab: DataFrame 
        Table with discordance Dj(ai,bk) of each alternative ai
        regarding each profile bk for each criterion j
    Dba: DataFrame 
        Table with discordance Dj(bk,ai) of each profile bk
        regarding each alternative ai for each criterion j
    """
    Dab = pd.DataFrame()
    Dba = pd.DataFrame()
    for sc in data.iloc[:, 0:28]:  # for each scenario : columns 0 to 27
        for pr in range(ref.shape[1]):  # for each reference profile
            alpha = (ref.iloc[:, pr] - data[sc] - data.iloc[:, 37]) / (
                    data.iloc[:, 38] - data.iloc[:, 37])
            beta = (data[sc] - ref.iloc[:, pr] - data.iloc[:, 37]) / (
                    data.iloc[:, 38] - data.iloc[:, 37])
            Dab = pd.concat([Dab, alpha], axis=1, ignore_index=True)
            Dba = pd.concat([Dba, beta], axis=1, ignore_index=True)
    Dab[Dab < 0] = 0
    Dab[Dab > 1] = 1
    Dba[Dba < 0] = 0
    Dba[Dba > 1] = 1
    return Dab, Dba


# Global concordance
def gconc(data, dconc1):
    """
    Calculates the global concordance

    PARAMETERS
    ----------
    data: Data Frame 
        Table with input data and parameters
    dconc1: DataFrame
        Table with the partial concordance 

    RETURNS
    ---------
    new_df: DataFrame
        Table with the global concordance
    """
    new_df = pd.DataFrame(index=['b0_max',
                                 'b1_min', 'b1_max',
                                 'b2_min', 'b2_max',
                                 'b3_min', 'b3_max',
                                 'b4_min', 'b4_max',
                                 'b5_min'],
                          columns=['S1.1', 'S1.2', 'S1.3', 'S1.4',
                                   'S2.1', 'S2.2', 'S2.3', 'S2.4',
                                   'S3.1', 'S3.2', 'S3.3', 'S3.4',
                                   'S4.1', 'S4.2', 'S4.3', 'S4.4',
                                   'S5.1', 'S5.2', 'S5.3', 'S5.4',
                                   'S6.1', 'S6.2', 'S6.3', 'S6.4',
                                   'S7.1', 'S7.2', 'S7.3', 'S7.4'])
    i = 0
    for j in range(0, len(dconc1.columns), 10):  # for each scenario : one line out of 10 (10 reference profiles)
        # C(ai,bk) for the scenario for each reference profile
        # b0min = sum(dconc1[j] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b0max = sum(dconc1[j] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b1min = sum(dconc1[j + 1] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b1max = sum(dconc1[j + 2] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b2min = sum(dconc1[j + 3] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b2max = sum(dconc1[j + 4] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b3min = sum(dconc1[j + 5] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b3max = sum(dconc1[j + 6] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b4min = sum(dconc1[j + 7] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b4max = sum(dconc1[j + 8] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        b5min = sum(dconc1[j + 9] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        # b5max = sum(dconc1[j + 11] * data.iloc[:, 28]) / sum(data.iloc[:, 28])
        th = [b0max, b1min, b1max, b2min, b2max, b3min, b3max, b4min, b4max, b5min]
        new_df[new_df.columns[i]] = th  # add the global concordance as a new column
        i = i + 1
    return new_df


# Degree of credibility
def credibility(dgconc, ddisc):
    """
    Calculates the credibility degree

    PARAMETERS
    ----------
    dgconc: Data Frame 
        Table with global concordance
    ddisc: DataFrame
        Table with the discordance 

    RETURNS
    ---------
    dcred: DataFrame
        Table with the credibility degree
    """
    # initialization
    dcred = pd.DataFrame(index=['b0_max',
                                 'b1_min', 'b1_max',
                                 'b2_min', 'b2_max',
                                 'b3_min', 'b3_max',
                                 'b4_min', 'b4_max',
                                 'b5_min'],
                          columns=['S1.1', 'S1.2', 'S1.3', 'S1.4',
                                   'S2.1', 'S2.2', 'S2.3', 'S2.4',
                                   'S3.1', 'S3.2', 'S3.3', 'S3.4',
                                   'S4.1', 'S4.2', 'S4.3', 'S4.4',
                                   'S5.1', 'S5.2', 'S5.3', 'S5.4',
                                   'S6.1', 'S6.2', 'S6.3', 'S6.4',
                                   'S7.1', 'S7.2', 'S7.3', 'S7.4'])
    for j in range(0, len(ddisc.columns), 10):
        sc = int(j / 10)
        degree = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for pr in range(len(dcred.index)):
            # verification if all Dj < C
            verif = sum(ddisc[j + pr][c] > dgconc[dgconc.columns[sc]][pr]
                        for c in ddisc.index)
            # case 1
            if verif == 0:
                degree[pr] = dgconc[dgconc.columns[sc]][pr]
            # case 2
            else:
                degree[pr] = (((1 - ddisc[j + pr][ddisc[j + pr]
                                                  > dgconc[dgconc.columns[sc]][pr]])
                               / (1 - dgconc[dgconc.columns[sc]][pr])).prod()) * dgconc[dgconc.columns[sc]][pr]
        dcred[dcred.columns[sc]] = degree
    return dcred


# Over-ranking
def over_ranking_relations(cred1, cred2, param):
    """
    Calculates the relations between each alternative and each profile

    PARAMETERS
    ----------
    cred1: Data Frame 
        Table with the credibility degree of the alternatives in relation to the profiles
    cred2: DataFrame
        Table with the credibility degree of the profiles in relation to the alternatives
    param: int
        Cut-off threshold

    RETURNS
    ---------
    new_df: DataFrame
        Table with the preference relation 
    """
    
    # initialization
    new_df = pd.DataFrame(index=['b0_max',
                                 'b1_min', 'b1_max',
                                 'b2_min', 'b2_max',
                                 'b3_min', 'b3_max',
                                 'b4_min', 'b4_max',
                                 'b5_min'],
                          columns=['S1.1', 'S1.2', 'S1.3', 'S1.4',
                                   'S2.1', 'S2.2', 'S2.3', 'S2.4',
                                   'S3.1', 'S3.2', 'S3.3', 'S3.4',
                                   'S4.1', 'S4.2', 'S4.3', 'S4.4',
                                   'S5.1', 'S5.2', 'S5.3', 'S5.4',
                                   'S6.1', 'S6.2', 'S6.3', 'S6.4',
                                   'S7.1', 'S7.2', 'S7.3', 'S7.4'])
    classementa = cred1.apply(lambda x: x - param)
    classementb = cred2.apply(lambda x: x - param)
    # 1 if outperform (S), 0 if not
    classementa[classementa > 0] = 1
    classementa[classementa < 0] = 0
    classementb[classementb > 0] = 1
    classementb[classementb < 0] = 0
    mask = (classementa == classementb) & (classementa == 1)
    new_df = new_df.mask(mask, "I")
    mask = (classementa == classementb) & (classementa == 0)
    new_df = new_df.mask(mask, "R")
    mask = (classementb != 0) & (classementa == 0)
    new_df = new_df.mask(mask, "<")
    mask = (classementa != 0) & (classementb == 0)
    new_df = new_df.mask(mask, ">")
    return new_df


# Pessimistic sorting
def pessimistic_sort(ranking, mpessi):
    """
    Builds the pessimistic sorting

    PARAMETERS
    ----------
    ranking: Data Frame 
        Table with the preference relations
    mpessi: DataFrame
        Table with the pessimistic sorting memory

    RETURNS
    ---------
    mpessi: DataFrame
        Table with the update of the pessimistic sorting memory
    """
    for sc in ranking:
        step = mpessi[sc]
        # print(step)
        for pr in reversed(range(len(ranking.index))):
            if ranking[sc][pr] == '>' or ranking[sc][pr] == 'I':
                step[step.index[pr]] = step[step.index[pr]] + 1  # classified
                break
        mpessi[sc] = step
        # print(mpessi)
    return mpessi


# Optimistic sorting
def optimistic_sort(ranking, mopti):
    """
    Builds the optimistic sorting

    PARAMETERS
    ----------
    ranking: Data Frame 
        Table with the preference relations
    mpessi: DataFrame
        Table with the optimistic sorting memory
    
    RETURNS
    ---------
    mpessi: DataFrame
        Table with the update of the optimistic sorting memory
        """
    for sc in ranking:
        step = mopti[sc]
        for pr in (range(len(ranking.index))):
            if ranking[sc][pr] == '<' or ranking[sc][pr] == 'R':
                step[step.index[pr]] = step[step.index[pr]] + 1  # classified
                break
        mopti[sc] = step
    return mopti
