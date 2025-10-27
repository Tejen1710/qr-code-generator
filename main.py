# main.py
import argparse, qrcode, os, datetime

def generate_qr(data: str, out_dir: str = "qr_codes"):
    os.makedirs(out_dir, exist_ok=True)
    img = qrcode.make(data)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(out_dir, f"qr_{ts}.png")
    img.save(path)
    print(f"[OK] QR saved to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://github.com/Tejen1710")
    args = parser.parse_args()
    generate_qr(args.url)
