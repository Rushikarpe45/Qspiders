# Package ---- Folder
# Modules --- Python File
# Create a folder(package) and create a python file inside it , save it as file1 and write the below
# code,
def valid_un(s):
    if '_' in s:
        return True
    else:
        return False

print(valid_un('Saku_r'))  # True

def valid_pw(s):
    if len(s) >= 8:
        u, l, d, sc = 0, 0, 0, 0
        for i in s:
            if 'A' <= i <= 'Z':
                u += 1
            elif 'a' <= i <= 'z':
                l += 1
            elif '0' <= i <= '9':
                d += 1
            elif i in '@_$':
                sc += 1
        
        if u >= 2 and l >= 2 and d >= 2 and sc >= 2:
            return True
        else:
            return False
    else:
        return False

print(valid_pw('Saku_R@123'))  # False, because it has only 1 uppercase and 1 special char
