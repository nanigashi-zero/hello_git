print("hello Github")
print("good night")

i = 4
j = 4

#内包表記で二次元配列tetrisを定義
tetris = [['' for count_1 in range (4)] for count_2 in range(i)]

#tetris 4×4行列の値初期化
for a in range(i):
    for b in range(j):
        tetris[a][b] = '1'

#tetris 行列内の文字列表示
for a in range(i):
    tetris_array = ''
    for b in range(j):
        tetris_array += tetris[a][b]
    print(tetris_array)
        