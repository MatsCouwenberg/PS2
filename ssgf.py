from flask import Flask, render_template
from flask_socketio import SocketIO
from pyzbar.pyzbar import decode
import cv2

app = Flask(__name__)
socketio = SocketIO(app)

# Global variables to store QR code data and orientation
qr_code_dict = {}
scanned_count = 0
stop_scan = False  # New variable to indicate whether to stop scanning

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

# Function to start QR code scanning
def start_qr_code_scan():
    global qr_code_dict, stop_scan
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    while not stop_scan:
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

        key = cv2.waitKey(1)
        if key == 27:  # ASCII code for 'esc' key
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to stop QR code scanning
def stop_qr_code_scan():
    global stop_scan
    stop_scan = True
# Route to serve the HTML page with the buttons
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO event to trigger QR code scanning
@socketio.on('start_scan')
def handle_start_scan():
    global qr_code_dict, scanned_count, stop_scan
    qr_code_dict = {}
    scanned_count = 0
    stop_scan = False
    start_qr_code_scan()
    socketio.emit('scan_result', qr_code_dict)

# SocketIO event to stop QR code scanning
@socketio.on('stop_scan')
def handle_stop_scan():
    stop_qr_code_scan()
    socketio.emit('scan_stopped', 'Scanning stopped.')

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
