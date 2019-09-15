
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


print(DATA_region[33]) #Test


