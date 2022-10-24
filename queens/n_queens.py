"""N Queen Problem"""

def n_queens_01(n):
    """N queens backtrace with DP"""
    solves = []
    # Marks unavailable cols, diags and anti_diags
    cols = [False] * n
    diags = [False] * (2 * n - 1)
    anti_diags = [False] * (2 * n - 1)

    def _cell_to_diag(row, col):
        """The first diag is on top left"""
        return row + col

    def _cell_to_anti_diag(row, col):
        """The first anti_diag is on bottem left"""
        return n - row + col - 1

    def _queen(row, solve):
        """
        Test every col of current row.
        Add valid  to current solve then find cols in the next row.
        """
        if row > n - 1:
            solves.append(solve)
            return
        for col in range(n):
            idx1 = _cell_to_diag(row, col)
            idx2 = _cell_to_anti_diag(row, col)
            if not cols[col] and not diags[idx1] and not anti_diags[idx2]:
                # Drop a queen on i-th row then mark col, diag and anti_diag
                cols[col] = diags[idx1] = anti_diags[idx2] = True
                _queen(row + 1, solve + [col])
                # Revert col, diag and anti_diag when tracing-back
                cols[col] = diags[idx1] = anti_diags[idx2] = False

    _queen(0, [])
    return solves


def n_queens_02(n):
    """N queens backtrace with DP"""

    def _queen(n, i, a, b, c):
        if i == n:
            yield a
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from _queen(n, i + 1, a + [j], b + [i + j], c + [i - j])
    
    return [solve for solve in _queen(n, 0, [], [], [])]
