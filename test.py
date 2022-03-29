from requests import get, post, delete
import random

print(post('http://127.0.0.1:5000/post').json())