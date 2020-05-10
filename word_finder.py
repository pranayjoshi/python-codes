def find_file(file_name, word):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if word in line:
                return True
                break
    return False
