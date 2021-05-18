from time import sleep
from datetime import datetime as dt


class TrafficLight:
    _states = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    __color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self.__color = color
            start_state_time = dt.now()
            print(f"Светофор переключился на '{self.__color}' "
                  f"на {sw_time} секунд")
            sleep(sw_time)



a=TrafficLight()
a.running()