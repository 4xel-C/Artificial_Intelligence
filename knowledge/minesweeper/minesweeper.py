import itertools
import random


class Minesweeper:
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence:
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    A sentence is generated each time a cell is uncovered
        => It will give the number of mines in the adjacent cell
        => And which cells are concerned by this number of mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if not self.count:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI:
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # update moves_made variable
        self.moves_made.add(cell)
        # mark the cell as safe (update self.safes and update all sentences with the safe cell)
        self.mark_safe(cell)

        # Generate a new sentence from the move and add it to the KB:
        #   -Give the count of mines of the proximate cells
        #   -Give the coordinate of al the cell concerned by the count
        set_cells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself of if the cell safe
                if (i, j) == cell or (i, j) in self.safes:
                    continue

                # if mine already detected, reduce the count and ignore the cell
                if (i, j) in self.mines:
                    count -= 1
                    continue

                # Add the cell to the new set for the sentence if within the range of the game board.
                if 0 <= i < self.height and 0 <= j < self.width:
                    set_cells.add((i, j))

        # adding new sentence to the knowledge
        self.knowledge.append(Sentence(set_cells, count))


        # Update the knowledge base if new inferences can be made from the additional informations
        #   ->If new information, update the KB and loop through all sentances to mark the safe or the mines to simplify each sentences.
        #   ->loop again until no inference can be made 
        kb_changed = True
        while kb_changed:
            kb_changed = False

            safes = set()
            mines = set()

            # Get all the safe and mine cells that can be concluded in the KB
            for sentence in self.knowledge:
                safes = safes | sentence.known_safes()
                mines = mines | sentence.known_mines()

            # Mark any safes:
            if safes:
                kb_changed = True
                for safe in safes:
                    self.mark_safe(safe)
            if mines:
                kb_changed = True
                for mine in mines:
                    self.mark_mine(mine)

            # Addition of new sentences that can be inferred from existing knowledge afer each sentences have been simplified
            for sentences in itertools.permutations(self.knowledge, 2):
                
                # Check if first sentence's cells is a subset of the other sentence
                if sentences[0].cells < sentences[1].cells:
                    # Create a new sentence infered by one sentence's cell beeing a subset of another.
                    new_sentence = Sentence(
                        (sentences[1].cells - sentences[0].cells),
                        (sentences[1].count - sentences[0].count),
                    )
                    if new_sentence not in self.knowledge:
                        kb_changed = True
                        self.knowledge.append(new_sentence)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        possible_safe_moves = set()
        possible_safe_moves = self.safes.copy()
        possible_safe_moves -= self.moves_made
        if possible_safe_moves:
            return random.choice(list(possible_safe_moves))
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        possibles_moves = set()
        for i in range(self.height):
            for j in range(self.width):
                possibles_moves.add((i, j))

        # get rid of already visited cells and mined cells:
        possibles_moves -= self.moves_made
        possibles_moves -= self.mines
        return random.choice(list(possibles_moves))
