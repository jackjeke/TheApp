##from kivymd.uix.dialog import MDInputDialog
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton

from urllib import parse
from kivy.network.urlrequest import UrlRequest
import certifi
from kivy.clock import Clock
##textinput = TextInput(text='Hello world')



class SearchPopup(MDDialog):
    
    def __init__(self,**kwargs):
        super(). __init__(**kwargs)
        
##        self.buttons=[search_button]

   
    
        bxlyout=BoxLayout(orientation='vertical')
        self.txt_inp=Label(text='Search By Name',color='black')
        self.txt_inp1=TextInput(text='',multiline=False,on_text_validate=self.printer)
        search_button=MDFlatButton(text='Take Me There',on_release=self.printer)
        
        bxlyout.add_widget(self.txt_inp)
        bxlyout.add_widget(self.txt_inp1)
##        bxlyout.add_widget(search_button)
        self.add_widget(bxlyout)
        self.size_hint=0.4,0.1

    def printer(self,*args):
##        print('Hie')
        address=self.txt_inp1.text
        print(address)
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        app_code ='3ZQHy8U1DD2BY5PCYAr6X4dkIJfWCvqxE6jfKX4anpI'
        app_id='yi3pflkQKYiZgEilQW8b'
        address = parse.quote(address)
        url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())

    def success(self, urlrequest, result):
        print("Success")
        print(result)
    def error(self, urlrequest, result):
        print("Error")
        print(result)
    def failure(self, urlrequest, result):
        print("Failure")
        print(result)
   
    
##    text_button_ok='Find Location'
    
