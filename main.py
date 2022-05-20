import pandas as pd

def findCentroid(point):
  distancesToCentroids = []
  for i in centroidsPos:
    distancesToCentroids.append(abs(i -point))
  min_value = min(distancesToCentroids)

  return distancesToCentroids.index(min_value)

#Driver code
completeData = pd.read_excel('peliculas.xlsx') #Read xlsx
data = []

#Extract the necessary columns and added to an array
for i in range(0, 20):
  data.append((completeData["Movie"].iloc[i], completeData["Genre"].iloc[i]))

#Data for k-means
centroidsPos = [1,2,3]

for i in range(0, 100):
  centroids = [[], [], []]
  matrixD = centroids
  matrixG = centroids
  
  print("The centroids are in: ", centroidsPos)
  
  for i in range(0, len(data)):
    current = findCentroid(data[i][1])
    centroids[current].append(data[i])
  
  #Reassign the centroids
  for i in range(0, len(centroids)):
    sum = 0
    for j in range(0, len(centroids[i])):
      sum += centroids[i][j][1]
    if(len(centroids[i]) > 0):
      centroidsPos[i] = sum/len(centroids[i])  #Average of the centroid
    #print("Average in centroid ", i , " is: ", average)

for i in range(1, 4):
    print("Centroid ",i, centroids[i-1])