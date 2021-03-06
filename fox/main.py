
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Animal()  #### deifines the main page to inherit from ####
        p.animals = [[snake()], [dog()], [cow()]] ### an array of each object
        self.response.write(p.print_out()) ### this prints out the actual page structure and html and also the buttons

        snake_sound = Animal()  #### snake properties that are displayed in the app
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

        dog_sound = Animal()   ### dog properties that are listed in the app
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
        dog_geolocation.Animal = "USA"

        cow_sound = Animal() # cow properties that are displayed in the app
        cow_sound.Animal = "Moo"
        cow_phylum = Animal()
        cow_phylum.Animal = "Chordata"
        cow_Class = Animal()
        cow_Class.Animal = "Mammalia"
        cow_order = Animal()
        cow_order.Animal = "Artiodactyla"
        cow_family = Animal()
        cow_family.Animal = "Bovidae"
        cow_genus = Animal()
        cow_genus.Animal = "Bos"
        cow_imgurl = Animal()
        cow_imgurl.Animal = "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/CH_cow_2.jpg/250px-CH_cow_2.jpg"
        cow_average_lifespan = Animal()
        cow_average_lifespan.Animal = "15 years"
        cow_habitat = Animal()
        cow_habitat.Animal = "fields and farms"
        cow_geolocation = Animal()
        cow_geolocation.Animal = "USA"


        if self.request.GET:

#### below is the conditional statement that tells the app which animals info to display when the button is clicked
            if self.request.GET['animal'] and self.request.GET['animal'] == 'Snake':
                ani = self.request.GET['animal']
                self.response.write("<div class='info'>" + "<br /><img src='" + snake_imgurl.Animal +"' />" + "<div class='data'>" +  "<br /> " + "<h2>" + ani + " species details below </h2> <br />" + "Phylum: " + snake_phylum.Animal + "<br />" + "Class: " + snake_Class.Animal + "<br />" + "Order: " + snake_order.Animal + "<br />" + "Family: " + snake_family.Animal + "<br />" + "Genus: " + snake_genus.Animal + "<br />" + "Average Lifespan: " + snake_average_lifespan.Animal + "<br />" + "Habitat: " + snake_habitat.Animal + "<br />" + "Geo-Location: " + snake_geolocation.Animal + "<br />" + "Makes a sound like: " + snake_sound.Animal + "</div></div>")
            elif self.request.GET['animal'] and self.request.GET['animal'] == "Dog":
                ani = self.request.GET['animal']
                self.response.write("<div class='info'>" +"<br /><img src='" + dog_imgurl.Animal +"' />" + "<div class='data'>" + "<br /> " + "<h2>" + ani + " species details below </h2> <br />" + "Phylum: " + dog_phylum.Animal + "<br />" + "Class: " + dog_Class.Animal + "<br />" + "Order: " + dog_order.Animal + "<br />" + "Family: " + dog_family.Animal + "<br />" + "Genus: " + dog_genus.Animal + "<br />" + "Average Lifespan: " + dog_average_lifespan.Animal + "<br />" + "Habitat: " + dog_habitat.Animal + "<br />" + "Geo-Location: " + dog_geolocation.Animal + "<br />" + "Makes a sound like: " + dog_sound.Animal + "</div></div>")
            elif self.request.GET['animal'] and self.request.GET['animal'] == "Cow":
                ani = self.request.GET['animal']
                self.response.write("<div class='info'>" +"<br /><img src='" + cow_imgurl.Animal +"' />" + "<div class='data'>" + "<br /> " + "<h2>" + ani + " species details below </h2> <br />" + "Phylum: " + cow_phylum.Animal + "<br />" + "Class: " + cow_Class.Animal + "<br />" + "Order: " + cow_order.Animal + "<br />" + "Family: " + cow_family.Animal + "<br />" + "Genus: " + cow_genus.Animal + "<br />" + "Average Lifespan: " + cow_average_lifespan.Animal + "<br />" + "Habitat: " + cow_habitat.Animal + "<br />" + "Geo-Location: " + cow_geolocation.Animal + "<br />" + "Makes a sound like: " + cow_sound.Animal + "</div></div>")
            else:
                pass





        # self.response.write(p.print_out)
class Animal(object): ##### this is the main object that all other objects inherit from
    def __init__(self): #constructor


##### below is the html page structure set up and css styles

        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Animal Database</title>
    <style>
            # body{
            # background:green;
            }

            .info {
                width:960px;
                min-width:960px;
                display:block;
                margin:0px auto;
                border: 2px black solid;
                padding:20px;
                height:450px;
                background:#FFFAFA;

                }

            .data {
                float:left;
                margin-right:30px;
                }

            .info img, .data {
                position:relative;
                left:200px;
                }

            .info img {
                position:relative;
                top:40px;
                }

            .btns {
                 width: 100%;
                 display:block;
                 position:relative;
                 left:630px;
                 margin-bottom:50px;
                 margin-top:30px;

                 }

            .instructions {
                text-align:center
                }

            .header {
                text-align: center;
                background:#025949;
                padding:40px;
                position:relative;
                top:-20px;
                }

            .header h1 {
                color:white;
                }

    </style>

    </head>

    <body>'''

        self._body = '''

<div class="header"><h1>Animal Database</h1></div>

<div class = "btns">

<a href=?animal=Snake><button>Snake</button></a>
<a href=?animal=Dog><button>Dog</button></a>
<a href=?animal=Cow><button>Cow</button></a>
</div>
<div class="instructions"><p>View each animal's information</p></div>
        '''
        self._close = '''

    </body>
</html>'''



    def print_out(self): ### these are the actual instances of each section of the page html this displays the content on the page
        return self._body + self._head + self._close




class snake(Animal): #### the snake object which inherits from the main animal class and contains the animal data
    def __init__(self):
        #constructor function for super class
        super(snake, self).__init__() #Page.__init__()
        self.__sound = "hsss"




    @property
    def sound(self, value):
        return self.__sound + self.__phylum  #### getter for the snake class

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







class dog(Animal): #### the dog object which inherits from the main animal class and contains the animal data
    def __init__(self):
        #constructor function for super class
        super(dog, self).__init__() #Page.__init__()

    @property
    def sound(self, value):### dog getter
        return self.__sound
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






class cow(Animal): #### the cow object which inherits from the main animal class and contains the animal data
    def __init__(self):
        #constructor function for super class
        super(cow, self).__init__() #Page.__init__()

    @property
    def sound(self, value):  #### cow getter
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







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
