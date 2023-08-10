def bubbleSort(array):
     length=len(array)
     for i in range(0,length,1):
          for j in range(0,length-1):
               if (array[j]>array[j+1]):
                    temp=array[j]
                    array[j]=array[j+1]
                    array[j+1]=temp
    

def insertionSort(array):
     length=len(array)
     for i in range(1,length,1):
          key=array[i]
          j=i-1
          while((j>-1)and (array[j]>key)):
               array[j+1]=array[j]
               j=j-1
          array[j+1]=key


def selectionSort(array):
     for i in range (0,len(array),1):
          small=i
          for j in range (i+1,len(array),1):
               if (array[j]<array[small]):
                    small=j
               temp=array[i]
               array[i]=array[small]
               array[small]=temp
                
          


          
