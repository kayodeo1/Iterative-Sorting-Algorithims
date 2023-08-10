import random #to generate random array
import time #to analyse algorithim runtime
import matplotlib.pyplot as plt # to  compare algorithim runtime on a graph
import Sort #importing the sortin algorithims from module Sort

arr=[]#initialising the array
Time=[]
arrSizes=[10,50,100,500,1000]#i.e the sizes of data we want to compare

def getTime(algorithim,array):#analysing the algorithim and appending the time taken for analysing into an array Time
    startTime=time.time()
    algorithim(array)
    stopTime=time.time()
    timeTaken=stopTime-startTime
    Time.append(timeTaken)
    

for i in range (len(arrSizes)):#analysing bubblesort
    for j in range (arrSizes[i]):
        arr.append(random.randint(1,100))
    
    getTime(Sort.bubbleSort,arr)  
    arr=[]
    
plt.plot(arrSizes,Time ,label="Bubble sort", color="blue")
Time=[]

for i in range (len(arrSizes)):#analysing bubblesort
    for j in range (arrSizes[i]):
        arr.append(random.randint(1,100))
        
    getTime(Sort.insertionSort,arr)  
    arr=[]
    
plt.plot(arrSizes,Time ,label="Insertion sort", color="yellow")
Time=[
      ]
for i in range (len(arrSizes)):#analysing bubblesort
    for j in range (arrSizes[i]):
        arr.append(random.randint(1,100))
        
    getTime(Sort.selectionSort,arr)  
    arr=[]
    
plt.plot(arrSizes,Time,label="Selection sort", color="red")
plt.show()


    


print(arr)