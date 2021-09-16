import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  p = np.array(list).reshape(3,3)

  result = {
    'mean': [np.mean(p,axis=0).tolist(), np.mean(p,axis=1).tolist(), np.mean(p, axis = None).tolist()],
    'variance': [np.var(p,axis=0).tolist(), np.var(p,axis=1).tolist(), np.var(p, axis = None).tolist()],
    'standard deviation': [np.std(p,axis=0).tolist(), np.std(p,axis=1).tolist(), np.std(p, axis = None).tolist()],
    'max': [np.max(p,axis=0).tolist(), np.max(p,axis=1).tolist(), np.max(p, axis = None).tolist()],
    'min': [np.min(p,axis=0).tolist(), np.min(p,axis=1).tolist(), np.min(p, axis = None).tolist()],
    'sum': [np.sum(p,axis=0).tolist(), np.sum(p,axis=1).tolist(), np.sum(p, axis = None).tolist()]
    }
  return result