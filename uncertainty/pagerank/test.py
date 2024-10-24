import random

corpus = {"1.html": {"2.html"}, "2.html": {"3.html", "1.html"}, "3.html": {"2.html"}}

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
            distribution[p] = (damping_factor*(1/len(links))) + ((1 - damping_factor) * (1 / len(corpus)))
        
        # if not present in the links of the page, it can only be chosen randomly
        else:
            distribution[p] = ((1 - damping_factor) * (1 / len(corpus)))
    
    return distribution

distribution = {'1.html': 0.05, '2.html': 0.475, '3.html': 0.475}
poids = distribution.values()

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    # initialize the dictionnary that will count how many pages will be visited
    pages_rank = dict()
    
    # initialize a dictionnary that will keep in memory distribution probability of a page to avoid computing multiples times the same page.
    distributions = dict()
    
    # choose the first page randomly and add it to the pagerank dict.
    page = random.choice(list(corpus))
    pages_rank[page] = 1
    
    # generate a sample of size n
    for i in range(n):
        if page not in distributions:
            distributions[page] = transition_model(corpus, page, damping_factor)
            
        # select randomly a page from the probability distribution and update the current page
        page = random.choices(list(distributions[page]), weights = list(distributions[page].values()), k=1)[0]
        
        # Add 1 to the pages_rank dictionnary, if the page does not exist, initialize the key to a value of 0
        pages_rank[page] = pages_rank.get(page, 0) + 1
    
    # divide the count of each page by the size of the sample to give their probability
    for p in pages_rank:
        pages_rank[p] /= n
    
    return pages_rank

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

    # loop until precision is enough
    stop = False
    while stop == False:
        # comparing old_page_ranks to new
        old_page_ranks = page_ranks.copy()
        
        # Computing page_rank calculation for each page
        for page in corpus:
            
            # calculating the chance to be selected randomly by the damping factor
            page_ranks[page] = (1 - damping_factor) / n
            
            # summing the probability of beeing accessed from another page
            for other_page in corpus:
                if page in corpus[other_page] and other_page != page:
                    page_ranks[page] += damping_factor*(page_ranks[other_page]/len(corpus[other_page]))
        
        # if too much variation, continue the whole loop, if all values does not variate: set stop to True and break the while loop
        for page in page_ranks:
            if not old_page_ranks[page] - 0.001 <= page_ranks[page] <= old_page_ranks[page] + 0.001:
                break
            stop = True
    
    return page_ranks

ranks = iterate_pagerank(corpus, 0.85)

print(sum(ranks.values()))