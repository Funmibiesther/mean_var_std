
import numpy as np


def calculate(my_list):
    if len(my_list)  !=9:
        raise ValueError('list must contain 9 number')
    else:
        arr = np.array(my_list).reshape(3,3)
           #mean
        mean_axis0 = list(arr.mean(axis=0))
        mean_axis1 = list(arr.mean(axis=1))
        mean_flatten = arr.mean()
          #varience
        var_axis0 = list(arr.var(axis = 0))
        var_axis1 = list(arr.var(axis = 1))
        var_flatten = arr.var()
           #standard deviation
        std_axis0 = list(arr.std(axis = 0))
        std_axis1 = list(arr.std(axis = 1))
        std_flatten = arr.std()
           #max
        max_axis0 = list(arr.max(axis = 0))
        max_axis1 = list(arr.max(axis = 1))
        max_flatten = arr.max()
           #min
        min_axis0 = list(arr.min(axis = 0))
        min_axis1 = list(arr.min(axis = 1))
        min_flatten = arr.min()
           #sum
        sum_axis0 = list(arr.sum(axis = 0))
        sum_axis1 = list(arr.sum(axis = 1))
        sum_flatten = arr.sum()


        result = {'mean' : [mean_axis0,mean_axis1,mean_flatten],
                  'variance' : [var_axis0,var_axis1,var_flatten],
                  'standard deviation' : [std_axis0,std_axis1,std_flatten],
                  'max' : [max_axis0,max_axis1,max_flatten],
                  'min' : [min_axis0,min_axis1,min_flatten],
                  'sum' : [sum_axis0,sum_axis1,sum_flatten],


                 }
        return result

        
