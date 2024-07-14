import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
cam = cv2.VideoCapture(0)


def face_detec(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(optimized_frame, scaleFactor=1.1, minNeighbors=(3))
    return faces

def box_face(frame):
    for x, y, w, h in face_detec(frame):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)


def close_all():
    cam.release()
    cv2.destroyAllWindows()
    exit()
    
    
def main():
    while True:
        _, frame = cam.read()
        box_face(frame)
        cv2.imshow("FaceTes AI", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_all()
  

if __name__ == '__main__':
    main()