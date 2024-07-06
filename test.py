import csv

from dms.models import Cell, Bookshelf


def write_csv(filename, bookshelf):
	with open(filename, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			Cell.objects.create(bookshelf=bookshelf, name=row['name'])