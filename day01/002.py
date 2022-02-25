## Mul 과 Matmul의 차이
import torch

X = torch.rand(3,2,5)
# Z = torch.tensor([1]) - X
Y = torch.rand(3,5,3)

X1 = torch.rand(3,2,2)
Y1 = torch.rand(3,2,4)

D = X.matmul(Y) # 행렬 곱 (내적)
print('D :', D)
print('D.shape : ', D.shape) 
print('X.mul(Y) : ', X1.mul(Y1))   
 # X*Y 와 동일. 각 원소 별로 곱하는 연산.(사이즈 맞춰야 연산 가능)
 # 사이즈 다른건 1하고만 되나...???
