# Image Downloader
Download photos and videos from Pexels and Pixabay


You need [Pexels](https://help.pexels.com/hc/en-us/articles/900004904026-How-do-I-get-an-API-key-) and [Pixabay](https://pixabay.com/api/docs/#api_key) api keys.


## Examples

```
from pexels import Pexels

p = Pexels(api_key="your_pexels_api_key")

query = 'nature'
num = 3

p.get_photo(query, num)
p.get_video(query, num)
```

```
from pixabay import Pixabay

p = Pixabay(api_key="your_pixabay_api_key")

query = 'nature'
num = 3

p.get_photo(query, num)
p.get_video(query, num)
```

## Dependency
- requests
