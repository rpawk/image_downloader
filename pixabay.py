from util import requests_get


class Pixabay():
    """
    https://pixabay.com/api/docs/
    """
    def __init__(self, api_key, verbose=True):
        self.api_key = api_key
        self.name = 'Pixabay'
        self.verbose = verbose

    def _get_params_video(self, query, num, update_params={}):
        params = {
            'key': self.api_key,
            'q': query,
            'video_type': 'film',
            'orientation': 'horizontal',
            'safesearch': 'true',
            'per_page': num
        }
        params.update(update_params)
        return params

    def get_video(self, query, num=10, params={}):
        BASE_URL = 'https://pixabay.com/api/videos/'
        _params = self._get_params_video(query, num, params)
        response = requests_get(BASE_URL, params=_params)

        data = response.json()
        hits = data['hits']
        for i, hit in enumerate(hits):
            if self.verbose:
                print(f"  Downloading Pixabay videos {i+1}/{num}")
            video_url = hit['videos']['large']['url']
            response = requests_get(video_url)
            if response is not None:
                with open(f'video_pixabay_{i+1:02d}.mp4', 'wb') as f:
                    f.write(response.content)

    def _get_params_photo(self, query, num, update_params={}):
        params = {
            'key': self.api_key,
            'q': query,
            'image_type': 'photo',
            'orientation': 'horizontal',
            'safesearch': 'true',
            'per_page': num
        }
        params.update(update_params)
        return params

    def get_photo(self, query, num=10, params={}):
        BASE_URL = 'https://pixabay.com/api/'
        _params = self._get_params_photo(query, num, params)
        response = requests_get(BASE_URL, params=_params)

        data = response.json()
        hits = data['hits']
        for i, hit in enumerate(hits):
            if self.verbose:
                print(f"  Downloading Pixabay photos {i+1}/{num}")
            image_url = hit['largeImageURL']
            response = requests_get(image_url)
            if response is not None:
                with open(f'photo_pixabay_{i+1:02d}.jpg', 'wb') as f:
                    f.write(response.content)

