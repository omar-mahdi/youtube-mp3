import requests
import webbrowser

API_KEY = ''


def search(query):
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=10&q={}&key={}'.format(
        query, API_KEY)
    request = requests.get(url)
    results = request.json()['items']
    output = ''
    for item in results:
        output += '{} {}\n'.format(str(results.index(item) + 1),
                                   item['snippet']['title'])
    print(output)
    selection = input('Choose a song number: ')
    selection = int(selection) - 1
    return results[selection]['id']['videoId']


def getLink(id):
    url = 'https://www.download-mp3-youtube.com/api/?api_key=NDY1OTg3NDk0&format=mp3&video_id={}'.format(
        id)
    request = requests.get(url)
    webbrowser.open(url)


def init():
    while True:
        selectedSong = input('Search for: ')
        getLink(search(selectedSong))
        answer = input('Do you want to search again? Y/N: ')
        if answer.lower() == 'n':
            break


init()
