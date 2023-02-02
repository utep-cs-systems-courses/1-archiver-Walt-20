#imports
import os, tarfile


user = input()
if user == '-help':
    print("c (create), filename(s)")
    print("x (extract), dst")
archive = input()

# check if user should have access to file

if archive == 'c':
    # create the tar file obj
    tar = tarfile.open(name='somename.tar', mode='w')
    files = ['foo.txt']
    # write in the desired files
    for f in files:
        tar.add(f)
    tar.close()

    # # save that new file as a tar
    # open(src, 'wb').write(open(src, 'rb').read())
    # print("success")
elif archive == "e":
    # extract the file and store in another directory
    open(dst, 'wb').write(open(src, 'rb').read())
    print("success")
else:
    print("you must enter c or e")