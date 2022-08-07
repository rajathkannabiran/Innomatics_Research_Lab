from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if (comment.find('\n') != -1):
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(comment)
        
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()