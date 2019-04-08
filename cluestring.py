def minkowskiDist(v1, v2, p):
    #Assumes v1 and v2 are equal length arrays of numbers
    dist = 0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)


class Example(object):
	def __init__(self,featuers,name,label):
		self.name=name
		self.featuers=featuers
		self.label=label
	def getFeauers(self):
		return self.featuers[:]
	def getDimnosinalty(self):
		return len(self.featuers) 


	def distance(self, other):
		return minkowskiDist(self.featuers,other.getFeauers(),2)


class Cluster(object):
	def __init__(self,examples):
		self.examples=examples
		self.centroid = self.computeCentroid()

	def update(self,examples):

		oldCentroid = self.centroid
		self.examples = examples
		self.centroid = self.computeCentroid()
		return oldCentroid.distance(self.centroid)  
	def computeCentroid(self):
		vals = pylab.array([0.0]*self.examples[0].dimensionality()) 

		for e in self.examples:
			vals += e.getFeauers()

		centroid = Example('centroid', vals/len(self.examples))
		return centroid
        

def kmeans(examples):
	initialCentroids = random.sample(examples, k) # random centroids of k(given) clusters 
	clusters = [] 
	for e in initialCentroids:
		clusters.append(cluster.Cluster([e])) 

	converged = False
	numIterations = 0 
	while not converged:
		numIterations += 1 
		newClusters = [] 
		for i in range(k):
		 	newClusters.append([]) 
		for e in examples:
			smallestDistance = e.distance(clusters[0].getCentroid())

            #Find the centroid closest to e
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e) 
        for c in newClusters: #Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
    return clusters
       
            

    
        

