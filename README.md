# HW4

The mandelbrot.py file represent the Mandelbrot set. A [-2,1] x [-1.5,1.5] grid was created with corresponding complex values using the numpy.meshgrid. From there, I created a 2D boolean array called mask, which shows what points were in the set based on the threshold of 50. Lastly, an image was saved as 'mandelbrot.png' of the grid with the values.

The markov_chain.py file showed the probability after an N amount of steps in a markov chain. I created a random n vector and random nxn matrix. The sum of the vector is 1 and the sum of each row in the matrix is also one. Then, starting from the initial state of the vector, I computed the transition after N times. In this case, n is 5 and N is 50.
