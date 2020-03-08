from .baseTest import BaseTest

class ArduinoTest(BaseTest):
    def __init__(self, device, **kwargs):
        # Pass arguments that werent explicitly defined to parent class
        # Set up device in parent class
        super().__init__(device, **kwargs) 
    
    def test(self):
        print("Hoping its a "+hex(65))
        r = self.device.readBytes(1)
        print(r)
        print("Pass" if r == b'\x41' else "Fail!")


