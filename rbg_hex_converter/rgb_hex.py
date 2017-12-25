"""RGB-HEX Converter"""

def rgb_hex():
  invalid_msg = "The input is not valid."
  red = int(raw_input("Enter the amount of red( 0 to 255 ): "))
  if red < 0 or red > 255:
    print invalid_msg
    return 0
  green = int(raw_input("Enter the amount of green( 0 to 255 ): "))
  if green < 0 or green > 255:
    print invalid_msg
    return 0
  blue = int(raw_input("Enter the amount of blue( 0 to 255 ): "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return 0
  val = (red << 16) + (green << 8) + blue
  hex_val = hex(val).upper()
  print hex_val

def hex_rgb():
  invalid_msg = "The input is not valid."
  hex_val =  raw_input("Enter an HEX Color: ")
  if len(hex_val) != 6:
    print invalid_msg
    return 0
  else:
    hex_val = int(hex_val,16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Red: %s, Green: %s, Blue: %s" % (str(red),str(green),str(blue))

def convert():
  
  while(True):
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      print "RGB to Hex..."
      rgb_hex()
    elif option == '2':
      print "Hex to RGB..."
      hex_rgb()
    elif option == 'x' or option == 'X':
      break
    else:
      print "Invalid option..."

convert()