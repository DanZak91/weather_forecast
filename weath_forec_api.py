import sys
import time
import requests

from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPointF, QByteArray


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.labels = QLabel(self)
        self.labels.move(-200, 0)
        self.labels.setFixedSize(947, 480)
        self.movie = QMovie('C:\\Users\OperatorDZ\Desktop\Api\dist\obla.gif')
        self.labels.setMovie(self.movie)
        self.movie.start()

        loadUi(".ui\weather.ui", self)

        # with open(r'C:\\Users\OperatorDZ\Desktop\Api\ekb.json') as file:
        #     pogoda = json.load(file)
        url = 'http://api.weatherapi.com/v1/forecast.json?key=1fc443927c364e4e8b5105921232205&q=Ekaterinburg&days=5' \
              '&aqi=yes&alerts=yes '
        response = requests.get(url)
        pogoda = response.json()

        self.city.setText(pogoda['location']['name'])
        self.oblast.setText(pogoda['location']['region'])
        self.vremya_city.setText(f"Local time: \n{time.ctime(pogoda['location']['localtime_epoch'])}")
        self.temperature.setText(f"+{int(pogoda['current']['temp_c'])} °C" if int(pogoda['current']['temp_c']) > 0
                                 else f"{int(pogoda['current']['temp_c'])} °C")
        self.opisan.setText(pogoda['current']['condition']['text'])
        self.data_obnovlen.setText(time.ctime(pogoda['current']['last_updated_epoch']))
        self.wind_kph.setText(f"Wind: {pogoda['current']['wind_kph']} kph")
        self.humidity.setText(f"Humidity: {pogoda['current']['humidity']}%")
        self.chance_of_rain.setText(
            f"Chance of rain: {pogoda['forecast']['forecastday'][0]['day']['daily_chance_of_rain']}%")

        self.icon_pogoda_pix = QPixmap()
        self.icon_pogoda_pix.loadFromData(
            QByteArray(requests.get(f"https:{pogoda['current']['condition']['icon']}").content))
        self.icon_pogoda = QLabel(self)
        self.icon_pogoda.setPixmap(self.icon_pogoda_pix)
        self.icon_pogoda.move(280, 140)
        self.icon_pogoda.resize(64, 64)
        self.icon_pogoda.setStyleSheet('background: transparent;')

        def shadow(x):
            shadows1 = QGraphicsDropShadowEffect(blurRadius=20.0, color=QColor("#1f90bd"), offset=QPointF(5.0, 5.0))
            shadows2 = QGraphicsDropShadowEffect(blurRadius=5.0, color=QColor("#140002"), offset=QPointF(5.0, 5.0))
            shadows3 = QGraphicsDropShadowEffect(blurRadius=1.0, color=QColor("#7D3507"), offset=QPointF(5.0, 5.0))
            if x == 1:
                return shadows1
            elif x == 2:
                return shadows2
            else:
                return shadows3

        self.icon_pogoda.setGraphicsEffect(shadow(1))
        self.temperature.setGraphicsEffect(shadow(1))
        self.city.setGraphicsEffect(shadow(1))
        self.oblast.setGraphicsEffect(shadow(1))
        self.vremya_city.setGraphicsEffect(shadow(1))
        self.opisan.setGraphicsEffect(shadow(1))
        self.data_obnovlen.setGraphicsEffect(shadow(1))
        self.wind_kph.setGraphicsEffect(shadow(1))
        self.humidity.setGraphicsEffect(shadow(1))
        self.chance_of_rain.setGraphicsEffect(shadow(1))
        self.shapka.setGraphicsEffect(shadow(3))

        self.date_today.setGraphicsEffect(shadow(2))
        self.date_tomorrow.setGraphicsEffect(shadow(2))
        self.date_after_tomorrow.setGraphicsEffect(shadow(2))

        self.temp_today.setGraphicsEffect(shadow(2))
        self.temp_tomorrow.setGraphicsEffect(shadow(2))
        self.temp_after_tomorrow.setGraphicsEffect(shadow(2))

        # CO = pogoda['current']['air_quality']['co']
        # O3 = pogoda['current']['air_quality']['o3']
        # SO2 = pogoda['current']['air_quality']['so2']
        # us_epa_index = pogoda['current']['air_quality']['us-epa-index']

        # Погода на последующие дни
        self.date_today.setText(pogoda['forecast']['forecastday'][0]['date'])
        self.date_tomorrow.setText(pogoda['forecast']['forecastday'][1]['date'])
        self.date_after_tomorrow.setText(pogoda['forecast']['forecastday'][2]['date'])

        self.temp_today.setText(
            f"{int(pogoda['forecast']['forecastday'][0]['day']['maxtemp_c'])}°/ {int(pogoda['forecast']['forecastday'][0]['day']['mintemp_c'])}°")
        self.temp_tomorrow.setText(
            f"{int(pogoda['forecast']['forecastday'][1]['day']['maxtemp_c'])}°/ {int(pogoda['forecast']['forecastday'][1]['day']['mintemp_c'])}°")
        self.temp_after_tomorrow.setText(
            f"{int(pogoda['forecast']['forecastday'][2]['day']['maxtemp_c'])}°/ {int(pogoda['forecast']['forecastday'][2]['day']['mintemp_c'])}°")

        self.icon_pogoda_today_pix = QPixmap()
        self.icon_pogoda_today_pix.loadFromData(
            QByteArray(
                requests.get(f"https:{pogoda['forecast']['forecastday'][0]['day']['condition']['icon']}").content))
        self.icon_pogoda_today = QLabel(self)
        self.icon_pogoda_today.setPixmap(self.icon_pogoda_today_pix)
        self.icon_pogoda_today.move(60, 305)
        self.icon_pogoda_today.resize(64, 64)
        self.icon_pogoda_today.setStyleSheet('background: transparent;')

        self.icon_pogoda_tomorrow_pix = QPixmap()
        self.icon_pogoda_tomorrow_pix.loadFromData(
            QByteArray(
                requests.get(f"https:{pogoda['forecast']['forecastday'][1]['day']['condition']['icon']}").content))
        self.icon_pogoda_tomorrow = QLabel(self)
        self.icon_pogoda_tomorrow.setPixmap(self.icon_pogoda_tomorrow_pix)
        self.icon_pogoda_tomorrow.move(266, 305)
        self.icon_pogoda_tomorrow.resize(64, 64)
        self.icon_pogoda_tomorrow.setStyleSheet('background: transparent;')

        self.icon_pogoda_after_tomorrow_pix = QPixmap()
        self.icon_pogoda_after_tomorrow_pix.loadFromData(
            QByteArray(
                requests.get(f"https:{pogoda['forecast']['forecastday'][2]['day']['condition']['icon']}").content))
        self.icon_pogoda_after_tomorrow = QLabel(self)
        self.icon_pogoda_after_tomorrow.setPixmap(self.icon_pogoda_after_tomorrow_pix)
        self.icon_pogoda_after_tomorrow.move(466, 305)
        self.icon_pogoda_after_tomorrow.resize(64, 64)
        self.icon_pogoda_after_tomorrow.setStyleSheet('background: transparent;')

        self.icon_pogoda_today.setGraphicsEffect(shadow(2))
        self.icon_pogoda_tomorrow.setGraphicsEffect(shadow(2))
        self.icon_pogoda_after_tomorrow.setGraphicsEffect(shadow(2))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
