# Traffic Sign Recognition

This project implements a convolutional neural network (CNN) for recognizing traffic signs using TensorFlow and OpenCV. The model is trained on images organized in directories named after their respective categories.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Model description and experimentation](#model-description-and-experimentation)

## Installation

To run this project, you need to have Python 3 and the following libraries installed:

- TensorFlow
- OpenCV
- NumPy
- scikit-learn

You can install the required libraries using pip:

```bash
pip install tensorflow opencv-python numpy scikit-learn
```

## Usage

To run the program, use the following command:
```bash
python traffic.py <data_directory> [model.h5]
```
- data_directory: Path to the directory containing the image data.
- model.h5 (optional): Name of the file to save the trained model.

The program will load images, train the model, and optionally save the trained model to the specified file.

## Model Architecture

The model consists of the following layers:

- Convolutional layer with 32 filters (6x6 kernel)
- Max-pooling layer (4x4 pool size)
- Flatten layer
- Dense layer with 256 units and ReLU activation
- Dropout layer (40%)
- Output layer with softmax activation for `NUM_CATEGORIES` units

## Training

The model is trained for a specified number of epochs (default is 10). You can modify the `EPOCHS` constant in the code to change the number of training epochs.

## Evaluation

After training, the model evaluates its performance on the test set and prints the results.

## Model description and experimentation
To build the Network, I started by  building the fundation  of my neural network:
    - a sequential network model
    - a convolutional layer, using 32 filters and a 3x3 kernel
    - a max-pooling using a 2x2 pool size
    - a hidden layer with 128 units and a dropout of 0.5
    - an output layer with the number of units equal to the number of categories with softmax activation.
    => This lead to an  accuracy of 0.9681

### Experimentation:  

#### kernel and pool size:

- Doubling the poolsize (4x4): accuracy: 0.9469 - loss: 0.2241
- quadrupling the poolsize (8x8): accuracy: 0.8164 - loss: 0.6406  
- poolsize 4x4, doubling filters kernel (6x6): accuracy: 0.9779 - loss: 0.1043
- poolsize 4x4, quadrupling filters kernel (12x12): accuracy: 0.9607 - loss: 0.1610
- poolsize 4x4, doubling filters kernel (6x6), adding more filteer (64): accuracy: 0.9725 - loss: 0.1227 => no clear improvment

Rising the pool size shown a clear decrease on accuracy; in other hand, doubling filter kernel to x4 shown mitigate the pool size increase, showing beetter result than the original network.
poolsize(4x4) and 6x6 filters kernel will be kept for an accuracy around 0.977

#### Additionnal Filter / pooling layer

Additionnal filter and pooling layeer  decreased the accuracy.

#### dropout

- Increasing dropout to 0.7 clearly decreased the accuracy (0.93)
- Decreasing drropout to 0.3: accuracy: 0.9735 - loss: 0.0995  no clear evolution
- dropout 0.4: slightly improved the model accuracy: 0.9768 - loss: 0.0927

#### hidden layer:

- doubling the numbers of units of the hidden layer (256) improved the accurracy up to 0.9825
- adding another hidden layer decreased the accuracy to 0.97
- quadrupling the numberr of units didn't improved the accuracy

I have also tested the importance of normalizing the img (division  by 255). No normalization shown a dramatic decrease of the performance of the model, showing an accuracy of 50%.