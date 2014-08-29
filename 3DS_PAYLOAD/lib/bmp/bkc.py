import sys;
import os
import pprint
from PIL import Image,ImageDraw



cwd = os.getcwd() 

if "\\" not in sys.argv[1]:
	sys.argv[1] = cwd+"\\"+sys.argv[1]

trans = (255,0,255)
grey  = (192,192,192)
black  = (0,0,0)
white  = (255,255,255)

filename = os.path.basename(sys.argv[1] )
extension = os.path.splitext(filename)[1][1:]
file_base = os.path.basename(os.path.splitext(sys.argv[1])[0])

org = Image.open(sys.argv[1])  

pixels = org.load()

colors = {}

size = (org.size[0],org.size[1])             # size of the image to create

width = org.size[0]
height = org.size[1]

bits = ""
num_components = len(pixels[0,0])

byte_array = [0 for x in range(org.size[0]*org.size[1])]

def get_color(_pixel):

	pixel = _pixel[0:3]

	#if (len(pixel) > 3):
	#	if (pixel[3] < 128):
	#			return "00";
		

	#print pixel
	if (pixel == white):
		return "1"
	return "0"

for i in range(org.size[0]):
	for j in range(org.size[1]):
		r,g,b = 0,0,0
		if num_components == 4:
			px = pixels[i,j]
			r = (pixels[i,j][0] // 32)
			g = (pixels[i,j][1] // 32)
			b = (pixels[i,j][2] // 64)

			#if px[3] > 128:
				#npixels[i,j] = (r*32,g*32,b*64) 
			#else: 
				#npixels[i,j] = (0,0,0)

		if num_components == 3:
			px = pixels[i,j]
			r = (pixels[i,j][0] // 32)
			g = (pixels[i,j][1] // 32)
			b = (pixels[i,j][2] // 64)
			#npixels[i,j] = (r*32,g*32,b*62)

		if num_components == 1:
			px = pixels[i,j]
			r = (pixels[i,j][0] // 32)
			g = (pixels[i,j][1] // 32)
			b = (pixels[i,j][2] // 64)
			#npixels[i,j] = (r,g,b)
		byte_array[(j*width+i)] = get_color(pixels[i,j])
		#print "org "+str(r)+"    "+str(g)+"    "+str(b)
		#print "org "+str(pixels[i,j])
		#print "red "+str(r)+" "+str(g)+" "+str(b)
		#byte =  str(bin(r)[2:]).zfill(3)+""+str(bin(g)[2:]).zfill(3)+""+str(bin(b)[2:]).zfill(2)
		#print pixels[i,j]
			#bit_array[j*org.size[0]+i] = 0
			#bit_array[j*org.size[0]+i] = 1
		#hex(int(byte,2))
		#print "bi2 0b"+str((bin(r//32)[2:5]).zfill(3))+""+str((bin(g//32)[2:5]).zfill(3))+""+str((bin(g//64)[2:4]).zfill(2))

for b in byte_array:
	bits = bits + b


im = Image.new('RGB', size) # create the image
npixels = im.load();

print len(bits)
print (height*width)
print len(byte_array)

for y in range(height):
	for x in range(width):
		
		if  bits[((y*width+x)*1)]  == "1":
			npixels[x,y] = white
		else:
			npixels[x,y] = black


f = open(file_base+".c",'w+');
f.write("/*\nC Source File for "+filename+"\n*/");
f.write("\nunsigned static int "+file_base[0:10]+"_size = "+str(len(byte_array)/4)+";\n");
f.write("unsigned static int "+file_base[0:10]+"_width = "+str(org.size[0])+";\n");
f.write("unsigned static int "+file_base[0:10]+"_height = "+str(org.size[1])+";\n");
f.write("unsigned static char "+file_base[0:10]+"_data[] = {\n");

i = 0

hex_values

while i < len(byte_array)-8:
	bitstring = byte_array[i]+byte_array[i+1]+byte_array[i+2]+byte_array[i+3]+byte_array[i+4]+byte_array[i+5]+byte_array[i+6]+byte_array[i+7]
	f.write(hex(int(bitstring,2))+",");
	if (i % 18 == 0):
		f.write("\n");
	i = i+8
	#f.write(str(+",");
#	if (i % 10 == 0):
#		f.write("\n")
f.write("};")
os.system("del tst.png")
im.save("tst.png")





		#print str(r)+" "+str(g)+" "+str(b)
		

#print len(colors)