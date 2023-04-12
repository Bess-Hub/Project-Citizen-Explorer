import requests
import xml.etree.ElementTree as ET

# Start by communicating with the API using the requests module
response = requests.get(url="https://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDeputados")

# Verify its status (remove # from line 8 to run the function)
# print(response)

# Verify its output language (remove # from line 11 to run the function)
# print(response.headers.get('content-type'))

# Now we know what we are dealing with... Text/XML
# If it was JSON the requests module already has its interpreter built in
# But for XML we will use ElementTree module

# Define root as the content of response and use ET to form string
root = ET.fromstring(response.content)

# Now we can play 8)
dep_name = []
dep_id = []
dep_foto = []
dep_uf = []
dep_gender = []

# Extract a list of names (remove the # to run the function)
for name in root.iter('nome'):
    dep_name.append(name.text)
    #print(*dep_name)
    
# Extract a list of ids (remove the # to run the function)
for id in root.iter('ideCadastro'):
    dep_id.append(id.text)
#    print(*dep_id)

# Extract a list of photo url (remove the # to run the function)
for urlFoto in root.iter('urlFoto'):
    dep_foto.append(urlFoto.text)
#    print(*dep_foto)

# Extract a list UF (remove the # to run the function)
for uf in root.iter('uf'):
    dep_uf.append(uf.text)
#    print(*dep_uf)

# Extract a list gender (remove the # to run the function)
for sexo in root.iter('sexo'):
    dep_gender.append(sexo.text)
#    print(*dep_gender)

# We can index dep_name and the other lists as the order of elements correspond to one another
# The first element of dep_id corresponds to the first congressperson listed in dep_name and so on

# Cucu attempt to spice things up, let's make a dropdown menu that allow us to select a congressperson from a menu
# The tkinter module worked for me on another exercise, it might work in this exercise as well
from tkinter import *

# We need an instance for a frame and some styling
win = Tk()
win.geometry("715x250")
win.title("Congressperson Selector")

# Lets set the menu
menu = StringVar()
menu.set("Select a Congressperson")

# Create a dropdown menu
drop = OptionMenu(win, menu, *dep_name)
drop.pack()

# Add a button
button = Button(win, text="Run, Forest!")
button.pack()

win.mainloop()

# Facing some issues, will study more and revisit.
