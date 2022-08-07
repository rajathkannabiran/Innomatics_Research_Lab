# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('-> {} > {}'.format(*i))
    
N=int(input())
html='\n'.join([input() for x in range(0, N)])  
parser=MyHTMLParser()
parser.feed(html)
parser.close()