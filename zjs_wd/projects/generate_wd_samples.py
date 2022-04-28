import pandas as pd
import numpy as np
import json

import os
root_path = os.path.dirname(os.path.abspath('__file__'))
#root_path = os.path.abspath(os.path.join(root_path, os.path.pardir))
#root_path = os.path.abspath(os.path.join(root_path, os.path.pardir))
print(10*'-'+' Current Path: {}'.format(root_path))
import sys
sys.path.append(root_path+'/tools/')

from samples_generator import gen_multi_models_hindcast
from samples_generator import gen_multi_models_forecast
from samples_generator import gen_one_model_hindcast
from samples_generator import gen_one_model_forecast
from variables import variables

with open(root_path+'/results_analyze/results/selected_subsignals.json') as handle:
    dictdump = json.loads(handle.read())
input_dict=dictdump['zjs']


for wavelet in ['db2','db5','db10','db15','db20','db25','db30','db35','db40','db45','bior 3.3','coif3','haar']:
     for lev in [1,2,3]:
         for leading_time in [1,3,5,7]:
             gen_multi_models_forecast(
                 path=root_path+'/zjs_wd/data/',
                 decomposer='wd',
                 lev=lev,
                 test_len=657,
                 start_id=5261,
                 stop_id=6574,
                 lags_dict=variables['lags_dict'],
                 leading_time=leading_time,
                 wavelet=wavelet,
             )
             gen_one_model_forecast(
                 path=root_path+'/zjs_wd/data/',
                 decomposer='wd',
                 lev=lev,
                 test_len=657,
                 start_id=5261,
                 stop_id=6574,
                 lags_dict=variables['lags_dict'],
                 leading_time=leading_time,
                 wavelet=wavelet,
             )

             gen_one_model_forecast(
                 path=root_path+'/zjs_wd/data/',
                 decomposer='wd',
                 lev=lev,
                 input_columns=input_dict[wavelet+"-"+str(lev)],
                 test_len=657,
                 start_id=5261,
                 stop_id=6574,
                 lags_dict=variables['lags_dict'],
                 leading_time=leading_time,
                 wavelet=wavelet,
             )
             gen_multi_models_hindcast(
                 path=root_path+'/zjs_wd/data/',
                 decomposer='wd',
                 lev=lev,
                 test_len=657,
                 lags_dict=variables['lags_dict'],
                 leading_time=leading_time,
                 wavelet=wavelet,
             )

             gen_one_model_hindcast(
                 path=root_path+'/zjs_wd/data/',
                 decomposer='wd',
                 lev=lev,
                 test_len=657,
                 lags_dict=variables['lags_dict'],
                 leading_time=leading_time,
                 wavelet=wavelet,
             )

             gen_one_model_hindcast(
                 path=root_path+'/zjs_wd/data/',
                 decomposer='wd',
                 lev=lev,
                 input_columns=input_dict[wavelet+"-"+str(lev)],
                 test_len=657,
                 lags_dict=variables['lags_dict'],
                 leading_time=leading_time,
                 wavelet=wavelet,
             )




