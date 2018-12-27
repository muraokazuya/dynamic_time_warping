# dynamic_time_warping
Calculate DTW distance of two 1-d time series a and b, returning its DTW distance divided by the sum of length of a and length of b.
Each cell of matrix stores DTW distance at each point.
Distance between i in a and j in b is |a[i]-b[j]|.
Matrix is initialized with np.Inf at [:,0] and [0,:] except [0,0].
