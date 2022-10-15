import numpy as np
import warnings

#prevents overflow encountered in square
warnings.filterwarnings('ignore')

def mandelbrot(N_max, threshold, n):
    #sets x and y parameters for a nxn 1D array
    x = np.linspace(-2, 1, n)
    y = np.linspace( -1.5, 1.5, n)
    
    #nxn grid (2D array)
    x1, y1 = np.meshgrid(x, y)
    #complex values
    c = x1 + 1j*y1
    
    z = 0
    #iteration to compute z for each complex value
    for j in range(N_max):
        z = z**2 + c
    
    #2D boolean array which checks when |z| < threshold
    mask = (abs(z) < threshold)
    
    return mask

#calls on the mandelbrot function
mask = mandelbrot(N_max = 50, threshold = 50, n = 500)

#shows and saves result of plot as "mandelbrot.png"
import matplotlib.pyplot as plt

plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')
