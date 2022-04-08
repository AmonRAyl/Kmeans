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
