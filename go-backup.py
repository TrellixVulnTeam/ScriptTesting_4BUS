import os.path
import tarfile
import time


#Time Format
time_string = time.strftime("%m%d%Y")

def make_tarfile(FILE_NAME, DIR, TIME=time_string):
    
    print("Backup Starting...")
    print("Backup Time will depend on the size of the backup")

    with tarfile.open(FILE_NAME + "_" + TIME + ".tar.gz","w:gz") as tar:
        tar.add(DIR, arcname=os.path.basename(DIR))
        for file in tar.getnames():
            print(f"Backup > {file}")
        tar.close()
    print(f"{FILE_NAME} has been Successfully Compress.")


def extract_tarfile(FILE_NAME, DIR):

    print("Starting the Extraction...")
    print(f"Extracting {FILE_NAME}...")

    with tarfile.open(FILE_NAME) as tar:
        print("Extraction Ongoing... Please wait...")
        tar.extractall(DIR) #Specific folder
        tar.close()
    print(f"{FILE_NAME} has been Successfully Extracted.")



while True:

    #MENU
    print("""

        SIMPLE BACKUP
        By: MC2022

        How to Use:
            Provide the PATH ex. C:\HelloWorld
            Provide the Folder with .tar.gz extension

        MENU: 
        1. Compress Directory/Folder
        2. Uncompress Directory/Folder
        3. Quit
    
    """)

    #MENU condition

    MENU = input("> ")

    if MENU in ['1', '2', '3']:


        #check if user choose 3 to quit.
        if MENU == '3':
            print("Bye")
            break
        
        #directory name
        DIR = input("Enter Directory PATH >  ")
        #folder NAME
        FILE_NAME = input("Enter FOLDER name > ")
        
        os.chdir(DIR)
        print(f"Current Directory: {os.getcwd()}")


        if MENU == '1':
            make_tarfile(FILE_NAME, DIR)
        elif MENU == '2':
            extract_tarfile(FILE_NAME, DIR)

    else:
        print("Choose only in the MENU")






    


