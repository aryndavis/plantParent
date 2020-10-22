import requests


def find_audio(audioFile):

    data = {
        'url': 'audioFile',
        'return': 'apple_music,spotify',
        'api_token': 'test'
    }
    result = requests.post('https://api.audd.io/', data=data)
    print(result.text)


find_audio('output.wav')
