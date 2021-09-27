#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:02:58 2021

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

# This dictionary contains all the information and parameters
# that are going to be given to the SOM to perform its task.

"""
    file_list : list
        List with the sample paths that are going to be classified
        by the SOM. If the list is empty, the program uses the
        search_pattern instead.
        
    search_pattern : str
        Search pattern for the files that are going to be 
        classified by the SOM. For example: 'feature_sample.*.config'
        
    training_file : str
        Path of the sample file used to train the SOM.
        
    features : list
        List containing the names of the features to be used.
        
    f : int or float
        Fraction of the sample data to use when training the SOM.
        Must be in the range (0,1].
                              
    sigma : int or float
        Maximum value for the sigma(t) function, which gives the
        standard deviation of a Gaussian neighborhood as a 
        function of the current iteration step.
        
    eta : int or float
        Maximum learning rate for the eta(t) function, which gives
        the learning rate as a function of the current iteration 
        step.
        
    N : int
        Number of output neurons of the SOM network, i.e. number 
        of groups in which to classify the atoms of the sample.
    
"""

PARAMS = {'file_list' : ['KMeans_HEA_tension_dump.2525000.clusters.config', 
                         'KMeans_HEA_tension_dump.2775000.clusters.config'], 
          'search_pattern' : '', 
          'training_file' : 'KMeans_HEA_tension_dump.2525000.clusters.config', 
          'features' : ['AtomicVolume','gr_coord', 'csp12', 'csp18'],
          'f' : 1,
          'sigma' : 1, 
          'eta' : 0.5, 
          'N' : 6}

