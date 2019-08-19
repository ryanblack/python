import json
import os
import math

if __name__ == '__main__':
  # read file
  file_name = "d:\\DISK\\!MYFAMILY\\KUCHUK STANISLAV\\11 KUCHUK STANISLAV - IT\\GIT\\python\\python\\coordinates.json"
  with open(file_name, 'r') as myfile:
   data=myfile.read()
  # parse file
  obj = json.loads(data)

  # get the origin
  origin = obj[0]["value"]
  origin = origin.split(",")
  xorigin = int(origin[0])
  yorigin = int(origin[1])

  #calculate distance for each coordinate
  l = []
  for i in obj:
    coordinate=i["value"]
    coordinate=coordinate.split(",")
    idtemp = i["id"]
    xtemp = int(coordinate[0])
    ytemp = int(coordinate[1])
    i['distance'] = math.sqrt(abs(xorigin-xtemp)**2+abs(yorigin-ytemp)**2)
    l.append(dict(i))

  #sort and output
  newlist = sorted(l, key = lambda i: i['distance'])
  for i in newlist:
    print(i)
 

  