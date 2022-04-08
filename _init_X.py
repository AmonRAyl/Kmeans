if X.dtype.kind != 'f':
    X = X.astype('float64')
if X.ndim ==3:
    Fil=X.shape[0]
    Col=X.shape[1]
    N=Fil*Col
    X=X.reshape((N,X.shape[2]))
self.X=X
