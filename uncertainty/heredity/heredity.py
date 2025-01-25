import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):
                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # Set the joint probability of this world to 1
    joint_probability = 1
    
    # iterate over each people to calculate their probability to represent the state of the world
    for person in people:
        
        # Initialize the probability of a person beeing in this state 
        individual_probability = 1
        
        # Recuparating data of interest
        trait = True if person in have_trait else False
        gene = 1 if person in one_gene else 2 if person in two_genes else 0
        mother = people[person]["mother"]
        father = people[person]["father"]
        
        # compute probability of having gene
        if not mother or not father:
            individual_probability *= PROBS["gene"][gene]
        else:
            # creating a dictionnary to save the probability of having the gene from the mother and the father
            prob_heredity = dict()
            
            # compute the probability of having the gene from the mother
            if mother in one_gene:
                prob_heredity[mother] = 0.5
            elif mother in two_genes:
                prob_heredity[mother] = 1 - PROBS["mutation"]
            else:
                prob_heredity[mother] = PROBS["mutation"]
              
            # compute probability of having the gene from the father
            if father in one_gene:
                prob_heredity[father] = 0.5
            elif father in two_genes:
                prob_heredity[father] = 1 - PROBS["mutation"]
            else:
                prob_heredity[father] = PROBS["mutation"]
            
            # computing probability of having 0, 1 or 2 genes:
            two_genes_probs = prob_heredity[father] * prob_heredity[mother]
            one_gene_prob = (prob_heredity[father] * (1-prob_heredity[mother])) + (prob_heredity[mother] * (1-prob_heredity[father]))
            zero_gene_prob = (1-prob_heredity[mother]) * (1-prob_heredity[father])
            if gene == 2:
                individual_probability *= two_genes_probs
            elif gene == 1:
                individual_probability *= one_gene_prob
            else:
                individual_probability *= zero_gene_prob
        
        # trait probability
        if person in have_trait:
            individual_probability *= PROBS['trait'][gene][True]
        else:
            individual_probability *= PROBS['trait'][gene][False]
        
        # Multiply the individual probability with the joint probability for each person 
        joint_probability *= individual_probability

    return joint_probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        
        # recuperate person information
        gene = 1 if person in one_gene else 2 if person in two_genes else 0
        trait = person in have_trait
        
        # update gene and trait with the probability of this specific world (addition of all world (path) possible to have the global probability)
        probabilities[person]["gene"][gene] += p
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # iterate over each person in probabilities
    for person in probabilities:
        
        # Calculate the normalization factor 
        factor_gene = 1 /sum(probabilities[person]["gene"].values())
        factor_trait = 1 /sum(probabilities[person]["gene"].values())
        
        for gene in probabilities[person]["gene"]:
            probabilities[person]["gene"][gene] *= factor_gene
        
        for trait in probabilities[person]["trait"]:
            probabilities[person]["trait"][trait] *= factor_trait        
            

if __name__ == "__main__":
    main()
