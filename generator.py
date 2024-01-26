import qrcode

rnummers = """0901062
0937870
0889003
"""

# Split the data into lines and add 'r' before each number
result_array = [f"r{line}" for line in rnummers.strip().split('\n')]

def generate_qr_code(data_to_encode, output_file="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )

    qr.add_data(data_to_encode)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save(output_file, 'PNG')

for rnummer in result_array:
    data_to_encode = rnummer
    output_file = f"{rnummer}.png"
    generate_qr_code(data_to_encode, output_file)
