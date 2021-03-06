# -*- coding: utf-8 -*-
"""deepneural.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kqgfPqC6OvUKAn0Uj94dSV8vvylF2x87
"""

import numpy as np
import pandas as pd
import os
from google.colab import files
uploaded=files.upload()

import io
X_train=pd.read_csv(io.BytesIO(uploaded['X_train.csv']))
X_train.head(3)

uploaded=files.upload()

y_train=pd.read_csv(io.BytesIO(uploaded['y_train.csv']))
y_train.head(3)

uploaded=files.upload()

X_test=pd.read_csv(io.BytesIO(uploaded['X_test.csv']))
X_test.head(3)

target = y_train['surface'].value_counts().reset_index().rename(columns = {'index' : 'target'})
target

print("the dimensions of the training dataset is as follows:{} features and {} samples".format(X_train.shape[1],X_train.shape[0]))

print("the dimensions of the target labels is as follows:{} features and {} samples".format(y_train.shape[1],y_train.shape[0]))

print("The dimensions of the test dataset is as follows:{} features and {} samples".format(X_test.shape[1],X_test.shape[0]))

# checking for missing and duplicated data in the dataset
X_train.isnull().sum()

y_train.isnull().sum()

X_test.isnull().sum()

X_train['is_duplicate'] = X_train.duplicated()
X_train['is_duplicate'].value_counts()

X_train = X_train.drop(['is_duplicate'], axis = 1)

y_train['is_duplicate'] = y_train.duplicated()
y_train['is_duplicate'].value_counts()

y_train = y_train.drop(['is_duplicate'], axis = 1)

X_test['is_duplicate'] = X_test.duplicated()
X_test['is_duplicate'].value_counts()

X_test = X_test.drop(['is_duplicate'], axis = 1)

# now we start plotting the correlation between variables in the training dataset
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style 
style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')

import plotly.offline as py 
from plotly.offline import init_notebook_mode, iplot
py.init_notebook_mode(connected=True) # this code, allow us to work with offline plotly version
import plotly.graph_objs as go # it's like "plt" of matplot
fig, ax = plt.subplots(1,1, figsize = (15,6))

hm = sns.heatmap(X_train.iloc[:,3:].corr(),
                ax = ax,
                cmap = 'coolwarm',
                annot = True,
                fmt = '.2f',
                linewidths = 0.05)
fig.subplots_adjust(top=0.93)
fig.suptitle('Orientation, Angular_velocity and Linear_accelaration Correlation Heatmap for Train dataset', 
              fontsize=14, 
              fontweight='bold')

# now we plot the correlation matrix for the test dataset

fig, ax = plt.subplots(1,1, figsize = (15,6))

hm = sns.heatmap(X_test.iloc[:,3:].corr(),
                ax = ax,
                cmap = 'coolwarm',
                annot = True,
                fmt = '.2f',
                linewidths = 0.05)
fig.subplots_adjust(top=0.93)
fig.suptitle('Orientation, Angular_velocity and Linear_accelaration Correlation Heatmap for Test dataset', 
              fontsize=14, 
              fontweight='bold')

plt.figure(figsize=(26, 16))
for i, col in enumerate(X_train.columns[3:]):
    ax = plt.subplot(3, 4, i + 1)
    sns.boxplot(X_train[col])
    #sns.distplot(X_test[col], bins=100, label='test')
    ax.legend()

# now that we visually that there exists outliers in the angular veocity and linear acceleration features.
# we now can use statistical method of data skeweness to detect outliers
for col in X_train.columns:
  print(X_train[col].skew())
  X_train[col].describe

x_trial_train=X_train.copy()

x_trial_train.head(3)

for col in x_trial_train.columns[7:13]:
  high_1=x_trial_train[col].quantile(0.90)
  low_1=x_trial_train[col].quantile(0.10)
  x_trial_train[col]=np.where(x_trial_train[col] > high_1, x_trial_train[col].quantile(0.5), x_trial_train[col])
  x_trial_train[col]=np.where(x_trial_train[col] < low_1, x_trial_train[col].quantile(0.5), x_trial_train[col])

for col in x_trial_train.columns:
  print(x_trial_train[col].skew())
  x_trial_train[col].describe

plt.figure(figsize=(26, 16))
for i, col in enumerate(x_trial_train.columns[3:]):
    ax = plt.subplot(3, 4, i + 1)
    sns.boxplot(x_trial_train[col])
    ax.legend()

