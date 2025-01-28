# BERT Masked Language Model with Attention Visualization

This project implements a masked language model using BERT (Bidirectional Encoder Representations from Transformers) and visualizes the attention scores for the model's predictions. It allows users to input a sentence containing a mask token, generates predictions for the masked word, and visualizes the attention weights of the model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Attention Visualization](#attention-visualization)

## Installation

To run this project, you need to have Python 3 and the following libraries installed:

- TensorFlow
- Pillow
- Transformers

You can install the required libraries using pip:

```bash
pip install tensorflow pillow transformers
```

## Usage
To run the program, use the following command:

```bash
python attention.py
```` 

The program will prompt you to input a sentence containing a mask token (e.g., "The cat sat on the [MASK]."). If you want to include the mask token in your input, ensure it is present in the sentence.

## Functionality

- **Input Handling**: The program accepts a sentence from the user, which must include a mask token.
- **Tokenization**: The input sentence is tokenized using a pre-trained BERT tokenizer.
- **Prediction Generation**: The model generates predictions for the masked token and prints the top K predictions.
- **Attention Visualization**: The program visualizes the self-attention scores for each attention head in the BERT model.

## Attention Visualization

The attention visualization generates graphical representations of self-attention scores for each layer and attention head in the BERT model. The diagrams show the tokens in the sentence, with cells shaded based on the attention weights. Lighter cells correspond to higher attention scores.

The generated images are saved with filenames that include both the layer number and head number, following the format `Attention_Layer{layer_number}_Head{head_number}.png`.