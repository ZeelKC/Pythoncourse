#file name and extenstion
name=input("Enter filename: ")
ex=name.split('.')
ex=ex[1]
if ex=='doc' or ex=='docx':
    print('Word document')
elif ex=='html' or ex=='htm':
    print('html file')
elif ex=='pdf':
    print('pdf')
elif ex=='ppt' or ex=='pptx':
    print('Power point presenation')
elif ex=='xls' or ex=='xlsx':
    print("excel sheet")
elif ex=='txt':
    print('text file')
elif ex=='py':
    print('python file')
elif ex=='c':
    print('c file')
elif ex=='jpg' or ex=='png':
    print('image')
elif ex=='zip':
    print("zip file")
elif ex=='mvk' or ex=='mp4':
    print('video file')
elif ex=='mp3':
    print('audio file')
else:
    print('extenstion unrecognized')