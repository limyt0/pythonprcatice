# Broadcasting
# view() (numpy의 경우는 reshape())

## X.shape
## X.view(3,10).shape
## torch.Size([3, 10])
import torch
X = torch.rand(3,2,5)
Y = torch.rand(3,5,3)

## 왜냐면 3*10 = 3*2*5 =30으로 같으므로!!  
# xshape = X.view(3,10).shape
# print(xshape)

# X = X.view(3,10) #이것도 가능.
# print(X.shape)
# X.view(3,10).shape #이건 x를 안바꿈
print(X.view(3,10).shape)

X = X.view(3,10) # 왜냐면 3*10 = #3*2*5 
# X = X.view(3,-1) # 
print(X)