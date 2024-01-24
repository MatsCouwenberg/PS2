from pyzbar.pyzbar import decode
import cv2

def read_qr_code(frame):
    decoded_objects = decode(frame)

    if decoded_objects:
        qr_code = decoded_objects[0]
        orientation = qr_code.orientation
        data = qr_code.data.decode('utf-8')
        return {"orientation": orientation, "data": data}
    else:
        return None

def continuous_qr_code_scan():
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

    qr_code_dict = {}  # Dictionary to store QR code data and orientation

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        qr_code_data = read_qr_code(frame)
        if qr_code_data:
            data = qr_code_data["data"]
            orientation = qr_code_data["orientation"]

            if data not in qr_code_dict:
                qr_code_dict[data] = orientation
                print("Added to dictionary:", data, orientation)


    cap.release()
    cv2.destroyAllWindows()

    print("Final QR Code Dictionary:", qr_code_dict)

if __name__ == "__main__":
    continuous_qr_code_scan()
