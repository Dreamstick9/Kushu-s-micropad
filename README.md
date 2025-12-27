# Kushu-s-micropad
<img width="1255" height="732" alt="Screenshot 2025-12-27 at 8 49 59 PM" src="https://github.com/user-attachments/assets/7a650d31-9c8f-4db7-ab7a-a5eaa6fa6f4c" />


## Inspiration
I wanted to create a "Megapad" that wasn't just keys—I needed control. I designed a custom macropad featuring **6 keys, 2 rotary encoders, and an OLED screen** so I could manage volume, scroll through pages, and see my layer status all at once. It's the ultimate desk companion for productivity (and fidgeting).

## Challenges
This project fought me every step of the way.

**Fusion 360 was a nightmare at first.** I'd never used it before, and just getting the sketches to lock in or the mouse controls to cooperate felt like a puzzle. The hardest technical hurdle was the mechanical integration specifically the USB-C port alignment and the internal clearance for the tall encoder pins.

There was a moment near the end where I almost skipped the final "Crash Test" because I was just done. I didn't think I had it in me to import the PCB into the case and align the joints. But I pushed through, learned how to use "Section Analysis" to X-Ray the case, and verified that the top plate sat flush on the shoulders without hitting the standoffs. Seeing that perfect cross section view in the end was the only thing that convinced me it would actually work.

## Specifications

### BOM:
* **1x** XIAO RP2040
* **6x** MX-Style Mechanical Switches
* **2x** EC11 Rotary Encoders (with push button)
* **1x** 0.91" OLED Display (I2C)
* **6x** 1N4148 Diodes
* **4x** M3x16 Bolts
* **4x** M3 Heatset Inserts
* **1x** 3D Printed Case & Plate

### Others:
* **Firmware:** KMK Firmware (CircuitPython)
* **Files:**
    * `Megapad_Full_Assembly.step` (CAD)
    * `gerbers.zip` (PCB Fabrication)



# Schematic
<img width="996" height="374" alt="Screenshot 2025-12-27 at 8 48 01 PM" src="https://github.com/user-attachments/assets/9c352dd8-d432-4d23-a992-b597a5a92ab7" />

# PCB
<img width="619" height="674" alt="Screenshot 2025-12-27 at 8 49 12 PM" src="https://github.com/user-attachments/assets/448f6ef0-2d22-4b14-adfc-7f3c1cfbb410" />

# Case
<img width="715" height="671" alt="Screenshot 2025-12-27 at 8 51 11 PM" src="https://github.com/user-attachments/assets/7d4f427e-8107-413c-90da-8f6259b5af35" />
