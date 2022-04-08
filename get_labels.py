Vect=[]
Mat=distance(self.X,self.centroids)
for i in Mat:
    Minim=i.min()
    vect = i;
    for j in range(self.K):
        if vect[j] == Minim:
            index=j
            break
    Vect.append(index)
self.labels=np.array(Vect)
