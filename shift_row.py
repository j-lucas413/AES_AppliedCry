#****************************************
#
#  Shift row
#
#****************************************

def shift_row(state_matrix):
  shifted = [[], [], [], []]

  # First row shifted by zero (no change)
  shifted[0] = [0, 0, 0, 0]
  shifted[0][0] = state_matrix[0][0]
  shifted[0][1] = state_matrix[0][1]
  shifted[0][2] = state_matrix[0][2]
  shifted[0][3] = state_matrix[0][3]

  # Second row shifted by one
  shifted[1] = [0, 0, 0, 0]
  shifted[1][0] = state_matrix[1][1]
  shifted[1][1] = state_matrix[1][2]
  shifted[1][2] = state_matrix[1][3]
  shifted[1][3] = state_matrix[1][0]

  # Third row shifted by two
  shifted[2] = [0, 0, 0, 0]
  shifted[2][0] = state_matrix[2][2]
  shifted[2][1] = state_matrix[2][3]
  shifted[2][2] = state_matrix[2][0]
  shifted[2][3] = state_matrix[2][1]

  # Fourth row shifted by three
  shifted[3] = [0, 0, 0, 0]
  shifted[3][0] = state_matrix[3][3]
  shifted[3][1] = state_matrix[3][0]
  shifted[3][2] = state_matrix[3][1]
  shifted[3][3] = state_matrix[3][2]
  
  return shifted