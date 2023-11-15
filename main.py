from time import sleep
import bluetooth
import board
import digitalio
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
kit.servo[5].actuation_range = 160
angulo = 60

voz = digitalio.DigitalInOut(board.D17)
voz.direction = digitalio.Direction.OUTPUT
voz.value = False

led1 = digitalio.DigitalInOut(board.D24)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D26)
led2.direction = digitalio.Direction.OUTPUT


perigo = digitalio.DigitalInOut(board.D6)
perigo.direction = digitalio.Direction.INPUT

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)
 
port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
 
bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("iniciando")
print("Waiting for connection on RFCOMM channel", port)
 
client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

try:
 while True:
    data = client_sock.recv(1024)
   
    if str(data) == "b'N0#'":
         print("frente")
         kit.continuous_servo[2].throttle = -0.5
         kit.continuous_servo[1].throttle = 0.5
         sleep(0.3)
         kit.continuous_servo[2] .throttle = 0
         kit.continuous_servo[1].throttle = 0
         
    if str(data) == "b'S0#'":
         print("ré")
         kit.continuous_servo[2].throttle = 0.5
         kit.continuous_servo[1].throttle = -0.5
         sleep(0.3)
         kit.continuous_servo [2] .throttle = 0
         kit.continuous_servo[1].throttle = 0
     
    if str(data) == "b'W0#'":
         print("esquerda")
         kit.continuous_servo[2].throttle = -0.5
         sleep(0.3)
         kit.continuous_servo [2] .throttle = 0
        
    if str(data) == "b'E0#'":
         print("direita")
         kit.continuous_servo[1].throttle = 0.5
         sleep(0.3)
         kit.continuous_servo [1] .throttle = 0   
         
    if str(data) == "b'04#'":
        led1.value=True
        led2.value=True
        print("farol")
             
    if str(data) == "b'01#'":    
        voz.value = True
        print("Apresentando")
                
    if str(data) == "b'03#'":
        try:
            angulo = angulo - 5
            kit.servo[5].angle = angulo
            print(angulo)
        except:
            print("angulo máximo atingido")
                
    if str(data) == "b'02#'":
        try:
            angulo = angulo + 5
            kit.servo[5].angle = angulo
            print(angulo)
        except: 
            print("angulo máximo atingido")                     
    
    if perigo.value == True:
           
         kit.continuous_servo[2] .throttle = 0
         kit.continuous_servo[1].throttle = 0
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 60
         print("Risco de Queda")
    
    if not data:
        break
        print(str(data))
except OSError:
 pass 
print("Disconnected.")
client_sock.close()
server_sock.close()
print("All done.")







    

