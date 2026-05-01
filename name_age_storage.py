import datetime
import json
import os

path = 'data1.json'


def check():
	if not os.path.exists(path):
		with open(path, 'w') as file:
			file.write('[]')


def add():
	with open(path, 'r') as file:
		data = json.load(file)

	name = input('\nEnter Name: ')
	age = input('Enter Age: ')
	info = {"name": name, "age": age}

	data.append(info)

	with open(path, 'w') as file:
		json.dump(data, file, indent=4)
		print('Added Successfully!')


def view():
	with open(path, 'r') as file:
		data = json.load(file)

	for el in data:
		print()
		for key, value in el.items():
				print(f'{key} - {value}')


def main():
	while True:
		check()
		print('\n================')
		print('  DATA PROGRAM')
		print('================')
		print('1. Add Entry')
		print('2. View Entries')
		print('3. Exit')
		print('================')

		inp = input('Enter Choice: ')

		if inp == '1':
			add()

		elif inp == '2':
			view()

		elif inp == '3':
			print('\nExiting...')
			break

		else:
				print('\nInvalid Input!')


main()

