import os
import time
try:
    for i in range(1, 52):
        with open(f"MDfile\\8A Roll no. {i}.docx", "w"):
            pass
except:
    pass
time.sleep(1)
try:
    for i in range(1, 52):
        os.remove(f"MDfile\\8A Roll no. {i}.docx")
except:
    pass


        
