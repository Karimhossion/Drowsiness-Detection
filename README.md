# Real-Time Drowsiness Detection

## Project Overview

Real-Time Drowsiness Detection is a computer vision and deep learning based project that aims to detect driver drowsiness in real time using a camera. The system observes the driver’s face and eye movements from live video input. If the driver shows signs of drowsiness, such as prolonged eye closure, the system generates an alert to warn the driver.

The main purpose of this project is to help reduce road accidents caused by drowsy driving. This system is designed to be low-cost, non-intrusive, and easy to use because it uses only a normal camera instead of wearable sensors like EEG devices.

---

## Problem Statement

Drowsy driving is one of the major causes of road accidents. Many drivers become tired during long-distance travel, night driving, or continuous driving without rest. In such situations, drivers may lose concentration, close their eyes for a longer time, or fall asleep while driving.

Existing drowsiness detection methods are not always practical. Some systems depend on self-assessment, passenger monitoring, or wearable sensors. These methods may be uncomfortable, expensive, or unreliable in real-world driving conditions.

Therefore, this project proposes a camera-based real-time drowsiness detection system that can detect eye states using computer vision and CNN, and then give an immediate alert when drowsiness is detected.

---

## Objectives

The main objectives of this project are:

- To develop a real-time driver drowsiness detection system.
- To detect the driver’s face and eye region from live camera input.
- To classify eye states as open or closed using a CNN model.
- To identify drowsiness based on continuous eye closure.
- To generate an alert when the driver becomes drowsy.
- To build a low-cost and non-intrusive system for road safety.

---

## Features

- Real-time video processing
- Face detection
- Eye detection
- Eye state classification
- CNN-based detection
- Drowsiness alert system
- Low-cost camera-based solution
- Non-intrusive system
- Suitable for driver safety applications

---

## Technologies Used

The following technologies and tools are used in this project:

- Python
- OpenCV
- TensorFlow / Keras
- Convolutional Neural Network
- Haar Cascade Classifier
- NumPy
- Matplotlib
- Webcam / Camera

---

## System Workflow

The working process of the system is described below:

1. The camera captures live video of the driver.
2. The system detects the driver’s face from the video frame.
3. The eye region is detected from the face.
4. The eye image is preprocessed before classification.
5. A CNN model classifies the eye state as open or closed.
6. If the eyes remain closed for a certain period, the system detects drowsiness.
7. An alert is generated to warn the driver.

---

## Methodology

This project follows a step-by-step methodology:

### 1. Data Collection

Eye images are collected or selected from a suitable dataset. The dataset contains images of open eyes and closed eyes.

### 2. Data Preprocessing

The images are resized, normalized, and prepared for model training. Preprocessing helps the model learn better features from the input images.

### 3. Model Training

A CNN model is trained to classify eye states. The model learns the difference between open eyes and closed eyes.

### 4. Real-Time Detection

The trained model is integrated with OpenCV to detect eye states from live camera video.

### 5. Alert Generation

If the system detects that the driver’s eyes remain closed for a certain time, it triggers an alert to notify the driver.

---

## Expected Outcomes

The expected outcomes of this project are:

- A working real-time drowsiness detection system.
- A trained CNN model for eye state classification.
- Detection of driver drowsiness from live camera input.
- An alert system to warn the driver.
- Improved understanding of computer vision and deep learning applications.
- A practical solution that can contribute to road safety.

---

## Project Structure

```text
Real-Time-Drowsiness-Detection/
│
├── Background Study/
│   ├── 1. Driver Drowsiness Detection System using Convolutional Neural Network.
│   ├── 2. IoT-Assisted Automatic Driver Drowsiness Detection through Facial Movement Analysis Using Deep Learning and a U-Net-Based Architecture.
│   ├── 3. A Robust and Efficient EEG-Based Drowsiness Detection System Using Different Machine Learning Algorithms.
│   ├── 4. Convolutional Neural Network for Drowsiness Detection Using EEG Signals.
│   ├── 5. Physiological Signal-Based Drowsiness Detection Using Machine Learning: Singular and Hybrid Signal Approaches.
│   ├── 6. EEG-Based Drowsiness and Alertness Recognition Using Feature Fusion and Deep Residual Networks.
│   ├── 7. Learning Multimodal Representations for Drowsiness Detection.
│   ├── 8. An Efficient System for Driver Drowsiness Detection Using Convolutional Neural Networks.
│   ├── 9. Driver Drowsiness Detection Based on Facial Expression Recognition Using Deep Learning.
│   ├── 10. Driver Drowsiness Detection System Based on Feature-Level Fusion of Facial and Bio-Signals.
│   ├── 11. Driver Drowsiness Classification Using Fuzzy Wavelet-Packet-Based Feature-Extraction Algorithm.
│   └── 12. From Facial Expression Recognition to Interpersonal Trust Inference: Recent Advances in the Machine Learning Perspective.
│
├── Project/
│   └── Project File
│
├── Proposal/
│   └── Project proposal related files
│
├── README.md
│
└── Other project files
```

---

## Advantages

- Low-cost solution
- Easy to use
- No wearable device required
- Real-time monitoring
- Useful for driver safety
- Can be improved for practical vehicle systems

---

## Limitations

This project may have some limitations:

- Performance may decrease in low-light conditions.
- Eye detection may be affected by glasses or face masks.
- Camera angle and head movement may affect accuracy.
- The system may need a good quality dataset for better performance.
- False alerts may occur in some situations.

---

## Future Improvements

In the future, this project can be improved by:

- Improving accuracy in low-light and night driving conditions.
- Using a larger and more diverse dataset.
- Adding head pose detection.
- Adding yawning detection.
- Deploying the system on mobile or embedded devices.
- Testing the system in real driving environments.
- Improving the alert system with audio and visual warnings.

---

## Applications

This project can be used in:

- Driver safety systems
- Smart vehicles
- Road accident prevention systems
- Transport monitoring systems
- Research projects related to computer vision
- Embedded AI-based safety systems

---

## Conclusion

This project presents a real-time drowsiness detection system using computer vision and deep learning. By detecting the driver’s eye state and generating an alert, the system can help reduce the risk of accidents caused by drowsy driving. The proposed system is simple, low-cost, and non-intrusive, making it suitable for practical driver safety applications.

---

## Author

**Md Karim,**
**Mst Khadiza Alam Momi,**
**Samia Akter Nipa**


Department of Computer Science and Engineering  
Varendra University  
Rajshahi, Bangladesh