class UnknownError:
    pass
def read_file_contents(file_name):
    try:
        f=open(file_name,'r')
    except FileNotFoundError:
        print("Given file does not exists")
    except PermissionError:
        print("There is no permission for read file")
    except UnknownError:
        print("UnknownError occured")
    else:
        text=f.read()
        print(text)
    finally:
        if not f.closed:
            f.close()

read_file_contents('Sample.txt')