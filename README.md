# ALERT EYE: Motion Detection System 👁️👁️

## Objective

The ALERT EYE project aims to detect motion using a Passive Infrared (PIR) sensor to identify changes in infrared radiation emitted by humans or animals within its field of view. This system can trigger alerts or initiate predefined actions, making it highly applicable for security systems, automated lighting, and real-time monitoring.

---

## Problem Statement

With growing safety and security concerns, constant vigilance in sensitive areas like homes, offices, and restricted zones is impractical. Existing solutions often suffer from:
- High costs and energy inefficiency.
- Frequent false alarms due to sensitivity issues.
- Limited adaptability to dynamic environments.

This project addresses these challenges by implementing a reliable, cost-effective, and energy-efficient motion detection system using a PIR sensor and Raspberry Pi 3.

---

## Hardware Components
1. **Raspberry Pi 3**  
   - Features: Quad-core ARM Cortex-A53 CPU, 1GB RAM, Wi-Fi, Bluetooth, and GPIO pins.
   - Purpose: Acts as the central processing unit for interfacing with the PIR sensor and executing motion detection logic.

2. **PIR Sensor (e.g., HC-SR501)**  
   - Function: Detects motion by sensing infrared radiation changes from moving objects like humans or animals.
   - Integration: Connected to Raspberry Pi GPIO pins for real-time data input.

3. **LED Indicators**  
   - Purpose: Visual feedback upon detecting motion.

4. **Notification System**  
   - Alerts via phone or PC screen using pre-configured scripts.

---

## Software
- **Programming Language:** Python
- **Libraries:**
  - `RPi.GPIO`: For controlling Raspberry Pi GPIO pins.
  - `time`: For delay management.
  - `os`: For executing system-level commands.

---

## Circuit Design
1. Raspberry Pi 3 connected to the PIR sensor through GPIO pins.
2. LED wired to an output GPIO pin for visual alerts.
3. Notification system integrated through scripts executed upon motion detection.

---

## Features
1. **Motion Detection:** Uses the PIR sensor to detect real-time motion.
2. **Visual Alert:** LED blinks upon detecting motion.
3. **Notification System:** Sends alerts to connected devices.
4. **Customizable Response:** Predefined actions can be modified to suit specific requirements.

---

## Setup Instructions
1. Assemble the components as per the provided circuit diagram.
2. Flash the Raspberry Pi with a compatible OS (e.g., Raspbian).
3. Install necessary Python libraries:
   ```bash
   sudo apt-get install python3-rpi.gpio
   ```
4. Clone the project repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd ALERT-EYE
   ```
5. Run the script:
   ```bash
   python3 motion_detection.py
   ```

---

## Code Overview
### Main Logic
1. Set GPIO pins for the PIR sensor (input) and LED (output).
2. Monitor PIR sensor for infrared radiation changes.
3. Trigger LED and send alerts when motion is detected.

---

## Applications
1. **Home and Office Security:** Detect unauthorized access.
2. **Smart Lighting:** Automate lighting based on motion detection.
3. **Healthcare:** Monitor patient activity or inactivity.

---

## Future Enhancements
1. AI-powered context-aware actions for home automation.
2. Integration with autonomous vehicles for safety monitoring.
3. Advanced healthcare monitoring for elderly and disabled individuals.

---

## Acknowledgments
This project builds on the robustness of Raspberry Pi and the reliability of PIR sensors to deliver an affordable and efficient solution to modern security needs.

--- 
# Contributors:
1) Siddhima Singh : [GitHub](https://github.com/siddhima-singh)
2) Aastha Kothari : [GitHub](https://github.com/AASTHAKOTHAR)
3) Lakshya Sharma : [GitHub](https://github.com/lakshya603)
