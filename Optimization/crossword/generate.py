import sys

from crossword import *  


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)  # noqa: F405
                j = variable.j + (k if direction == Variable.ACROSS else 0)  # noqa: F405
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # iterate in all items inside domains, and compare the length of each variable with all the words.
        for var, words in self.domains.items():
            word_list = []
            for word in words:
                if var.length != len(word):
                    word_list.append(word)
            for w in word_list:
                self.domains[var].remove(w)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """       
        # return False if there is no overlap
        if x == y:
            return False

        if not self.crossword.overlaps[x, y]:
            return False

        # if x and y overlap on the ith character of x and jth charater of y        
        i, j = self.crossword.overlaps[x, y]
 
        # keep track of word to remove
        word_list = []

        # for each word in x, check 
        for word_x in self.domains[x]:
            found_match = False
            for word_y in self.domains[y]:
                
                # if there is a possible match, break and repeat to the next x words.
                if word_x[i] == word_y[j]:
                    found_match = True
                    break
            
            if not found_match:
                word_list.append(word_x)
        
        for word in word_list:
            self.domains[x].remove(word)

        return True if word_list else False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            # initialize arcs as an empty list; will store arcs as tupple (x, y) where x and y are variables
            arcs = []
            for var in self.domains:
                neighbors = self.crossword.neighbors(var)
                for neighbor in neighbors:
                    arcs.append((var, neighbor))
        
        while arcs:
            
            # take the first element from the queue
            x, y = arcs.pop(0)
            
            # try to revise the arc, and if it's revised, append all the arcs connected to it to the queues
            if self.revise(x, y):
                
                # if a domain happens to be empty => Wrong solution => return False
                if not self.domains[x]:
                    return False 
                neighbors = self.crossword.neighbors(x)
                for neighbor in neighbors:
                    if neighbor != y:
                        arcs.append((neighbor, x))
                        
        # return True if all arcs consistency are inforced
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # compare the number of variable with the number of assignment and ensure that all variable in the domains are in the assigned dictionnary.
        if len(self.domains) != len(assignment) or not all([var in assignment for var in self.domains]):
            return False
        
        # ensure that all variables are assigned:
        for var in assignment:
            if not assignment[var]:
                return False
        
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for var in assignment:
            
            # check length of assignment
            if var.length != len(assignment[var]):
                return False
            
            # check neighbors of each var in the assignement 
            neighbors = self.crossword.neighbors(var)
            for neighbor in neighbors:
                if neighbor in assignment:
                    i, j = self.crossword.overlaps[var, neighbor]
                    if assignment[var][i] != assignment[neighbor][j]:
                        return False
        
        # Return True if no problem  
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # Initialize a dictionnary to keep track of all possible values in the domain and how many time each conflict to their neighbor
        value_count = {word: 0 for word in self.domains[var]}
        
        # find all neighbors
        neighbors = self.crossword.neighbors(var)

        # check for each word of the domain var, how many times it conflicts with the potential words of the neighbors (overlaping variable)
        for word_x in self.domains[var]:
            for neighbor in neighbors:

                # if the considered neighbor is already assigned, continu to the next value
                if neighbor in assignment:
                    continue

                # check each word of the other variable and count the conflict
                i, j = self.crossword.overlaps[var, neighbor]
                for word_y in self.domains[neighbor]:
                    if word_x[i] != word_y[j]:
                        value_count[word_x] += 1
        
        # create a sorted list of all possible value, sorted by the lowest count of conflicts
        sorted_values = [word for word, _ in sorted(value_count.items(), key=lambda item: item[1])]
        return sorted_values
    
    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Recuperated variables not assigned:
        var_list = [var for var in self.domains if var not in assignment]

        # sort the list by minimum values heuristic, and if equal domains, sort by descending number of neighbor
        var_list.sort(key=lambda x: (len(self.domains[x]), -len(self.crossword.neighbors(x))))
        return var_list[0] if var_list else None

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        
        # Select heuristicly a variable and a value in the domains (variable with the least variable and the most neighbors)
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            
            # Create a copy of the original domains to restore if inferences made on a wrong variable
            original_domain = self.domains.copy()

            # Domain should be modified here to only contain the value assigned for the variable, so it's taken into consideration while doing the AC3 algorithm
            
            # Use ac3 algorithm on all neighbor Y of X to make inference on the domains if possible
            # if ac3 leads to a domain with only 1 value possible, the heuristic selection in the backtrack function will automaticly pick it on the next iteration
            self.ac3(arcs=[(neighbor, var) for neighbor in self.crossword.neighbors(var)])
            
            # if there is no empty domains (impossible) and asignment consistant: 
            if all(len(self.domains[neighbor]) > 0 for neighbor in self.crossword.neighbors(var)):
                if self.consistent(new_assignment):
                    result = self.backtrack(new_assignment)
                    if result is not None:
                        return result
                
            # If the new_assignement is not consistent, restore original domain
            self.domains = original_domain
            
        # return None if no solution possibles
        return None
                
def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)  # noqa: F405
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)

if __name__ == "__main__":
    main()
