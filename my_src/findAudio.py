import requests


def find_audio(audioFile):

    data = {
        'url': 'https://audd.tech/example1.mp3',
        'return': 'apple_music,spotify',
        'api_token': 'test'
    }
    result = requests.post('https://api.audd.io/', data=data)
    print(result.text)
