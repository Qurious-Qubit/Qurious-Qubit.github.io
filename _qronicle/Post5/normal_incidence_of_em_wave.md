---
layout: post
title: "Reflection and Transmission of Uniform Plane Waves at Normal Incidence"
description: "A step-by-step mathematical derivation of the reflection and transmission coefficients when an electromagnetic plane wave strikes a boundary between two different media."
order: 5
topic: [EM-Theory, L1-Foundational, Derivation]
images:
  - /images/qronicle/post5/image1.png
resources:
  - name: "Reflection of Uniform Plane Waves (Poriyaan)"
    link: "https://eee.poriyaan.in/topic/reflection-of-uniform-plane-waves-11872/"
references:
  - name: "Reflection of Plane Wave at Normal Incidence (YouTube)"
    link: "https://www.youtube.com/watch?v=umcmpHSFn-c"
  - name: "Reflection of Uniform Plane Waves (Poriyaan)"
    link: "https://eee.poriyaan.in/topic/reflection-of-uniform-plane-waves-11872/"
---

## Uniform Plane Waves at a Boundary

In previous posts, we derived how uniform plane waves propagate through a single, continuous medium. However, in practical engineering—whether you are routing signals through a standard RF circuit or sending control pulses down into a cryogenic quantum processor—waves rarely travel through an infinite vacuum. 

Eventually, the wave will encounter a boundary between two different materials. When an electromagnetic wave strikes a new medium, its energy splits: part of the wave transmits into the new material, and part of it reflects backward.

In this post, we will mathematically derive exactly how much of the wave is reflected and how much is transmitted when a wave strikes a boundary head-on (at a 90-degree angle). In electromagnetics, this is known as **Normal Incidence**.

---

## Defining the Geometry

Imagine a perfectly flat boundary located at $z=0$. 
* To the left of the boundary ($z<0$) is **Medium 1**, characterized by an intrinsic impedance of $\eta_1$.
* To the right of the boundary ($z>0$) is **Medium 2**, characterized by an intrinsic impedance of $\eta_2$.

An **Incident Wave** is traveling through Medium 1 in the $+z$ direction. We will orient its electric field ($E_i$) along the x-axis and its magnetic field ($H_i$) along the y-axis.

When this incident wave hits the boundary at $z=0$, it produces two distinct waves:
1. A **Transmitted Wave** ($E_t, H_t$) that continues traveling forward into Medium 2 in the $+z$ direction.
2. A **Reflected Wave** ($E_r, H_r$) that travels backward through Medium 1 in the $-z$ direction.

Because the reflected wave travels in the opposite direction, the Right-Hand Rule dictates that the cross product of its electric and magnetic fields must point in the $-z$ direction. By standard convention, we assume the electric field remains in the $+x$ direction, which means the magnetic field must flip to the $-y$ direction ($-H_r$).

---

## Electromagnetic Boundary Conditions

To solve for the reflected and transmitted waves, we must apply electromagnetic boundary conditions. At the interface between two standard dielectric media, the components of the electric and magnetic fields that are tangential (parallel) to the boundary surface must be continuous.

Since our wave is arriving at normal incidence, the entire $\mathbf{E}$ and $\mathbf{H}$ fields are parallel to the boundary at $z=0$. 

Therefore, the total electric field in Medium 1 must equal the total electric field in Medium 2:

$$E_i + E_r = E_t$$

Similarly, the total magnetic field must be continuous across the boundary:

$$H_i - H_r = H_t$$

*(Note the minus sign on $H_r$, representing the flipped direction of the reflected magnetic field).*

---

## Deriving the Reflection Coefficient ($\Gamma$)

The **Reflection Coefficient ($\Gamma$)** is defined as the ratio of the reflected electric field to the incident electric field: $\Gamma = \frac{E_r}{E_i}$.

To find this, we relate the electric and magnetic fields using the intrinsic impedance of the media ($H = \frac{E}{\eta}$). We can rewrite our magnetic fields as follows:

