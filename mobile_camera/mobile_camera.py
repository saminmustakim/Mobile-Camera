import urllib.request
import cv2
import numpy as np

def mobile_camera(ip_address):
    if ip_address.endswith("/"):
        ip = ip_address+"shot.jpg"
    else:
        ip = ip_address+"/"+"shot.jpg"
    url = ip
    while True:
        im_array = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
        img = cv2.imdecode(im_array, -1)
        cv2.imshow("IPWebcam", img)
        q = cv2.waitkey(0)
        if q == ord("q"):
            break
        cv2.destroyAllWindows()
