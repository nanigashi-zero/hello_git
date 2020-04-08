print("hello Github")
print("good night")

#テトリスボードの初期化をメソッド化
def init_board():
    i = 10 #縦
    j = 10 #横

    #内包表記で二次元配列tetrisを定義
    tetris = [['' for count_1 in range(j)] for count_2 in range(i)]

    #tetris 4×4行列の値初期化
    for a in range(i):
        for b in range(j):
            tetris[a][b] = '0'

    #tetris 行列内の文字列表示
    for a in range(i):
        tetris_array = ''
        for b in range(j):
            tetris_array += tetris[a][b]
        print(tetris_array)

#テトリスブロックを配列として保存する関数        
def init_tetrisblock():

    #tetrisblockに回転する分を含めたテトリスブロックを保存する
    tetrisblock = [
            # i
            [[[1, i] for i in range(4)],
             [[i, 1] for i in range(4)]] * 2,
            # o
            [[[0, 0], [0, 1], [1, 0], [1, 1]]] * 4,
            # t
            [[[0, 1]] + [[1, i] for i in range(3)],
             [[1, 2]] + [[i, 1] for i in range(3)],
             [[2, 1]] + [[1, i] for i in range(3)],
             [[1, 0]] + [[i, 1] for i in range(3)]],
            # j
            [[[0, 0]] + [[1, i] for i in range(3)],
             [[0, 2]] + [[i, 1] for i in range(3)],
             [[2, 2]] + [[1, i] for i in range(3)],
             [[2, 0]] + [[i, 1] for i in range(3)]],
            # l
            [[[0, 2]] + [[1, i] for i in range(3)],
             [[2, 2]] + [[i, 1] for i in range(3)],
             [[2, 0]] + [[1, i] for i in range(3)],
             [[0, 0]] + [[i, 1] for i in range(3)]],
            # s
            [[[0, 1], [0, 2], [1, 0], [1, 1]],
             [[0, 0], [1, 0], [1, 1], [2, 1]]] * 2,
            # z
            [[[0, 0], [0, 1], [1, 1], [1, 2]],
             [[0, 1], [1, 0], [1, 1], [2, 0]]] * 2
        ]
    #init_tetrisblockを実行した場合tetrisblockを返り血とする
    return tetrisblock

init_board()     

a = init_tetrisblock()
print(a)