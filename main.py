import tkinter as tk
import requests
from PIL import Image,ImageTk #pip install pillow

root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")

#Key: 8e9472e54c81f5db1c429c82e639d7d1
#API: api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description'].title()
        temp = weather['main']['temp']
        windspeed = weather['wind']['speed']
        final_str = f'City: {city}\nCondition: {condition}\nTemperature: {temp} °F\nWindspeed: {windspeed} mph'
    except Exception as e:
        final_str = 'There was a problem retrieving that information'
        print("Error:", e)
    return final_str

     




def get_weather(city):
    weather_key='8e9472e54c81f5db1c429c82e639d7d1'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    # print(response.json())
    weather=response.json()

   # print(weather['name'])
   # print(weather['weather'][0]['description'])
   # print(weather['main']['temp'])
   # print(weather['wind']['speed'])


    result['text']=format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon_name):
    icon_url = f"http://openweathermap.org/img/wn/{icon_name}@2x.png"
    icon_response = requests.get(icon_url, stream=True)
    if icon_response.status_code == 200:
        icon_data = icon_response.raw
        icon_image = Image.open(icon_data)
        icon_image = icon_image.resize((100, 100), Image.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Label to display icon
        icon_label = tk.Label(frame_two, image=icon_photo, bg="white")
        icon_label.image = icon_photo  # Keep a reference
        icon_label.place(x=40, y=5)  # You can adjust x/y




 
img=Image.open('./bp.png')
img=img.resize((600,500),Image.LANCZOS)
img_photo=ImageTk.PhotoImage(img)

bp_lbl=tk.Label(root,image=img_photo)
bp_lbl.place(x=0,y=0,width=600,height=500)



heading_title=tk.Label(bp_lbl,text='Earth including over 200,000 cities!',fg='purple',bg='sky blue',font=('times new roman',18,'bold'))
heading_title.place(x=80,y=18)


frame_one=tk.Frame(bp_lbl,bg="#FFFF00",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')



btn=tk.Button(frame_one,text='get weather',fg='red',font=('times new roman',17,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)


frame_two=tk.Frame(bp_lbl,bg="#98FF98",bd=5)
frame_two.place(x=80,y=130,width=450,height=310)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='ne')
result.place(relwidth=1,relheight=1)


root.mainloop()
