%% Question 2

clear all

%% Part(a)

OriginalNorm = @(a, b) sqrt(a^2 + b^2);

OriginalNorm(3, 4)

%% Part (b)

% Written in the file ScaledNorm.
ScaledNorm(3, 4)

%% Part (c)

% Written in the file MorelMorrison

MorelMorrison(3, 4, 10)

%% Part (d)

a = realmax;
b = realmax;

OriginalNorm(a, b) % Inf
ScaledNorm(a,b) % Inf

%% Part (e)

x = [3 4];

tic
ScaledNorm(3, 4)
toc

tic
VectorizedScaledNorm(x)
toc