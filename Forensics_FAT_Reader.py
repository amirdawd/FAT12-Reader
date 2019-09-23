hex_file = open('image.dat', 'rb')
data = []
data = hex_file.read().hex()
ByteList = []
i =0
for x in data:          # creating a list of bytes
    while (len(data) > i):
        ByteList.append(data[i] + data[i+1])
        i=i+2

def decimal_offset(list, index): #returns a hex value of the given decimal index
    return list[index]


bootSector = []
for x in range(0,512):
    bootSector.append(ByteList[x])
print(bootSector)

FAT_Region_1= []
FAT_Region_2= []
for x in range(512, 5119):
    FAT_Region_1.append(ByteList[x])

for x in range(5120, 9215):
    FAT_Region_2.append(ByteList[x])


for x in range(0,200):
    print(FAT_Region_1[x] + '\t' + FAT_Region_2[x])

DATA_region= []
for x in range(16896,len(ByteList)): #Data Region starts at the 33th sector
    DATA_region.append(ByteList[x])

Root_Directory= []
for x in range(9728, 16895):
    Root_Directory.append(ByteList[x])

Dir_File_Name= []
Dir_Extension=[]
Dir_Attributes= []
Dir_Reserved= []
Dir_CreationTime=[]
Dir_Creation_Date=[]
Dir_Last_Acess_Date=[]
Dir_Last_Write_Time=[]
Dir_Last_Write_Date=[]
Dir_First_Logical_Cluster=[]
Dir_File_Size=[]

def range1(start, end):
    return range(start,end+1)



def createList(list, start, finish):
    for x in range1(start+224, finish+224):
        list.append(Root_Directory[x])



createList(Dir_File_Name,0,7)
createList(Dir_Extension,8,10)
createList(Dir_Attributes,11,11)
createList(Dir_Reserved,12,13)
createList(Dir_CreationTime,14,15)
createList(Dir_Creation_Date,16, 17)
createList(Dir_Last_Acess_Date,18,19)
createList(Dir_Last_Write_Time,22,23)
createList(Dir_Last_Write_Date,24,25)
createList(Dir_First_Logical_Cluster,26,27)
createList(Dir_File_Size,28,31)


print(FAT_Region_1)
print(FAT_Region_2)

print(Dir_File_Size)

zip_File= []
for x in range1(148992,157225):
    zip_File.append(ByteList[x])

new_file = open("./" + "hello1" ,"wb+" )

for x in zip_File:
    s = bytearray(x, encoding='utf32')
    new_file.write(s)


for x in range1(39,42):
    print(bootSector[x])
