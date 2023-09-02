%% Question 1
clear all

%% Part (a)

OriginalExpression = @(x) (x - sin(x)) / x^3;

OriginalExpression(0) % NaN

%% Part (b)
% Source of error: the sin function; the division
% To avoid the source of error: 

% Written in ModifiedExpression
ModifiedExpression(0) % NaN

%% Part (c)

x = logspace(-1, -10, 100);
original = [];
modified = [];

for i = 1:100
    value = x(i);
    original = [original OriginalExpression(value)];
    modified = [modified ModifiedExpression(value)];
end

%% Part (d)
tiledlayout(2,1)

nexttile
plot(x, original, "ro-")
hold on
plot(x, modified, "b*-")
title("Plotting Original and Modified Expression using plot")
legend("Origianl Expression", "Modified Expression")
xlabel("x")
ylabel("f")

% modifed graph
nexttile
semilogx(x, original, "ro-")
hold on
semilogx(x, modified, "b*-")
title("Plotting Original and Modified Expression using smilogx")
legend("Origianl Expression", "Modified Expression")
xlabel("x")
ylabel("f")

% The semilogx function scales the axes to logarithmical spaces. 
% So it is more helpful for us to visualize our data since
% our data is logarithmical spaced. 

%% Part (e)
x = logspace(-1, -10, 100);
original = [];

tic
for i = 1:100
    value = x(i);
    original = [original OriginalExpression(value)];
end
toc

VectorizedOriginalExpression = @(x) (x - sin(x)) / x.^3;

tic
VectorizedOriginalExpression(x);
toc