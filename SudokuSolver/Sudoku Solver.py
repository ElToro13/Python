class Mul():
    def combine(self, A, B):
        "Combines the elements of two given arrays."
        return [a + b for a in A for b in B]


class SudokuSolver(Mul):

    def __init__(self, grid=''):
        self.numbers = '123456789'
        self.characters = 'ABCDEFGHI'
        self.cols = self.numbers
        comb = Mul()
        self.squares = comb.combine(self.characters, self.cols)

        self.Total = ([comb.combine(self.characters, c) for c in self.cols] +
                      [comb.combine(r, self.cols) for r in self.characters] +
                      [comb.combine(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

        self.belongs = dict((s, [u for u in self.Total if s in u])
                            for s in self.squares)

        self.peers = dict((s, set(sum(self.belongs[s], [])) - set([s]))
                          for s in self.squares)

    def possible_values(self, grid):
        "Lists all the possible values for a particular cell."

        values = dict((s, self.numbers) for s in self.squares)
        for s, d in self.StrToDict(grid).items():
            if d in self.numbers and not self.update(values, s, d):
                return False
        return values

    def StrToDict(self, grid):
        "Converts the given string of sudoku values into dictionary."
        values = [c for c in grid if c in self.numbers or c in '0.']
        assert len(values) == 81
        return dict(zip(self.squares, values))

    def update(self, values, s, d):
        "Keeps updating the values by elimination of other values."
        other_values = values[s].replace(d, '')
        if all(self.remove(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def remove(self, values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')

        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.remove(values, s2, d2) for s2 in self.peers[s]):
                return False

        for u in self.belongs[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:

                if not self.update(values, dplaces[0], d):
                    return False
        return values

    def solve(self, grid):
        return self.depth_first(self.possible_values(grid))

    def depth_first(self, values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False

        if all(len(values[s]) == 1 for s in self.squares):
            return values

        n, s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.selected(self.depth_first(self.update(values.copy(), s, d))
                             for d in values[s])

    def selected(self, seq):
        "Return some element of seq that is true."
        for e in seq:
            if e: return e
        return False


