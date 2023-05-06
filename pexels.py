from util import requests_get


class Pexels():
    """
    https://www.pexels.com/api/documentation/
    """
    def __init__(self, api_key, verbose=True):
        self.api_key = api_key
        self.name='Pexels'
        self.verbose = verbose

    def _get_params_headers(self, query, num, update_params={}):
        params = {
            'query': query,
            'per_page': num
        }
        params.update(update_params)
        headers = {
            'Authorization': self.api_key
        }
        return params, headers

    def get_video(self, query, num=10, params={}):
        BASE_URL = 'https://api.pexels.com/videos/search'
        _params,_headers = self._get_params_headers(query, num, params)
        response = requests_get(BASE_URL, params=_params, headers=_headers)

        data = response.json()
        videos = data['videos']
        for i, video in enumerate(videos):
            if self.verbose:
                print(f"  Downloading Pexels videos {i+1}/{num}")
            video_url = f"https://www.pexels.com/download/video/{video['id']}"
            response = requests_get(video_url)
            if response is not None:
                with open(f'video_pexels_{i+1:02d}.mp4', 'wb') as f:
                    f.write(response.content)

    def get_photo(self, query, num=10, params={}):
        BASE_URL = 'https://api.pexels.com/v1/search'
        _params,_headers = self._get_params_headers(query, num, params)
        response = requests_get(BASE_URL, params=_params, headers=_headers)

        data = response.json()
        photos = data['photos']
        for i, photo in enumerate(photos):
            if self.verbose:
                print(f"  Downloading Pexels photos {i+1}/{num}")
            image_url = photo['src']['large']
            response = requests_get(image_url)
            if response is not None:
                with open(f'photo_pexels_{i+1:02d}.jpg', 'wb') as f:
                    f.write(response.content)

