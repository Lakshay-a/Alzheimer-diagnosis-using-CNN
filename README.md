
# Alzheimer’s Disease Diagnosis using CNN 

![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Model Performance](#model-performance)
  - [Transfer Learning with DenseNet-121](#transfer-learning-with-densenet-121)
  - [K-Fold Cross-Validation](#k-fold-cross-validation)
  - [ROC-AUC Score](#roc-auc-score)
- [Snapshots](#snapshots)
  - [ROC-AUC Curve](#roc-auc-curve)
  - [Front-End Interface](#front-end-interface)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)

## Introduction

This project offers an innovative solution for diagnosing Alzheimer's disease by combining advanced deep-learning techniques, optimization algorithms, and medical image processing. It focuses on the multi-class classification to differentiate between Alzheimer's Disease (AD), Mild Cognitive Impairment (MCI), and Cognitively Normal (CN) stages using MRI scans, thereby enhancing early detection and improving diagnostic accuracy. By employing transfer learning with a DenseNet-121 model pre-trained on the RadImageNet database, this tool aims to contribute to better patient outcomes through more precise diagnoses significantly. The application features a user-friendly front-end interface that allows easy image uploads and provides immediate classification results, making it accessible for clinical use.


## Features

- **Transfer Learning with DenseNet-121**: Utilizes a DenseNet-121 architecture pre-trained on the RadImageNet database for superior feature extraction in medical images.
- **K-Fold Cross-Validation**: Employs k-fold cross-validation to verify model accuracy and robustness across different data subsets.
- **High Accuracy**: Achieved a test accuracy of 95.13%, ensuring reliable multi-class classification.
- **User-Friendly Interface**: Front-end application for uploading images and viewing results.
- **Real-time Classification**: Immediate feedback upon image submission.
- **Performance Metrics**: Includes a ROC-AUC curve to demonstrate model efficacy.


## Model Performance

The model has achieved a **test accuracy of 95.13%**, indicating high reliability in classifying MRI scans into AD, MCI, and CN stages.

### Transfer Learning with DenseNet-121

**Pre-trained on RadImageNet**: The DenseNet-121 model was pre-trained on the RadImageNet database, which is specifically designed for medical imaging tasks. This enhances the model's ability to extract relevant features from MRI scans.

**Transfer Learning Benefits**: By leveraging a pre-trained model, the training time is reduced, and performance is improved due to the model's prior knowledge.

### K-Fold Cross-Validation

Employed k-fold cross-validation to ensure the model's performance is consistent across different subsets of the data. This method helps in assessing how the results of the model will generalize to an independent dataset.

### ROC-AUC Score

The Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) metric have been utilized to evaluate the model's performance. An **ROC-AUC score of 0.99** demonstrates the model's efficacy in distinguishing between different stages of Alzheimer's Disease.

## Snapshots

### ROC-AUC Curve

<img width="717" alt="Screenshot 2024-10-11 at 2 26 13 AM" src="https://github.com/user-attachments/assets/35eec27a-ee3f-40d2-b695-03ab573853f0">

The ROC-AUC curve demonstrates the trade-off between sensitivity and specificity at various threshold settings.

### Front-End Interface

<img width="1512" alt="Screenshot 2024-10-11 at 2 22 48 AM" src="https://github.com/user-attachments/assets/a36e36ea-d8f5-4bbb-a664-24d633c696a3">

<img width="1512" alt="Screenshot 2024-10-11 at 2 23 30 AM" src="https://github.com/user-attachments/assets/8a1efbd1-4dec-4e89-9e0e-9b6cf7674a45">

The intuitive interface allows users to easily upload images and receive instant diagnoses.
## Acknowledgements

 - **Dataset**: Special thanks to [ADNI](https://adni.loni.usc.edu) for providing the MRI images used for training and testing.
- **RadImageNet**: Utilized the [RadImageNet](https://github.com/BMEII-AI/RadImageNet) database for pre-training the DenseNet-121 model.
- **Libraries and Frameworks**: This project utilizes TensorFlow, Keras, Flask, and other open-source libraries.

## Authors

- [Lakshay Arora](https://github.com/Lakshay-a)
- [Aditya Vohra](https://github.com/adityavohra2003)
- [Anchit Bansal](https://github.com/anchit11)

