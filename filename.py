#file name and extenstion
name=input("Enter filename: ")
ex=name.split('.')
ex=ex[1]
d={'doc':'Word document','html':'html file','pdf':'pdf','ppt':'Power point presenation','xls':'excel sheet','txt':'text file' ,
     'py':'python file','c':'c file','jpg':'image','zip':'zip file','mvk':'video file','mp3':'audio file'}
if ex=='doc' or ex=='docx':
    print(d['doc'])
elif ex=='html' or ex=='htm':
    print(d['html'])
elif ex=='pdf':
    print(d['pdf'])
elif ex=='ppt' or ex=='pptx':
    print(d['ppt'])
elif ex=='xls' or ex=='xlsx':
    print(d['xls'])
elif ex=='txt':
    print(d['txt'])
elif ex=='py':
    print(d['py'])
elif ex=='c':
    print(d['c'])
elif ex=='jpg' or ex=='png':
    print(d['jpg'])
elif ex=='zip':
    print(d['zip'])
elif ex=='mvk' or ex=='mp4':
    print(d['mvk'])
elif ex=='mp3':
    print(d['mp3'])
else:
    print('extenstion unrecognized')
