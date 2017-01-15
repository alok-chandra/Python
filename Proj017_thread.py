import threading

class AlokMessenger(threading.Thread):
    def run(self):
       # print("Hola Hola")
        for _ in range(30):
            print("Sending message from thread: ",threading.current_thread().getName())

x=AlokMessenger(name="Send out Messages")
y=AlokMessenger(name="Receive Messages")
x.start()
y.start()

