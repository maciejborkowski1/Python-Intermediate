import os
import urllib.request as ur

dataDir = r'c:\Python intermediate\temp'

pages = [{'name': 'google', 'url': 'http://www.google.com/'},
         {'name': 'github', 'url': 'http://www.github.com/'}]

for page in pages:
    try:
        fullName = "{}.html".format(page['name'])
        path = os.path.join(dataDir, fullName)
        print('Try to download {} site to {} location...'.format(page['name'], path))
        ur.urlretrieve(page['url'], path)
    except:
        print('Cannot download {} - unexcepted error'.format(page['url']))
        break
else:
    print('Script finished successfull')
