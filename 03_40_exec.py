import os

filesToProcess = [
    r"C:\Python intermediate\temp\03_40_file1.py",
    r"C:\Python intermediate\temp\03_40_file2.py"
    ]

for file in filesToProcess:
    print('Result of {} below:'.format(os.path.basename(file)))
    source = open(file, 'r')
    source = source.read()
    exec(source)

