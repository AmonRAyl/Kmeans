tot = 0
for j in range(self.K):
    total=0
    for i in range(self.X.shape[0]):
        if self.labels[i] == j:
            total = total + cdist([self.centroids[j]],[self.X[i]],'euclidean')**2
    tot = total + tot
WCD = tot/self.X.shape[0]
return WCD
