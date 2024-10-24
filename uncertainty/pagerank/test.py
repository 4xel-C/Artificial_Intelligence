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

print(transition_model({"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}, "1.html", 0.85))