symbol_dict={
'0':['0000','0  0','0  0','0  0','0000'],
'1':['  1 ',' 11 ','  1 ','  1 ',' 111'],
'2':[' 22 ','2  2','  2 ',' 2  ','2222'],
'3':['3333','   3',' 333','   3','3333'],
'4':['4  4','4  4','4444','   4','   4'],
'5':['5555','5   ','5555','   5','5555'],
'6':['6666','6   ','6666','6  6','6666'],
'7':['7777','   7','  7 ',' 7  ','7   '],
'8':['8888','8  8','8888','8  8','8888'],
'9':['9999','9  9','9999','   9','9999']
}


input_digit = input("請輸入0~9: \n")
print("\n\n\n")

digit_symbol_list_0 = []
digit_symbol_list_1 = []
digit_symbol_list_2 = []
digit_symbol_list_3 = []
digit_symbol_list_4 = []


for i in range(5):
    for l in range(int(input_digit)):
        for j in range(4):
            for k in range(int(input_digit)):
                print(symbol_dict [str(input_digit)] [i][j], end='')
        print()
