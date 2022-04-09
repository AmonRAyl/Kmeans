__authors__ = ['1566576', '1563118', '1564785']
__group__ = 'DL.15'

import numpy as np
import utils
import random
from scipy.spatial.distance import cdist

class KMeans:

    def __init__(self, X, K=1, options=None):
        """
         Constructor of KMeans class
             Args:
                 K (int): Number of cluster
                 options (dict): dictÂºionary with options
        """
        self.num_iter = 0
        self.K = K
        self._init_X(X)
        self._init_options(options)  # DICT options

    def _init_X(self, X):
        """Initialization of all pixels, sets X as an array of data in vector form (PxD)
            Args:
                X (list or np.array): list(matrix) of all pixel values
                    if matrix has more than 2 dimensions, the dimensionality of the smaple space is the length of
                    the last dimension
        """

        ## Miramos si la matriz es float , sino la ponemos a float
        ## Miramos dimension si esta es 3 la pasamos a 2
        if X.dtype.kind != 'f':
            X = X.astype('float64')
        if X.ndim == 3:
            Fil = X.shape[0]
            Col = X.shape[1]
            N = Fil * Col
            X = X.reshape((N, X.shape[2]))
        self.X = X

    def _init_options(self, options=None):
        """
        Initialization of options in case some fields are left undefined
        Args:
            options (dict): dictionary with options
        """
        if options == None:
            options = {}
        if not 'km_init' in options:
            options['km_init'] = 'first'
        if not 'verbose' in options:
            options['verbose'] = False
        if not 'tolerance' in options:
            options['tolerance'] = 0
        if not 'max_iter' in options:
            options['max_iter'] = np.inf
        if not 'fitting' in options:
            options['fitting'] = 'WCD'  # within class distance.

        # If your methods need any other prameter you can add it to the options dictionary
        self.options = options

    def _init_centroids(self):
        """
        Initialization of centroids
       """
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

    def get_labels(self):
        """        Calculates the closest centroid of all points in X
        and assigns each point to the closest centroid
        """
        Mat = distance(self.X, self.centroids)
        self.labels = np.argmin(Mat, axis=1)

    def get_centroids(self):
        """
        Calculates coordinates of centroids based on the coordinates of all the points assigned to the centroid
        """
        np.copyto(self.old_centroids,self.centroids)
        List=[]
        for i in range(self.K):
            PuntosK=np.where(self.labels==i)
            Puntos=self.X[PuntosK]
            List.append(np.mean(Puntos,axis=0))
        self.centroids=np.array(List)

    def converges(self):
        """
        Checks if there is a difference between current and old centroids
        """
        res = np.allclose(self.centroids, self.old_centroids,0.0001,0.0001,equal_nan=False)
        return res

    def fit(self):
        """
        Runs K-Means algorithm until it converges or until the number
        of iterations is smaller than the maximum number of iterations.
        """
        bool = False
        self._init_centroids()
        j = 0
        while bool == False and j < self.options['max_iter']:
            self.get_labels()
            self.get_centroids()
            j+=1
            if self.converges() == True:
                bool = True

    def whitinClassDistance(self):
        """
         returns the whithin class distance of the current clustering
        """
        Wcd=0
        for j in range(self.K):
            Puntos=np.where(self.labels == j)
            Inter=self.X[Puntos]
            Wcd+=np.sum(cdist([self.centroids[j]],Inter,'euclidean')**2)
        return Wcd/self.X.shape[0]

    def find_bestK(self, max_K):
        """
         sets the best k anlysing the results up to 'max_K' clusters
        """
        self.K = 1
        self.fit()
        WCDK = self.whitinClassDistance()
        for i in range(2, max_K):
            self.K = i
            self.fit()
            WCD = self.whitinClassDistance()
            DEC = 100 * WCD / WCDK
            WCDK = WCD
            if 100 - DEC < 20:
               self.K = i-1
               break

def distance(X, C):
    """
    Calculates the distance between each pixcel and each centroid
    Args:
        X (numpy array): PxD 1st set of data points (usually data points)
        C (numpy array): KxD 2nd set of data points (usually cluster centroids points)

    Returns:
        dist: PxK numpy array position ij is the distance between the
        i-th point of the first set an the j-th point of the second set
    """
    deuc = cdist(X, C, 'euclidean')
    return deuc

def get_colors(centroids):
    """
    for each row of the numpy matrix 'centroids' returns the color laber folllowing the 11 basic colors as a LIST
    Args:
        centroids (numpy array): KxD 1st set of data points (usually centroind points)

    Returns:
        lables: list of K labels corresponding to one of the 11 basic colors
    """
    mat=utils.get_color_prob(centroids)
    lista=[]
    for i in range(mat.shape[0]):
        lista.append(utils.colors[np.where(mat[i] == np.amax(mat[i]))])
    return lista