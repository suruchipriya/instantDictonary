from distutils.version import LooseVersion
import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    div1 = jp. Div(a=div, classes="grid grid-cols-3 gap-4 p-4 border border-black")

    jp.Input(a=div1, placeholder="Enter first Value", classes="font-input")
    jp.Input(a=div1, placeholder="Enter second value", classes="font-input")
    jp.Div(a=div1,text="Result goes here...", classes="text-gray-600")
    jp.Div(a=div1, text="Just another div...",classes="text-gray-608")
    jp.Div(a=div1, text="Yet another div", classes="text-gray-600")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")

    jp.Button(a=div2, text="Calculate",
              classes="border border-blue-500 =-2 py-1 px-4 rounded"
        "text-blue-600 hover:bg-red-500 hover:text-white")

    jp. Div(a=div2, text="I an a cool interactive div!")

    return wp

#jp.Route("/home", home)

jp.justpy()

# netstat -ano | findstr :8000
# taskkill /pid 67687 /F
