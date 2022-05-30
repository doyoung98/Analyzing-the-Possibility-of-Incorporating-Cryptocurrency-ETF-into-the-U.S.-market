import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt
import time

from sklearn import datasets
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.stats import norm

def Calculate_Average_Correlation(data_init, cluster_number):
    
    # data information: (row: date, column: etf in certain cluster)
    
    clst_dataframe_list = []

    # gather correlation between mean_return and certain etf in this list
    correlation_list = []
    
    # gather average correlation of each clusters in this list
    clst_average_correlation_list = []

    for clst_num in range( np.max(cluster_number) + 1):
              
        data = data_init.transpose()
        data['cluster'] = cluster_number
        
        # used for gathering etf in same cluster
        clst_dataframe_iter = data[data['cluster'] == clst_num].drop(columns = 'cluster').transpose() 
        clst_dataframe_iter['avg_return'] = clst_dataframe_iter.mean(axis = 1)
        
        for etf_name in clst_dataframe_iter.columns[:-1]:
            correlation = clst_dataframe_iter.loc[:, [etf_name, 'avg_return']].corr()
            correlation_list.append(correlation.iloc[0, 1])
        
        clst_average_correlation_list.append(np.mean(correlation_list))

    return clst_average_correlation_list