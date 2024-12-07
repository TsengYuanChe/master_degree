using Quadmath, GenericSchur, LinearAlgebra, DelimitedFiles
const F=Float128
const p=F(pi)
const r=sqrt(F(10))/2
const m=F(1)
N=30
MP=Matrix{F}(undef,N,N)
MK=Matrix{F}(undef,N,N)

for b=1:N
    MP[b,b]=1/p/r*sum(1/(j+1/2) for j in 0:(2*b-1))
end
for c=1:N
    MK[c,c]=(c^2-1)/m/r/r
end
M=(MK+MP)
e = diagm(M)
E=real(filter(z->imag(z)==F(0),e))
writedlm("dia10000.csv",E)