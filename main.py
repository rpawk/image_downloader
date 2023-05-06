import os
from pexels import Pexels
from pixabay import Pixabay

downloaders = [
        Pexels(api_key=os.environ['PEXELS_API_KEY']),
        Pixabay(api_key=os.environ['PIXABAY_API_KEY'])
        ]


num = 3
query = 'nature'

for d in downloaders:
    d.get_photo(query, num)
    d.get_video(query, num)
