using SpecialFunctions

function calculate_expression(j1, j2, J, m1, m2, M)
    # 預先計算分母和分子中的 binomial 係數
    numerator = binomial(2j1, j1 + j2 - J) * binomial(2j2, j1 + j2 - J)
    denominator = binomial(j1 + j2 + J + 1, j1 + j2 - J) *
                  binomial(2j1, j1 - m1) *
                  binomial(2j2, j2 - m2) *
                  binomial(2J, J - M)
    
    # 公式的平方根部分
    coefficient = sqrt(numerator / denominator)
    
    # 計算求和部分
    sum_result = 0.0
    for k in 0:(j1 - m1)
        term = (-1)^k * 
               binomial(j1 + j2 - J, k) * 
               binomial(j1 - j2 + J, j1 - m1 - k) * 
               binomial(j2 - j1 + J, j2 + m2 - k)
        sum_result += term
    end
    
    # 最終結果
    return coefficient * sum_result
end

# 測試函數
j1, j2, J = 1, 1, 2  # 替換為實際值
m1, m2, M = 0, 0, 0  # 替換為實際值

result = calculate_expression(j1, j2, J, m1, m2, M) - ((-1)^((J / 2) - m1)/sqrt(J+1))
println("Result: $result")