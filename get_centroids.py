np.copyto(self.old_centroids,self.centroids)
List=[]
for i in range(self.K):
    PuntosK=np.where(self.labels==i)
    Puntos=self.X[PuntosK]
    List.append(np.mean(Puntos,axis=0))
self.centroids=np.array(List)
