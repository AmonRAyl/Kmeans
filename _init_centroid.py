aux = []
if self.options['km_init'].lower() == 'first':#Pillamos los primeros valores diferentes entre ellos
    for j in range(self.X.shape[0]):
        t=0
        for elem in aux:  # comprobamos para no repetir valores
            valor = self.X[j]
            if (valor == elem).all():
                t = 1
                break
        if t != 1:
            aux.append(self.X[j])
        if len(aux) == self.K:
            break
elif self.options['km_init'].lower() =='random':#Opcion de generacion aleatoria
    while len(aux)!=self.K:
        valor=self.X[random.randint(0,self.X.shape[0])]
        t = 0
        for elem in aux:  # comprobamos para no repetir valores
            if (valor == elem).all():
                t = 1
                break
        if t != 1:
            aux.append(valor)
elif self.options['km_init'].lower() == 'custom':  # Opcion de generacion personalizada, vamos pegando saltos de shape[0]/K si no se llena k++
    k=self.K
    j=int(self.X.shape[0]/k)
    while len(aux) != self.K:
        valor=self.X[j]
        t = 0
        for elem in aux:  # comprobamos para no repetir valores
            if (valor == elem).all():
                t = 1
                break
        if t != 1:
            aux.append(valor)
        if j > self.X.shape[0]:
            k=k+1
            j=0
            j=int(self.X.shape[0]/k)+j
        else:
            j=int(self.X.shape[0]/k)+j

self.centroids = np.array(aux[0:])
self.old_centroids = np.array(aux[0:])#No se que hacer con lo de los antiguos
