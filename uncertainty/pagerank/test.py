import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.

    Return a dictionnary containing the chance to choose each page from an actual page.
    """
    distribution = dict()

    # fetch the pages name linked in the actual page
    links = corpus[page]

    for p in corpus:
        if p in links:

            # if page present in links, probability to be selected is probality to be clicked on the link + probability of beeing randomly chosen
            distribution[p] = (damping_factor*(1/len(links))) + \
                ((1 - damping_factor) * (1 / len(corpus)))

        # if not present in the links of the page, it can only be chosen randomly
        else:
            distribution[p] = ((1 - damping_factor) * (1 / len(corpus)))

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # initialize the dictionnary that will count how many pages will be visited
    page_ranks = dict()

    # initialize a dictionnary that will keep in memory distribution probability of a page to avoid computing multiples times the same page.
    distributions = dict()

    # choose the first page randomly and add it to the pagerank dict.
    page = random.choice(list(corpus))
    page_ranks[page] = 1

    # generate a sample of size n
    for i in range(n):
        if page not in distributions:
            distributions[page] = transition_model(corpus, page, damping_factor)

        # select randomly a page from the probability distribution and update the current page
        page = random.choices(list(distributions[page]), weights=list(
            distributions[page].values()), k=1)[0]

        # Add 1 to the page_ranks dictionnary, if the page does not exist, initialize the key to a value of 0
        page_ranks[page] = page_ranks.get(page, 0) + 1

    # divide the count of each page by the size of the sample to give their probability
    for p in page_ranks:
        page_ranks[p] /= n

    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # saving the number of pages in a variable to avoid calculating the len multiple time
    n = len(corpus)

    # initialization of starting page ranks as all equals
    page_ranks = {page: (1/n) for page in corpus}
    new_ranks = {page: None for page in corpus}

    # loop until precision is enough
    stop = False
    while not stop:

        # Computing page_rank calculation for each page
        for page in corpus:

            # calculating the chance to be selected randomly by the damping factor
            new_ranks[page] = (1 - damping_factor) / n

            # summing the probability of beeing accessed from another page
            sigma = 0
            for other_page in corpus:
                # if page has no link, equal probability among the other pages
                if len(corpus[other_page]) == 0:
                    sigma += page_ranks[other_page]/n
                elif page in corpus[other_page]:
                    sigma += page_ranks[other_page]/len(corpus[other_page])
            new_ranks[page] += damping_factor * sigma

        # Normalizing probabilities to 1
        factor = sum(page_ranks.values())
        page_ranks = {page: (rank / factor) for page, rank in page_ranks.items()}

        # check variations of each page, if one still vary too much,  start the loop again
        stop = True
        for page in page_ranks:
            if abs(new_ranks[page] - page_ranks[page]) >= 0.001:
                stop = False  # Si une page n'a pas convergé, on continue
                break
        
        # update the ranks with the new values
        page_ranks = new_ranks.copy()

    return page_ranks


if __name__ == "__main__":
    main()
