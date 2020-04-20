from adafruit_circuitplayground.express import cpx

while True:
  temp_c = cpx.temperature
  temp_f = temp_c*1.8 + 32
  print(temp_c)
  print(temp_f)
