using Quadmath, GenericSchur, LinearAlgebra, DelimitedFiles
const F=Float128
const p=F(pi)
const r=sqrt(F(10))/2
const m=F(1)
N=10000
MP=Matrix{F}(undef,N,N)
MK=Matrix{F}(undef,N,N)
for a=1:N
    for b=1:N
        MP[a,b]=(-1)^(a+b)/p/r*sum(1/(j+abs(a-b)+1/2) for j in 0:(2*min(a-1,b-1)+1))
    end
end
for c=1:N
    MK[c,c]=(c^2-1)/m/r/r
end
M=(MK)
e=eigvals(M)
E=real(filter(z->imag(z)==F(0),e))
writedlm("energy10000.csv",E)

