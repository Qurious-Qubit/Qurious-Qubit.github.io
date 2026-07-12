---
layout: post
title: "Tracking the Peaks: Understanding Gamma, Frequency, and Wave Speed"
description: "What exactly is the propagation constant? Discover how the mathematical relationship between space and time dictates the speed of waves in our universe."
category: explore
order: 14
slug: "14"
thumbnail: /images/posts/post14/image1.gif
images:
  - /images/posts/post14/image1.gif
  - /images/posts/post14/image2.gif
resources:
  - name: "Superposition of sine waves"
    link: "https://www.andrew.cmu.edu/user/cmorning/waves/waves11.html"
  - name: "Optics basics: What is a wave? Part IV: Important quantities | Skulls in the Stars"
    link: "https://skullsinthestars.com/2007/12/12/optics-basics-what-is-a-wave-part-iv-important-quantities/"
---

## What Exactly is Gamma ($\gamma$)?

When we solve the fundamental wave equation, we always end up with a solution that looks something like this:

$$f(x, t) = A e^{j\omega t - \gamma x}$$

We know that $\omega$ is the **angular frequency**. It tells us how fast the wave oscillates in *time* (like a pendulum swinging back and forth). 

But what is $\gamma$? Gamma is the **propagation constant**, and it tells us how the wave behaves in *space*. 

In most physical systems, $\gamma$ is actually a complex number: $\gamma = \alpha + j\beta$. 
* The real part ($\alpha$) dictates how much the wave fades or decays as it travels. 
* The imaginary part ($\beta$), known as the **phase constant**, dictates how the wave oscillates in space (the actual wavelength). 

To keep things simple and focus on movement, let's assume our wave doesn't lose any energy ($\alpha = 0$). Our wave equation simplifies to:

$$f(x, t) = A e^{j(\omega t - \beta x)}$$

---

## Tracking the Peak: Finding the Speed

Imagine you are standing on a beach watching a water wave roll in. If you lock your eyes onto one single crest (peak) of the wave and follow it as it moves, how fast are your eyes moving?

Mathematically, the peak of a wave occurs when the phase (the part inside the exponent) is a constant value. Let's set it to zero for simplicity:

$$\omega t - \beta x = 0$$

If we want to find the speed of this peak, we just solve for distance over time ($v = \frac{x}{t}$):

$$\beta x = \omega t$$

$$v = \frac{x}{t} = \frac{\omega}{\beta}$$

This is an incredibly profound realization! The speed at which a wave travels through the universe is simply the ratio of its time-oscillation ($\omega$) to its space-oscillation ($\beta$).

---

## The Linear vs. Non-Linear World

Here is where physics gets really interesting. What happens if you send multiple waves of different frequencies down a medium at the same time?

### Case 1: The Linear Relationship
Imagine a scenario where $\beta$ is a perfect, direct multiple of $\omega$ (for example, $\beta = 2\omega$). 

If you calculate the speed ($v = \frac{\omega}{\beta}$), the $\omega$ terms perfectly cancel out, leaving $v = \frac{1}{2}$. 
This means that **no matter what the frequency is, the speed is exactly the same**. All waves travel together in perfect harmony. We call this a non-dispersive medium. (A vacuum is a perfect example: all colors of light travel at the exact same speed, $c$).

### Case 2: The Non-Linear Relationship
What if $\beta$ is a complex function of $\omega$ (like $\beta = \omega^2$)? 
Now, if you calculate the speed, $v = \frac{\omega}{\omega^2} = \frac{1}{\omega}$. 

The $\omega$ doesn't cancel out! This means **different frequencies travel at completely different speeds**. High frequencies might travel slower, and low frequencies might travel faster. As the waves travel, they stretch apart, smear out, and completely change their shape. This is called **Dispersion**. (This is exactly how a glass prism splits white light into a rainbow!)

---

## Interactive Visualization

To really understand this, let's look at it visually. In the interactive simulation below, you can control the Frequency ($\omega$) and the Spatial Constant ($\beta$) for two different waves. 

Try clicking **"Force Linear Relation"**. You will see that even though the waves have different frequencies, they travel at the exact same speed. Because they travel together, their Sum (the green wave at the bottom) maintains a perfectly stable shape as it moves.

Now, manually change $\beta_2$ so it is no longer proportional. Watch how the blue wave outpaces the red wave, and look closely at the green wave at the bottom—the shape of the wave is constantly warping and shifting!

{% include posts/Post14/wave-dispersion.html %}

Notice that green wave at the bottom? It creates packets, or "envelopes" of energy. When dealing with complex signals, we don't just care about the speed of a single peak; we care about the speed of that entire packet! 

In our next post, we will dive deep into these two different speeds: The **Phase Velocity** (the speed of the individual peaks) and the **Group Velocity** (the speed of the information packet itself).