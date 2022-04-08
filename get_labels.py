Vect=[]
Mat=distance(self.X,self.centroids)
for i in Mat:
    Minim=i.min()
    vect = i.getA();
    for j in range(self.K):
        if vect[0][j] == Minim:
            index=j
            break
    Vect.append(index)
self.labels=np.array(Vect)
