from urllib.request import urlopen
import json

TAG = '<script id="__NEXT_DATA__" type="application/json">'
TAG2 = '</script><noscript>'
def read_url(url):
	return urlopen(url).read().decode('utf-8')

def weekdayid(id):
	return ['', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс',][id]

def read_office_by_id(id):
	result = 'Отделение {}\n'.format(id)
	try:
		data = read_url('https://www.pochta.ru/offices/{}'.format(id))		
		lines = data.split('\n')
		for line in lines:
			if line.find(TAG) > 0:
				json_data = line[line.find(TAG)+len(TAG):-len(TAG2)]
				data = json.loads(json_data)
				result = result + data['props']['pageProps']['office']['address']['fullAddress'] + '\n'
				result = result + 'Праздники:\n'
				for day in data['props']['pageProps']['office']['holidays']:
					result = result + '{} - {}\n'.format(day['date'], weekdayid(day['weekDayId']))
				for day in data['props']['pageProps']['office']['workingHours']:
					if 'beginWorkTime' in day:
						result = result + '{}: {}-{}\n'.format(weekdayid(day['weekDayId']), day['beginWorkTime'], day['endWorkTime'])
					else:
						result = result + '{}: выходной\n'.format(weekdayid(day['weekDayId']))
	except:
		result = result + 'Ошибка!'
	return result

def tests():
	print('tests')
	for id in range(399500, 399501):
		print(read_office_by_id(id))

if __name__=='__main__':
	tests()