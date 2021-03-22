import PySimpleGUI as sg
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

l = []
PATH = 'C:\Program Files (x86)\chromedriver.exe'
URL = 'https://www.komplett.dk/category/10412/hardware/pc-komponenter/grafikkort?nlevel=10000%C2%A728003%C2%A710412&hits=192'

class GraphicsCard:
    name = ''
    price = ''

    def __str__(self):
        return self.name + " - " + self.price


def main():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)

    elements = driver.find_elements_by_class_name('product-list-item')

    for element in elements:
        newGraphicsCard = GraphicsCard();
        newGraphicsCard.name = getElementText(element, '.product-link .text-content h2')
        newGraphicsCard.price = getElementText(element, '.product-price span.product-price-now')
        l.append(newGraphicsCard)
    layout = [[sg.Listbox(l, size=(100, 50), key='__list__')], [sg.Button("Close")], [sg.Button("Print")]]
    window = sg.Window("Graphicgards", layout)
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        # End program if user closes window or
        # presses the OK button
        if event == "Close":
            window.close()
            break


def getElementText(element, selector):
    try:
        return element.find_element_by_css_selector(selector).text
    except NoSuchElementException as e:
        return ''

layout = [[sg.Text("Webscrapping Komplett for graphicgards",size=(20, 0))], [sg.Button("Start", size=(30, 1))]]
window = sg.Window("Webscrapping", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Start":
        window.close()
        main()
        break


