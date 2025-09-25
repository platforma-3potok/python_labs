Cтудент группы БИВТ-25-8 Ищейкин Кирилл Алексеевич
# Лабараторные работы

## Лабараторная работа №1

- 1 задание
### Код
```python
Name = input('Введите имя:')
Age = int(input('Введите возраст:'))
print(f'Привет, {Name}! Через год тебе будет {Age+1}.')
```
### Вывод
![](images/lab01/image_1.png)

- 2 задание
### Код  
```python
a = int(input())
b = int(input())
sum = a + b
avg = round((a + b)/ 2, 2)
print(sum, avg, sep='; ')
```
### Вывод
![](images/lab01/image_2.png)

- 3 задание
### Код
```python
price= int(input())
discount= int(input())
vat= int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {round(base, 2)} ₽')
print(f'НДС: {round(vat_amount, 2)} ₽')
print(f'Итого к оплате: {round(total, 2)} ₽')
```
### Вывод
![](images/lab01/image_3.png)

- 4 задание
### Код  
```python
m = int(input())
h = m // 60
hm = m % 60
print(f'{h}:{hm}')
```
### Вывод
![](images/lab01/image_4.png)

- 5 задание
### Код  
```python
FCS = input()
initials = ''
len_FCS = len(FCS)
k = len_FCS - FCS.count(' ')
if FCS[0] != ' ':
	initials += FCS[0]
for i in range(1, len_FCS):
	if FCS[i] != ' ' and FCS[i-1] == ' ':
		initials += FCS[i]
print(initials)
print(k)
```
### Вывод
![](images/lab01/image_5.png)

- 6 задание
### Код  
```python
N = int(input())
list_student = []
for i in range(N):
	student = input('')
	student = student.split()
	list_student.append(student)
koch = 0
kzaoch = 0
for i in range(N):
	if list_student[i][-1] == 'True':
		format = True
	else:
		format = False
	if format:
		koch += 1
	else:
		kzaoch += 1
print(koch, kzaoch)
```
### Вывод
![](images/lab01/image_6.png)

- 7 задание
### Код  
```python
s = input()
len_s = len(s)
out_s = ''
num = '0123456789'
for i in range(len_s):
	if s[i].upper() == s[i]:
		first_ind = i
		break
for i in range(first_ind, len_s):
	if s[i] in num:
		second_ind = i + 1
		break
d = second_ind - first_ind
for i in range(first_ind, len_s, d):
	out_s += s[i]
print(out_s)
```
### Вывод
![](images/lab01/image_7.png)
## Лабараторная работа №2
