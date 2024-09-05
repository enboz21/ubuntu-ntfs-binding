import os

# sudo mount -t ntfs-3g /dev/sdh1 /media/enboz21/dışbirim

dad=os.getlogin()
yol=f"/media/{dad}/"
def tek(i):
    print("varolan dosya isimleri")
    filess = os.listdir(yol)
    for file in filess:
        i=i+1
        print(f"{i}. {file}")
    return i


s=str
b=True
while(b):
    i=0
    i=tek(i)
    print('yeni dosya için "y" ye basın')
    s=input()
    if(s.isdigit()):
        if int(s) <= i and int(s) > 0:
            b = False

    elif(s=="y"):
        print("dosya ismi")
        ad=input()
        os.chdir(yol)
        os.system(f"sudo -S mkdir {ad}")
filess = os.listdir(f"/media/{dad}/")
strf=filess[i-1]
print("sürücünün port bilgisi")
d=input()
os.system(f"sudo -S mount -t ntfs-3g /dev/{d} /media/{dad}/{strf}")

