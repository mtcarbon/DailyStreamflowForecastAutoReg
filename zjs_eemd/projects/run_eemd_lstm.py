import os
root_path = os.path.dirname(os.path.abspath('__file__'))
# root_path = os.path.abspath(os.path.join(root_path, os.path.pardir))
# root_path = os.path.abspath(os.path.join(root_path, os.path.pardir))
print(10*'-'+' Root Path: {}'.format(root_path))

import sys
sys.path.append(root_path+'/tools/')
from build_lstm import my_lstm
lev=12



# for k in range(1,lev+1):
#     for i in [8,16,24,32]:
#         for j in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,]:
#             my_lstm(
#                 path=root_path+'/zjs_eemd/',
#                 lev=lev,
#                 pattern='multi_models_1_ahead_hindcast',
#                 HU1=i,
#                 DR1=j,
#                 MODEL_ID=k,
#             )

for lead in [1,3,5,7]:
    for i in [8,16,24,32]:
        for j in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,]:
            my_lstm(
                path=root_path+'/zjs_eemd/',
                lev=lev,
                pattern='one_model_'+str(lead)+'_ahead_hindcast_pacf_mis',
                HU1=i,
                DR1=j,
                MODEL_ID=None,
            )



