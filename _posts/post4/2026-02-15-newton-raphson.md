---
layout: post
title: "Newton-Raphson Method: Finding Roots with Tangents"
description: "Learn how the Newton-Raphson method uses tangent lines to quickly find function roots. Step-by-step derivation, formula explanation , and practical example for calculating square roots."
category: explore
order: 4
thumbnail: /images/posts/post4/image1.png
images:
  - /images/posts/post4/image1.png
  - /images/posts/post4/image2.gif
  - /images/posts/post4/image3.png
resources:
  - name: "Newton's method - Wikipedia"
    link: "https://en.wikipedia.org/wiki/Newton%27s_method"
references:
  - name: "Newton's method - Wikipedia"
    link: "https://en.wikipedia.org/wiki/Newton%27s_method"
  - name: "Newton's Method - Wolfram MathWorld"
    link: "https://mathworld.wolfram.com/NewtonsMethod.html"
  - name: "Newton-Raphson Method - Brilliant.org"
    link: "https://brilliant.org/wiki/newton-raphson-method/"
---

Have you ever needed to find the exact point where a function crosses the x-axis? These points are called "roots," and they're incredibly important in various fields, from engineering to economics. While some functions have easily solvable roots, many don't. That's where numerical methods come in, and one of the most powerful and widely used is the Newton-Raphson method.


## What is the Newton-Raphson Method?

At its core, the Newton-Raphson method is an iterative technique for finding successively better approximations to the roots (or zeroes) of a real-valued function. It leverages the idea of a tangent line to quickly home in on the root. Imagine you have a curve and you want to find where it hits the ground (the x-axis). The Newton-Raphson method essentially involves:

1. **Making an initial guess.**
2. **Drawing a tangent line at that guess.**
3. **Finding where that tangent line crosses the x-axis.** This intersection point becomes your *new, improved guess*.
4. **Repeating the process** until your guesses get extremely close to the actual root.

This iterative process creates a sequence of approximations that typically converges very rapidly to the root.

## Derivation of the Formula

Now, let's get into the mathematics behind it. Consider a function $f(x)$ and we want to find its root, i.e., $x$ such that $f(x) = 0$. Let's make an initial guess $x_n$. We want to find a better approximation, $x_{n+1}$.

The equation of the tangent line to the curve $y = f(x)$ at the point $(x_n, f(x_n))$ is given by:

$$y - f(x_n) = f'(x_n)(x - x_n)$$

where $f'(x_n)$ is the derivative of $f(x)$ evaluated at $x_n$. We want to find where this tangent line intersects the x-axis. At the x-axis, $y = 0$. So, we substitute $y=0$ and let $x = x_{n+1}$ (our next approximation):

$$-f(x_n) = f'(x_n)(x_{n+1} - x_n)$$

Rearranging the terms to solve for $x_{n+1}$ gives us the famous **Newton-Raphson formula**:

$$\Large x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

## Example: Finding the Square Root of a Number

Let's say we want to find the square root of 2. This is equivalent to finding the root of the function $f(x) = x^2 - 2$.

1. $f(x) = x^2 - 2$
2. $f'(x) = 2x$
3. Let's choose an initial guess $x_0 = 1.5$.

Now, let's iterate:

* **Iteration 1:**
  $$x_1 = 1.5 - \frac{(1.5)^2 - 2}{2(1.5)} = 1.5 - \frac{2.25 - 2}{3} = 1.5 - \frac{0.25}{3} \approx 1.4167$$

* **Iteration 2:**
  $$x_2 = 1.4167 - \frac{(1.4167)^2 - 2}{2(1.4167)} = 1.4167 - \frac{2.0070 - 2}{2.8334} \approx 1.4142$$

Notice how quickly we approached the actual value of $\sqrt{2} \approx 1.41421356$.

## Advantages and Limitations

### Advantages:
* **Rapid Convergence:** When it converges, it does so very quickly, often quadratically (meaning the number of accurate decimal places roughly doubles with each iteration).
* **Versatility:** Can be applied to a wide range of differentiable functions.

### Limitations:
* **Requires Derivative:** You need to be able to calculate the derivative of the function.
* **Initial Guess Sensitivity:** A poor initial guess can lead to slow convergence, divergence, or convergence to a different root.
* **Division by Zero:** If $f'(x_n) = 0$ at any point during the iteration, the method breaks down.