* Incident: $H_i = \frac{E_i}{\eta_1}$
* Reflected: $H_r = \frac{E_r}{\eta_1}$
* Transmitted: $H_t = \frac{E_t}{\eta_2}$

Substitute these into our magnetic boundary condition equation:

$$\frac{E_i}{\eta_1} - \frac{E_r}{\eta_1} = \frac{E_t}{\eta_2}$$

Next, substitute the electric boundary condition ($E_t = E_i + E_r$) into the right side of the equation:

$$\frac{E_i - E_r}{\eta_1} = \frac{E_i + E_r}{\eta_2}$$

To isolate the electric fields, cross-multiply by the impedances:

$$\eta_2(E_i - E_r) = \eta_1(E_i + E_r)$$

$$\eta_2 E_i - \eta_2 E_r = \eta_1 E_i + \eta_1 E_r$$

Now, group the incident terms ($E_i$) on the left and the reflected terms ($E_r$) on the right:

$$\eta_2 E_i - \eta_1 E_i = \eta_1 E_r + \eta_2 E_r$$

$$E_i(\eta_2 - \eta_1) = E_r(\eta_2 + \eta_1)$$

Divide both sides to solve for the Reflection Coefficient ($\Gamma = \frac{E_r}{E_i}$):

$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}$$

---

## Deriving the Transmission Coefficient ($\tau$)

The **Transmission Coefficient ($\tau$)** is defined as the ratio of the transmitted electric field to the incident electric field: $\tau = \frac{E_t}{E_i}$.

We can derive this by starting with the same magnetic boundary condition:

$$\frac{E_i}{\eta_1} - \frac{E_r}{\eta_1} = \frac{E_t}{\eta_2}$$

This time, instead of substituting for $E_t$, we rearrange the electric boundary condition to solve for $E_r$ ($E_r = E_t - E_i$) and substitute that in:

$$\frac{E_i}{\eta_1} - \frac{E_t - E_i}{\eta_1} = \frac{E_t}{\eta_2}$$

Distribute the negative sign and combine the $E_i$ terms:

$$\frac{E_i - E_t + E_i}{\eta_1} = \frac{E_t}{\eta_2}$$

$$\frac{2E_i - E_t}{\eta_1} = \frac{E_t}{\eta_2}$$

Separate the fraction on the left:

$$\frac{2E_i}{\eta_1} - \frac{E_t}{\eta_1} = \frac{E_t}{\eta_2}$$

Move the $E_t$ term to the right side and factor it out:

$$\frac{2E_i}{\eta_1} = E_t \left( \frac{1}{\eta_1} + \frac{1}{\eta_2} \right)$$

Find a common denominator for the terms in the parentheses:

$$\frac{2E_i}{\eta_1} = E_t \left( \frac{\eta_1 + \eta_2}{\eta_1 \eta_2} \right)$$

Finally, solve for the Transmission Coefficient ($\tau = \frac{E_t}{E_i}$) by dividing the $E$ terms and multiplying the impedances across:

$$\frac{E_t}{E_i} = \frac{2\eta_1 \eta_2}{\eta_1 (\eta_1 + \eta_2)}$$

The $\eta_1$ terms cancel out, leaving us with:

$$\tau = \frac{2\eta_2}{\eta_2 + \eta_1}$$

*Note: By looking closely at the equations, we can also prove a fundamental relationship between the two coefficients. If you calculate $1 + \Gamma$, you will find that it mathematically equals exactly $\tau$.*

$$1 + \Gamma = \tau$$

In our next post, we will take these two simple equations ($\Gamma$ and $\tau$) and explore what they actually imply for physical engineering. We will see why the relationship between $\eta_1$ and $\eta_2$ governs the entire discipline of high-frequency design, and why managing these coefficients is the absolute prerequisite for building reliable quantum hardware.