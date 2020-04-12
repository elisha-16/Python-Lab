def subarray(a,N,K):
    for l in range(0,N):
        sum=a[l]
        for j in range(l+1,N):
            sum = sum + a[j]
            if (sum == K):
                print(l, j)
                return 1

    print('not found')

T=int(input('No. of testcases:'))
for k in range(T):
    N,K=input().split()
    N=int(N)
    K=int(K)
    a=[int(i) for i in input().split()]
    subarray(a,N,K)








