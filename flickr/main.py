import requests
response = requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=582a580d3b84d364139264bef57fe7aa&user_id=195500972%40N07&sort=views&per_page=50&format=json&nojsoncallback=1")
data = response.json()
print(data)