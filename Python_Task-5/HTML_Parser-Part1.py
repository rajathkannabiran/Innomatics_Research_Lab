# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
n=int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for j in attrs:
            print('->', j[0], '>', j[1])
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for j in attrs:
            print('->', j[0], '>', j[1])
            
Parser = MyHTMLParser()
Parser.feed(''.join([input().strip() for i in range(0, n)]))