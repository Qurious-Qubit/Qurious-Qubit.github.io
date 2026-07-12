---
layout: post
title: "The Universal Wave Solution: Solving the Second-Order Differential Equation"
description: "Why do we always assume exponential solutions for waves? A simple mathematical derivation showing how nature's fundamental equations are solved."
category: explore
order: 13
slug: "13"
thumbnail: /images/posts/post13/image1.jpg
images:
  - /images/posts/post13/image1.jpg
  - /images/posts/post13/image2.jpg
references:
  - name: "Solving the damped wave equation on a semi-infinite string"
    link: "https://www.youtube.com/watch?v=LN6muWDBCVA"
resources:
  - name: "Wave equation: general solution via Fourier transform"
    link: "https://www.youtube.com/watch?v=oTnJZy81x2o"
  - name: "Solving the damped wave equation on a semi-infinite string"
    link: "https://www.youtube.com/watch?v=LN6muWDBCVA"
---

Whether we are looking at the voltage across a transmission line, the electric field of an electromagnetic wave, or even the quantum state of a particle, we repeatedly stumble upon the exact same mathematical problem. 

We keep ending up with a second-order differential equation for a wave that travels in space ($x$ or $z$) and oscillates in time ($t$). Mathematically, it looks something like this:

$$\frac{\partial^2 f(x,t)}{\partial x^2} = \gamma^2 f(x,t)$$

This equation simply says: "Find a function $f(x,t)$ whose double spatial derivative is equal to itself, multiplied by some constant squared ($\gamma^2$)." 

Since this pops up everywhere in engineering and physics, let us solve it generically once and for all using a beautiful technique called **Separation of Variables**.

## Splitting Space and Time

Trying to solve for space and time simultaneously is a headache. But what if we assume that the spatial behavior of the wave is completely independent of its time behavior? 

We can split our function $f(x,t)$ into two separate functions multiplied together: one strictly for space $X(x)$, and one strictly for time $T(t)$.

$$f(x,t) = X(x) \cdot T(t)$$

Since we are dealing with AC circuits and continuous waves, we already know how the wave behaves in time. It oscillates sinusoidally! Using Euler's formula, we can represent this time oscillation simply as $T(t) = e^{j\omega t}$. 

So, our function becomes:

$$f(x,t) = X(x) e^{j\omega t}$$

Now, let's plug this back into our original differential equation:

$$\frac{\partial^2}{\partial x^2} \left[ X(x) e^{j\omega t} \right] = \gamma^2 \left[ X(x) e^{j\omega t} \right]$$

Because we are taking a partial derivative with respect to space ($x$), the time component ($e^{j\omega t}$) is treated as a constant and completely ignores the derivative. We can factor it out on both sides:

$$e^{j\omega t} \frac{d^2 X(x)}{dx^2} = \gamma^2 X(x) e^{j\omega t}$$

The $e^{j\omega t}$ terms cancel out beautifully! We have successfully eliminated time from our problem, leaving us with a simple, ordinary differential equation purely in space:

$$\frac{d^2 X(x)}{dx^2} = \gamma^2 X(x)$$

## The Magic of the Exponential Guess

Now we need to solve for $X(x)$. In mathematics, when we face linear differential equations, we don't usually solve them by brute force. Instead, we make a highly educated guess (an *ansatz*) and see if it fits. 

What function do we know that basically remains unchanged when we take its derivative? As we know from the beautiful properties of Taylor series (which we covered deeply in our post: [The Function That Is Its Own Derivative](/blog/post-12/)), the exponential function $e^x$ is its own derivative. 

So, let's guess that our spatial solution looks like this:

$$X(x) = e^{\gamma x}$$

Let us verify if this guess is correct by taking the derivatives.

The first derivative with respect to $x$ is:

$$\frac{d X(x)}{dx} = \gamma e^{\gamma x}$$

Now, let's take the second derivative:

$$\frac{d^2 X(x)}{dx^2} = \gamma \cdot \gamma e^{\gamma x} = \gamma^2 e^{\gamma x}$$

If we look closely, $e^{\gamma x}$ is exactly our original guessed function $X(x)$. So we can substitute it back:

$$\frac{d^2 X(x)}{dx^2} = \gamma^2 X(x)$$

Perfect! It matches our spatial equation exactly. But wait, is there another solution?

What if we guessed $X(x) = e^{-\gamma x}$? 
The first derivative gives a negative sign: $-\gamma e^{-\gamma x}$. 
But when we take the second derivative, the negative sign multiplies by itself and becomes positive again! So, $e^{-\gamma x}$ is also a perfectly valid solution.

## The Complete Generalized Solution

Because our differential equation is linear, the Principle of Superposition applies. This means that if we have two valid solutions, any combination of them added together is also a valid solution.

Therefore, the most general mathematical solution for the spatial part is:

$$X(x) = A e^{-\gamma x} + B e^{+\gamma x}$$

Here, $A$ and $B$ are just unknown constants (amplitudes) that will be decided by our boundary conditions (like the voltage at the source or the load impedance).

## The Final Physical Interpretation

To get the complete picture of our wave in both space and time, we simply multiply our time solution ($e^{j\omega t}$) back into our spatial solution:

$$f(x, t) = \left( A e^{-\gamma x} + B e^{+\gamma x} \right) e^{j\omega t}$$

If we expand this out:

$$f(x, t) = A e^{j\omega t - \gamma x} + B e^{j\omega t + \gamma x}$$

Even though we just did pure mathematics, these two terms describe the physical reality of how energy moves through the universe:

* **The Forward Wave ($A e^{j\omega t - \gamma x}$):** The negative sign on the spatial exponent means that as the distance $x$ increases, the wave experiences a phase delay (and possibly attenuation). This represents the signal traveling forward away from the source.
* **The Backward Wave ($B e^{j\omega t + \gamma x}$):** The positive sign means the wave is traveling in the opposite direction, from $+x$ back towards $0$. In engineering, we call this the **reflected wave**.

So, whenever you see a second-order spatial derivative in a textbook, you don't need to panic or re-derive it. You can confidently jump straight to the exponential solution, knowing that the math perfectly models exactly what the physical wave is doing!