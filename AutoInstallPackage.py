import os

packages = ['flask','flask-vue']
try:
    for pac in packages:
        os.system('pip install '+pac)
    print('Install success!')
except:
    print('Install failed!')