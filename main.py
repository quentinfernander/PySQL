import os 
import sqlite3
#traverse file statement 
def main():

    path = input("Type out a path that needs traversin' \n")

    print ()
    if os.path.exists(path):
        file_dict = {}
        for root,directories,files in os.walk(path):
            
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_dict[file_path] = file_size 

        trigger = True
        while trigger:
            which_case = input("By SQL or Dict sort \n")
            if which_case == "SQL" or which_case == "Dict":
                trigger = False
            else:
                print ("Type in 'SQL' or 'Dict' ")

        if which_case == "Dict":
            by_dict(file_dict)
        else: 
            by_SQL(file_dict)
            ("This will not return any files. To do so, type : sqlite3 file_dict.db \n Now run queries through the command line!")
        
    else: 
        print(f"{path} does not exist")

    
def by_dict(dict):
    count = 0
    for path, size in sorted(dict.items(), key=lambda x:x[1], reverse = True):
        if count > 19:
            break
        print(f"{path}: {size}")
        count += 1

def by_SQL(dict):
    'create table based on file_dict'
    connection = sqlite3.connect('file_dict.db')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS files")
    connection.commit()

    cursor.execute("CREATE TABLE files(id integer primary key, path TEXT, size INTEGER)")
    connection.commit()
    for path, size in dict.items():
        cursor.execute("INSERT INTO files(path, size) VALUES(?,?)", (path, size))
        connection.commit()
    print("files ready to be queried using table name 'files' and column names 'path and size'")
    

    

if __name__ == '__main__':
    main()
