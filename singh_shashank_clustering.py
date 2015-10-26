
# This algorithm is used to perform clustering of objects for Iris Dataset using K-means clustering algorithm.

import sys
import urllib
import math
import operator
files = sys.argv

f = open(files[4], 'r')
# number of iterations
iter = int(files[3])
# number of clusters
k = int(files[2])
# the centroid points
centroids = {}
# list of points belonging to each cluster
cluster_points = {}
# all unique names from the list of points
names = set()
names_in_data = set()

for i, line in enumerate(f.readlines()):
    values = line.split(',')
    for j in range(len(values)-1):
        values[j] = float(values[j])
    values[len(values) - 1] = values[len(values) - 1].rstrip('\n')
    centroids[values[len(values) - 1]] = values
    names.add(values[len(values) - 1])
f.close()

points = {}

f = open(files[1], 'r')
for i, line in enumerate(f.readlines()):
    values = line.split(',')
    if len(values) != 5:
        continue
    for j in range(len(values)-1):
        values[j] = float(values[j])
    values[len(values) - 1] = values[len(values) - 1].rstrip('\n')
    points[i] = values
    names_in_data.add(values[len(values) - 1])

flag = 0
for i in range(iter):
    if k != len(centroids):
        print('K != number of initial points in the file')
        flag = 1
        break

    else:
        for key in centroids.keys():
            cluster_points[key] = []
        for j in points.keys():
            mindistance = float('inf')
            cluster = ''
            # find which cluster this point j belongs to.
            for l in centroids.keys():
                x = math.pow((centroids[l][0] - points[j][0]), 2)
                y = math.pow((centroids[l][1] - points[j][1]), 2)
                z = math.pow((centroids[l][2] - points[j][2]), 2)
                w = math.pow((centroids[l][3] - points[j][3]), 2)
                d = math.sqrt(x + y + z + w)
                if d < mindistance:
                    mindistance = d
                    cluster = l
            cluster_points[cluster].append(points[j])

        # calculate the centroid again after points have been assigned.
        for l in cluster_points.keys():
            x, y, z, w = 0, 0, 0, 0
            for j in range(len(cluster_points[l])):
                x += cluster_points[l][j][0]
                y += cluster_points[l][j][1]
                z += cluster_points[l][j][2]
                w += cluster_points[l][j][3]
            centroids[l] = []
            length = len(cluster_points[l])
            if length == 0:
                centroids[l] = [0, 0, 0, 0]
            else:
                centroids[l] = [x/float(length), y/float(length), z/float(length), w/float(length)]

names = list(names)
sum = 0
for name, cluster in cluster_points.items():
    # contains no. of occurence of each distinct name type
    occ = {}
    for n in names_in_data:
        occ[n] = 0
    for points in cluster:
        occ[points[len(points) - 1]] += 1
    # print(occ)
    res = sorted(occ.items(), key=lambda x: (-x[1], x[0]))
    value = res[:1][0][0]
    for key in occ.keys():
        if key != value:
            sum += occ[key]
    print(' '.join(['Cluster', value]))
    for point in cluster:
        print(point)

# if k == number of points in initial points then..
if flag != 1:
    print('Number of points assigned to wrong cluster:')
    print(sum)



