class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)

    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])

def add(x, y):
    return x + y

n = int(input())
q = int(input())

t, x, y, v = [0] * q, [0] * q, [0] * q, [0] * q
for i in range(q):
    t[i], x[i], y[i], v[i] = map(int,input().split())

s = segtree([1] * n, add, 0)

sum = [0] * n

for i in range(q):
    if t[i] == 0:
        sum[x[i]] = v[i]
#print(sum)
pot = [0] * (n + 1)
for i in range(1, n):
    pot[i + 1] = sum[i] - pot[i]
#print(pot)
for i in range(q):
    if t[i] == 0:
        s.set(x[i], 0)
    elif t[i] == 1:
        a = min(x[i], y[i])
        b = max(x[i], y[i])
        it = s.prod(a, b)
        if it == 0:
            print(pot[y[i]] + (v[i] - pot[x[i]]) if (b - a) % 2 == 0 else pot[y[i]] - (v[i] - pot[x[i]]))
        else:
            print('Ambiguous')