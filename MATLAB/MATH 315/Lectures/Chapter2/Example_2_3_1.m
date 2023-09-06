%% Example 2.3.1
% In this example, we will see the errors introduced by arithematical
% operations

%% Defining the Functions
p_1 = @(x) (1-x).^10;
p_2 = @(x) x.^10-10*x.^9+45*x.^8-120*x.^7+210*x.^6-252*x.^5+210*x.^4-120*x.^3+45*x.^2-10*x+1;

%% Ploting the Functions
x = linspace(0, 2, 100);

plot(x, p_1(x))
hold on
plot(x, p_2(x))
legend("Factor", "Expanded")
saveas(gcf, "Ex2_3_1_Ploting_Functions.png")

% It seems that the two functions are the same.
%% Zooming In
y = linspace(0.99, 1.01, 100);

hold off
plot(y, p_1(y))
hold on
plot(y, p_2(y))
legend("Factor", "Expanded")
saveas(gcf, "Ex2_3_1_Zooming_In.png")

% Now the expanded version introduces more error than the factored
% version. 