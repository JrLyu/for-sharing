function p = VectorizedScaledNorm(x)
    c = max(x);
    x = x ./ c;
    p = c * sqrt(x(1)^2 + x(2)^2);
end