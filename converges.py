res = np.allclose(self.centroids, self.old_centroids,0.0001,0.0001,equal_nan=False)
return res
