Mat = distance(self.X, self.centroids)
self.labels = np.argmin(Mat, axis=1)
