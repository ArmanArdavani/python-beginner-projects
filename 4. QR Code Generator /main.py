import qrcode

def get_entires():
    entries = []
    while True:
        data = input('Enter the text or URL for the QR code (or press Enter to stop): ')
        if data == "":
            break
        file_name = input("Enter the filename for this QR code: ")
        if not file_name.endswith(".png"):
            file_name += ".png"
        entries.append((data, file_name))
    return entries


def make_qrcode(entries):
    for data, file_name in entries:
        img = qrcode.make(data)
        img.save(file_name)
        print(f"QR code saved as {file_name}")


def main():
    entries = get_entires()
    make_qrcode(entries)

if __name__ == "__main__":
    main()

