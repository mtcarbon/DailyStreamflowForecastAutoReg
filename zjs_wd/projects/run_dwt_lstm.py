import os
root_path = os.path.dirname(os.path.abspath('__file__'))

import sys
sys.path.append(root_path+'/tools/')
from build_lstm import my_lstm

# wavelet='db35'
# for lev in [1,2,3]:
#     for lead in [1,3,5,7]:
#         for k in range(1,lev+2):
#             for i in [8,16,24,32]:
#                 for j in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,]:
#                     my_lstm(
#                         path=root_path+'/zjs_wd/',
#                         lev=lev,
#                         pattern='multi_models_'+str(lead)+'_ahead_forecast_pacf',
#                         HU1=i,
#                         DR1=j,
#                         MODEL_ID=k,
#                         wavelet=wavelet,
#                     )

# wavelet ='db35'
# lev=3
# for lead in [1,3,5,7]:
#     for i in [8,16,24,32]:
#         for j in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,]:
#             my_lstm(
#                 path=root_path+'/zjs_wd/',
#                 lev=lev,
#                 pattern='one_model_'+str(lead)+'_ahead_forecast_pacf_mis',
#                 HU1=i,
#                 DR1=j,
#                 MODEL_ID=None,
#                 wavelet=wavelet,
#             )

for lead in [1,3,5,7]:
    for i in [8,16,24,32]:
            for j in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,]:
                my_lstm(
                    path=root_path+'/zjs_wd/',
                    lev=3,
                    pattern='one_model_'+str(lead)+'_ahead_hindcast_pacf_mis',
                    HU1=i,
                    DR1=j,
                    MODEL_ID=None,
                    wavelet='db45',
                )

