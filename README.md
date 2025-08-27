# Smart Suitcase

## 📖 Overview
The **Smart Suitcase** project was developed to provide a hands-free travel experience by enabling autonomous tracking and obstacle avoidance. Through the integration of computer vision, fuzzy control, and embedded systems, the suitcase is capable of following its owner in real-time, avoiding collisions, and preventing loss in crowded environments such as airports. This work was carried out as part of a graduation thesis at **Ho Chi Minh City University of Technology, Faculty of Electrical & Electronics Engineering**, under the supervision of Assoc. Prof. Huynh Thai Hoang.  

![Smart Suitcase Concept](figures/concept.png)

---

## 🎯 Objectives
The motivation behind this project was to design a cost-effective smart suitcase that is both user-friendly and technically efficient. Unlike many commercial products, the prototype emphasizes affordability while still achieving real-time tracking and autonomous navigation. The system relies on the Intel Movidius Neural Compute Stick for owner detection, an ARM-based controller for motor control, and an Android application with a web interface for seamless user interaction. The ultimate goal was to deliver a practical, low-cost solution that surpasses the limitations of existing smart luggage on the market.  

![Objective Diagram](figures/objectives.png)

---

## ⚙️ Methodology
The methodology combines both hardware and software design into a unified system. On the software side, a deep learning model was trained to perform logo-based object detection, enabling the suitcase to identify and track its owner. This detection process was enhanced with a fuzzy logic controller, which refined the tracking response and improved obstacle avoidance. On the hardware side, an ARM-based controller was responsible for driving the motors and handling communication with peripheral sensors. Ultrasonic sensors were integrated for real-time distance measurement, while Node.js-based server processes ensured smooth data transfer through TCP/IP and SPI protocols. To support user interaction, a mobile Android application was built to notify the owner in case of lost tracking, complemented by a web interface for non-Android users.  

![System Overview](figures/system_overview.png)  
![Training Process](figures/training_process.png)  
![Motor Control](figures/motor_control.png)  
![Android Application](figures/android_app.png)

---

## 📊 Results and Analysis
The system demonstrated reliable real-time tracking under different conditions, including rotation, varying distances, and partial occlusion of the target logo. The fuzzy controller proved effective in adapting to these challenges by adjusting the control signals dynamically, thereby improving accuracy. Obstacle avoidance tests showed that the suitcase could handle one or more obstacles, as well as situations where the path was directly blocked. Finally, the integration of the server and Android application provided an effective anti-loss mechanism, alerting the user when the suitcase lost its target and offering the flexibility to switch easily between automatic and manual control.  

![Tracking Results](figures/tracking_results.png)  
![Fuzzy Controller](figures/fuzzy_controller.png)  
![Obstacle Avoidance](figures/obstacle_avoidance.png)  
![Android + Server Interface](figures/android_server.png)

---

## ✅ Merits and Limitations
The project successfully demonstrated the feasibility of building a smart suitcase that could track its owner in real-time while also offering a server-assisted alarm system to prevent loss. The combination of auto and manual modes gave users greater flexibility, and the integration of fuzzy control improved tracking robustness. However, some limitations were observed. The system struggled in low-light environments due to visual detection constraints, and it required a Wi-Fi connection to update data to the server. Movement speed was slower than expected, and noise sometimes appeared during obstacle detection, affecting overall performance.  

---

## 🚀 Future Work
Several directions for improvement were identified. Hardware optimization and aesthetic enhancement would make the suitcase more appealing for practical use. Integrating a weight sensor could add a built-in luggage scale, while designing a removable battery would increase convenience for travelers. On the algorithmic side, future development could include skeleton-based body tracking to improve owner detection and the ability for the suitcase to follow from the side rather than just from behind. These improvements would bring the product closer to a market-ready solution.  

---

## 👥 Team and Acknowledgment
This project was carried out by **Hoang Trong Dai (1510633)** and **Ly Kim Tien (1513418)**, under the guidance of **Assoc. Prof. Huynh Thai Hoang**. The team is grateful for the continuous support of the Faculty of Electrical & Electronics Engineering at Ho Chi Minh City University of Technology.  

---

## 📅 Date
**05/03/2022** – Ho Chi Minh City University of Technology, Department of Control Engineering & Automation