x_trial_train_2=X_train.copy()
for col in x_trial_train_2.columns[7:13]:
  high_2=x_trial_train_2[col].quantile(0.95)
  low_2=x_trial_train_2[col].quantile(0.05)
  x_trial_train_2[col]=np.where(x_trial_train_2[col] > high_2, x_trial_train_2[col].quantile(0.5), x_trial_train_2[col])
  x_trial_train_2[col]=np.where(x_trial_train_2[col] < low_2, x_trial_train_2[col].quantile(0.5), x_trial_train_2[col])

for col in x_trial_train_2.columns:
  print(x_trial_train_2[col].skew())
  x_trial_train_2[col].describe

plt.figure(figsize=(26, 16))
for i, col in enumerate(x_trial_train_2.columns[3:]):
    ax = plt.subplot(3, 4, i + 1)
    sns.boxplot(x_trial_train_2[col])
    ax.legend()

# now we perform same outlier detection and removal for testing dataset
x_test_trial=X_test.copy()
plt.figure(figsize=(26, 16))
for i, col in enumerate(X_test.columns[3:]):
    ax = plt.subplot(3, 4, i + 1)
    sns.boxplot(X_test[col])
    ax.legend()

for col in x_test_trial.columns[7:13]:
  high_3=x_test_trial[col].quantile(0.95)
  low_3=x_test_trial[col].quantile(0.05)
  x_test_trial[col]=np.where(x_test_trial[col] > high_3, x_test_trial[col].quantile(0.5), x_test_trial[col])
  x_test_trial[col]=np.where(x_test_trial[col] < low_3, x_test_trial[col].quantile(0.5), x_test_trial[col])

plt.figure(figsize=(26, 16))
for i, col in enumerate(x_test_trial.columns[3:]):
    ax = plt.subplot(3, 4, i + 1)
    sns.boxplot(x_test_trial[col])
    ax.legend()

# now we start the process of feature engineering
from numpy.fft import *

# train

def filter_signal(signal, threshold=1e3):
  fourier = rfft(signal)
  frequencies = rfftfreq(signal.size, d=20e-3/signal.size)
  fourier[frequencies > threshold] = 0
  return irfft(fourier)

def fast_fourier(noise_1,noise_2):
  for col in noise_1.columns:
    if col[0:3] == 'ang' or col[0:3] == 'lin':
      # Apply filter_signal function to the data in each series
      denoised_data_tr = noise_1.groupby(['series_id'])[col].apply(lambda x: filter_signal(x))
    
  
      # Assign the denoised data back to X_train

      list_denoised_data_tr=[]
      for arr in denoised_data_tr:
        for val in arr:
          list_denoised_data_tr.append(val)

      noise_1[col] = list_denoised_data_tr

  return noise_1, noise_2


def inertia_calculate(data_1, data_2):
  data_1_updated,data_2_updated=fast_fourier(data_1,data_2)
  ixx_train=[]
  ixy_train=[]
  ixz_train=[]
  iyy_train=[]
  iyz_train=[]
  izz_train=[]
  x_tr=data_1_updated['orientation_X'].tolist()
  y_tr=data_1_updated['orientation_Y'].tolist()
  z_tr=data_1_updated['orientation_Z'].tolist()  

  ixx_test=[]
  ixy_test=[]
  ixz_test=[]
  iyy_test=[]
  iyz_test=[]
  izz_test=[]
  x_te=data_2_updated['orientation_X'].tolist()
  y_te=data_2_updated['orientation_Y'].tolist()
  z_te=data_2_updated['orientation_Z'].tolist()  
  
  for element in range(len(x_tr)):
    ixx_train.append(y_tr[element]**2+z_tr[element]**2)
    ixy_train.append(x_tr[element]*y_tr[element])
    ixz_train.append(x_tr[element]*z_tr[element])
    iyz_train.append(y_tr[element]*z_tr[element])
    iyy_train.append(x_tr[element]**2+z_tr[element]**2)
    izz_train.append(x_tr[element]**2+z_tr[element]**2)
  data_1_updated['inertia_x']=ixx_train
  data_1_updated['inertia_xy']=ixy_train
  data_1_updated['inertia_xz']=ixz_train
  data_1_updated['inertia_yz']=iyz_train
  data_1_updated['inertia_y']=iyy_train
  data_1_updated['inertia_z']=izz_train

  for element in range(len(x_te)):
    ixx_test.append(y_te[element]**2+z_te[element]**2)
    ixy_test.append(x_te[element]*y_te[element])
    ixz_test.append(x_te[element]*z_te[element])
    iyz_test.append(y_te[element]*z_te[element])
    iyy_test.append(x_te[element]**2+z_te[element]**2)
    izz_test.append(x_te[element]**2+z_te[element]**2)
  data_2_updated['inertia_x']=ixx_test
  data_2_updated['inertia_xy']=ixy_test
  data_2_updated['inertia_xz']=ixz_test
  data_2_updated['inertia_yz']=iyz_test
  data_2_updated['inertia_y']=iyy_test
  data_2_updated['inertia_z']=izz_test

  return data_1_updated, data_2_updated


