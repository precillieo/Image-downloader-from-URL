# Image-downloader-from-URL
This image downloader script downloads images from rows of urls contained in a csv file. 
* Ensure your csv file and this python file are in the same directory.
* Pass your csv file's name to the ```filename``` variable.
* The expected format of your csv file.
  * column 1 containing the names of each of the images.
  * Column 2 for the URLs.
  * Take away the column headers for seamless run.
   
```
import urllib
import urllib.request

filename = "train_self"

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 


# open file to read
with open("{0}.csv".format(filename), 'r') as csvfile:
    # iterate on all lines
    i = 0
    for line in csvfile:
        splitted_line = line.split(',')
        # check if we have an image URL
        if splitted_line[1] != '' and splitted_line[1] != "\n":
            request= urllib.request.Request(splitted_line[1],None, headers)
            response= urllib.request.urlopen(request)
            data=response.read()
            with open(splitted_line[0]+".jpg", 'wb') as f:
            	f.write(data)
            print ("Image saved for {0}".format(splitted_line[0]))
            i += 1
        else:
            print ("No result for {0}".format(splitted_line[0]))
```

Paste the code in your favorite editor.

![alt text](https://github.com/Precillieo/Financial-Model/blob/main/image%20scrapper.jpg)
