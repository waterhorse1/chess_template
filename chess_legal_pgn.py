import pickle as pkl

def get_pgn(san_list):
    pgn = ""
    for idx, san in enumerate(san_list):
        if idx % 2 == 0:
            pgn += f"{idx//2+1}. {san}"
        else:
            pgn += f" {san} "
    return pgn

import numpy as np

def legal_move_all_fen2san(game, step=0):
    legal_move_all_dict = {}
    length = 0 
    for move in game.mainline_moves():
        length += 1
    if length <=3:
        size = 1
    else:
        size = 2
    step = np.random.choice(list(range(length)), size=size, replace=False)
    length = 0 
    moves = []
    board = game.board()
    legal_moves = list(board.legal_moves)
    legal_moves_san = [board.san(move) for move in legal_moves]
    legal_moves = [str(lm) for lm in legal_moves_san]
    legal_move_all_dict[board.fen()] = legal_moves
    for move in game.mainline_moves():
        moves.append(move)
        if len(moves)-1 in step:
            legal_moves = list(board.legal_moves)
            legal_moves_san = [board.san(move) for move in legal_moves]
            legal_moves = [str(lm) for lm in legal_moves_san]
            legal_move_all_dict[board.fen()] = legal_moves
        board.push(move)
        length += 1
    return legal_move_all_dict

def legal_move_all_pgn2uci(game, step=0):
    legal_move_all_dict = {}
    length = 0 
    for move in game.mainline_moves():
        length += 1
    if length <=3:
        size = 1
    else:
        size = 2
    step = np.random.choice(list(range(length)), size=size, replace=False)
    length = 0 
    moves = []
    board = game.board()
    legal_moves = list(board.legal_moves)
    legal_moves_san = [board.san(move) for move in legal_moves]
    legal_moves = [str(lm) for lm in legal_moves_san]
    legal_move_all_dict[board.fen()] = legal_moves
    for move in game.mainline_moves():
        moves.append(board.san(move))
        if len(moves)-1 in step:
            legal_moves = list(board.legal_moves)
            legal_moves = [str(lm) for lm in legal_moves]
            legal_move_all_dict[get_pgn(moves)] = legal_moves
        board.push(move)
        length += 1
    return legal_move_all_dict

def legal_move_all_pgn2san(game, step=0):
    legal_move_all_dict = {}
    length = 0 
    for move in game.mainline_moves():
        length += 1
    if length <=3:
        size = 1
    else:
        size = 2
    step = np.random.choice(list(range(length)), size=size, replace=False)
    length = 0 
    moves = []
    board = game.board()
    legal_moves = list(board.legal_moves)
    legal_moves_san = [board.san(move) for move in legal_moves]
    legal_moves = [str(lm) for lm in legal_moves_san]
    legal_move_all_dict[board.fen()] = legal_moves
    for move in game.mainline_moves():
        moves.append(board.san(move))
        if len(moves)-1 in step:
            legal_moves = list(board.legal_moves)
            legal_moves_san = [board.san(move) for move in legal_moves]
            legal_moves = [str(lm) for lm in legal_moves_san]
            legal_move_all_dict[get_pgn(moves)] = legal_moves
        board.push(move)
        length += 1
    return legal_move_all_dict

all_games = pkl.load(open('./games.pkl', 'rb'))
all_dict = {}
for idx, g in enumerate(all_games):
    print(idx)
    try:
        dict = legal_move_all_pgn2uci(g)
        all_dict.update(dict)
    except Exception as e:
        print(e)

pkl.dump(all_dict, open('./legal_uci_pgn.pkl', 'wb'))