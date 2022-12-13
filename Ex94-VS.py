import numpy as np

def Inp_Matrix(n1, n2):
  A = np.zeros((n1,n2))
  for i in range(n1):
    print('Nhap phan tu hang {}: '.format(i+1))
    lst = list(map(float, input('').split()))
    if len(lst) != n2:
      print('Nhap lai day so')
    else:
      for j in range(n2):
        A[i][j] = lst[j]
  return A

def Count_Matrix(A):
  values, count = np.unique(A, return_counts = True)
  Alst = values.tolist()
  Acount = count.tolist()
  lst = []
  for i in range(len(Alst)):
    if int(Acount[i]) >= A.shape[0]:
      lst.append(values[i])
  return lst

def List_Matrix(lst, A):
  out_lst = []
  for i in lst:
      count = 0
      for j in range(A.shape[0]):
          if A[j,:].tolist().count(i) > 0:
              count += 1
      if count == A.shape[0]:
          out_lst.append(i)
  return out_lst

n1 = int(input('Nhap so hang: '))
n2 = int(input('Nhap so cot: '))

A = Inp_Matrix(n1, n2)

print('Matrix input:')
print(A)

lst = Count_Matrix(A)

print('Matrix output: ')
print(List_Matrix(lst, A))