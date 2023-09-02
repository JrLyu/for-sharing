function p = MorelMorrison(a, b, N)
    p = max(abs(a), abs(b));
    q = min(abs(a), abs(b));
    for i = 1:N
        r = (q / p)^2;
        s = r / (4 + r);
        p = p + 2 * s * p;
        q = s * q;
    end
end