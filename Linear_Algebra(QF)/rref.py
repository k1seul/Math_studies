# code from https://gist.github.com/sgsfak/77a1c08ac8a9b0af77393b24e44c9547
import numpy as np

def rref(B, tol=1e-8, debug=False):
  A = B.copy()
  rows, cols = A.shape
  r = 0
  pivots_pos = []
  row_exchanges = np.arange(rows)
  for c in range(cols):

    ## Find the pivot row:
    pivot = np.argmax (np.abs (A[r:rows,c])) + r
    m = np.abs(A[pivot, c])
    if m <= tol:
      ## Skip column c, making sure the approximately zero terms are
      ## actually zero.
      A[r:rows, c] = np.zeros(rows-r)
    else:
      ## keep track of bound variables
      pivots_pos.append((r,c))

      if pivot != r:
        ## Swap current row and pivot row
        A[[pivot, r], c:cols] = A[[r, pivot], c:cols]
        row_exchanges[[pivot,r]] = row_exchanges[[r,pivot]]
        

      ## Normalize pivot row
      A[r, c:cols] = A[r, c:cols] / A[r, c];

      ## Eliminate the current column
      v = A[r, c:cols]
      ## Above (before row r):
      if r > 0:
        ridx_above = np.arange(r)
        A[ridx_above, c:cols] = A[ridx_above, c:cols] - np.outer(v, A[ridx_above, c]).T
      ## Below (after row r):
      if r < rows-1:
        ridx_below = np.arange(r+1,rows)
        A[ridx_below, c:cols] = A[ridx_below, c:cols] - np.outer(v, A[ridx_below, c]).T
      r += 1
    ## Check if done
    if r == rows:
      break;
  return (A, pivots_pos, row_exchanges)

A = np.array([[1,4,9,16],
             [4,9,16,25],
             [9,16,15,36],
             [16,25,36,49]])

print(f"{A:}")
print("-"*5+"After rref"+"-"*5)
A, _, _ = rref(A)
print(f"{A:}")
