mat=utils.get_color_prob(centroids)
lista=[]
for i in range(mat.shape[0]):
    lista.append(utils.colors[np.where(mat[i] == np.amax(mat[i]))])
return lista
