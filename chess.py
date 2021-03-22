import chess
import random

def evaluate_board(board):
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    #count the number of the different type of pieces for BLACK and WHITE    
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    wk = len(board.pieces(chess.KING, chess.WHITE))
    bk = len(board.pieces(chess.KING, chess.BLACK))  
    #count the relative strength of the pieces on the board    
    eval = 10*(wp-bp)+30*(wn-bn)+30*(wb-bb)+50*(wr-br)+90*(wq-bq)+900*(wk-bk)
    return eval  
        
def minimax(board, depth, maximizingPlayer):
    if depth == 0:
        return evaluate_board(board)    
    if maximizingPlayer:
        maxEval = -10000
        for move in board.legal_moves:
            board.push(move)   
            eval = minimax( board, depth-1, False)
            maxEval = max(maxEval, eval)
            board.pop()
        return maxEval
    else:
        minEval = 10000
        for move in board.legal_moves:
            board.push(move)   
            eval = minimax( board, depth-1, True)
            minEval = min(minEval, eval)
            board.pop()
        return minEval  
        
def selectmove(depth):
    bestMove = chess.Move.null()
    bestValue = -2000
    moveList = []
    for move in board.legal_moves:
        moveList.append(move)  
    random.shuffle(moveList) 
    for move in moveList:    
        board.push(move)
        boardValue = minimax(board, depth-1, True)
        if boardValue > bestValue:
            bestValue = boardValue;
            bestMove = move
        board.pop()
    return bestMove

board = chess.Board()
while not board.is_game_over():
    if board.turn:
        print('\n###############\nCOMPUTER PLAYS')
        move = selectmove(3)
        board.push(move)       
    else:
        print('\n###############\nUSER PLAYS')
        condition = True
        while condition:
            val = input('INSERT MOVE (format [a-h][1-8][a-h][1-8]) :') 
            move = chess.Move.from_uci(val)
            if move in board.legal_moves:
                board.push(move)
                condition = False
            else:
                print('MOVE NOT LEGAL !!')            
    print('###  '+str(move)+'   ###') 
    print(board)
print('\n\nResult : '+board.result())  