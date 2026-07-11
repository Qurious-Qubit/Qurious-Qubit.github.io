---
layout: post
title: "The Universal Wave Solution: Solving the Second-Order Differential Equation"
description: "Why do we always assume exponential solutions for waves? A simple mathematical derivation showing how nature's fundamental equations are solved."
category: explore
order: 13
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

We keep ending up with a second-order differential equation that looks something like this:

$$\frac{d^2 f(x)}{dx^2} = \gamma^2 f(x)$$

This equation simply says: "Find a function $f(x)$ whose double derivative is equal to itself, multiplied by some constant squared ($\gamma^2$)." 

Since this pops up everywhere in engineering and physics, let us solve it generically once and for all.

## The Magic of the Exponential Guess

In mathematics, when we face linear differential equations, we don't usually solve them by brute force. Instead, we make a highly educated guess (an *ansatz*) and see if it fits. 

What function do we know that basically remains unchanged when we take its derivative? As we know from the beautiful properties of Taylor series, the exponential function $e^x$ is its own derivative. 

So, let's guess that our solution looks like this:

$$f(x) = e^{\gamma x}$$

Let us verify if this guess is correct by taking the derivatives.

The first derivative with respect to $x$ is:

$$\frac{d f(x)}{dx} = \gamma e^{\gamma x}$$

Now, let's take the second derivative:

$$\frac{d^2 f(x)}{dx^2} = \gamma \cdot \gamma e^{\gamma x} = \gamma^2 e^{\gamma x}$$

If we look closely, $e^{\gamma x}$ is exactly our original function $f(x)$. So we can substitute it back:

$$\frac{d^2 f(x)}{dx^2} = \gamma^2 f(x)$$

Perfect! It matches our original equation exactly. But wait, is there another solution?

What if we guessed $f(x) = e^{-\gamma x}$? 
The first derivative gives a negative sign: $-\gamma e^{-\gamma x}$. 
But when we take the second derivative, the negative sign multiplies by itself and becomes positive again! So, $e^{-\gamma x}$ is also a perfectly valid solution.

## The Complete Generalized Solution

Because our differential equation is linear, the Principle of Superposition applies. This means that if we have two valid solutions, any combination of them added together is also a valid solution.

Therefore, the most general mathematical solution is:

$$f(x) = A e^{-\gamma x} + B e^{+\gamma x}$$

Here, $A$ and $B$ are just unknown constants (amplitudes) that will be decided by our boundary conditions (like the voltage at the source or the load impedance).

## Adding the Time Domain (The Phasor Connection)

So far, we have only solved for space ($x$). But waves don't just exist in space; they oscillate in time. 

In AC circuits and microwave engineering, we assume our sources are oscillating sinusoidally at a specific angular frequency ($\omega$). Using Euler's formula, we represent this time oscillation as $e^{j\omega t}$. 

To get the complete picture of our wave in both space and time, we simply multiply our spatial solution by this time variation:

$$f(x, t) = \left( A e^{-\gamma x} + B e^{+\gamma x} \right) e^{j\omega t}$$

If we expand this out:

$$f(x, t) = A e^{-\gamma x} e^{j\omega t} + B e^{+\gamma x} e^{j\omega t}$$

## The Physical Interpretation

Even though we just did pure mathematics, these two terms describe the physical reality of how energy moves through the universe:

* **The Forward Wave ($A e^{-\gamma x}$):** The negative sign in the exponent means that as the distance $x$ increases, the wave experiences a phase delay (and possibly attenuation). This represents the signal traveling forward away from the source.
* **The Backward Wave ($B e^{+\gamma x}$):** The positive sign means the wave is traveling in the opposite direction, from $+x$ back towards $0$. In engineering, we call this the **reflected wave**.

So, whenever you see a second-order spatial derivative in a textbook, you don't need to panic or re-derive it. You can confidently jump straight to $A e^{-\gamma x} + B e^{+\gamma x}$, knowing that the math perfectly models exactly what the wave is physically doing!