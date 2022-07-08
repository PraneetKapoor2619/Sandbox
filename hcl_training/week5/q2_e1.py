fhandle1 = open("img1.png", "rb")
fhandle2 = open("img3.png", "wb+")

fhandle2.write(fhandle1.read())
fhandle1.close()
fhandle2.close()