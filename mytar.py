#imports
import os, tarfile


user = input()

# check if user should have access to file
if user == 'c':
    # create the tar file obj
    tar = tarfile.open(name='foogoo.tar', mode='w')
    # list the files to be put in the .tar
    files = ['src/foo.txt', 'src/goo.gif']
    # write in the desired files
    for f in files:
        tar.add(f)
    tar.close()
    print("success")
elif user == 'e':
    # extract the file and store in another directory
    open(os.listdir('dst'), 'wb').write(open(os.listdir, 'rb').read())
    print("success")
else:
    print("you must enter c or e")