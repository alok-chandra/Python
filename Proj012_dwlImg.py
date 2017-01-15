import random
import urllib.request

def download_web_Image(url):
    name=random.randrange(1,1000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(url,full_name)

download_web_Image("http://cdn.collider.com/wp-content/uploads/2016/06/suicide-squad-poster-slice-600x200.png")

