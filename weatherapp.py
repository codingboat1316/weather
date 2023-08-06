from tkinter import*
from tkinter import messagebox as mb
import requests
from PIL import Image
from datetime import datetime
import json


root = Tk()
root.title('Weather Application')
root.configure(bg='skyblue')
root.geometry("700x600")



def get_weather():
    global city
    city = city_input.get()
    


    API_key = "c97ec15b6e4e809999ea4b1d4210ba90"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']-273.15
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = (data['wind']['speed'])*3.6
        epoch_time = data['dt']
        date_time = datetime.fromtimestamp(epoch_time)
        desc = data['weather'][0]['description']
        cloudy = data['clouds']['all']


        timelabel.config(text=str(date_time))
        temp_field.insert(0,'{:.2f}'.format(temp)+"celcius")
        pressure_field.insert(0,str(pressure) + "hPa")
        humid_field.insert(0,str(humidity) + "%")
        wind_field.insert(0, '{:.2f}'.format(wind) + "km/h")
        cloud_field.insert(0,str(cloudy) +  "%")
        desc_field.insert(0,str(desc))
        
   

def reset():
    city_input.delete(0,END)
    temp_field.delete(0,END)
    pressure_field.delete(0,END)
    humid_field.delete(0,END)
    wind_field.delete(0,END)
    cloud_field.delete(0,END)
    desc_field.delete(0,END)
    timelabel.config(text='')


def get_forecast():
    url1 = 'https://wttr.in/{}.png'.format(city)
    response1 = requests.get(url1)
    path = 'forecast_weather.png'
    if response1.status_code == 200:
        with open(path,'wb')as f:
            f.write(response1.content)
    im = Image.open(path)
    im.show()


title = Label(root, text='Weather Detection And Forecast',fg='black',font=('times new roman',17,'bold','underline'),bg='skyblue')
label1=Label(root, text='Enter the city name:',font=('times new roman',15),bg='skyblue')
city_input=Entry(root,width=24,fg='black',font=12)
timelabel=Label(root,text='',font=('bold',14),fg='yellow')


btn_submit = Button(root, text='Get weather',width=10,font=('times new roman',13,'bold'),bd=5,bg='black',fg='white',command=get_weather)
btn_forecast = Button(root, text='Weather forecast',width=14,font=('times new roman',13,'bold'),bd=5,bg='black',fg='white',command=get_forecast)
btn_reset = Button(root,text='Reset',font=('times new roman',13,'bold'),bd=5,bg='white',fg='black',command=reset)


label2 = Label(root, text="Temperature:",font=('times new roman',15),bd=10,bg='skyblue')
label3 = Label(root, text="Pressure:",font=('times new roman',15),bd=5,bg='skyblue')
label4 = Label(root, text="Humidity:",font=('times new roman',15),bd=5,bg='skyblue')
label5 = Label(root, text="Wind:",font=('times new roman',15),bd=5,bg='skyblue')
label6 = Label(root, text="Cloudiness:",font=('times new roman',15),bd=5,bg='skyblue')
label7 = Label(root, text="Description:",font=('times new roman',15),bd=5,bg='skyblue')


temp_field = Entry(root,width=24,font=7)
pressure_field = Entry(root,width=24,font=7)
humid_field = Entry(root,width=24,font=7)
wind_field = Entry(root,width=24,font=7)
cloud_field = Entry(root,width=24,font=7)
desc_field = Entry(root,width=24,font=7)

title.grid(row=0,column=1,pady=10,padx=5)
label1.grid(row=1,column=0,padx=5,pady=5)
btn_submit.grid(row=2,column=1,pady=10)
label2.grid(row=3,column=0,padx=5,pady=5,sticky='w')
label3.grid(row=4,column=0,padx=5,pady=5,sticky='w')
label4.grid(row=5,column=0,padx=5,pady=5,sticky='w')
label5.grid(row=6,column=0,padx=5,pady=5,sticky='w')
label6.grid(row=7,column=0,padx=5,pady=5,sticky='w')
label7.grid(row=8,column=0,padx=5,pady=5,sticky='w')
btn_forecast.grid(row=9,column=1,pady=10)


city_input.grid(row=1,column=1,padx=5,pady=5)
temp_field.grid(row=3,column=1,padx=5,pady=5)
pressure_field.grid(row=4,column=1,padx=5,pady=5)
humid_field.grid(row=5,column=1,padx=5,pady=5)

wind_field.grid(row=6,column=1,padx=5,pady=5)
cloud_field.grid(row=7,column=1,padx=5,pady=5)
desc_field.grid(row=8,column=1,padx=5,pady=5)
btn_reset.grid(row=10,column=1,padx=5,pady=10)


             
root.mainloop()       
