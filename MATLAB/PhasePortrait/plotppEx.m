%% Use plotpp

odefun = @(t, x) [0.005*x(2)*x(1)-0.2*x(1); -0.005*x(1)*x(2)];
plotpp(odefun, 'xlim',[0, 100], 'ylim', [0, 100], tspan=100);