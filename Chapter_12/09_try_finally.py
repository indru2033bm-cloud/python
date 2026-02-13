
def main():
    try:
        a = int(input("Hey there, enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am in finally block") # This block will always execute whether there is an exception or 
         # not. It is used to perform clean up actions like closing files, releasing resources etc.