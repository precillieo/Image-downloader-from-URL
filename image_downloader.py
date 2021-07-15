
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

