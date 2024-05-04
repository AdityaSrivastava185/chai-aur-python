import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(files):
    with open('youtube.txt', 'w') as file:
        json.dump(files, file)

def list_all_files(files):
    print("\n")
    print("*" * 70)
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file['name']}, Duration: {file['time']} ")
    print("\n")
    print("*" * 70)

def add_file(files):
    name = input("Enter file name: ")
    time = input("Enter file time: ")
    files.append({'name': name, 'time': time})
    save_data_helper(files)

def update_file(files):
    list_all_files(files)
    index = int(input("Enter the file number to update"))
    if 1 <= index <= len(files):
        name = input("Enter the new file name")
        time = input("Enter the new file time")
        files[index-1] = {'name':name, 'time': time}
        save_data_helper(files)
    else:
        print("Invalid index selected")


def delete_file(files):
    list_all_files(files)
    index = int(input("Enter the file number to be deleted"))
    
    if 1<= index <= len(files):
        del files[index-1]
        save_data_helper(files)
    else:
        print("Invalid file index selected")


def main():
    files = load_data()
    while True:
        print("\n Youtube Manager")
        print("1. List all youtube files ")
        print("2. Add a youtube file ")
        print("3. Update a youtube file details ")
        print("4. Delete a youtube file ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(files)

        match choice:
            case '1':
                list_all_files(files)
            case '2':
                add_file(files)
            case '3':
                update_file(files)
            case '4':
                delete_file(files)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main() 