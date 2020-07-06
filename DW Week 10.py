# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:35:04 2020

@author: hobin
"""

import numpy as np 
ls = [[ 1, 3], [2, 4], [3, 6], [4,8] ]
a = np.array(ls)

print(a.shape) #prints the number of row and columns

print(a[:,[0]]) #extracts and prints a[row:columns] , in this case column 0 from all the rows

print(a[:,[0]].shape) #prints the number of rows and columns, shows it is a 2D numpy array


import numpy as np
from sklearn import datasets
b = datasets.load_breast_cancer()
print(b.feature_names[3])   #gives the name of the 3rd feature
b.data[:,[3]]  
print(b.data[:,[3]]) #gives the data of the 3rd feature


b.shape # dimension of matrix, returns as tuple(columns, rows)
b.shape[0] # number of rows
b.shape[1] # number of columns
b.size # number of elements
b.I # find inverse of matrix

# indexing, slicing
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b[row][column]
b[0,:] # whole of first row, = [1 2 3], shape = (3,)
b[[0],:] # whole of first row, = [[1 2 3]], shape = (1, 3)
b[:,0] # whole of first column, = [1 4 7], shape = (3,)
b[:,[0]] # whole of first column, = [[1], [4], [7]], shape = (3, 1)

b[[1,2,3]] # if A is (30,) array, select columns 1,2,3


# Linear Regression is only used to predict numerical data using numerical inputs
# K Neighbour is used to predict categorical data


# W10 C1
import numpy as np
from sklearn.metrics import confusion_matrix

def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    
    total_correct_predictions = c_matrix[0,0] + c_matrix[1,1]
    print(total_correct_predictions)
    total_records = np.sum(c_matrix)
    total_positive = (c_matrix[1,0] + c_matrix[1,1])
    accuracy = round((total_correct_predictions/total_records), 3)
    sensitivity = round((c_matrix[1,1]/ total_positive), 3)
    false_negativity = round((c_matrix[0,1] / (c_matrix[0,0] + c_matrix[0,1])), 3)
    result = {'confusion matrix': c_matrix, 'total records': total_records, 'accuracy': accuracy, 'sensitivity': sensitivity, 'false positive rate': false_negativity}
    
    return result

#actual_targets   =   [ 'cat' ,   'cat' ,   'cat' ,   'cat' ,   'bird' ,   'bird' , 'bird' , 'bird' ] 
#predicted_targets  =   [ 'cat' ,   'cat' ,   'bird' ,   'bird' ,   'cat' ,   'bird' ,   'bird' ,   'bird' ]   
#labels   =   ['bird','cat'] 
#print(get_metrics(actual_targets, predicted_targets, labels))


# Virus Example
#actual_targets = ['virus'] * 8 + ['no virus'] * 4
#print(actual_targets)
#predicted_targets = ['virus' , 'virus','no virus' , 'virus' , 'virus', 'no virus', 'virus', 'virus' ,'virus' , 'no virus', 'no virus','no virus']
#print(predicted_targets)

#labels = ['no virus', 'virus']
#print(get_metrics(actual_targets, predicted_targets, labels))


# W10 C2

import numpy as np

def five_number_summary(x):
    rows, columns = x.shape
    output = []
    for i in range(columns):
        minimum = np.min(x[:, [i]])
        maximum = np.max(x[:, [i]])
        median = np.median(x[:, [i]])
        first_25 = np.percentile(x[:,[i]], 25)
        first_75 =  np.percentile(x[:,[i]], 75)
        
        result = {'minimum': minimum,
                  'first quartile': first_25,
                  'median': median,
                  'third quartile': first_75,
                  'maximum': maximum}
        
        output.append(result)
        
    return output


# W10 C3

import numpy as np

def normalize_minmax(data):
    if data.ndim != 2:
        return None
    else:
        rows, columns = data.shape
        for i in range(columns):
            minvalue = np.min(data[:,[i]])
            maxvalue = np.max(data[:,[i]])
            
            #element wise operations
            # try deriving this formula
            data[:,[i]] =  (data[:,[i]] - minvalue) / (maxvalue - minvalue)
        
        return data


from sklearn import datasets
b = datasets.load_breast_cancer()
some_cols = b.data[:,[2,3]]
data = normalize_minmax(some_cols)
print(data)



# W10 C4

from sklearn.model_selection import train_test_split 
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np

def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    
    total_correct_predictions = c_matrix[0,0] + c_matrix[1,1]
    print(total_correct_predictions)
    total_records = np.sum(c_matrix)
    total_positive = (c_matrix[1,0] + c_matrix[1,1])
    accuracy = round((total_correct_predictions/total_records), 3)
    sensitivity = round((c_matrix[1,1]/ total_positive), 3)
    false_negativity = round((c_matrix[0,1] / (c_matrix[0,0] + c_matrix[0,1])), 3)
    result = {'confusion matrix': c_matrix, 'total records': total_records, 'accuracy': accuracy, 'sensitivity': sensitivity, 'false positive rate': false_negativity}
    
    return 

def normalize_minmax(data):
    if data.ndim != 2:
        return None
    else:
        rows, columns = data.shape
        for i in range(columns):
            minvalue = np.min(data[:,[i]])
            maxvalue = np.max(data[:,[i]])
            
            #element wise operations
            # try deriving this formula
            data[:,[i]] =  (data[:,[i]] - minvalue) / (maxvalue - minvalue)
        
        return data

def knn_classifier(bunchobject, feature_list, size, seed , k ): 
    
    # Step 2: Get the data
    data = bunchobject.data[:, feature_list]
    target = bunchobject.target
    print(data.shape)
    
    # Step 2.5
    data = normalize_minmax(data) # Dont forget this step!
    
    # Step 3: Split the data into training set and test size
    data_train, data_test, target_train, target_test =  train_test_split(data, target, test_size=size, random_state=seed)
    
    # step 4: Build the model using training set
    clf = neighbors.KNeighborsClassifier(n_neighbors = k)
    clf.fit(data_train, target_train)
    
    # Step 5: Make predictions using the test set
    target_predict = clf.predict(data_test)

    # Step 6: Evaluate your model
    # binary classification  => get the confusion matrix
    # label parameters: [negative case, positive case]
    # positive is malignant/ more crucial => 0
    # negative is benign => 1
    # to check which is positive or negative
    label = [1,0]
    print(np.unique(target))
    results = get_metrics(target_test, target_predict, label)
    print(results)
    results = get_metrics(target_test, target_predict, label)
    
    return results

b = datasets.load_breast_cancer()

#feature list is an arbitrary choice
selected_features = list(range(20)) #we want to select columns 0 to 19 of the dataset

#checking the counts if sitive or negative
target, counts = np.unique(b.target, return_counts = True)
print(target, counts)
print(b.DESCR)

knn.classifier(b.selected_features, 0.4, 2752, 3)



# W10 C5

import numpy as np
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def linear_regression(bunchobject, x_index, y_index, size, seed):
    # Step 2: Collect Data
    x = bunchobject.data[: , [x_index]]
    y = bunchobject.data[: , [y_index]]
    
    # Step 3: Split the data into training and test set
    x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = size, random_state = seed)
    print(x_train.shape)
    print(x_test.shape)
    
    # Step 4: Build the model using the training set
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)  # machine learns the model first
    print(regr.coef_, regr.intercept_)
    
    # Step 5: Use the data in the test set to predict
    y_predict = regr.predict(x_test)
    
    mse = mean_squared_error(y_test, y_predict) 
    r2 = r2_score(y_test, y_predict)
    print(mse, r2)
    
    results= {'coefficients': regr.coef_, 'intercept': regr.intercept_, 'mean squared error': mse, 'r2 score': r2}
    
    return x_train, y_train, x_test, y_predict, results
    
from sklearn import datasets
b = datasets.load_breast_cancer()
linear_regression(b, 0, 3, 0.4, 2752)


# W10 C6

import numpy as np
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    
    # Step 2: Collect Data
    x = bunchobject.data[: , [x_index]]
    y = bunchobject.data[: , [y_index]]
    
    poly = PolynomialFeatures(order, include_bias = False)
    x = poly.fit_transform(x)
    print(x.shape)
    
    x_train, x_test, y_train, y_test = train_test_split(x , y, test_size = size, random_state = seed)
    
    
    # Step 4: Build the model using the training set
    regrem = linear_model.LinearRegression()
    regrem.fit(x_train, y_train)  # machine learns the model first
    print(regrem.coef_, regrem.intercept_)
    
    # Step 5: Use the data in the test set to predict
    y_predict = regrem.predict(x_test)
    
    mse = mean_squared_error(y_test, y_predict) 
    r2 = r2_score(y_test, y_predict)
    print(mse, r2)
    
    results= {'coefficients': regrem.coef_, 'intercept': regrem.intercept_, 'mean squared error': mse, 'r2 score': r2}
    
    return x_train[:, [x_index]], y_train, x_test[:, [x_index]], y_predict, results


# W10 C7

import numpy as np
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# place any functions you need from CS1-3 here

def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    
    total_correct_predictions = c_matrix[0,0] + c_matrix[1,1]
    print(total_correct_predictions)
    total_records = np.sum(c_matrix)
    total_positive = (c_matrix[1,0] + c_matrix[1,1])
    accuracy = round((total_correct_predictions/total_records), 3)
    sensitivity = round((c_matrix[1,1]/ total_positive), 3)
    false_negativity = round((c_matrix[0,1] / (c_matrix[0,0] + c_matrix[0,1])), 3)
    result = {'confusion matrix': c_matrix, 'total records': total_records, 'accuracy': accuracy, 'sensitivity': sensitivity, 'false positive rate': false_negativity}
    
    return result

def normalize_minmax(data):
    if data.ndim != 2:
        return None
    else:
        rows, columns = data.shape
        for i in range(columns):
            minvalue = np.min(data[:,[i]])
            maxvalue = np.max(data[:,[i]])
            
            #element wise operations
            # try deriving this formula
            data[:,[i]] =  (data[:,[i]] - minvalue) / (maxvalue - minvalue)
        
        return data

def knn_classifier_full(bunchobject, feature_list, size, seed):
     
    # Step 2: Get the data
    data = bunchobject.data[:, feature_list]
    target = bunchobject.target
    print(data.shape)
    
    # Step 2.5
    data = normalize_minmax(data) # Dont forget this step!
    
    # Step 3: Split the data into training set, validation and test set
    data_train, data_part2, target_train, target_part2 =  train_test_split(data, target, test_size=size, random_state=seed)
    data_validation, data_test, target_validation, target_test = train_test_split(data_part2, target_part2, test_size = 0.50, random_state=seed)
    
    # Step 4: Decide the best value for k
    ls_results = []
    for k in range(1, 21):
        #fit the data to the training set
        clf = neighbors.KNeighborsClassifier(n_neighbors=k)
        clf.fit(data_train, target_train)

        # predict based on the validation set
        target_pred = clf.predict(data_validation)
        
        # Get the results
        label = [1,0] # label [negative, positive]
        results = get_metrics(target_validation, target_pred, label)
        accuracy = results['accuracy']
        ls_results.append(accuracy)
        
    print (ls_results)
    max_accuracy = max(ls_results)
    # get the index of the largest accuracy
    best_k = ls_results.index(max_accuracy) +1
     
    #Step ... Evaluate the model using the test set.
    #build your best model (i.e. model with the best k) 
    clf = neighbors.KNeighborsClassifier(n_neighbors=best_k)
    clf.fit( data_train, target_train)
    #make a prediction with the test set 
    target_predicted = clf.predict(data_test)
    #evaluate the results
    label = [1, 0]
    result = get_metrics( target_test, target_predicted, label )

    clf = neighbors.KNeighborsClassifier(n_neighbors=best_k)
    clf.fit(data_train, target_train)
    
    #predict based on the validation set 
    target_pred = clf.predict(data_validation) 

    #get the results
    label = [1, 0] # [negative case, positive case]
    results= get_metrics(target_validation, target_pred, label )
    
    out_result = {'best k':best_k,'validation set': results,'test set':result}
    return out_result
    



















