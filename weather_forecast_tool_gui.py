from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk
import math
root=Tk()
root.title("Weather App")
root.geometry("750x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

def getMaxTemp(data, day):
    allMaxTemps = [data["list"][i]['main']['temp_max'] for i in range(day*8, day*8 + 8)]
    return max(allMaxTemps)
    
def getMinTemp(data, day):
    allMinTemps = [data["list"][i]['main']['temp_min'] for i in range(day*8, day*8 + 8)]
    return min(allMinTemps)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(api)
    json_data = response.json()
    

    base_url2 = "https://api.openweathermap.org/data/2.5/onecall"
    latitude = location.latitude
    longitude = location.longitude
    # api_2 = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&exclude=hourly,daily&appid={api_key}"
    api_2 = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"
    response_2 = requests.get(api_2)
    json_data2 = response_2.json()
    # print(json_data2)


    #current
    temp=json_data['main']['temp']
    humidity=json_data['main']['humidity']
    pressure=json_data['main']['pressure']
    wind=json_data['wind']['speed']
    description=json_data['weather'][0]['description']
    

    t.config(text=(math.ceil(temp-273.15),"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    #first cell
    firstdayimage=json_data2['list'][0]['weather'][0]['icon']
    
    photo1=ImageTk.PhotoImage(file=f"icons/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    # tempday1=str(math.ceil(json_data2['list'][0]['main']['temp'] -273.15))+"°C"
    # tempminday1=str(math.ceil(json_data2['list'][0]['main']['temp_min'] -273.15))+"°C"
    # tempmaxday1=str(math.ceil(json_data2['list'][0]['main']['temp_max'] -273.15))+"°C"

    # tempday1=str(json_data2['list'][0]['main']['temp'])+"°C"
    tempminday1=str(getMinTemp(json_data2, 0))+"°C"
    tempmaxday1=str(getMaxTemp(json_data2, 0))+"°C"

    #tempnight1=json_data2['list'][0]['main']['temp']

    day1temp.config(text=f"Min:{tempminday1}\n Max:{tempmaxday1}")


    #second cell
    seconddayimage=json_data2['list'][8]['weather'][0]['icon']
    
    img=(Image.open(f"icons/{seconddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    # tempday2=str(json_data2['list'][8]['main']['temp'])+"°C"
    tempminday2=str(getMinTemp(json_data2, 1))+"°C"
    tempmaxday2=str(getMaxTemp(json_data2, 1))+"°C"
    #tempnight2=json_data2['list'][1]['main'][0]['temp']['night']

    day2temp.config(text=f"Min:{tempminday2}\n Max:{tempmaxday2}")



    #third cell
    thirddayimage=json_data2['list'][16]['weather'][0]['icon']
    img=(Image.open(f"icons/{thirddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo3=ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    # tempday3=str(json_data2['list'][16]['main']['temp'])+"°C"
    tempminday3=str(getMinTemp(json_data2, 2))+"°C"
    tempmaxday3=str(getMaxTemp(json_data2, 2))+"°C"
    #tempnight2=json_data2['list'][1]['main'][0]['temp']['night']

    day3temp.config(text=f"Min:{tempminday3}\n Max:{tempmaxday3}")


    #fourth cell
    fourthdayimage=json_data2['list'][24]['weather'][0]['icon']
    img=(Image.open(f"icons/{fourthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo4=ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4

    # tempday4=str(json_data2['list'][24]['main']['temp'])+"°C"
    tempminday4=str(getMinTemp(json_data2, 3))+"°C"
    tempmaxday4=str(getMaxTemp(json_data2, 3))+"°C"
    #tempnight2=json_data2['list'][1]['main'][0]['temp']['night']

    day4temp.config(text=f"Min:{tempminday4}\n Max:{tempmaxday4}")


    #fifth cell
    fifthdayimage=json_data2['list'][32]['weather'][0]['icon']
    img=(Image.open(f"icons/{fifthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo5=ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    # tempday5=str(json_data2['list'][32]['main']['temp'])+"°C"
    tempminday5=str(getMinTemp(json_data2, 4))+"°C"
    tempmaxday5=str(getMaxTemp(json_data2, 4))+"°C"
    #tempnight2=json_data2['list'][1]['main'][0]['temp']['night']

    day5temp.config(text=f"Min:{tempminday5}\n Max:{tempmaxday5}")


    
    # #sixth cell
    # sixthdayimage=json_data2['list'][40]['weather'][0]['icon']
    # img=(Image.open(f"icons/{sixthdayimage}@2x.png"))
    # resized_image=img.resize((50,50))
    # photo6=ImageTk.PhotoImage(resized_image)
    # sixthimage.config(image=photo6)
    # sixthimage.image=photo6

    # tempday6=str(json_data2['list'][5]['main']['temp'])+"°C"
    # tempminday6=str(json_data2['list'][5]['main']['temp_min'])+"°C"
    # tempmaxday6=str(json_data2['list'][5]['main']['temp_max'])+"°C"
    # #tempnight2=json_data2['list'][1]['main'][0]['temp']['night']

    # day6temp.config(text=f"Temp:{tempday6}\n Min:{tempminday6}\n Max:{tempmaxday6}")


    # #seventh cell
    # seventhdayimage=json_data2['list'][6]['weather'][0]['icon']
    # img=(Image.open(f"icons/{seventhdayimage}@2x.png"))
    # resized_image=img.resize((50,50))
    # photo7=ImageTk.PhotoImage(resized_image)
    # seventhimage.config(image=photo7)
    # seventhimage.image=photo7

    # tempday7=str(json_data2['list'][6]['main']['temp'])+"°C"
    # tempminday7=str(json_data2['list'][6]['main']['temp_min'])+"°C"
    # tempmaxday7=str(json_data2['list'][6]['main']['temp_max'])+"°C"
    # #tempnight2=json_data2['list'][1]['main'][0]['temp']['night']

    # day7temp.config(text=f"Temp:{tempday7}\n Min:{tempminday7}\n Max:{tempmaxday7}")




    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second=first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third=first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth=first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth=first+timedelta(days=5)
    day5.config(text=fifth.strftime("%A"))

    # sixth=first+timedelta(days=6)
    # day6.config(text=sixth.strftime("%A"))

    # seventh=first+timedelta(days=7)
    # day7.config(text=seventh.strftime("%A"))





##icon
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)
Round_box=PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff", width = 200).place(x=30,y=110)

#label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label3=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=180)

label4=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=200)


##search box
Search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('popping',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file="Images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)


##Bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=35,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=305,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=405,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=505,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=605,y=30)
# Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
# Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)


#clock (here we will place time)
clock=Label(root,font=("Helvetica",30,'bold'), fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20), fg="white",bg="#57adff")
timezone.place(x=500,y=20)

long_lat=Label(root,font=("Helvetica",10), fg="white",bg="#57adff")
long_lat.place(x=500,y=50)

#thpwd
t=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)
h=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)
p=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)
w=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)
d=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

#first cell
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=40,y=315)

day1=Label(firstframe,font=('arial 20',10),bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#282829",width="90",height="60")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="#282829",fg="#57adff",font="arial 12 bold")
day1temp.place(x=80,y=50)

#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=310,y=325)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=5,y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=25)

day2temp=Label(secondframe,bg="#282829",fg="#fff",font="arial 8")
day2temp.place(x=2,y=70)

#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=410,y=325)

day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=5,y=5)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=25)

day3temp=Label(thirdframe,bg="#282829",fg="#fff",font="arial 8")
day3temp.place(x=2,y=70)

#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=510,y=325)

day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=5,y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=25)

day4temp=Label(fourthframe,bg="#282829",fg="#fff",font="arial 8")
day4temp.place(x=2,y=70)

#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=610,y=325)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=5,y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=25)

day5temp=Label(fifthframe,bg="#282829",fg="#fff",font="arial 8")
day5temp.place(x=2,y=70)

# #sixth cell
# sixthframe=Frame(root,width=70,height=115,bg="#282829")
# sixthframe.place(x=705,y=325)

# day6=Label(sixthframe,bg="#282829",fg="#fff")
# day6.place(x=10,y=5)

# sixthimage=Label(sixthframe,bg="#282829")
# sixthimage.place(x=7,y=20)

# day6temp=Label(sixthframe,bg="#282829",fg="#fff",font="arial 7")
# day6temp.place(x=2,y=70)

# #seventh cell
# seventhframe=Frame(root,width=70,height=115,bg="#282829")
# seventhframe.place(x=805,y=325)

# day7=Label(seventhframe,bg="#282829",fg="#fff")
# day7.place(x=10,y=5)

# seventhimage=Label(seventhframe,bg="#282829")
# seventhimage.place(x=7,y=20)

# day7temp=Label(seventhframe,bg="#282829",fg="#fff",font="arial 7")
# day7temp.place(x=2,y=70)

root.mainloop()
