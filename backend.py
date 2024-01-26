from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Global variables to store QR code data and orientation
qr_code_dict = {}
scanned_count = 0

# Route to serve the HTML page with the button
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO event to trigger QR code scanning
@socketio.on('start_scan')
def handle_start_scan():
    global qr_code_dict, scanned_count
    qr_code_dict = {}
    scanned_count = 0
    socketio.emit('scan_started')  # Inform the client that the scan has started

# Start QR code scanning when the scan has started
@socketio.on('scan_started_ack')
def start_qr_code_scan():
    global qr_code_dict, scanned_count
    while scanned_count < 2:
        # Simulate QR code scanning logic here
        # In your real application, integrate the actual QR code scanning logic

        # For demonstration purposes, we'll add some dummy data
        dummy_data = f"Dummy Data {scanned_count + 1}"
        dummy_orientation = f"Orientation {scanned_count + 1}"

        if dummy_data not in qr_code_dict:
            qr_code_dict[dummy_data] = dummy_orientation
            scanned_count += 1
            print("Added to dictionary:", dummy_data, dummy_orientation)

    socketio.emit('scan_result', qr_code_dict)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
