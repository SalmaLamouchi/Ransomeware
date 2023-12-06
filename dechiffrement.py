from cryptography.fernet import Fernet
import os 
def decrypt(items,clef):
    f=Fernet(clef)
    for item in items:
        with open(item,'rb')as File:
            File_data=File.read()
            decrypted_data=f.decrypt(File_data)
        with open(item,'wb') as File:
            File.write(decrypted_data)
def lire_clef():
    return open('clef.key','rb').read()
clef=lire_clef()
path="/Users/salma/PycharmProjects/Ransomeware/files"
os.remove(path+'/'+'readme.txt')
items=os.listdir(path)
chemin=[path+'/'+item for item in items]
decrypt(chemin,clef)






