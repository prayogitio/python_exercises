color_list = ["Blue", "Yellow", "Green", "Red"] #list
print(color_list[1])
color_list[3] = "Brown"
print(color_list)
print(len(color_list))
print(color_list[0:3])
color_list.insert(1, "Orange")
print(color_list)
color_list.append("Purple")
print(color_list)

color_dict = {'one':'blue', 'two':'yellow'} #dictionary
print(color_dict['one'])
print(color_dict.keys())
print(color_dict.values())

x = [100,200,300,400,500,600]
for y in x:
	print(x[3])

test = input("input your number: ")
test_num = int(test)
while (test_num > 0):
	print(test_num)
	test_num -= 1;

test_string = str(test_num)
print(test_string + "ladklasjdf")