def angular_momentum(dataset_1,dataset_2):
  lx_train=[]
  ly_train=[]
  lz_train=[]
  lx_test=[]
  ly_test=[]
  lz_test=[]
  out_1,out_2=inertia_calculate(dataset_1,dataset_2)
  k_tr=out_1['angular_velocity_X'].tolist()
  l_tr=out_1['angular_velocity_Y'].tolist()
  m_tr=out_1['angular_velocity_Z'].tolist()
  h_tr=out_1['inertia_x'].tolist()
  f_tr=out_1['inertia_y'].tolist()
  g_tr=out_1['inertia_z'].tolist()
  q_tr=out_1['inertia_xz'].tolist()
  n_tr=out_1['inertia_yz'].tolist()
  s_tr=out_1['inertia_xy'].tolist()
  k_te=out_2['angular_velocity_X'].tolist()
  l_te=out_2['angular_velocity_Y'].tolist()
  m_te=out_2['angular_velocity_Z'].tolist()
  h_te=out_2['inertia_x'].tolist()
  f_te=out_2['inertia_y'].tolist()
  g_te=out_2['inertia_z'].tolist()
  q_te=out_2['inertia_xz'].tolist()
  n_te=out_2['inertia_yz'].tolist()
  s_te=out_2['inertia_xy'].tolist()
  for element in range(len(k_tr)):
    lx_train.append(h_tr[element]*k_tr[element]-s_tr[element]*l_tr[element]-q_tr[element]*m_tr[element])
    ly_train.append(f_tr[element]*l_tr[element]-s_tr[element]*k_tr[element]-n_tr[element]*m_tr[element])
    lz_train.append(g_tr[element]*m_tr[element]-q_tr[element]*k_tr[element]-n_tr[element]*l_tr[element])
  out_1['angular_momentum_x']=lx_train
  out_1['angular_momentum_y']=ly_train
  out_1['angular_momentum_z']=lz_train
  for element in range(len(k_te)):
    lx_test.append(h_te[element]*k_te[element]-s_te[element]*l_te[element]-q_te[element]*m_te[element])
    ly_test.append(f_te[element]*l_te[element]-s_te[element]*k_te[element]-n_te[element]*m_te[element])
    lz_test.append(g_te[element]*m_te[element]-q_te[element]*k_te[element]-n_te[element]*l_te[element])
  out_2['angular_momentum_x']=lx_test
  out_2['angular_momentum_y']=ly_test
  out_2['angular_momentum_z']=lz_test

  return out_1,out_2

#data_update=angular_momentum(df)
#data_update.head(5)
  
def kinetic_energy(dataset_3,dataset_4):
  data_update_3, data_update_4=angular_momentum(dataset_3,dataset_4)
  trans_kin_energy_train=[]
  trans_kin_energy_test=[]
  lin_acc_x_tr=data_update_3['linear_acceleration_X'].tolist()
  lin_acc_y_tr=data_update_3['linear_acceleration_Y'].tolist()
  lin_acc_z_tr=data_update_3['linear_acceleration_Z'].tolist()
  lin_acc_x_te=data_update_4['linear_acceleration_X'].tolist()
  lin_acc_y_te=data_update_4['linear_acceleration_Y'].tolist()
  lin_acc_z_te=data_update_4['linear_acceleration_Z'].tolist()
  for element in range(len(lin_acc_x_tr)):
    trans_kin_energy_train.append(0.5*(lin_acc_x_tr[element]**2+lin_acc_y_tr[element]**2+lin_acc_z_tr[element]**2))
  data_update_3['translational Kinetic Energy']=trans_kin_energy_train
  for element in range(len(lin_acc_x_te)):
    trans_kin_energy_test.append(0.5*(lin_acc_x_te[element]**2+lin_acc_y_te[element]**2+lin_acc_z_te[element]**2))
  data_update_4['translational Kinetic Energy']=trans_kin_energy_test


  return data_update_3,data_update_4

