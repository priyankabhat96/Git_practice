with open ("test.txt", 'r') as file:
    lines = file.readlines()
    #rev_lines = reversed(lines)

    with open("write_file.txt", 'w') as file_write:
        for line in reversed(lines):
            file_write.write(line)
