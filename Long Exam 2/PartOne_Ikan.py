1. 
"""
Procedural Programming involves structured programming.
On the other hand, Object Oriented Programming focuses more on identification of classes of objects. In OOP, parang nasisimplify niya ang mga bagay bagay 
kasi the object will be contained in a class. At sa loob ng class, nadedefine ang mismong object, nadedescribe ang kaniyang mga attributes, and nadedefine 
kung ano ang mga kaya niyang iperform. tapos pwede pang gamit gamitin or ulit ulitin yung mga name/procedures thru inheritance; 
unlike procedural programming na dapat isang beses lang madefine para hindi magkaroon ng error.
Moreover, Procedural Programming is more tedious to do than OOP because it's usually longer and you have to repeat the same procedure/codes for another related variable. 
"""


2.
"""
Graphical User Interface (GUI) is a software that presents multiple visual components. It displays objects that can convey information, and it represents actions
that can be done by the user. In geomatics, GUI can be used for easier visualization of geomatics-related phenomena. For example, we can use/make GUI to create an 
application na pinapakita ang mga [residential, commercial, agricultural, etc.,] areas pati na rin ang iba't ibang hazards and risk na nakapaligid sa isang town. We
can design it like how battle royales sa mobile games are designed para naeexplore 'yung town hehe.
"""

3. 
"""
Nangyayari ang operation overloading kapag nag-inherit ang child class ng mga methods mula sa parent class and inimpliment ito ng child class sa ibang paraan.
Moreover, nagkakaroon ng operation overloading kapag maraming classes ang gumagamit ng iisang interface lamang. 


"""

4.
"""

In Inheritance, mayroong parent or superclass, and child or subclass. Child classes can inherit attributes/methods from their parent class. We use inheritance
para hindi maging redundant 'yung mga codes natin.
For example, we want to create codes that can compute for the latitude of our traverse. we can start with 
class Lines:
    def (self, distance, azimuth):
        self.distance = distance
        self.azimuth = azimuth
class Latitude (Lines): -----> In this part, ininherit ng subclass na Latitude ang kaniyang parent class na Lines. 
    def (self):
        return -self.distance * cos (self.azimuth)  ---> As we can see, hindi na muli idinefine 'yung self.distance and self.azimuth. Parang kinuha na lang noong
    child class ang attributes ng kaniyang parent class to create its own method. In this way, hindi nagiging redundant 'yung codes natin.

"""

5.

"""


Front-end is the user interface. Ito ang mga nakikita natin na visual elements sa isang app/website (like buttons, text, etc). While, ang back-end naman ang gumagawa ng dirty works for the whole
system. Ito ang nagrereceive, nagpprocess, and nagsesend ng requests na nagmula sa user. On the other hand, databases are the ones who store all the data needed
for the system. Ito ang nagbibigay ng data na nirequest ng server.
For instance, tumingin tayo sa isang interactive na map displaying the hazards that surround a place. Lahat ng nakikita natin sa website ay ang front end.
if we want to see the hazards surrounding a specific place, the backend will receive our request and it will send a request sa database to supply the needed information.
Then, once na nagkaroon na ng data, issend/ipprocess na ulit ito ng backend para magreflect sa atin yung desired map natin.


"""