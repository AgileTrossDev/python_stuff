Just a sliding window operation for iterable objects..


my_list = [1, 2, 3,4,5,6,7,8,9,0]
for i in my_list:
...     print(i)
... 
1
2
3
4
5
6
7
8
9
0
a = main.window(my_list,5)
print (a)
<generator object window at 0x7fbd8b32fd58>
for i in a:
...     print(i)
... 
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3, 4, 5, 6, 7]
[4, 5, 6, 7, 8]
[5, 6, 7, 8, 9]
[6, 7, 8, 9, 0]

