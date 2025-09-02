# Task 4: Neural Network for Learning Addition

## Overview
This project implements a simple feedforward neural network using NumPy to learn the addition of two integers (0-99). The model is trained to approximate the sum of two numbers through supervised learning.

The neural network architecture includes:
- **Input layer**: 2 features (two integers)
- **Hidden layer**: 4 neurons with sigmoid activation
- **Output layer**: 1 neuron predicting the sum

Training is performed using backpropagation and gradient descent to minimize mean squared error.

## Colab Link
https://colab.research.google.com/drive/1pt4Kco6TJGND4rTvM3wM59gEb4o2t8NM?usp=sharing

## Features

- Custom implementation of forward and backward propagation
- Min-Max normalization for input and output data
- Training on 100,000 randomly generated samples
- Evaluation on 100 unseen test samples

## How It Works

### 1. Data Generation
- `X_train`: 100,000 samples of two random integers between 0 and 99
- `y_train`: Sum of each pair in `X_train`
- `X_test`: 100 samples for evaluation
- `y_test`: True sums for `X_test`

### 2. Normalization
- Inputs and outputs are scaled to the range [0, 1] using Min-Max scaling
- This improves training stability and convergence

### 3. Model Training
- Trained for 5000 epochs with a learning rate of 0.1
- Loss is printed every 100 epochs

### 4. Prediction and Evaluation
- Test inputs are scaled using training data statistics
- Predictions are inverse-scaled to match original output range
- Results are printed in the format:  
  `a + b ≈ predicted_sum (expected true_sum)`


## Requirements

- Python 3.x
- NumPy

## How to run
1. Open the notebook in Google Colab
2. Execute all cells to train the model and view predictions
