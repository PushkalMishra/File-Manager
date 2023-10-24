import os

def list_files():
    path=input("enter the path")
    print(f"Listing files in {path}:")
    for item in os.listdir(path):
        print(item)

def rename():
    path = input("enter the path")
    filename=input("enter the file name to rename")
    final_filename=input("enter the file name")
    my_source = os.path.join(path, filename)
    my_dest = os.path.join(path, final_filename)
    os.rename(my_source, my_dest)

def create():
    path=input("enter the path")
    print("enter the name of the folder")
    name=input()
    folder_path=os.path.join(path,name)
    if(not os.path.exists(folder_path)):
        os.mkdir(folder_path)
       
def remove(): 
    while True:
        print("1.Remove a file")
        print("2.Remove directory")
        print("3.Exit")
        ch=int(input("enter the choice"))
        if(ch==1):
            path=input("enter the path")
            file_name=input("enter the file name")
            path=os.path.join(path,file_name)
            if(os.path.exists(path)):
                os.remove(path)
            else:
                print("file not found")    
        elif(ch==2):
            path=input("enter the path")
            directory_name=input("enter the directory_name")
            path=os.path.join(path,directory_name)
            if(os.path.exists(path)):
                os.rmdir(path)
            else:
                print("directory not found")    
        elif(ch==3):
            break
        else:
            print("Invalid choice")
def main():
    while True:
        print("1. List files and directories")
        print("2. Change directory")
        print("3. Create directory")
        print("4. Delete file and directory")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_files()
        elif choice == '2':
            rename()
        elif choice == '3':
            create()
        elif choice == '4':
            remove()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()