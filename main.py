import turtle
import time
import json
import urllib.request

ISS_URL = "http://api.open-notify.org/iss-now.json"
ASTRONAUTS_URL = "http://api.open-notify.org/astros.json"
astronauts_response = urllib.request.urlopen(ASTRONAUTS_URL)
astronauts = json.loads(astronauts_response.read())

print ("Welcome to ISS Search, an instant look at the International Space Station!")
input("Press enter when you are ready to continue...")
print ("Currently, these astronauts are on the international space station")
time.sleep(1)
for a in astronauts["people"]:
	print (a["name"])

input ("Press enter when you're ready to see where it is...")
	
window = turtle.Screen()
window.setup(720,360)
window.setworldcoordinates(-180, -90, 180, 90)
window.bgpic("world_map.png")
window.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
	iss_response = urllib.request.urlopen(ISS_URL)
	iss_stats = json.loads(iss_response.read())
	longitude = (iss_stats["iss_position"]["longitude"])
	latitude = (iss_stats["iss_position"]["latitude"])
	iss.goto(float(longitude),float(latitude))
	time.sleep(1)
exit()
	

