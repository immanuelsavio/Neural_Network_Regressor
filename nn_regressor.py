import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


dataframe = pandas.read_csv("13-8-17.csv", delimiter=',')
dataset = dataframe.values

X = dataset[:,0:3]
Y = dataset[:,3]

print(Y)