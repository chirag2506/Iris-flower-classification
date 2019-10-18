import csv
import random
import math
import operator
import sys



def loadDataset(filename,split_ratio,training_data,test_data):
    
    with open(filename,"r") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        
        for x in range(len(dataset)- 1):    # iterate each row of dataset
            for y in range(4):              #iterate first 4 columns of xth row
                dataset[x][y] = float(dataset[x][y])
                
            if random.random() < split_ratio:        # split data into two parts, training_data and test_data. The distribution is random and approximate ratio of split is equal to split_ratio
                training_data.append(dataset[x])
            else:
                test_data.append(dataset[x])
                
 
               
def euclidean_distance(ins1,ins2,features):
    
    distance = 0
    for x in range(features):
        distance += pow(ins1[x] - ins2[x],2)

    return math.sqrt(distance)


def getNeighbours(training_data,test_ins,k):
    
    distances = []      # list to store distance of test_data instance from every training_data instance 
    features = len(test_ins) - 1   # Number of features to consider in finding euclidean distance


    for x in range(len(training_data)):                  #iterate each row of training_data 
        distance = euclidean_distance(test_ins,training_data[x], features)
        distances.append((training_data[x],distance))

    '''
    distances now contains a list of tuples where first element is the training_data row and second element is distance
    '''
    distances.sort(key = operator.itemgetter(1))  # sort distances according to second element of tuple, i.e distance.


    neighbours = []
    for x in range(k):                      #append k nearest neighbours of test_data instance in list called neighbours
        neighbours.append(distances[x][0])
        
    return neighbours


def getResponseVotes(neighbours):
    
    classvotes = {}       # a dictionary to store frequency of each type of neighbour

    
    for x in range(len(neighbours)):       # iterate through each neighbour
        response = neighbours[x][-1]       # response is the last column of our dataset ('type of iris' in case of iris dataset)

        if response in classvotes:
            classvotes[response] +=1
        else:
            classvotes[response] = 1

    '''
    create a sorted list of tuples in descending order.
    In iris data set, this tuple is of form:(iris-type, frequency of iris-type)
    '''
    sortedvotes = sorted(classvotes.items(),key = operator.itemgetter(1),reverse = True)    

    return sortedvotes[0][0]     # return predicted iris-type




def main():
    
    d1 = float(sys.argv[1])
    d2 = float(sys.argv[2])
    d3 = float(sys.argv[3])
    d4 = float(sys.argv[4])   
    
    training_data = []
    test_data = []
    quest_data = [d1,d2,d3,d4]
    

    filename = "iris.data"       # name of data file to load
    split_ratio = 0.66           # splitting ratio of training and test data set
    k = 3                        # k is the no. of nearest neighbors we wish to take vote from

    loadDataset(filename,split_ratio,training_data,test_data)

    neighbours = getNeighbours(training_data, quest_data, k)
    prediction = getResponseVotes(neighbours)
    print(prediction)
    
if __name__ == "__main__":          
    main()