def rotational_kinetic(data_update_5,data_update_6):
  update_5_train, update_6_test =kinetic_energy(data_update_5,data_update_6)
  rot_kin_energy_train=[]
  rot_kin_energy_test=[]
  in_tr=update_5_train['inertia_x'].tolist()
  in_te=update_6_test['inertia_x'].tolist()
  for element in range(len(in_tr)):
    rot_kin_energy_train.append(0.5*in_tr[element]**2+0.5*in_tr[element]**2+0.5*in_tr[element]**2)
  update_5_train['rot_kin_energy']=rot_kin_energy_train
  for element in range(len(in_te)):
    rot_kin_energy_test.append(0.5*in_te[element]**2+0.5*in_te[element]**2+0.5*in_te[element]**2)
  update_6_test['rot_kin_energy']=rot_kin_energy_test

  return update_5_train, update_6_test

#final_1=rotational_kinetic()
#final_1.head(5)

def quaternion_to_euler(qx,qy,qz,qw):
    import math
    # roll (x-axis rotation)
    sinr_cosp = +2.0 * (qw * qx + qy + qz)
    cosr_cosp = +1.0 - 2.0 * (qx * qx + qy * qy)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    
    # pitch (y-axis rotation)
    sinp = +2.0 * (qw * qy - qz * qx)
    if(math.fabs(sinp) >= 1):
        pitch = copysign(M_PI/2, sinp)
    else:
        pitch = math.asin(sinp)
        # yaw (z-axis rotation)
    siny_cosp = +2.0 * (qw * qz + qx * qy)
    cosy_cosp = +1.0 - 2.0 * (qy * qy + qz * qz)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    
    return roll, pitch, yaw

def eular_angle(data_7,data_8):
  final_tr, final_te=rotational_kinetic(data_7,data_8)
  a_tr=final_tr['orientation_X'].tolist()
  b_tr=final_tr['orientation_Y'].tolist()
  c_tr=final_tr['orientation_Z'].tolist()
  d_tr=final_tr['orientation_W'].tolist()
  a_te=final_te['orientation_X'].tolist()
  b_te=final_te['orientation_Y'].tolist()
  c_te=final_te['orientation_Z'].tolist()
  d_te=final_te['orientation_W'].tolist()
  nx_tr=[]
  ny_tr=[] 
  nz_tr=[]
  nx_te=[]
  ny_te=[] 
  nz_te=[]
  for i in range(len(a_tr)):
    xx_tr, yy_tr, zz_tr = quaternion_to_euler(a_tr[i], b_tr[i], c_tr[i], d_tr[i])
    nx_tr.append(xx_tr)
    ny_tr.append(yy_tr)
    nz_tr.append(zz_tr)
  final_tr['euler_x']=nx_tr
  final_tr['euler_y']=ny_tr
  final_tr['euler_z']=nz_tr
  for i in range(len(a_te)):
    xx_te, yy_te, zz_te = quaternion_to_euler(a_te[i], b_te[i], c_te[i], d_te[i])
    nx_te.append(xx_te)
    ny_te.append(yy_te)
    nz_te.append(zz_te)
  final_te['euler_x']=nx_te
  final_te['euler_y']=ny_te
  final_te['euler_z']=nz_te

  return final_tr,final_te
    

#xtrain_update,xtest_update=eular_angle(X_train,X_test)
#xtrain_update.head(5)
#xtest_update.head(5)
#xtest_update.shape
def fe_eng_tr(last_train, last_test):
    df_new_train = pd.DataFrame()
    model_train=eular_angle(last_train,last_test)[0]
    for col in model_train.columns:
        if col in ['row_id','series_id','measurement_number']:
            continue
        df_new_train[col + '_mean'] = model_train.groupby(['series_id'])[col].mean()
        df_new_train[col + '_median'] = model_train.groupby(['series_id'])[col].median()
        df_new_train[col + '_max'] = model_train.groupby(['series_id'])[col].max()
        df_new_train[col + '_min'] = model_train.groupby(['series_id'])[col].min()
        df_new_train[col + '_std'] = model_train.groupby(['series_id'])[col].std()
        df_new_train[col + '_range'] = df_new_train[col + '_max'] - df_new_train[col + '_min']
        df_new_train[col + '_maxtoMin'] = df_new_train[col + '_max'] / df_new_train[col + '_min']
        #in statistics, the median absolute deviation (MAD) is a robust measure of the variablility of a univariate sample of quantitative data.
        df_new_train[col + '_mad'] = model_train.groupby(['series_id'])[col].apply(lambda x: np.median(np.abs(np.diff(x))))
        df_new_train[col + '_abs_max'] = model_train.groupby(['series_id'])[col].apply(lambda x: np.max(np.abs(x)))
        df_new_train[col + '_abs_min'] = model_train.groupby(['series_id'])[col].apply(lambda x: np.min(np.abs(x)))
        df_new_train[col + '_abs_avg'] = (df_new_train[col + '_abs_min'] + df_new_train[col + '_abs_max'])/2
    return df_new_train


