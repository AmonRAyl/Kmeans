bool = False
self._init_centroids()
j = 0
while bool == False and j < self.options['max_iter']:
    self.get_labels()
    self.get_centroids()
    j+=1
    if self.converges() == True:
        bool = True
