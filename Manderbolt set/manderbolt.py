from PIL import Image,ImageDraw
from math import log,log2
from collections import defaultdict
from math import floor, ceil
itermax=80

def manderbolt(c):
  z,n=0,0
  while abs(z)<=2 and n<itermax:
    z=z*z+c
    n+=1
  if n==itermax:return n
  return n+1-log(log2(abs(z)))

def linear_interpolation(color1, color2, t):
  return color1 * (1 - t) + color2 * t
w,h=600,400

rstart,rend,istart,iend=-2,1,-1,1
histogram=defaultdict(lambda: 0)

values={}

img=Image.new('RGB',(w,h),(0,0,0))
draw=ImageDraw.Draw(img)

for x in range(w):
  for y in range(h):
    c = complex(rstart+(x/w)*(rend-rstart),istart+(y/h) *(iend-istart))    
    m=manderbolt(c)
    values[(x,y)]=m
    if m<itermax:histogram[floor(m)]+=1
total=sum(histogram.values())
hues=[]
j=0
for i in range(itermax):
  j+=histogram[i]/total
  hues.append(j)
hues.append(j)
im = Image.new('HSV', (w,h), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(w):
  for y in range(h):
    m=values[(x,y)]
    hue=255-int(255*linear_interpolation(hues[floor(m)], hues[ceil(m)], m % 1))
    saturation=255
    value=255 if m <itermax else 0
    draw.point([x,y],(hue,saturation,value))
im.convert('RGB').save('output.png', 'PNG')



            

