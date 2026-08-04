---
layout: post
title: "Hands-On: Measuring a Filter with a Vector Network Analyzer"
description: "It is time to step into the lab. Let us boot up a Rohde & Schwarz Vector Network Analyzer and manually measure a filter's S-Parameters."
order: 22
slug: "22"
topic: [Theory, Practical, Microwave-Engg, Quantum-Tech, L3-Advanced]
images:
  - /images/qronicle/post22/image1.jpg
references:
  - name: "R&S ZNL/ZNLE Vector Network Analyzers - Product Video"
    link: "https://www.youtube.com/watch?v=l6yArXbUw7M"
  - name: "Webinar: Fundamentals of VNA Measurements"
    link: "https://www.rohde-schwarz.com/us/knowledge-center/webinars/webinar-fundamentals-of-vna-measurements-vd_257263.html"
  - name: "Getting Started with the ZNL - Reflection Measurements"
    link: "https://www.youtube.com/watch?v=NyZiLIfd3wE"
  - name: "Getting Started with the ZNL - Transmission Measurements"
    link: "https://www.youtube.com/watch?v=x_jL5jtVd-w"
resources:
  - name: "R&S ZNL/ZNLE User Manual (PDF)"
    link: "https://www.batterfly.com/PDF/rohde-schwarz/znl-znle/ZNL_ZNLE_usermanual_EN.pdf"
  - name: "R&S ZNLE Specifications (PDF)"
    link: "https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/pdm/cl_brochures_and_datasheets/specifications/5215_1882_22/ZNLE_specs_en_5215-1882-22_v0700.pdf"
  - name: "Rohde and Schwarz ZNLE6 - Vector Network Analyzer (1MHz - 6GHz) | TEquipment"
    link: "https://www.tequipment.net/Rohde-&-Schwarz/ZNLE6/Network-Analyzer/?srsltid=AfmBOopwwHF9wKgfcewBjuDswGl-j503G5lVQKEGi7EAYhDzDiadhEvX"
---

## From Math to the Lab Bench

We have derived the math of S-Parameters and visualized the "Perfect Mountain" of a filter's transmission and reflection traces. Now, it is time to actually measure one. 

For this walkthrough, we will be referencing the industry-standard **Rohde & Schwarz ZNL / ZNLE** series of Vector Network Analyzers. These machines are incredible pieces of engineering, capable of achieving a dynamic range of up to $120 \text{ dB}$ (meaning they can accurately measure a signal that has been crushed by a factor of a trillion).

Let us connect a physical Bandpass Filter and extract its S-Parameter matrix manually.

---

## Step 1: The Setup and Preset

Before we begin, we must connect our Device Under Test (DUT). We connect the input of the filter to **Port 1** of the VNA, and the output of the filter to **Port 2**. 

If someone else used the VNA before you, it might be full of strange markers, offset delays, and weird frequency ranges. 
*   **The Action:** Press the **`[Preset]`** hardkey on the front panel.
*   **The Result:** This resets the instrument to a well-defined default configuration. By default, the analyzer will start sweeping across its entire frequency range and display the forward transmission parameter, $S_{21}$.

---

## Step 2: Defining the Sweep Range

Your filter only operates over a specific bandwidth, so sweeping the VNA's entire maximum frequency range makes the data look cramped and ruins your resolution. We need to narrow our focus.

*   **The Action:** Press the **`[Freq]`** key on the front panel. 
*   **The Entry:** Use the touchscreen or the physical keypad to set the **Start Frequency** just below your filter's passband, and the **Stop Frequency** just above it. (For example, if testing a 2 GHz filter, you might set Start to 1.5 GHz and Stop to 2.5 GHz).
*   **The Fix:** Your trace might now be off the top or bottom of the screen. Press the **`[Scale]`** key, tap "Scale Values", and hit **"Auto Scale Trace"**. The VNA will automatically adjust the Y-axis (dB) so the entire trace fits perfectly on your screen.

---

## Step 3: The Crucial Step — Calibration

If you look at the screen right now, the measurement is slightly wrong. The cables connecting the VNA to your filter have their own attenuation and phase delay. We have to mathematically remove the cables from the measurement so we only see the filter itself.

*   **The Action:** Remove the filter and grab a physical Calibration Kit. 
*   **The Setup:** Press the **`[Cal]`** key and select **"Start... (Manual)"** to open the Calibration Setting wizard.
*   **The Execution:** For a full 2-port measurement, you will select the **TOSM** calibration type (Through, Open, Short, Match). The wizard will instruct you to connect the Open, Short, and Match (a perfect $50 \ \Omega$ load) standards one by one to each port, and then connect Port 1 directly to Port 2 (the Through).
*   **The Result:** The VNA calculates the exact error profile of your cables. Once you hit "Apply" and reconnect your filter, a "Cal" label appears on the screen. You are now measuring *only* the filter!

---

## Step 4: Reading the Matrices ($S_{21}$ and $S_{11}$)

Now we want to view both the Transmission ($S_{21}$) and the Reflection ($S_{11}$) to verify the Conservation of Energy rule we learned in Post 21.

*   **The Action:** Press the **`[Meas]`** key to open the Measurement menu. Here you can tell the VNA exactly which S-Parameter from the matrix you want to plot. 
*   **The View:** Press **`[Trace]`** to add a second trace to the screen. Assign $S_{21}$ to Trace 1, and $S_{11}$ to Trace 2. 

You should now see the "Perfect Mountain." Where $S_{21}$ is high and flat ($0 \text{ dB}$), $S_{11}$ should drop into a deep valley ($-20 \text{ dB}$ or lower). 

---

## Step 5: Precision Analysis using Markers

We can visually see the filter working, but as engineers, we need exact numbers. What is the exact insertion loss? Where exactly are the $-3 \text{ dB}$ cutoff frequencies? We find this using Markers.

*   **The Action:** Press the **`[Mkr]`** key. 
*   **The Execution:** A marker triangle (M1) appears on the trace. An info field in the corner of the diagram will show you the exact frequency and exact dB value at that physical point.
*   **The Search:** You can manually drag the marker with your finger on the touchscreen, or use the **`[Mkr ->]`** search key. Tapping "Peak" will instantly snap the marker to the highest point of your filter's passband, telling you your exact lowest insertion loss.
*   **Advanced Features:** To quickly find the exact bandwidth, you can use the built-in band filter function (accessed via the **`[Mkr ->]`** hardkey and the **Bandfilter** button). This automatically calculates your filter's center frequency, bandwidth, and quality factor.

By systematically using the `[Freq]`, `[Cal]`, `[Meas]`, and `[Mkr]` keys, you have just manually extracted the complete scattering matrix of a physical microwave component!