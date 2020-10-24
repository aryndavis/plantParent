import requests


def find_audio(audioFile):

    data = {
        'url': 'https://audd.tech/example1.mp3',  # fake link, will need to fix
        'return': 'apple_music,spotify',
        'api_token': 'test'  # api
    }
    result = requests.post('https://api.audd.io/', data=data)
    print(result.text, result.json()['status'])
    if result.status_code == 200 and result.json()['status'] == 'success':
        return result.json()
    elif result.json()['status'] != 'success':
        return 'error'


def print_audio_nice(results):

    sentence = ''
    if results == 404 or results == 'error':
        raise ValueError("this request didn't go through correctly")

    artist = results['result']['artist']
    title = results['result']['title']
    album = results['result']['album']
    print(f"The song is {title} by {artist} on the album {album}")
    sentence = "The song is " + title
    sentence += " by " + artist
    sentence += " on the album " + album
    return sentence

# results = find_audio('output.wav')
# print_audio_nice(results)
