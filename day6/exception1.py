def check(list1, name):
	try:
		total = 0
		for ele in list1:
			total += int(ele)
		avg = total // len(list1)
		pwd = avg + name
		return int(pwd)
	except ValueError:
		print('Value error while check')
	except TypeError:
		print('Type error while check')
	except NameError:
		print('Name error while check')
	finally:
		print('Finally in called function')
	print('From end of inside of method')

list1 = [10, 20, 30, 40, 50, 60, '7A']
try:
	check(list1, 'ABC')
except NameError:
	print('Name error in Main')
finally:
	print('Finally in Main')