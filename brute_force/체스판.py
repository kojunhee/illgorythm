compare_list1 = []
compare_list2 = []

for i in range(8):
    compare_list1.append(['B','W','B','W','B','W','B','W'])
    compare_list1.append(['W','B','W','B','W','B','W','B'])
    compare_list2.append(['W','B','W','B','W','B','W','B'])
    compare_list2.append(['B','W','B','W','B','W','B','W'])
#print(compare_list1,"\n\n\n",compare_list2)

rows, columns = map(int,input().split())

input_list = []
for i in range(rows):
    input_list.append(list(input()))

def check_list(list8):
    answer1 = 0
    answer2 = 0
    for test_row in range(8):
            for test_column in range(8):
                if list8[test_row][test_column] == compare_list1[test_row][test_column]:
                    answer1 += 1
                else:
                    answer2 += 1
    if answer1 >= answer2:
        return answer1
    else :
        return answer2

answer = 0

list8 = []

for i in range(rows-7):
    for j in range(columns-7):
        for k in range(8):
            list8.append(input_list[i:i+8][k][j:j+8])
        temp = check_list(list8)
        if answer < temp:
            answer = temp
print(answer)
        
