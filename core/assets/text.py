import re

if __name__ == '__main__':
    val = re.match(r'^(.+)(_[hg\d])$', "hssskkk_younn_h")
    print(val)
    val = val.group(2)
    print(val)