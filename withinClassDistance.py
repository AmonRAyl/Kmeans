Wcd=0
for j in range(self.K):
    Puntos=np.where(self.labels == j)
    Inter=self.X[Puntos]
    Wcd+=np.sum(cdist([self.centroids[j]],Inter,'euclidean')**2)
return Wcd/self.X.shape[0]
