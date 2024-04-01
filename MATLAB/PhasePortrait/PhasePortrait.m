%% Plot the Phase Portrait
clear; clc;

f = @(t, Y) [5*Y(1)+0*Y(2); 5*Y(1)+5*Y(2)];

y1 = linspace(-10,10,20);
y2 = linspace(-10,10,20);

% creates two matrices one for all the x-values on the grid, and one for
% all the y-values on the grid. Note that x and y are matrices of the same
% size and shape, in this case 20 rows and 20 columns
[x,y] = meshgrid(y1,y2);
u = zeros(size(x));
v = zeros(size(x));

% we can use a single loop over each element to compute the derivatives at
% each point (y1, y2)
t=0; % we want the derivatives at each point at t=0, i.e. the starting time
for i = 1:numel(x)
    Yprime = f(t,[x(i); y(i)]);
    u(i) = Yprime(1);
    v(i) = Yprime(2);
end

for i = 1:numel(x)
    Vmod = sqrt(u(i)^2 + v(i)^2);
    u(i) = u(i)/Vmod;
    v(i) = v(i)/Vmod;
end

quiver(x,y,u,v,'r'); figure(gcf)
xlabel('y_1')
ylabel('y_2')
axis tight equal;

%% 
hold on
for y10 = [95]
    [ts,ys] = ode45(f,[0,50],[0;y10]);
    plot(ys(:,1),ys(:,2))
    plot(ys(1,1),ys(1,2),'bo') % starting point
    plot(ys(end,1),ys(end,2),'ks') % ending point
end
for y20 = [5]
    [ts,ys] = ode45(f,[0,50],[0;y20]);
    plot(ys(:,1),ys(:,2))
    plot(ys(1,1),ys(1,2),'bo') % starting point
    plot(ys(end,1),ys(end,2),'ks') % ending point
end

