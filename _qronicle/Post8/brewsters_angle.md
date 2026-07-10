---
layout: post
title: "The Magic Angle: Deriving Brewster's Angle for Zero Reflection"
description: "Is it possible to transmit a signal with absolutely zero reflection? Let's do the math and derive the exact conditions for perfect transmission."
order: 8
images:
  - /images/qronicle/post8/image1.webp
topic: [Theory, EM-Theory, L1-Foundational, Derivation]
---

## Can We Have Zero Reflection?

In our previous post, we derived the Fresnel equations for a wave hitting a boundary at an angle (oblique incidence). We saw that whenever a wave moves from one medium to another, some of the energy bounces back. In the world of quantum control and microwave engineering, reflections are our biggest enemy because they distort our carefully crafted control pulses.

So, here is a million-dollar question: **Is there a specific angle where the reflection becomes exactly zero?** Let's not just guess. Let's do the math and see for ourselves. To find this "magic angle" (known in physics as Brewster's Angle), all we have to do is take our reflection coefficients ($\Gamma$) from the last post and set them to exactly zero.

---

## The Generalized TE Case (Perpendicular Polarization)

For a Transverse Electric (TE) wave, our reflection coefficient formula was:

$$\Gamma_{TE} = \frac{\eta_2 \cos(\theta_i) - \eta_1 \cos(\theta_t)}{\eta_2 \cos(\theta_i) + \eta_1 \cos(\theta_t)}$$

For reflection to be zero, the numerator must be zero. So, we set:

$$\eta_2 \cos(\theta_i) = \eta_1 \cos(\theta_t)$$

Let's square both sides to make it easier to work with our trigonometric identities:

$$\eta_2^2 \cos^2(\theta_i) = \eta_1^2 \cos^2(\theta_t)$$

We know two fundamental things from basic electromagnetics:
1. Intrinsic impedance squared is $\eta^2 = \frac{\mu}{\epsilon}$.
2. From Snell's Law ($k_1 \sin(\theta_i) = k_2 \sin(\theta_t)$), we can square it to get $\mu_1 \epsilon_1 \sin^2(\theta_i) = \mu_2 \epsilon_2 \sin^2(\theta_t)$. Which means $\sin^2(\theta_t) = \frac{\mu_1 \epsilon_1}{\mu_2 \epsilon_2} \sin^2(\theta_i)$.

Now, let's substitute $\eta^2$ and replace $\cos^2(\theta)$ with $(1 - \sin^2(\theta))$ in our main equation:

$$\frac{\mu_2}{\epsilon_2} (1 - \sin^2(\theta_i)) = \frac{\mu_1}{\epsilon_1} (1 - \sin^2(\theta_t))$$

Now, plug in that Snell's Law substitution for $\sin^2(\theta_t)$:

$$\frac{\mu_2}{\epsilon_2} - \frac{\mu_2}{\epsilon_2} \sin^2(\theta_i) = \frac{\mu_1}{\epsilon_1} - \frac{\mu_1}{\epsilon_1} \left( \frac{\mu_1 \epsilon_1}{\mu_2 \epsilon_2} \right) \sin^2(\theta_i)$$

Notice that the $\epsilon_1$ terms on the right side cancel out beautifully:

$$\frac{\mu_2}{\epsilon_2} - \frac{\mu_2}{\epsilon_2} \sin^2(\theta_i) = \frac{\mu_1}{\epsilon_1} - \frac{\mu_1^2}{\mu_2 \epsilon_2} \sin^2(\theta_i)$$

Now, just group the $\sin^2(\theta_i)$ terms on one side:

$$\left( \frac{\mu_1^2}{\mu_2 \epsilon_2} - \frac{\mu_2}{\epsilon_2} \right) \sin^2(\theta_i) = \frac{\mu_1}{\epsilon_1} - \frac{\mu_2}{\epsilon_2}$$

Multiply everything by $\epsilon_2$ and solve for $\sin^2(\theta_i)$. After a bit of basic algebra, you get the **Generalized Brewster's Angle for TE**:

$$\sin^2(\theta_{B,TE}) = \frac{\mu_2 (\mu_1 \epsilon_2 - \mu_2 \epsilon_1)}{\epsilon_1 (\mu_1^2 - \mu_2^2)}$$

---

## The Generalized TM Case (Parallel Polarization)

Now let's do the exact same process for the Transverse Magnetic (TM) wave. Our formula was:

$$\Gamma_{TM} = \frac{\eta_2 \cos(\theta_t) - \eta_1 \cos(\theta_i)}{\eta_2 \cos(\theta_t) + \eta_1 \cos(\theta_i)}$$

Set the numerator to zero:

$$\eta_2 \cos(\theta_t) = \eta_1 \cos(\theta_i)$$

Square both sides and replace the terms just like we did before:

$$\frac{\mu_2}{\epsilon_2} (1 - \sin^2(\theta_t)) = \frac{\mu_1}{\epsilon_1} (1 - \sin^2(\theta_i))$$

Substitute Snell's law for $\sin^2(\theta_t)$:

$$\frac{\mu_2}{\epsilon_2} \left( 1 - \frac{\mu_1 \epsilon_1}{\mu_2 \epsilon_2} \sin^2(\theta_i) \right) = \frac{\mu_1}{\epsilon_1} - \frac{\mu_1}{\epsilon_1} \sin^2(\theta_i)$$

$$\frac{\mu_2}{\epsilon_2} - \frac{\mu_1 \epsilon_1}{\epsilon_2^2} \sin^2(\theta_i) = \frac{\mu_1}{\epsilon_1} - \frac{\mu_1}{\epsilon_1} \sin^2(\theta_i)$$

Group the $\sin^2(\theta_i)$ terms together and solve. You will arrive at the **Generalized Brewster's Angle for TM**:

$$\sin^2(\theta_{B,TM}) = \frac{\epsilon_2 (\mu_1 \epsilon_2 - \mu_2 \epsilon_1)}{\mu_1 (\epsilon_2^2 - \epsilon_1^2)}$$

---

## The Practical Reality: What Happens When $\mu_1 = \mu_2$?

Okay, we have our two heavy generalized equations. But let's talk practically as engineers. 

Whether we are sending signals through air, routing them along Teflon cables, or shooting them into the silicon or sapphire substrate of a quantum chip, almost all the materials we work with are **non-magnetic**. 

This means their permeability is basically just the permeability of free space ($\mu_1 = \mu_2 = \mu_0$). 

Let's see what happens to our math when we apply this real-world condition ($\mu_1 = \mu_2 = \mu$).

### The Impact on TE (Perpendicular)
Let's look at the denominator of our TE formula: $\epsilon_1 (\mu^2 - \mu^2)$. 

Wait a minute, $\mu^2 - \mu^2 = 0$! Since we cannot divide by zero, the only way this equation can mathematically exist is if the numerator is *also* zero. For the numerator to be zero, $\mu \epsilon_2 - \mu \epsilon_1$ must equal 0, which means $\epsilon_1 = \epsilon_2$. 

But if $\mu_1 = \mu_2$ and $\epsilon_1 = \epsilon_2$, then Medium 1 and Medium 2 are exactly the same material! There is no boundary at all. 

**The Conclusion:** For standard non-magnetic materials, there is absolutely no angle where a TE wave will have zero reflection. It simply does not exist.

### The Impact on TM (Parallel)
Now let's apply $\mu_1 = \mu_2 = \mu$ to our TM formula:

$$\sin^2(\theta_{B,TM}) = \frac{\epsilon_2 (\mu \epsilon_2 - \mu \epsilon_1)}{\mu (\epsilon_2^2 - \epsilon_1^2)}$$

We can pull the $\mu$ out of the numerator and cancel it with the $\mu$ in the denominator:

$$\sin^2(\theta_{B,TM}) = \frac{\epsilon_2 (\epsilon_2 - \epsilon_1)}{(\epsilon_2^2 - \epsilon_1^2)}$$

Now, remember your high school algebra! $a^2 - b^2 = (a-b)(a+b)$. We can expand the denominator:

$$\sin^2(\theta_{B,TM}) = \frac{\epsilon_2 (\epsilon_2 - \epsilon_1)}{(\epsilon_2 - \epsilon_1)(\epsilon_2 + \epsilon_1)}$$

The $(\epsilon_2 - \epsilon_1)$ terms perfectly cancel out, leaving us with a beautiful, simple equation:

$$\sin^2(\theta_{B,TM}) = \frac{\epsilon_2}{\epsilon_1 + \epsilon_2}$$

In trigonometry, $\sin^2(\theta) = \frac{\tan^2(\theta)}{1 + \tan^2(\theta)}$. If you look closely at our fraction, we can divide the top and bottom by $\epsilon_1$ to match this format:

$$\sin^2(\theta_{B,TM}) = \frac{\epsilon_2 / \epsilon_1}{1 + (\epsilon_2 / \epsilon_1)}$$

By comparing the two, it is clear that $\tan^2(\theta_{B,TM}) = \frac{\epsilon_2}{\epsilon_1}$. Taking the square root gives us the final, classic Brewster's Angle formula:

$$\tan(\theta_{B,TM}) = \sqrt{\frac{\epsilon_2}{\epsilon_1}} = \frac{n_2}{n_1}$$

**The Conclusion:** For a TM polarized wave traveling between standard non-magnetic materials, if you hit the boundary at exactly this angle, 100% of your signal will transmit. Zero reflection. 

This is incredibly important in optical and microwave engineering. If you know the dielectric properties of the materials you are designing with, you can completely eliminate reflections just by controlling the polarization and the physical angle of your hardware!