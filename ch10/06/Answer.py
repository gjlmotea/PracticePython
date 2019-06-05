operation_symbol_dict={'+','-','*','/'}

symbol_dict={
'0':['****','*  *','*  *','*  *','****'],
'1':['  * ',' ** ','  * ','  * ',' ***'],
'2':[' ** ','*  *','  * ',' *  ','****'],
'3':['****','   *',' ***','   *','****'],
'4':['*  *','*  *','****','   *','   *'],
'5':['****','*   ','****','   *','****'],
'6':['****','*   ','****','*  *','****'],
'7':['****','   *','  * ',' *  ','*   '],
'8':['****','*  *','****','*  *','****'],
'9':['****','*  *','****','   *','****']
}


operation = input("請輸入任一正整數:\n")

operation_list = []

for symbol in operation:
    operation_list.append(symbol)

operation_symbol_list_0 = []
operation_symbol_list_1 = []
operation_symbol_list_2 = []
operation_symbol_list_3 = []
operation_symbol_list_4 = []
## 這邊用5個list，每個lis儲存 運算式 "一行的符號" 
for symbol in operation_list:
    operation_symbol_list_0.append(symbol_dict [str(symbol)] [0])
    operation_symbol_list_1.append(symbol_dict [str(symbol)] [1])
    operation_symbol_list_2.append(symbol_dict [str(symbol)] [2])
    operation_symbol_list_3.append(symbol_dict [str(symbol)] [3])
    operation_symbol_list_4.append(symbol_dict [str(symbol)] [4])

print(*operation_symbol_list_0, sep=' ')
print(*operation_symbol_list_1, sep=' ')
print(*operation_symbol_list_2, sep=' ')
print(*operation_symbol_list_3, sep=' ')
print(*operation_symbol_list_4, sep=' ')



