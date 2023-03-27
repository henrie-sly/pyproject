my_list = [1,2,3]
my_list.append([555,12,345])
my_list.extend([234,'more_example'])
my_list.insert(2,'insert_example')
print(my_list)

my_list = [1,2,3,'example',3.132,10,30]
del my_list[5]
print(my_list)
my_list.remove('example')
print(my_list)

a = my_list.pop(1)
print('Popped Element:',a,'List Remaining:',my_list)
my_list.clear()
print(my_list)

my_list = [1,2,3,10,30,10]
print(len(my_list))
print(my_list.index(10))
print(my_list.count(10))
print(sorted(my_list))
my_list.sort(reverse=True)
print(my_list)

my_dict = {}
print(my_dict)

my_dict = dict()
print(my_dict)

my_dict = {1:'Python',2:'Java'}
print(my_dict)

my_dict = {'First':'Python','Second':'Java','Third':'Ruby'}

my_tuple = (1,2,3)
my_tuple1 = my_tuple + (1,4,5,6,)
print(my_tuple1)
print(my_tuple)

my_set = set()
print(type(my_set))
