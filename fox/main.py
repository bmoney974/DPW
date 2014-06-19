
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #snake
        # s = snake()
        # s.phylum = "Chordata"
        # s.Class = "Reptilia"
        # s.order = "Squamata"
        # s.family = "Acrochordidae"
        # s.genus = "Acrochordus"
        # s.imgurl = "http://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Wart_snake_1.jpg/220px-Wart_snake_1.jpg"
        # s.average_lifespan = "4.1 years"
        # s.habitat = "rivers and streams"
        # s.geolocation = "India"
        # s.sound = "hsss"
        #
        # #dog
        # d = Animal()
        # d.phylum = "Chordata"
        # d.Class = "Mammalia"
        # d.order = "Carnivora"
        # d.family = "Canidae"
        # d.genus = "Canis"
        # d.imgurl = "http://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/260px-YellowLabradorLooking_new.jpg"
        # d.average_lifespan = "10-13 years"
        # d.habitat = "homes and yards"
        # d.geolocation = "USA"
        #
        # #cow
        # c = Animal()
        # c.phylum = "Chordata"
        # c.Class = "Mammalia"
        # c.order = "Artiodactyla"
        # c.family = "Bovidae"
        # c.genus = "Bos"
        # c.imgurl = "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/CH_cow_2.jpg/250px-CH_cow_2.jpg"
        # c.average_lifespan = "4.1 years"
        # c.habitat = "fields and farms"
        # c.geolocation = "USA"

        p = Animal()
        p.animals = [['snake'], ['dog'], ['cow']]
        self.response.write(p.print_out())

class Animal(object): #borrowing stuff from the object class
    def __init__(self): #constructor



        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = '''
<a href=?animal=Snake><button>Snake</button></a>
<a href=?animal=Dog><button>Dog</button></a>
<a href=?animal=Cow><button>Cow</button></a>

        '''
        self._close = '''
    </body>
</html>'''


        # self._phylum = 0
        # self._Class = 0
        # self._order = 0
        # self._family = 0
        # self._genus = 0
        # self._imgurl = 0
        # self._average_lifespan = 0
        # self._habitat = 0
        # self._geolocation = 0
        # self._sound = "growl"




    def print_out(self):
        return self._head + self._body + self._close + str(snake_sound.Animal + " " + dog_sound.Animal + " " + cow_sound.Animal + " " + snake_phylum.Animal + " " + snake_Class.Animal + " " + dog_Class.Animal)



# snd = Animal()
# snd.Animal = "hsss"
# print snd.Animal

class snake(Animal):
    def __init__(self):
        #constructor function for super class
        super(snake, self).__init__() #Page.__init__()
        self.__sound = "hsss"





    @property
    def sound(self, value):
        return self.__sound + self.__phylum

    @sound.setter
    def sound(self, value):
        self.__sound = value
        self.__phylum = value
        self.__Class = value
        self.__order = value
        self.__family = value
        self.__genus = value
        self.__imgurl = value
        self.__average_lifespan = value
        self.__habitat = value
        self.__geolocation = value
        # self.__sound = "growl"


snake_sound = Animal()
snake_sound.Animal = "Hsss"
snake_phylum = Animal()
snake_phylum.Animal = "Chordata"
snake_Class = Animal()
snake_Class.Animal = "Reptilia"
snake_order = Animal()
snake_order.Animal = "Squamata"
snake_family = Animal()
snake_family.Animal = "Acrochordidae"
snake_genus = Animal()
snake_genus.Animal = "Acrochordus"
snake_imgurl = Animal()
snake_imgurl.Animal = "http://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Wart_snake_1.jpg/220px-Wart_snake_1.jpg"
snake_average_lifespan = Animal()
snake_average_lifespan.Animal = "4.1 years"
snake_habitat = Animal()
snake_habitat.Animal = "Rivers and Streams"
snake_geolocation = Animal()
snake_geolocation.Animal = "India"
print snake_sound.Animal




class dog(Animal):
    def __init__(self):
        #constructor function for super class
        super(dog, self).__init__() #Page.__init__()

    @property
    def sound(self, value):
        return self.__sound
    @sound.setter
    def sound(self, value):
        self.__sound = value
        self.__sound = value
        self.__phylum = value
        self.__Class = value
        self.__order = value
        self.__family = value
        self.__genus = value
        self.__imgurl = value
        self.__average_lifespan = value
        self.__habitat = value
        self.__geolocation = value

dog_sound = Animal()
dog_sound.Animal = "Woof"
dog_phylum = Animal()
dog_phylum.Animal = "Chordata"
dog_Class = Animal()
dog_Class.Animal = "Mammalia"
dog_order = Animal()
dog_order.Animal = "Carnivora"
dog_family = Animal()
dog_family.Animal = "Canidae"
dog_genus = Animal()
dog_genus.Animal = "Canis"
dog_imgurl = Animal()
dog_imgurl.Animal = "http://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/260px-YellowLabradorLooking_new.jpg"
dog_average_lifespan = Animal()
dog_average_lifespan.Animal = "10 - 3 years"
dog_habitat = Animal()
dog_habitat.Animal = "homes and yards"
dog_geolocation = Animal()
snake_geolocation.Animal = "USA"




class cow(Animal):
    def __init__(self):
        #constructor function for super class
        super(cow, self).__init__() #Page.__init__()

    @property
    def sound(self, value):
        return self.__sound
    @sound.setter
    def sound(self, value):
        self.__sound = value

cow_sound = Animal()
cow_sound.Animal = "Moo"
print cow_sound.Animal




    # @property
    # def animals(self):
    #     return
    #     pass
    # #
    # @animals.setter
    # def animals(self, arr):
    #     #change my private inputs variable
    #     self.__animals = arr
    #     #sort through the mega array and create HTML inputs based on the info there
    #     for item in arr:
    #         self._form_inputs += '<input type="' + item[1] + '"' + '"name=" ' + item[0]
    #     # if there is a third item add it in
    #         try:
    #            self._form_inputs += '" placeholder="' + item[2] + '" />'
    #     # other wise end the tag
    #         except:
    #             self._form_inputs += '" />'
    #     print self._form_inputs
    #
    #     #POLYMORPHISM ALERT!!! --------------- method overriding
    # def print_out(self):
    #     return self._head + self._body + self._form_open + self._form_inputs + self._form_close
    #
    #





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
