
import webapp2
import urllib2 # gives us python classes and code need to requesting info receive and open it
# from xml.dom import minidom
from xml.dom import minidom
class MainHandler(webapp2.RequestHandler): # controller
    def get(self):
        p = FormPage()
        p.inputs = [['movie', 'text', 'Movie Title'], ['Submit', 'submit']]


        if self.request.GET: # only if there is a zip variable in the url
            # get info from API
            wm = WeatherModel() #creates our model
            wm.movie = self.request.GET['movie'] # sends zip from url to model
            wm.callApi() # tells it to connect to the API

            wv = WeatherView() #creates our view
            wv.wdos = wm.dos # takes data objects from model and gives them to view
            p._body = wv.content

            self.response.write(p.print_out_form())




class WeatherView(object):
    ''' This class handles how the data is show to the user '''

    def __init__(self):
        self.__wdos = []
        self.__content = '<br />'

    # def update(self):
    #     for do in self.__wdos:
    #         self.__content += do.day
    #         self.__content += "  High: " + do.high + "  Low: " + do.low
    #         self.__content += "  Condition: " + do.condition
    #         self.__content += '<img src="images/' + do.code + '.png" width="30" /><br />'

    @property
    def content(self):
        return self.__content


    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr
        print self.__wdos
        self.update()



class WeatherModel(object):
    ''' This model handles fetching, parsing and sorting of data from Yahoos weather API '''
    def __init__(self):
        self.__url = "http://www.omdbapi.com/?t=hitch"
        self.__movie = ''
        self.__xmldoc = ''


    def callApi(self):
        # loads the request
        request = urllib2.Request(self.__url+self.__movie)
        # use the urllib 2 library to create an object to get the url
        opener = urllib2.build_opener()
        # use url to get a result - request info from api
        result = opener.open(request)
         #parse data
        self.__xmldoc = minidom.parse(result)

        #sorting data
        list = self.__xmldoc.getElementsByTagName("Movie Title")
        self._dos = []
        for tag in list:
            do = WeatherData()
            do.title = tag.attributes['title'].value
            do.year = tag.attributes['year'].value
            do.type = tag.attributes['type'].value

            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def movie(self):
            pass

    @movie.setter
    def movie(self, m):
        self.__movie = m

class WeatherData(object):
    ''' this data object holds the data fetched by the model and shown by the view'''
    def __init__(self):
        self.title = ''
        self.year = ''
        self.type = ''



class Page(object): #borrowing stuff from the object class
    def __init__(self): #constructor


        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>My Weather App</title>
    </head>
    <body>'''

        self._body = 'Movie Scoop '
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
        return self._head + "Movie Scoop " + self._form_open + self._form_inputs + self._form_close + self._body + self._close





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
