import os
import sys

# take a look at bufferreader in fd-io-demos repository 
# check out write file as well and the while loop. Index slicing till we get all the buffer
# do this ^


def mytar(file_names, target_file):

    # open the tar_file for storing
    tar_fd = os.open(target_file, os.O_CREAT | os.O_WRONLY) 
    # looking through all files provided
    for file_name in file_names:
        # setting the file descriptor equal to the # current file
        fd = os.open(file_name, os.O_RDONLY)
        # getting file information
        file_info = os.stat(file_name)
        # obtaiing file size
        file_size = file_info.st_size
        # reading the file descriptor and size
        file_content = os.read(fd, file_size)
        # creating tar header with encoding
        header = f"{file_name}:{file_size}\n".encode()
        # write header of to tar descriptor
        os.write(tar_fd, header)
        # write file contents to tar descriptor
        # os.write(tar_fd, file_content)
        # close current file descriptor
        os.close(fd)
    # close tar descriptor
    os.close(tar_fd)
    sys.stdout.write("success\n")

def extract_tar(target_file):
    # traverse the tar files
    tar_name = target_file 
    # open the tar file
    tar_fd = os.open(tar_name, os.O_RDONLY)
    file_info = os.stat(tar_name)
    file_size = file_info.st_size
    # read the file content
    file_content = os.read(tar_fd, file_size).decode()
    # use information found in headers to create files and write contents
    sys.stdout.write(file_content)
    os.close(tar_fd)

if __name__ == '__main__':
    mode = sys.argv[1]
    target_file = sys.argv[-1]
    if mode == 'c':
        file_names = sys.argv[2:-1]
        mytar(file_names, target_file)
    elif mode == 'x':
        extract_tar(target_file)
    else:
        sys.stdout.write("Usage: mytar.py c|x <file1> <file2> ... <fileN>")
        sys.exit(1)
