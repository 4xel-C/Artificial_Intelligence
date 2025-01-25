# Genetic Inheritance Probability Simulation

This program calculates the probabilities of gene inheritance and trait expression in a population based on genetic data. It simulates different genetic scenarios, including various combinations of gene copies (0, 1, or 2) and whether or not individuals exhibit a particular trait. The results provide a probabilistic model of the genetic inheritance process, useful for understanding patterns of inheritance in genetics.

## Requirements

- Python 3.x
- Required libraries:
  - `csv`
  - `itertools`
  - `sys`

## Usage

1. Prepare a CSV file containing the following fields for each person:
   - `name`: The name of the individual.
   - `mother`: The name of the individual's mother (or leave blank if unknown).
   - `father`: The name of the individual's father (or leave blank if unknown).
   - `trait`: A value of `1` if the person exhibits the trait, `0` if not, or leave blank if unknown.

2. Run the script with the CSV file as an argument:

   ```bash
   python heredity.py data.csv
   ```
- Replace data.csv for your data file (exemple in the folder [data](/uncertainty/heredity/data/))

### Functions

#### `load_data(filename)`
Loads gene and trait data from the provided CSV file into a dictionary. The dictionary contains information about each person's name, parents, and whether they exhibit the trait.

#### `powerset(s)`
Returns a list of all possible subsets of a given set `s`. This is used to generate all possible combinations of people who might have the gene or trait.

#### `joint_probability(people, one_gene, two_genes, have_trait)`
Calculates the joint probability of a specific set of people having certain numbers of gene copies (0, 1, or 2) and exhibiting or not exhibiting the trait. This function takes into account the probability of inheritance from the parents and the mutation rate.

#### `update(probabilities, one_gene, two_genes, have_trait, p)`
Updates the probability distributions for each person based on a new joint probability `p`. The distributions are updated for both the gene (0, 1, or 2 copies) and the trait (True or False).

#### `normalize(probabilities)`
Normalizes the probability distributions so that the total probability for each person sums to 1. This ensures that the distributions are valid and consistent.

