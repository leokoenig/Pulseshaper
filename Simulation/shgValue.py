import numpy as np

# shgValue  calculate 4. moment which is relevant for shg. 
# normalize in order to get results in a reasonable numeric range 
# which is important for optimization

def shgValue(y):
   y = y / np.sum( np.power( np.abs(y) ,2) )
   shg = np.sum( np.power( np.abs(y) ,4) )

   return shg