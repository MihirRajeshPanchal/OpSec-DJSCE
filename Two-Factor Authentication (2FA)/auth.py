import pyotp
import qrcode
import base64

def generate_secret_key():
    secret_key = pyotp.random_base32()
    return secret_key

def generate_qr_code(username, secret_key):
    otp_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(
        name=username,
        issuer_name='MihirApp'
    )
    img = qrcode.make(otp_uri)
    img.save(f'{username}_2fa.png')

def verify_otp(secret_key, user_otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_otp)

if __name__ == "__main__":
    
    username = "mihir"
    secret_key = generate_secret_key()
    print(f"Secret Key for user '{username}': {secret_key}")
    
    
    generate_qr_code(username, secret_key)
    
    totp = pyotp.TOTP(secret_key)
    print(totp.now())
    
    entered_otp = input("Enter the OTP from your authenticator app: ")
    if verify_otp(secret_key, entered_otp):
        print("Authentication successful!")
    else:
        print("Authentication failed.")
