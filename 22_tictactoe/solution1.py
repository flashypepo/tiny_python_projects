#!/usr/bin/env python3
"""Tic-Tac-Toe"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--state',
                        help='Board state',
                        metavar='str',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        choices='XO',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='int',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', args.state):
        parser.error(f'--state "{args.state}" must be 9 characters of ., X, O')

    if args.player and args.cell and args.state[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    state = list(args.state)
    player = args.player
    cell = args.cell

    if player and cell:
        state[cell - 1] = player

    print(format_board(state))
    winner = find_winner(state)
    print(f'{winner} has won!' if winner else 'No winner.')


# --------------------------------------------------
def format_board(state):
    """Format the board"""

    cells = [str(i) if c == '.' else c for i, c in enumerate(state, 1)]
    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        bar,
        cells_tmpl.format(*cells[:3]), bar,
        cells_tmpl.format(*cells[3:6]), bar,
        cells_tmpl.format(*cells[6:]), bar
    ])


# --------------------------------------------------
def find_winner(state):
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [state[i], state[j], state[k]]
            if combo == [player, player, player]:
                return player


# --------------------------------------------------
if __name__ == '__main__':
    main()
