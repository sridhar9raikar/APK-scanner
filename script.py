from os import listdir
import os
import subprocess
from zipfile import ZipFile
print("download dex2jar,apktool and store it in /usr/local/bin folder\n")
print("download jd-cli and keep the extracted folder in path directory\n") 
#download tools


apk=input('enter name of apk file with extension\n')
print(os.path.abspath('.'))
print(os.path.dirname(os.getcwd()))
print(os.getcwd())

path=os.path.dirname((os.path.abspath('.')))
print('path ->',path)
unzip='unzip '+ os.path.abspath('.')+'//'+apk
os.system(unzip)
"""
with ZipFile(apk+'.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
"""
dex2jar_command='sh /usr/local/bin/dex2jar/d2j-dex2jar.sh ' 
apkcommand='apktool d '+apk
jarextract_command='java -jar ./jd-cli/jd-cli.jar -od'



length_op=int(len(path))
i=0
dexfile='classes.dex'
#while(os.path.exists(dexfile)):
while(i<5):
    if(os.path.exists(dexfile)):
        os.system(dex2jar_command +dexfile)
        print("dex------->",dexfile)
    i=i+1
    dexfile='classes'+str(i)+'.dex'


os.system(apkcommand)
print("success")
i=0
jarfile='classes-dex2jar.jar'
while(i<5):
    print("hi")
    if(os.path.exists(jarfile)):
        os.system(jarextract_command+' op'+str(i) +" "+jarfile)
        print("<<<<--------------->>>>>>",jarfile)
    i=i+1
    print("hi boyz")
    jarfile='classes'+str(i)+'-dex2jar.jar'
    print(jarfile)

#os.system(jarextract_command)
search_words=['Request_install_package','send_sms','Receive_sms','Bind_install_referrer_package','read_external_storage', 'Write_external_storage', 'Access_WiFi_state',
              'change_WiFi_state', 'Record_audio','record_video','Bind_device_admin','coinhive','crypto','instantcoffee']
print("\n\n")
with open(path+"//AM_op.txt", "w") as f:
    with open('Swiggy//AndroidManifest.xml',encoding="utf8",errors='ignore') as curFile:
        text3=curFile.readlines()
        curFile.seek(0)
        text2=curFile.read()
        for word in search_words:
            if(text2.find(word) == -1):
                print("...no")
            else:
                index = [x for x in range(len(text3)) if word in text3[x].lower()]
                f.write(word+"present in Android Manifest.xml at line no."+ str(index) +"\n")
                print("...yes!")
                print(word,index)
                print("\n")

files = []
i=0
while(i<5):
    path1= os.path.abspath('.') + '//op'+str(i)
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path1):
        for file in f:
            if '.java' in file:
                files.append(os.path.join(r, file))
    i=i+1

print('----------------------')
print(len(files))
"""for f in files:
    print(f)
"""
print('\nWRITNG TO FILE RESULT.TXT\n')
with open(path+"//result.txt", "w") as res:
    for f in files:
        with open(f,encoding='utf8',errors='ignore') as currentfile:
            text3=currentfile.readlines()
            currentfile.seek(0)
            text2=currentfile.read()
            for word in search_words:
                if not (text2.find(word) == -1):
                    index = [x for x in range(len(text3)) if word in text3[x].lower()]
                    res.write(word+" present in "+f[length_op:]+"  at line no. "+ str(index) +"\n"+" total occurences of "+word+" in this file = "  +str(text2.count(word))+"\n\n\n")
                    #print("yes!",end=' ')
                
                    
            #print("\n")


    
        
