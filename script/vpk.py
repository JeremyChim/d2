import subprocess



def vpk_create(vpk_bat):
    subprocess.run(vpk_bat, shell=True)



if __name__ == '__main__':
    vpk_create('C:/Users/Jeremy/Desktop/d2/vpk/vpk.bat')

