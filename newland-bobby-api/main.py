
import webapp2
import urllib2 # gives us python classes and code need to requesting info receive and open it
# from xml.dom import minidom
from xml.dom import minidom
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['movie', 'text', 'Movie Title'], ['Submit', 'submit']]
        self.response.write(p.print_out_form())
        if self.request.GET:
            # get info from API
            movie = self.request.GET['movie']
            url = "http://www.omdbapi.com/?s=" + movie + "&" + "r=XML"
            # assemble the request
            request = urllib2.Request(url)
            # use the urllib 2 library to create an object to get the url
            opener = urllib2.build_opener()

            # use url to get a result - request info from api
            result = opener.open(request)

            #parse xml
            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('Movie'))
            self.content = '<br />'

            list = xmldoc.getElementsByTagName('Title')
            for item in list:
                self.content += " Title: " + item.attributes['Title'].value
                self.content += " Year: " + item.attributes['Year'].value
                self.content += " Type: " + item.attributes['Type'].value

                self.content += '<br />'
            self.response.write(self.content)
            print self.content


class Page(object): #borrowing stuff from the object class
    def __init__(self): #constructor


        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Movie Genius</title>
    </head>
    <body>'''

        self._body = 'Movie Genius '
        self._close = '''
    </body>
</html>'''

    def print_out(self):
            return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constructor function for super class
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method = "GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        #<input type="text" value="" name="first_name" placeholder="First Name" />
        #<input type=""text value="" name="last_name" placeholder="Last Name" /> ['first_name', 'First Name']
        #<input type='Submit' value='Submit' />

    @property
    def inputs(self):
        return
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through the mega array and create HTML inputs based on the info there
        for item in arr:
            self._form_inputs += '<input type= "' + item[1] + '"' + ' name= "' + item[0]
        # if there is a third item add it in
            try:
                self._form_inputs += '" placeholder= "' + item[2] + '" />'
        # other wise end the tag
            except:
                self._form_inputs += '" />'
        print self._form_inputs

        #POLYMORPHISM ALERT!!! --------------- method overriding
    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
