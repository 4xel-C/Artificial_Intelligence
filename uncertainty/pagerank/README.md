# PageRank Algorithm Implementation

This project implements the PageRank algorithm, a method originally used by Google to rank web pages in search engine results. The implementation provides two approaches to compute the PageRank of pages in a given corpus: sampling and iterative computation.

---

## Features

- **Crawling HTML Pages**: Parses a directory of HTML files to build a representation of links between pages.
- **Transition Model**: Computes a probability distribution for transitioning between pages.
- **Sampling Method**: Estimates PageRank values by simulating random walks through the corpus.
- **Iterative Method**: Converges to the PageRank values using iterative updates.

---

## How to Run

1. Place your HTML files in a directory.
2. Run the script with the directory name as an argument:
   ```bash
   python pagerank.py corpus
    ```

## Functions Overview

### 1. `crawl(directory)`
Parses HTML files in a directory and extracts links between pages.  
**Returns**: A dictionary where keys are page names and values are sets of linked pages.

---

### 2. `transition_model(corpus, page, damping_factor)`
Computes the probability distribution over the next page to visit from the current page.  
**Parameters**:
- **`corpus`**: Dictionary of pages and their links.
- **`page`**: The current page.
- **`damping_factor`**: Probability of following a link rather than choosing randomly.

**Returns**: A dictionary with page names as keys and transition probabilities as values.

---

### 3. `sample_pagerank(corpus, damping_factor, n)`
Estimates PageRank values by simulating `n` random samples.  
**Parameters**:
- **`corpus`**: Dictionary of pages and their links.
- **`damping_factor`**: Probability of following a link.
- **`n`**: Number of samples.

**Returns**: A dictionary with page names as keys and their PageRank values as values.

---

### 4. `iterate_pagerank(corpus, damping_factor)`
Computes PageRank values iteratively until convergence.  
**Parameters**:
- **`corpus`**: Dictionary of pages and their links.
- **`damping_factor`**: Probability of following a link.

**Returns**: A dictionary with page names as keys and their PageRank values as values.

---

### 5. `is_linked(corpus, page)`
Checks if a given page is linked by any other page in the corpus.  
**Returns**: `True` if the page is linked, `False` otherwise.

---

## Constants

- **`DAMPING = 0.85`**: The damping factor used in the PageRank algorithm.
- **`SAMPLES = 10000`**: Number of samples for the sampling method.

---

## Example Output

After running the script, you will see the PageRank values computed using both the sampling and iterative methods:

```plaintext
PageRank Results from Sampling (n = 10000)
  1.html: 0.2723
  2.html: 0.3948
  3.html: 0.3329

PageRank Results from Iteration
  1.html: 0.2731
  2.html: 0.3937
  3.html: 0.3332
```

## Requirements

- Python >= 3.12