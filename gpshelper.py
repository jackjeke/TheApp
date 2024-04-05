from kivymd.app import MDApp
from gpsblinker import GpsBlinker
class GpsHelper():
    def run (self):
##        pass
        #starts blinking gPS blinker

        #get reference to GpsBlinker then call blink()

        gps_blinker=MDApp.get_running_app().root.ids.my_blinker
        gps_blinker.blink()
##        GpsBlinker().blink()
