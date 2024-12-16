import requests


def main():

	places = ["Лондон", "svo", "Череповец"]

	for place in places:

		url_weather = 'https://wttr.in/{0}?MnTqu&lang=ru'.format(place)
		response = requests.get(url_weather)
		response.raise_for_status()
		print(response.text)

if __name__ == '__main__':
    main()

