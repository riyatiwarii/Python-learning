# Use of function from func1 file to func2

def reverse_string(str1):
    if len(str1) % 4 == 0:
        return ''.join(reversed(str1))
    return str1
if __name__ == '__main__':
    print(reverse_string('Riya'))
    print(reverse_string('python'))