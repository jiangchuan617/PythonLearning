file_read = open('readme','r')
file_write = open('readme[复制]','w')

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
 
file_read.close()
file_write.close()