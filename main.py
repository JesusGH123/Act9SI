import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def getDistance(x1, x2):
  return abs(x2-x1)
  
def findCentroid(x2):
  distancesToCentroids = []
  for x1 in centroidsPos:
    distancesToCentroids.append(getDistance(x1, x2))
  min_value = min(distancesToCentroids)

  return distancesToCentroids.index(min_value), min_value

def getMatrixD():
  matrixD = [[], [], [], []]
  for aData in data:
    matrixD[0].append(aData[1])
  for i in range(1, len(matrixD)):
    for aData in matrixD[0]:
      matrixD[i].append(round(getDistance(centroidsPos[i-1], aData), 2))
  
  return matrixD
  
def getMatrixG():
  matrixG = [[], [], [], []]
  for aData in data:
    matrixG[0].append(aData[1])

  for j in range(0, len(matrixD[0])):
    minElem = sys.maxsize
    for i in range(1, len(matrixG)):
      if(matrixD[i][j] < minElem):
        minElem = matrixD[i][j]
    for i in range(1, len(matrixG)):
        if(matrixD[i][j] == minElem):
          matrixG[i].append(1)
        else:
          matrixG[i].append(0)
  
  return matrixG
  
#Driver code
completeData = pd.read_excel('peliculas.xlsx') #Read xlsx
data = []
category = "Likes"
maxVal = max(completeData[category].tolist()) #Max element

#Extract the necessary columns and added to an array
for i in range(0, len(completeData)):
  data.append((completeData["Movie"].iloc[i], completeData[category].iloc[i]))

centroidsPos = [5000, 20000, 35000]  #Centroids initial position
limit = int(input("Cuantas iteraciones quieres hacer?: "))
for i in range(0, limit):
  centroids = [[], [], []]
  matrixD = getMatrixD()
  matrixG = getMatrixG()

  for i in range(0, len(data)):
    centroid, distToCentroid = findCentroid(data[i][1])
    centroids[centroid].append(data[i])  #Append data to the corresponding centroid
  
  #Print data in each iteration
  print("The centroids are in: ", centroidsPos)
  print("MatrixD: ")
  for i in range(0, len(matrixD)):
    if(i>0): 
      print("C",i, sep="", end=" ")
    print(matrixD[i])
  print("MatrixG: ")
  for i in range(0, len(matrixG)):
    if(i>0):
      print("C",i, sep="", end=" ")
    print(matrixG[i])
  print("\n")
  
  #Reassign the centroids
  for i in range(0, len(centroids)):
    sum = 0
    for j in range(0, len(centroids[i])):
      sum += centroids[i][j][1]
    if(len(centroids[i]) > 0):
      centroidsPos[i] = sum/len(centroids[i])  #Average of the centroid

for i in range(1, 4):
  if(i > 0): print("Centroid ", i)
  for j in range(0, len(centroids[i-1])):
    print('\t- Movie: "', centroids[i-1][j][0], f'" {category}:', centroids[i-1][j][1], sep="")

#Graphics
matrixD = matrixD.pop(0)  #Delete the title column
plt.plot([i for i in range(0, len(data))], np.array(matrixD).flatten(), 'ro')
plt.axis([1, len(data), 0, maxVal + 1])
plt.xlabel('Movies')
plt.ylabel(f'{category}')
plt.show()