
import webapp2
import urllib2 # gives us python classes and code need to requesting info receive and open it
# from xml.dom import json
import json
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'], ['Submit', 'submit']]
        if self.request.GET:
            # get info from API
            zm = ZipModel() # tells it to connect the api
            zm.zip = self.request.GET['zip'] # sends the zip from the URL to the model
            zm.callApi()
            zv = ZipView() # creates view
            zv.zdos = zm.dos # takes data objects from model and give them to view

            p._body = "<hr /><br />This the Zip Code for:" + zv.content
        self.response.write(p.print_out_form())

class ZipView(object):
    ''' this class handles how the data is shown to the user  '''
    def __init__(self):
        self.__zdo = []
        self.__content = '<br />'

    def update(self):
        for do in self.__zdos:
            self.__content += do.city
            self.__content += do.state

    @property
    def content(self):
        return self.__content


    @property
    def zdos(self):
        pass
    @zdos.setter
    def zdos(self, arr):
        self.__zdos = arr
        self.update()


class ZipModel(object):
    '''    This model handles fetching parsing and sorting data from api '''

    def __init__(self):
        self.__url = "http://zip.elevenbasetwo.com/v2/US/"
        self.__zip = ''

        # parse URL

    def callApi(self):
     # assemble the request
        request = urllib2.Request(self.__url + self.__zip)
        # use the urllib 2 library to create an object to get the url
        opener = urllib2.build_opener()
        # use url to get a result - request info from api
        result = opener.open(request)
        self._dos = []
            # sorts the data
        jsondoc = json.load(result)
        do = ZipData()
        do.city = "City: " + jsondoc["city"] + "<br />"
        do.state = "State: " + jsondoc["state"]
        self._dos.append(do)

    @property
    def dos(self):
        return self._dos


    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z


class ZipData(object):
    ''' this data object holds the data fetched by the model shown by the view'''
    def __init__(self):
        self.city = ''
        self.state = ''

class Page(object): #borrowing stuff from the object class
    def __init__(self): #constructor


        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>U.S. Zip Code Lookup</title>
    </head>
    <body>'''

        self._body = 'Look up a U.S. Zip Code '
        self._close = '''
    </body>
</html>'''

    def print_out(self):
            return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constructor function for super class
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form id = "zinput" method = "GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''


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
        return self._head + "U.S. Zip Code Lookup <br />" + self._form_open + self._form_inputs + self._form_close + self._body + self._close





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)