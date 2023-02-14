# NMEA Instruments


## PyQt/PySide with QML
Best for Raspberry Pi, microcontrollers, industrial and consumer electronics

When using PyQt and PySide you actually have two options for building your GUIs. We've already introduced the Qt Widgets API which is well-suited for building desktop applications. But Qt also provides a declarative API in the form of Qt Quick/QML.

Using Qt Quick/QML you have access to the entire Qt framework for building your applications. Your UI consists of two parts: the Python code which handles the business logic and the QML which defines the structure and behavior of the UI itself. You can control the UI from Python, or use embedded Javascript code to handle events and animations.

Qt Quick/QML is ideally suited for building modern touchscreen interfaces for microcontrollers or device interfaces -- for example, building interfaces for microcontrollers like the Raspberry Pi. However you can also use it on desktop to build completely customized application experiences, like those you find in media player applications like Spotify, or to desktop games.

Installation pip install pyqt6 or pip install pyside6

A simple Hello World app in PyQt6 with QML. Save the QML file in the same folder as the Python file, and run as normally.

# Examples
## main.py
´´´

import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

sys.exit(app.exec())

´´´

## main.qml
´´´

import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }

}

´´´
