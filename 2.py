RGB = {
'RED' : (255,0,0),
'ff0000' : (255,0,0),
'GREEN' : (0,255,0),
'00ff00' : (0,255,0),
'BLUE' : (0,0,255),
'00000ff' : (0,0,255),
}
key = input("Введите ключ: ")
if key in RGB.keys():
    print(RGB[key])