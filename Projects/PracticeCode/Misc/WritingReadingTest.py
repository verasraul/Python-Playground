#__author__ = 'verasraul'

#
# nFile = open('sample.csv', 'w')#'open' creates new empty file, 'w' writes to the file
# nFile.write("First, Last, Account\n")
# nFile.write("Raul, Veras, Hotmail\n")
# nFile.close()





nfile = open('sample.csv', 'r')
text = nfile.read()
print(text)