
import time
import numpy as np
import facebook
import random
group = '1164034027854428'



link = 'https://www.facebook.com/groups/' + group
token = input("Enter token ")
msg="Have a wonderful Saturday friends"
array_watched = np.zeros(30)
index = random.randint(1,30)
array_watched[index]
link = "https://www.youtube.com/watch?v=3AtDnEC4zak&list=PLy1bC-662HHKXOVHInxvhSRReDz0d4xCI&index="+ str(index)
graph = facebook.GraphAPI(access_token=token)
x = graph.put_object(group, 'feed', message=msg, link=link)
print(x)
print("Successfuly")

