Mat=[]
for i in X:
    fila=[]
    for j in C:
        deuc=math.sqrt((i[0]-j[0])**2+(i[1]-j[1])**2+(i[2]-j[2])**2)#suponiendo 3 dimensiones
        fila.append(deuc)
    Mat.append(np.array(fila))
return Mat
