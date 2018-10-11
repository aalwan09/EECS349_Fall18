from node import Node
import math
# import csv
# import pandas
# import random

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''

def init_entropy(class_set):
    '''
    Calculates the intial entropy for the classified data
    '''
    weight_true, weight_false, weight = (0,) * 3
    
    for item in class_set:
        if item == True:
            weight_true += 1
        else:
            weight_false += 1
        weight += 1
        
    weight_true = weight_true / float(weight)
    weight_false = weight_false / float(weight)
    
    entropy = -(weight_true * math.log(weight_true,2) + weight_false * math.log(weight_false,2))   
    return entropy

def get_entropy(attribute_set, class_set):
    '''
    Calculate the entropy for attributes
    '''
    
    true_pos, true_neg, false_pos, false_neg = (0,) * 4
    
    for item in zip(attribute_set, class_set):
        if item[0] == True:
            if item[1] == True:
                true_pos += 1
            else:
                false_neg += 1
        else:
            if item[1] == True:
                false_pos += 1
            else:
                true_neg += 1
        
    
    true_attr = true_pos + false_neg
    false_attr = false_pos + true_neg
    total_attr = len(class_set)
    
    percent_true = true_attr / total_attr
    percent_false = false_attr / total_attr
    
    if true_attr == 0:
        #calculate the proportion of true given true and false given true
        true_given_true, false_given_true = (0,) * 2
    else:
        true_given_true = true_pos / true_attr
        false_given_true = false_neg / true_attr
        
    if false_attr == 0:
        #calculate the proportion of true given false and false given false
        true_given_false , false_given_false = (0,) * 2
    else:
        true_given_false = false_pos / false_attr
        false_given_false = true_neg / false_attr
        
    if true_given_true == 0 or false_given_true == 0:
        entropy_true = 0
    else: 
        entropy_true = -(true_given_true * math.log(true_given_true, 2) + 
                         false_given_true * math.log(false_given_true, 2))
        
    if true_given_false == 0 or false_given_false == 0:
        entropy_false = 0
    else:
        entropy_false = -(true_given_false * math.log(true_given_false, 2) + 
                          false_given_false * math.log(false_given_false, 2))
    
    final_entropy = ((percent_true * entropy_true) + 
                     (percent_false * entropy_false))
    
    return final_entropy



        
    
    
    
    













def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''




