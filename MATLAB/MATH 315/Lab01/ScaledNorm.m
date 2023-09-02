function p = ScaledNorm(a, b)
    c = max(abs(a), abs(b));
    a = a / c;
    b = b / c;
    p = c * sqrt(a^2 + b^2);
end