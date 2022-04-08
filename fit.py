bool = False
self._init_centroids()
j = 0
while bool == False and j < 1000:
    self.get_labels()
    self.get_centroids()
    j = j + 1
    if self.converges() == True:
        bool = True
    else:
        bool = False
