# Fish Weight Predictor

Welcome to the Fish Weight Predictor project! This repository contains the code and resources for predicting the weight of fish based on their measurements using a machine learning model.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model](#model)
- [Frontend](#frontend)
- [Installation](#installation)
- [Usage](#usage)


## Introduction

The Fish Weight Predictor is a machine learning project designed to predict the weight of fish from various measurements such as length, height, and width. The project involves building a predictive model, creating a frontend for user interaction, and deploying the model on Heroku for easy accessibility.

## Dataset

The dataset used for this project is the Fish Market dataset, which contains information about different fish species and their corresponding measurements. The dataset includes the following features:
- Species
- Weight
- Length1
- Length2
- Length3
- Height
- Width

## Model

The machine learning model is built using Python and scikit-learn. The following steps are involved in the model creation:
1. Data Preprocessing
2. Feature Engineering
3. Model Training
4. Model Evaluation

## Frontend

The frontend of the Fish Weight Predictor is a simple webpage built using HTML. It allows users to input the measurements of a fish and get the predicted weight.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ritik-1101/Fish_Weight_Predictor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Fish_Weight_Predictor
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py or Flask run
   ```

## Usage

To use the Fish Weight Predictor, follow these steps:

1. Open the browser and enter ```127.0.0.1:5000/```
2. Enter the measurements of the fish.
3. Click the 'Predict' button to get the predicted weight.
