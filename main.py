import matplotlib as plt
import numpy as np
from sklearn import datasets , linear_model

diabetes = datasets.load_diabetes()

#diabetes_x =diabetes.data
#(['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])

print(diabetes.DESCR)
