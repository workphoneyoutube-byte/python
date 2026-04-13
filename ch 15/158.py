# create a class called FileItem that represents any file in an opertaing system
# Use attributes such as permission, owner, size, date created 

# create a class called CSVFile that inherits from FileItem and that represnets a csv file in an OS
# Use attributes specific to a csv file

# create a class JPGFile that inherits from FileItem and represents a JPG 
# Use attributes specific to a jpg file

# create a class MP3File that inherits from FileItem and that represents an MP3 file
# Use attributes specific to a MP3 file

class FileItem:
    def __init__(self,fileName,owner,permission,size,createdDate):
        self.fileName = fileName
        self.owner = owner
        self.permission = permission
        self.size = size
        self.dateCreated = createdDate
    
    def display(self):
        print("File Name: " + self.fileName)
        print("Owner: " + self.owner)
        print("Permissions: " + self.permission)
        print("File Size: " + self.size)
        print("Date Created: " + str(self.dateCreated))

class CSVFile(FileItem):
    def __init__(self,fileName,owner,permission,size,createdDate,delimiter,headerRow,textQualifier,escapeRules,lineBreak,encoding):
        FileItem.__init__(self,fileName,owner,permission,size,createdDate)
        self.delimiter = delimiter
        self.headerRow = headerRow
        self.textQualifier = textQualifier
        self.escapeRules = escapeRules
        self.lineBreak = lineBreak
        self.encoding = encoding

    def display(self):
        super().display()
        print("Delimiter: " + self.delimiter)
        print("Header Row: " + self.headerRow)
        print("Text Qualifier: " + self.textQualifier)
        print("Escape Rules: " + self.escapeRules)
        print("Line Break: " + self.lineBreak)
        print("Encoding: " + self.encoding)

class JPGFile(FileItem):
    def __init__(self,fileName,owner,permission,size,createdDate,compression,colorModel,transparency,layers,metaSupport):
        FileItem.__init__(self,fileName,owner,permission,size,createdDate)
        self.compression = compression
        self.colorModel = colorModel
        self.transparency = transparency
        self.layers = layers
        self.metaSupport = metaSupport
        self.size = size
    
    def display(self):
        super().display()
        print("Image Compression: " + self.compression)
        print("Color Model: " + self.colorModel)
        print("Transparency: " + self.transparency)
        print("Layers: " + self.layers)
        print("Metadata Support: " + self.metaSupport)
        print("File Size: " + self.size)

class MP3File(FileItem):
    def __init__(self,fileName,owner,permission,size,createdDate,compression,bitrate,bitrateSpeed,samplingRate,channels,metaTags):
        FileItem.__init__(self,fileName,owner,permission,size,createdDate)
        self.compression = compression
        self.bitrate = bitrate
        self.bitrateSpeed = bitrateSpeed
        self.samplingRate = samplingRate
        self.channels = channels
        self.metaTags = metaTags

    def display(self):
        super().display()
        print("Audio Compression: " + self.compression)
        print("Bitrate: " + self.bitrate)
        print("Bitrate Speed: " + self.bitrateSpeed)
        print("Sampling Rate: " + self.samplingRate)
        print("Channels: " + self.channels)
        print("Metadata Tags: " + self.metaTags)

txt = CSVFile("Jason Report","User1","rw-r--r--","15MB","2024-01-01",",","Yes","\"","\\","\\n","UTF-8")
txt.display()

img = JPGFile("Dog.jpg","User2","rwxr-xr-x","2MB","2024-02-01","Lossy","RGB","No","1","Yes")
img.display()

audio = MP3File("TripHop.mp3","User3","rw-r--r--","5MB","2024-03-01","Lossy","320kbps","Variable","44.1kHz","Stereo","Yes")
audio.display()