using Quadmath, LinearAlgebra, SparseArrays, DelimitedFiles

const F = Float128
const p = F(pi)
const r = sqrt(F(10)) / 2
const m = F(1)
N = 10000

V = Matrix{F}(undef, N, N)
for i in 1:N
    for j in i:N
        perturbation = F(0.02) * rand(F) - F(0.01)
        V[i, j] = perturbation
        V[j, i] = perturbation
    end
end

writedlm("purturb10000.csv", V)