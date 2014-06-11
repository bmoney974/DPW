'''
Bobby Newland
date 6-10-14
DPW
Simple Login
'''


import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): # declaring a class
    def get(self):  # function that starts everything. Catalyst
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Login Form</title>
        <style>
            .form_info {
                width:80%;
                display:block;
                margin:0px auto;
                border: 5px solid black;
                padding:20px;
                min-width:500px;

                }
                form {
                    width:500px;
                    margin:0px auto;
                    }

                h1,p {
                    text-align:center;
                    }

                .form_info p {
                    padding-bottom: 20px;
                    }

                form {
                    position:relative;
                    left:50px;
                    }

                    select {
                    position:relative;
                    left:45px;
                    margin-top:20px;
                    }

                    #checkbox, #checkbox2 {
                        position:relative;
                        left:45px;
                        margin-top:20px;
                        }

                    #check-label, #check-label2 {
                        position:relative;
                        left:55px;
                        margin-top:20px;
                        }

                        input[type="submit"] {
                            position:relative;
                            left:295px;
                            }

        </style>
    </head>
    <body>'''

        page_body = '''
        <h1>Join This Cool Site</h1>
        <div class= "form_info">
        <p>Fill out the form below</p>
        <form id="site" method="GET">
        <label>Name: </label><input type ="text" name="user" />
        <label>Email: </label><input type ="text" name="email" /><br />
        <select id="Gender" name ="gender" form="site">
            <option value="Male">Male</option>
            <option value="Female">Female></option>
        </select> <br />
        <input id="checkbox" type ="checkbox" name ="age" value="yes"><span id="check-label">I am over 18 years old</span> <br />
        <input id="checkbox2" type ="checkbox" name ="newsletter" value="yes"><span id="check-label2">Send me the newsletter</span> <br />
        <input type="submit" value="Submit" />'''

        page_close = '''
        </form>

    </body>

</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET["user"]
            email = self.request.GET["email"]
            gender = self.request.GET["gender"]
            newsletter = self.request.GET["newsletter"]
            age = self.request.GET["age"]
            self.response.write(page_head +"Name: " + user + ' ' + "Email: " + email + ' ' + "Gender: " +gender + ' ' + "Receive Newsletter: "+newsletter + ' ' + "Over 18: " + age + ' ' + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #Print









#never touch this below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
