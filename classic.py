"""Classic Algorithms"""

def hanoi(n):
    """HanoiTower with n disks"""
    steps = []

    def _move(disk, src, dst):
        """Move disk from src to dst"""
        steps.append(f"Move disk {disk} from {src} to {dst}")

    def _hanoi(n, src, aux, dst):
        """
        Hanoi recursive unit
        Solve problem: Move n disks from src to dst via aux.
        It can be divided into 3 steps:
        Step 1: Solve sub problem: Move n - 1 disks from src to aux via dst as aux
        Step 2: Move the nth disk from src to dst
        Step 3: Solve sub problem: Move n - 1 disks from aux to dst via src as aux
        """
        if n == 1:
            _move(n, src, dst)
        else:
            _hanoi(n - 1, src, dst, aux)
            _move(n, src, dst)
            _hanoi(n - 1, aux, src, dst)

    _hanoi(n, 'A', 'B', 'C')
    return steps


def n_queens(n):
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
