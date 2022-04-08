np.copyto(self.old_centroids,self.centroids)
aux=[]
for i in range(self.K):
    sumax=0
    sumay=0
    sumaz=0
    tot=0
    for j in range(self.X.shape[0]):
        if self.labels[j] == i:
            sumax=sumax+self.X[j][0]
            sumay=sumay+self.X[j][1]
            sumaz=sumaz+self.X[j][2]
            tot=tot+1
    mediox=(sumax)/tot
    medioy=(sumay)/tot
    medioz=(sumaz)/tot
    aux.append([mediox,medioy,medioz])
self.centroids=np.array(aux)
