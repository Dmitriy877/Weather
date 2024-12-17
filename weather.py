import requests


def main():

	places = ["Лондон", "svo", "Череповец"]

	payload = {"MnTqu":"", "lang":"ru"}

	for place in places:

		weather_url = 'https://wttr.in/{0}?MnTqu&lang=ru'.format(place)
		response = requests.get(weather_url, params=payload)
		response.raise_for_status()
		print(response.text)

if __name__ == '__main__':
    main()

