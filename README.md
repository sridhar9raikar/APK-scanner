# APK-scanner
STEPS

1)download dex2jar and apktool

2)download  jd-cli from below link and keep it in the same folder as your script.py file 
->link:https://github.com/kwart/jd-cmd/tree/master/jd-cli
3)have your .apk file in the same folder as your script.py and jd-cli 
4)run the script.py from the command line
python3 script.py

dex2jar converts .dex files to .jar
apktool is used to read the AndroidManifest.xml which is otherwise encrypted
jd-cli extracts jar files thus revealing all java files used.

the output is a result.txt which gives the occurence of keywords(in script) in all .java files.
the output is a AM_OP.txt which gives the occurence of keywords IN AndroidManifest.xml


Further Work:
Backtrace the use of keywords to know if they are actually called or not.(REVERSE-ENGINNERING)

Any help is appreciated.
Thank you
