import fill_arrays_loop as fal
import numpy as np

def main():
    # Defining limits and spaces

    # Creating two  arrays
    x = np.linspace(fal.xmin, fal.xmax, fal.n)
    y = np.empty(fal.n)
    # Vectorizing h(x)
    h_vec = np.vectorize(fal.h)
    # Filling array
    y = h_vec(x)
    # This is overwriting y.

    # Output
    print("{0:>10s} {1:>10s}".format("x", "h(x)"))
    for i in range(fal.n):
        print("{0:>10.1f} {1:>10.6f}".format(x[i], y[i]))

if __name__ == '__main__':
    main()
# Terminal Output:
'''
$ python fill_arrays_vectorized.py
         x       h(x)
      -4.0   0.000134
      -3.8   0.000292
      -3.6   0.000612
      -3.4   0.001232
      -3.2   0.002384
      -3.0   0.004432
      -2.8   0.007915
      -2.6   0.013583
      -2.4   0.022395
      -2.2   0.035475
      -2.0   0.053991
      -1.8   0.078950
      -1.6   0.110921
      -1.4   0.149727
      -1.2   0.194186
      -1.0   0.241971
      -0.8   0.289692
      -0.6   0.333225
      -0.4   0.368270
      -0.2   0.391043
       0.0   0.398942
       0.2   0.391043
       0.4   0.368270
       0.6   0.333225
       0.8   0.289692
       1.0   0.241971
       1.2   0.194186
       1.4   0.149727
       1.6   0.110921
       1.8   0.078950
       2.0   0.053991
       2.2   0.035475
       2.4   0.022395
       2.6   0.013583
       2.8   0.007915
       3.0   0.004432
       3.2   0.002384
       3.4   0.001232
       3.6   0.000612
       3.8   0.000292
       4.0   0.000134
'''
