from node import Node
import math
from parse import parse
import random
# import csv
# import pandas


def makeDataSets(filename, trainingSize):
    '''
    Create training and testing datasets
    Put data into list format instead of dictionary format (easier to work with)
    '''
    dataset = parse(filename)
    
    attributes = list(dataset[1].keys())
    examples = []
    
    for item in dataset:
        examples.append(list(item.values()))
    
    print(examples[1])
    print(attributes)
    
    # create the training and testing datasets
    trainingSet = []
    testingSet = []
    
    if trainingSize < len(examples):
        trainingSet = random.sample(examples, trainingSize)
        testingSet = examples
        
        for item in trainingSet:
            testingSet.remove(item)
    else:
        print('The dataset provided is too small!')
		
        return [attributes, trainingSet, testingSet]
    
  
def mode(listOfLists):
    '''
    Calculates the most common classification 
    '''
    counter = 0
    
    for row in listOfLists:
        for col in listOfLists:
            if col == True:
                counter += 1
            else:
                counter -= 1
    
    if counter > 0:
        return True
    else:
        return False
 
    
def sameClass(listOfLists):
   '''
   Checks to see if all of the classifications of an attribute are the same
   '''
   var = None
    
   for row in listOfLists:
       if var == None:
           var = row[-1]
       else:
           if var != row[-1]:
               return 2
        
   if var == True:
       return 1
   else:
       return 0


def updateAttr(lst, attr):
    '''
    Updates the list of attributes in decision tree (used in ID3)
    '''
    var = None
    
    for i, item in enumerate(lst):
        if item == attr:
            var = i
            break
    
    out = lst[0:var] + lst[var+1:len(lst)]
    
    return out


def updateExamples(listOfLists, lst, attr, bool_item):
    '''
    Updates the list of examples in decision tree (used in ID3)
    '''
    var = None
    out = []
    
    for i, item in enumerate(lst):
        if item == attr:
            var = i
            break
    
    for row in listOfLists:
        if row[var] == bool_item:
            out.append(row[0:var] + row[var+1:len(row)])
    
    return out


def splitLists(example):
    '''
    Splits both the attribute and the class lists
    '''
    classList = []
    attrList = []
    
    for ex in example:
        classList.append(ex[-1])
        attrList.append(ex[:-1])
        
    return [attrList, classList]


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


def chooseAttr(listOfAttr, example):
    '''
    Identifies and chooses an attribute based on information gain
    Selects the one with the lowest entropy
    '''
    # initialize variables
    classList = splitLists(example)[1]
    initEntropy = init_entropy(classList)
    
    # iterate through each attribute
    currAttr = None
    
    for i, attr in enumerate(listOfAttr):
        currList = []
        
        for ex in splitLists(example)[0]:
            currList.append(ex[i])
            
        if get_entropy(currList, classList) < initEntropy:
            initEntropy = get_entropy(currList, classList)
            currAttr = attr
            
    # perform checks and then return
    if (currAttr == None):
        currAttr = listOfAttr[0]
    
    return listOfAttr.index(currAttr)


def get_examples(exampleSet, cond, index):
    '''
    obtains the example sets
    '''
    outputList = []
    
    for ex in exampleSet:
        if ex[index] == cond:
            outputList.append(ex)
            
    return outputList
    

def ID3(examples, listOfAttr, default):
    '''
    Takes in an array of examples, and returns a tree (an instance of Node) 
    trained on the examples.  Each example is a dictionary of attribute:value pairs,
    and the target class variable is a special attribute with the name "Class".
    Any missing attributes are denoted with a value of "?"
    '''       
    if not examples:
        return default
  
    elif (sameClass(examples) != 2):
        return sameClass(examples)
    
    elif not listOfAttr:
        return mode(examples)
    
    else:
        index = chooseAttr(listOfAttr, examples)
        
        best = listOfAttr[index]
        
        tree = Node(best)
        
        for i, item in enumerate([True, False]):
            example = get_examples(examples, item, index)
            
            subTree = ID3(updateExamples(example, listOfAttr, best, item),
                          updateAttr(listOfAttr, best), mode(examples))
            
            tree.addBranch(item, subTree)
            
    return tree


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
    counter = 0
    
    for i, item in enumerate(examples):
        if item == node[1]:
            counter += 1
    
    output = float(counter) / len(node)
    
    return output
  

def evaluate(node, example):
    '''
    Takes in a tree and one example.  Returns the Class value that the tree
    assigns to the example.
    '''
    
    




