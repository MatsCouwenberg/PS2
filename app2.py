from flask import Flask, render_template
from pyzbar.pyzbar import decode
import cv2

app = Flask(__name__)


# Function to read QR code from a frame
def read_qr_code(frame):
    decoded_objects = decode(frame)

    if decoded_objects:
        qr_code = decoded_objects[0]
        orientation = qr_code.orientation
        data = qr_code.data.decode('utf-8')

        if orientation == 'UP':
            letter_orientation = 'A'
        elif orientation == 'RIGHT':
            letter_orientation = 'B'
        elif orientation == 'DOWN':
            letter_orientation = 'C'
        elif orientation == 'LEFT':
            letter_orientation = 'D'
        else:
            letter_orientation = orientation

        return {"orientation": letter_orientation, "data": data}
    else:
        return None


def continuous_qr_code_scan():
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    qr_code_dict = {}  # Dictionary to store QR code data and orientation
    scanned_count = 0

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
                scanned_count += 1
                print("Added to dictionary:", data, orientation)

            if scanned_count == 2:
                yield qr_code_dict
                break

        key = cv2.waitKey(1)
        if key == 27:  # ASCII code for 'esc' key
            break

    cap.release()
    cv2.destroyAllWindows()


@app.route('/')
def index():
    global qr_code_dict
    updates = continuous_qr_code_scan()

    # Include the first element directly in the loop
    for update in updates:
        qr_code_dict = update
        break

    if qr_code_dict:
        # Print the full dictionary to the console
        print("Final QR Code Dictionary:", qr_code_dict)
        return render_template('index.html', updates=updates, qr_code_dict=qr_code_dict)
    else:
        return "Scanning QR codes, please wait..."


if __name__ == '__main__':
    app.run(debug=True)
