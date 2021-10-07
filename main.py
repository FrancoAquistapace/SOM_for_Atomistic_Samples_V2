#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:01:47 2021

@author: francoaquistapace

Copyright 2021 Franco Aquistapace

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

# Import modules and SOM
import pandas as pd
import time

from SOM import *

# Import parameters
from input_params import PARAMS

# Fixed seed for consistent results
np.random.seed(1982) 


# Keep track of the header lines in each file
all_header_lines = []

# Keep track of the min and the max values of every feature 
# in the training data
min_max_features = []

# Let's streamline the process of opening a file and
# extracting the features
def open_and_extract(fname,features,training=False):
    '''
    Parameters
    ----------
    fname : str
        Sample file path.
    features : list of str
        List with the features of the sample that are going to be used.

    Returns
    -------
    Original and normalized dataframes with the selected features of the 
    sample, ready for training of the SOM or to be classified. Also returns 
    the header lines of the file.

    '''
    
    file = open(fname,'r')
    found_cols = False
    header_lines = []
    line_count = 0
    while not found_cols:
        line = file.readline()
        line_count += 1
        if 'ITEM: ATOMS' in line:
            columns = line.split()
            columns.pop(0) # Pop 'ITEM:'
            columns.pop(0) # Pop 'ATOMS'
            found_cols = True
        header_lines.append(line)
    file.close()
    
    df = pd.read_csv(fname,sep=' ', 
                     skiprows=line_count, names=columns)
    
    
    norm_df = df[features].copy()
    # For the training process we use the min and max values 
    # of every feature from the same sample, and save them to properly
    # rescale the samples to be analized later
    if training:
        for feat in features:
            min_value = norm_df[feat].min()
            max_value = norm_df[feat].max()
            delta = max_value - min_value
            norm_df[feat] = (norm_df[feat] - min_value) / delta
            
            # Save min and max for later
            min_max_features.append([min_value, max_value])
            
    else:
        for i in range(len(features)):
            feat = features[i]
            min_value = min_max_features[i][0]
            max_value = min_max_features[i][1]
            delta = max_value - min_value
            norm_df[feat] = (norm_df[feat] - min_value) / delta
        
    return df, norm_df, header_lines

# Initialize features
FEATURES = PARAMS['features']

print('Initializing SOM...')

# Build SOM model
SIGMA = PARAMS['sigma']
ETA = PARAMS['eta']
SIZE = (len(FEATURES),PARAMS['N'])
som = SOM(sigma=SIGMA, eta=ETA, size=SIZE)


# Start timing...
time1 = time.time()



# Get training data and shuffle it
training_path = PARAMS['training_file']
print('Preparing training data from file %s' % training_path)
og_training_df = open_and_extract(training_path, FEATURES, training=True)[1]
f = PARAMS['f']
if f == '1':
    f = int(1)
else:
    f = float(f)
training_df = og_training_df.sample(frac=f)


# Train the SOM
print('Training SOM...')
som.train(training_df)

print('SOM trained succesfully')    



# Predict atom groups and write ouputs for every file requested

files = PARAMS['file_list']
search_pattern = PARAMS['search_pattern']


# Check if the user has specified a search pattern instead
if len(files) == 0 and search_pattern == '':
    print('Error: either a list of files or a'+\
          ' search pattern must be specified')
    exit()

if len(files) == 0 and not search_pattern == '':
    print('This mode is not available yet.')
    exit()

# File list mode
if not len(files) == 0:
    for i in range(len(files)):
        print('\nAnalizing file %d of %d...' % (i+1,len(files)))
        file = files[i]
        df, norm_df, header_lines = open_and_extract(file, FEATURES)
        
        print('Predicting atom groups...')
        results = som.predict(norm_df)
        # We only need the last column, which contains the grouping result
        result_cols = results.columns.to_list()
        groups = results[result_cols[-1]]
        
        # Concat new DataFrame
        new_df = pd.concat([df,groups], axis=1)
        
        
        # Save new file with the group assigned to each atom
        print('Writing results...')
        new_path = 'SOM_' + file
        new_file = open(new_path, 'w')
        
        # Write the header of the file
        for i in range(len(header_lines)):
            line = header_lines[i]
            if i == len(header_lines) - 1:
                line = line.replace('\n', ' som_cluster\n')
            new_file.write(line)
        
        # Now let's write the new data
        final_string = new_df.to_csv(index=False, sep=' ', 
                                 float_format='%s', header=False)
        new_file.write(final_string)
        
            
        new_file.close()
        
        

# Finish timing
time2 = time.time()

print('\nProcess completed')
print('Elapsed time: ' + str(round(time2-time1,3)) + ' seconds')
    

