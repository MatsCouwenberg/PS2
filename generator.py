import qrcode

rnummers = ['r0937899', 'r0937894', 'r0999894', 'r1937894', 'r0937594', 'r0977894']

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

    img.save(output_file)

for rnummer in rnummers:
    data_to_encode = rnummer
    output_file = f"{rnummer}.png"
    generate_qr_code(data_to_encode, output_file)
