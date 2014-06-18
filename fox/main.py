
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Animal()
        p.animals = [['snake'], ['dog'], ['cow']]
        self.response.write(p.print_out())
        #snake
        s = Animal()
        s.phylum = "Chordata"
        s.Class = "Reptilia"
        s.order = "Squamata"
        s.family = "Acrochordidae"
        s.genus = "Acrochordus"
        s.imgurl = "http://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Wart_snake_1.jpg/220px-Wart_snake_1.jpg"
        s.average_lifespan = "4.1 years"
        s.habitat = "rivers and streams"
        s.geolocation = "India"


class Animal(object): #borrowing stuff from the object class
    def __init__(self): #constructor


        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = 'Filler '
        self._close = '''
    </body>
</html>'''
        self.phylum = 0
        self.Class = 0
        self.order = 0
        self.family = 0
        self.genus = 0
        self.imgurl = 0
        self.average_lifespan = 0
        self.habitat = 0
        self.geolocation = 0


    def print_out(self):
            return  self._head + self._body + self._close

class snake(Animal):
    def __init__(self):
        #constructor function for super class
        super(snake, self).__init__() #Page.__init__()


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
            self._form_inputs += '<input type="' + item[1] + '"' + '"name=" ' + item[0]
        # if there is a third item add it in
            try:
               self._form_inputs += '" placeholder="' + item[2] + '" />'
        # other wise end the tag
            except:
                self._form_inputs += '" />'
        print self._form_inputs

        #POLYMORPHISM ALERT!!! --------------- method overriding
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
