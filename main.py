#переменные
'''name = 'Abu Bakr'
age = 17

print(name)
print(age)

age = 3

print(age)
we
#можно использовать
user_name = 'Abu Bakr'
user_age = 16
count2 = 20'''

#нельзя использовать
'''2count = 20
user-number = 16
for = 20 #мы к нему что-то либо будем присваивать,именно строку или значение и это будет ошибка, либо мы будем использовать его как цикл for и это тоже будет ошибка
class = 20 '''#это тоже самое что и for
#это зарезервированное слово, его нельзя использовать как переменную

#разбор по пайтам 
'''num = 21            #int
num_duble = 2.16    #float
str_text = 'test'   #str
bool_value = True   #bool
number = '21'         #str'''

#print(type(num))
#print(type(num_duble))  т  
#print(type(str_text))
#print(type(bool_value))
#print(type(number))

#print( 5 + 5 ) #10
#print("1"+"6") #16 если мы складываем строки, то они просто склеиваются
#print('no'*5) #nonononono

#print("me" + "17" + "years") #это ошибка, потому что мы складываем строку и число, а это разные типы данных

'''print(int("5") + 5) #10, мы преобразовали строку в число и сложили их
print(float("3.4")*8) #27.2, мы преобразовали строку в число и умножили их
print(str(70) + '%')'''#70% мы преобразовали число в строку и склеили их
#это называется преобразование типов данных

#также есть булевских значений ,которые могут быть True или False
'''print(bool(1), bool(0)) '''#True False, 1 это True, 0 это False

#вывод(print) и ввод данных(input)
'''customer = input("what do you have?")
print('we have nothing , but we have ' + customer)

count = input("напишите число")# тоже самое int но без скобок, но лучше использовать скобки
print(int(count) + 23)'''

#у нас есть в принте строчка штука F
user_studend = 'Abu Bakr'
courese = 1
point = 4.25
print(f"student {user_studend} course {str(courese)} point {str(point)}") #это новый способ когда мы используем f и в скобках указываем переменные, которые мы хотим вывести, и они будут преобразованы в строку автоматически