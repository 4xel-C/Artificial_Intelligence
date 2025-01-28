# Noun Phrase Chunking

This project implements a simple noun phrase chunker using Natural Language Toolkit (nltk) in Python. The program parses sentences based on a defined context-free grammar (CFG) and identifies noun phrase chunks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Grammar Structure](#grammar-structure)
- [Functionality](#functionality)

## Installation

To run this project, you need to have Python 3 and the `nltk` library installed. You can install the required library using pip:

```bash
pip install nltk
```

## Usage
To run the program, use the following command:
```bash
python parser.py
```
- **filename** (optional): Path to a text file containing a sentence. If no filename is provided, the program will prompt you to input a sentence.  
The program will parse the input sentence and print the parse tree along with the identified noun phrase chunks.

## Grammar Structure

The grammar used for parsing is defined in two parts: **Terminals** and **Nonterminals**.

### Terminals

The terminals include various parts of speech such as adjectives, adverbs, conjunctions, determiners, nouns, prepositions, and verbs.

### Nonterminals

The nonterminals define the structure of sentences, noun phrases, verb phrases, and adjective phrases.

## Functionality

- **Preprocessing**: The input sentence is tokenized, converted to lowercase, and cleaned to remove non-alphabetic words.
- **Parsing**: The program uses a chart parser to parse the input sentence based on the defined grammar.
- **Noun Phrase Chunking**: The program identifies and extracts noun phrase chunks from the parsed tree.