def fe_eng_te(last_train, last_test):
    df_new_test = pd.DataFrame()
    model_test=eular_angle(last_train,last_test)[1]
    for col in model_test.columns:
        if col in ['row_id','series_id','measurement_number']:
            continue
        df_new_test[col + '_mean'] = model_test.groupby(['series_id'])[col].mean()
        df_new_test[col + '_median'] = model_test.groupby(['series_id'])[col].median()
        df_new_test[col + '_max'] = model_test.groupby(['series_id'])[col].max()
        df_new_test[col + '_min'] = model_test.groupby(['series_id'])[col].min()
        df_new_test[col + '_std'] = model_test.groupby(['series_id'])[col].std()
        df_new_test[col + '_range'] = df_new_test[col + '_max'] - df_new_test[col + '_min']
        df_new_test[col + '_maxtoMin'] = df_new_test[col + '_max'] / df_new_test[col + '_min']
        #in statistics, the median absolute deviation (MAD) is a robust measure of the variablility of a univariate sample of quantitative data.
        df_new_test[col + '_mad'] = model_test.groupby(['series_id'])[col].apply(lambda x: np.median(np.abs(np.diff(x))))
        df_new_test[col + '_abs_max'] = model_test.groupby(['series_id'])[col].apply(lambda x: np.max(np.abs(x)))
        df_new_test[col + '_abs_min'] = model_test.groupby(['series_id'])[col].apply(lambda x: np.min(np.abs(x)))
        df_new_test[col + '_abs_avg'] = (df_new_test[col + '_abs_min'] + df_new_test[col + '_abs_max'])/2
    return df_new_test

final_train_sample=fe_eng_tr(x_trial_train_2, x_test_trial)
#final_train_sample.shape
final_test_sample=fe_eng_te(x_trial_train_2, x_test_trial)
#final_test_sample.shape
from sklearn.preprocessing import StandardScaler
final_train_sample_stand=final_train_sample.copy()
final_test_sample_stand=final_test_sample.copy()
for i in final_train_sample_stand.columns:
  scale_1 = StandardScaler().fit(final_train_sample_stand[[i]])

  final_train_sample_stand[i] = scale_1.transform(final_train_sample_stand[[i]])

for i in final_test_sample_stand.columns:
  scale_2 = StandardScaler().fit(final_test_sample_stand[[i]])

  final_test_sample_stand[i] = scale_2.transform(final_test_sample_stand[[i]])
#from sklearn.preprocessing import LabelEncoder
#le = LabelEncoder()
#y_train['surface'] = le.fit_transform(y_train['surface'])

#y_train.head()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train['surface'] = le.fit_transform(y_train['surface'])

# Now we can implement autoencoder neural networks
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(170, input_dim=264, activation='relu'))
	model.add(Dense(9, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
estimator = KerasClassifier(build_fn=baseline_model, epochs=2000, batch_size=50, verbose=0)
kfold = KFold(n_splits=10, shuffle=True)
results = cross_val_score(estimator, final_train_sample_stand.values, y_train['surface'].values, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

from keras.models import Sequential
from keras.layers import Dense
model_1 = Sequential()
model_1.add(Dense(265, activation='relu', input_shape=(264,)))
model_1.add(Dense(100, activation='relu'))
model_1.add(Dense(70, activation='relu'))
model_1.add(Dense(9, activation='softmax'))
model_1.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
                   
model_1.fit(final_train_sample_stand, y_train['surface'],epochs=100, batch_size=50, verbose=1)
score = model_1.evaluate(final_train_sample_stand, y_train['surface'],verbose=1)

print(score)