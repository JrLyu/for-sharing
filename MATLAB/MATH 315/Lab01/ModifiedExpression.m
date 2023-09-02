function f = ModifiedExpression(x)
    syms t;
    T = taylor(sin(t), t);
    f = (x - subs(T, t, x)) / x^3;
end