#Main function

#How do you run your code automatically?

#Determine how the script was run using "__name__"
print(f'Name: {__name__}')
print(f'File: {__file__}')

#Create some code
def test():
    print('This is a test function')

def main():
    print('This is the main function')
    test()

#Run automatically
if __name__ == "__main__":
    main()

#Now run it from a different script - see test.py