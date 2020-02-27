import os

def save_source(address, source):
    name = address.replace('.', '-') + '.html'
    path = './data/' + name

    if os.path.exists(path):
        return 'page exists'
    else:
        f = open(path, 'w')
        f.write(source)
        f.close()
        return 'page created'
