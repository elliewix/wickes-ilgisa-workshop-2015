import csv

with open('illinoisjeopardy.csv', 'rt') as fin:
	fin = csv.reader(fin)
	headers = next(fin)
	data = [r for r in fin]

print headers

occ = headers.index('occ')
soc = headers.index('SOC')
main = headers.index('main')
sub = headers.index('sub')

drops = [occ, soc, main, sub]

for each in drops[::-1]:
	headers.pop(each)

print headers

newrows = []

for row in data:
	for each in drops[::-1]:
		row.pop(each)
	if row[-1] == '':
		row[-1] == 'FALSE'
	newrows.append(row)

print newrows[:10]

with open('jeopardysmallillinois.csv', 'wt') as fout:
	fout = csv.writer(fout)
	fout.writerow(headers)
	fout.writerows(newrows)