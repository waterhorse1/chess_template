import pickle as pkl
import json
import random
import multiprocessing

random.seed(42)
legal_san_fen = pkl.load(open('./legal_san_fen.pkl', 'rb'))
legal_san_pgn = pkl.load(open('./legal_san_pgn.pkl', 'rb'))
legal_uci_pgn = pkl.load(open('./legal_uci_pgn.pkl', 'rb'))

def list2str(data, description, template):
    key, value = data
    value = " ".join(value)
    content = random.sample(template, k=1)[0].format(key, value)
    data_dict = {"description": description, 'content': content}
    return data_dict

all_legal_template = [
    "Generate all legal moves for the given FEN of chess game: {}. Note that it considers the king in check situation. The legal moves are: {}.",
    "Please generate all the legal moves for the provided FEN of the chess game: {} taking into consideration that the king might be in check. The resulting moves are {}.",
    "Could you produce a list of all legal moves for the given FEN of the chess game: {} while also considering the possibility of the king being in check? The resulting moves are {}.",
    "I request you to generate all legal moves for the given FEN of the chess game: {}, taking into account the king's possible checkmate situation. The resulting moves are {}.",
    "Can you please provide me with a list of all legal moves for the given FEN of the chess game: {} while also considering the king's check condition? The resulting moves are {}.",
    "Kindly generate all legal moves for the provided FEN of the chess game: {} taking into account the possibility of the king being in check. The resulting moves are {}.",
    "Please list down all the legal moves that can be made for the provided FEN of the chess game: {} while taking the king's check situation into account. The resulting moves are {}.",
    "May I request you to generate all legal moves for the given FEN of the chess game: {} while also considering the possibility of the king being in check? The resulting moves are {}.",
    "It would be great if you could generate a list of all legal moves for the given FEN of the chess game: {} taking into consideration that the king might be in check. The resulting moves are {}.",
    "Can you generate all legal moves for the provided FEN of the chess game: {} taking into consideration that the king might be in check? The resulting moves are {}.",
    "I would appreciate it if you could generate all legal moves for the given FEN of the chess game: {} while taking into account the king's check condition. The resulting moves are {}."
]
def apply_template_san_fen(x):
    return list2str(x, "Generate all legal moves in SAN format given the board FEN", [t.replace('legal moves', 'legal moves in SAN format') for t in all_legal_template])
def apply_template_san_pgn(x):
    return list2str(x, "Generate all legal moves in SAN format given the board PGN", [t.replace('legal moves', 'legal moves in SAN format').replace('FEN', 'PGN') for t in all_legal_template])
def apply_template_uci_pgn(x):
    return list2str(x, "Generate all legal moves in UCI format given the board PGN", [t.replace('legal moves', 'legal moves in UCI format').replace('FEN', 'PGN') for t in all_legal_template])

with multiprocessing.Pool(processes=8) as pool:
    # 在多个进程中并行应用filter()函数
    legal_san_fen = list(pool.map(apply_template_san_fen, list(legal_san_fen.items())))

with multiprocessing.Pool(processes=8) as pool:
    # 在多个进程中并行应用filter()函数
    legal_san_pgn = list(pool.map(apply_template_san_pgn, list(legal_san_pgn.items())))

with multiprocessing.Pool(processes=8) as pool:
    # 在多个进程中并行应用filter()函数
    legal_uci_pgn = list(pool.map(apply_template_uci_pgn, list(legal_uci_pgn.items())))

all_data = legal_san_fen + legal_san_pgn + legal_uci_pgn

with open('./legal_more.jsonl', "w") as f:
    for item in all_data:
        json.dump(item, f)
        f.write("\n")


