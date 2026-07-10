---
layout: post
title: "Beyond the Straight Line: Deriving Snell's Law and Fresnel Equations from Scratch"
description: "What happens when a microwave hits a boundary at an angle? A very simple, layman-friendly derivation of oblique incidence, Snell's Law, and the Fresnel equations."
order: 7
topic: [Theory, EM-Theory, L1-Foundational, Derivation]
images:
  - /images/qronicle/post7/image1.png
resources:
  - name: "Oblique Incidence of Uniform Plane Waves (Poriyaan)"
    link: "https://eee.poriyaan.in/topic/oblique-incidence-of-uniform-plane-waves-11873/"
  - name: "Oblique Incidence on a Dielectric Boundary (YouTube)"
    link: "https://youtu.be/0F8BMUGEix8?si=5CqbeeWsyTgVCcky"
  - name: "Reflection at Oblique Incidence (YouTube)"
    link: "https://youtu.be/Qf3KlHfrL9s?si=BKdkyTvjQrJMtXxJ"
---

## Hitting at an Angle: The Oblique Incidence

In our last few posts, we saw what happens when an electromagnetic wave hits a boundary straight-on (normal incidence). But practically speaking, waves don't always travel in a perfectly straight line into a new material. Sometimes they hit the boundary at a certain angle. This is what we call **Oblique Incidence**.

Now, you might remember Snell's Law from high school physics, right? Normally, textbooks just give you Snell's Law and ask you to use it. But as engineers working on quantum hardware, we shouldn't just assume things. Today, we are going to derive Snell's Law and the reflection formulas (called Fresnel equations) purely from the basics, without assuming anything beforehand!

Basically, we have a flat boundary at $z = 0$. Above it is Medium 1 (where the wave comes from), and below it is Medium 2. The incident wave hits this boundary at an angle of $\theta_i$. It then splits into a reflected wave bouncing back at an angle of $\theta_r$, and a transmitted wave passing through at an angle of $\theta_t$.

---

## Phase Matching: Deriving Snell's Law from Scratch

When the wave hits the boundary, the electric and magnetic fields must be perfectly continuous across that surface at all times. For this to happen, the "phase" of the incident, reflected, and transmitted waves must perfectly match all along the boundary surface.

The phase of a wave is determined by its wave vector ($k$). For the waves to be perfectly locked together at the boundary interface (along the x-axis), their tangential phase components must be exactly equal. 

So, we can simply write:
$$k_i \sin(\theta_i) = k_r \sin(\theta_r) = k_t \sin(\theta_t)$$

Let's look at the first two terms: the incident and reflected waves. Because both of these waves are traveling in the exact same material (Medium 1), their wave numbers are identical ($k_i = k_r$). 
If we cancel them out, we get:
$$\sin(\theta_i) = \sin(\theta_r)$$
$$\theta_i = \theta_r$$
**Result 1:** The angle of reflection is exactly equal to the angle of incidence. This is the Law of Reflection!

Now let's take the first and third terms. We know that the wave number $k = \omega \sqrt{\mu \epsilon}$. If we substitute this in, the angular frequency ($\omega$) cancels out on both sides:
$$\sqrt{\mu_1 \epsilon_1} \sin(\theta_i) = \sqrt{\mu_2 \epsilon_2} \sin(\theta_t)$$

Since the speed of light in a material is inversely proportional to the refractive index ($n \propto \sqrt{\mu \epsilon}$), we can rewrite this as:
$$n_1 \sin(\theta_i) = n_2 \sin(\theta_t)$$

**Result 2:** We just derived Snell's Law purely from electromagnetic phase matching! No assumptions needed.

---

## The Fresnel Equations: Finding the Reflection

Now that we know the angles, we need to find out *how much* of the wave is actually reflected. 

When a wave comes in at an angle, things get a bit tricky because the electric field ($\mathbf{E}$) and magnetic field ($\mathbf{H}$) are pointing in different directions. To make the math simple, we split this problem into two specific cases: Perpendicular Polarization and Parallel Polarization.

### Case 1: Perpendicular Polarization (Tangential E-Field)
Also known as TE (Transverse Electric) polarization. Suppose the Electric field is entirely parallel (tangential) to the flat boundary surface, sticking straight out along the y-axis. 

Because the entire E-field is tangential, the boundary condition is super simple:
$$E_i + E_r = E_t$$

But the Magnetic field ($\mathbf{H}$) is tilted at an angle. To get the tangential part of the magnetic field, we have to use a little trigonometry (just multiplying by cosine of the angle). 
$$H_i \cos(\theta_i) - H_r \cos(\theta_r) = H_t \cos(\theta_t)$$

We already know that $H = \frac{E}{\eta}$. Let's substitute that in, and remember that $\theta_i = \theta_r$:
$$\frac{E_i}{\eta_1} \cos(\theta_i) - \frac{E_r}{\eta_1} \cos(\theta_i) = \frac{E_t}{\eta_2} \cos(\theta_t)$$

Now, replace $E_t$ with $(E_i + E_r)$ and shift all the $E_i$ terms to one side and $E_r$ terms to the other, just like we did in the normal incidence derivation. After cross-multiplying, we find the Reflection Coefficient for the Perpendicular case ($\Gamma_{TE} = \frac{E_r}{E_i}$):

$$\Gamma_{TE} = \frac{\eta_2 \cos(\theta_i) - \eta_1 \cos(\theta_t)}{\eta_2 \cos(\theta_i) + \eta_1 \cos(\theta_t)}$$

### Case 2: Parallel Polarization (Tangential H-Field)
Also known as TM (Transverse Magnetic) polarization. Here, the situation is flipped. The Magnetic field is entirely parallel to the boundary, and the Electric field is tilted.

The boundary condition for the tangential H-field is:
$$H_i + H_r = H_t$$
$$\frac{E_i}{\eta_1} - \frac{E_r}{\eta_1} = \frac{E_t}{\eta_2}$$

For the tangential E-field, we have to use the cosine trick:
$$E_i \cos(\theta_i) + E_r \cos(\theta_i) = E_t \cos(\theta_t)$$

From this, we can write $E_t = (E_i + E_r) \frac{\cos(\theta_i)}{\cos(\theta_t)}$. 
If we substitute this $E_t$ back into the first equation and solve for the ratio of $E_r$ to $E_i$, we get the Reflection Coefficient for the Parallel case ($\Gamma_{TM}$):

$$\Gamma_{TM} = \frac{\eta_2 \cos(\theta_t) - \eta_1 \cos(\theta_i)}{\eta_2 \cos(\theta_t) + \eta_1 \cos(\theta_i)}$$

---

## Why Does This Matter?

Look closely at the formulas we just derived. They are almost identical to our old normal incidence formula ($\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}$), except now we have these cosine terms attached to the impedances!

This means the "effective impedance" a wave feels depends entirely on the angle it hits the boundary. If you are routing high-frequency signals in a quantum computer, any bend, kink, or angled transition in the hardware will change the reflection behavior based on these exact Fresnel equations. Mastering these basics gives you the power to actually control how the wave behaves in the real world.