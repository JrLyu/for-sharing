# Supervised Machine Learning

# Linear Regression Model

Basic notations: 

- $x$ is the input variable, or **feature**.
- $y$ is the output variable, or **target**.
- $m$ is the number of training examples.
- $(x,y)$ is a single training example.
- $(x^{(i)},y^{(i)})$ is the i-th training example.
    - Note: the “i” here is an index, rather than exponent.
- $\hat{y}$ is the prediction, or the estimated $y$.
- $f$ is the model, or hypothesis.

## Representing the Model

Linear regression with one variable, univariate linear regression: 

$$
f_{w,b}(x)=wx+b
$$

$w$ and $b$ are parameters/coefficients/weights

## Cost Function

![Screen Shot 2022-07-18 at 5.31.56 PM.png](Supervised%20Machine%20Learning%202cbac7f066be468ebded12a94c06491f/Screen_Shot_2022-07-18_at_5.31.56_PM.png)

The Error: 

$$
\hat{y}^{(i)}=f_{w,b}\left(x^{(i)}\right)
$$

$$
f_{w,b}\left(x^{(i)}\right)=wx^{(i)}+b
$$

$$
\text{Error}=\hat{y}^{(i)}-y^{(i)}
$$

The Squared error cost function (***J***): 

$$
\begin{aligned} J(w,b)&=\frac{1}{2m}\sum_{i=1}^m\left(\hat{y}^{(i)}-y^{(i)}\right)^2\\&=\frac{1}{2m}\sum_{i=1}^m\left(f_{w,b}\left(x^{(i)}\right)-y^{(i)}\right)^2\end{aligned}
$$

The job is the find $w$ and $b$ such that $\hat{y}^{(i)}$ is close to $y^{(i)}$ for all $(x^{(i)},y^{(i)})$, i.e., 

$$
\text{minimize}_{w,b}J(w,b)
$$

## Visualizing the Cost Function

In linear regression, the cost function is always a bowl-shaped function: 

![Screen Shot 2022-07-18 at 5.41.38 PM.png](Supervised%20Machine%20Learning%202cbac7f066be468ebded12a94c06491f/Screen_Shot_2022-07-18_at_5.41.38_PM.png)

At the bottom of the “bowl”, the cost function is minimized. 

## Gradient Descent

The outlined procedure of gradient descent is: 

- Start with some $w$ and $b$
- Keep changing $w$ and $b$ to reduce $J(w,b)$
- Until we settle at or near a minimum.

*Refer to the concept of Gradient $\nabla f$.

### Formula

Gradient descent algorithm - Repeat until convergence: 

$$
w=w-\alpha\frac{\partial}{\partial w}J(w,b)\\b=b-\alpha\frac{\partial}{\partial b}J(w,b)
$$

α is the learning rate. 

Key: Simultaneously update $w$ and $b$.

![Screen Shot 2022-07-18 at 5.50.08 PM.png](Supervised%20Machine%20Learning%202cbac7f066be468ebded12a94c06491f/Screen_Shot_2022-07-18_at_5.50.08_PM.png)

### The Learning Rate

The learning rate cannot be too big or too small: 

![Screen Shot 2022-07-18 at 5.50.48 PM.png](Supervised%20Machine%20Learning%202cbac7f066be468ebded12a94c06491f/Screen_Shot_2022-07-18_at_5.50.48_PM.png)

### More on the Formula

Recall:

- $f_{w,b}(x)=wx+b$
- $J(w,b)=\frac{1}{2m}\sum_{i=1}^m\left(f_{w,b}\left(x^{(i)}\right)-y^{(i)}\right)^2$.

Hence, 

$$
\begin{aligned}\frac{\partial}{\partial w}J(w,b)&=\frac{\partial}{\partial w}\frac{1}{2m}\sum_{i=1}^m\left(f_{w,b}(x^{(i)})-y^{(i)}\right)^2\\&=\frac{\partial}{\partial w}\frac{1}{2m}\sum_{i=1}^m\left(wx^{(i)}+b-y^{(i)}\right)^2\\&=\frac{1}{2m}\sum_{i=1}^m\left(wx^{(i)}+b-y^{(i)}\right)2x^{(i)}\\&=\frac{1}{m}\sum_{i=1}^m\left(f_{w,b}(x^{(i)})-y^{(i)}\right)x^{(i)}\end{aligned}
$$

$$
\begin{aligned}\frac{\partial}{\partial b}J(w,b)&=\frac{\partial}{\partial b}\frac{1}{2m}\sum_{i=1}^m\left(f_{w,b}(x^{(i)})-y^{(i)}\right)^2\\&=\frac{\partial}{\partial b}\frac{1}{2m}\sum_{i=1}^m\left(wx^{(i)}+b-y^{(i)}\right)^2\\&=\frac{1}{2m}\sum_{i=1}^m\left(wx^{(i)}+b-y^{(i)}\right)2\\&=\frac{1}{m}\sum_{i=1}^m\left(f_{w,b}(x^{(i)})-y^{(i)}\right)\end{aligned}
$$

Therefore, the gradient descent algorithm becomes: 

$$
\text{repeat until convergence: }\\w=w-\alpha\frac{1}{m}\sum_{i=1}^m\left(f_{w,b}(x^{(i)})-y^{(i)}\right)x^{(i)}\\b=b-\alpha\frac{1}{m}\sum_{i=1}^m\left(f_{w,b}(x^{(i)})-y^{(i)}\right)\\\text{Update }w\text{ and }b\text{ simultaneously.}
$$

### Gradient Descent in Action

![Screen Shot 2022-07-18 at 6.01.02 PM.png](Supervised%20Machine%20Learning%202cbac7f066be468ebded12a94c06491f/Screen_Shot_2022-07-18_at_6.01.02_PM.png)

Note: Sometimes, we might encounter cost functions with more than one local minima, indicated by the diagram above. However, in linear regression, we always have a cost function with one and only one local minimum, and that minima is called the global minimum.