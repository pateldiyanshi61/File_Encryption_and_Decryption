from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

key = get_random_bytes(16)

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Directory to store encrypted files
ENCRYPTED_FOLDER = 'encrypted'
if not os.path.exists(ENCRYPTED_FOLDER):
    os.makedirs(ENCRYPTED_FOLDER)

# Directory to store decrypted files
DECRYPTED_FOLDER = 'decrypted'
if not os.path.exists(DECRYPTED_FOLDER):
    os.makedirs(DECRYPTED_FOLDER)

def encrypt_file(input_path, output_path, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_path, 'rb') as f:
        plaintext = f.read()
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    with open(output_path, 'wb') as f:
        f.write(ciphertext)

def decrypt_file(input_path, output_path, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_path, 'rb') as f:
        ciphertext = f.read()
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, AES.block_size)
    with open(output_path, 'wb') as f:
        f.write(plaintext)

@app.route('/txt', methods=['GET', 'POST'])
def txt():
    msg=''
    if request.method == 'POST':
        # Check if the post request has the 'file' part
        if 'txt' not in request.files:
            return "No file part"
        
        file = request.files['txt']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            if request.form.get('encrypt'):
                # Encrypt the uploaded file
                encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{file.filename}')
                encrypt_file(filename, encrypted_filename, key)
                msg= f"File encrypted and saved as {encrypted_filename}"
            
            elif request.form.get('decrypt'):
                # Decrypt the uploaded file
                decrypted_filename = os.path.join(DECRYPTED_FOLDER, f'decrypted_{file.filename}')
                decrypt_file(filename, decrypted_filename, key)
                msg= f"File decrypted and saved as {decrypted_filename}"

    return render_template('txt.html', msg=msg)

@app.route('/audio', methods=['GET', 'POST'])
def audio():
    msg=''
    if request.method == 'POST':
        # Check if the post request has the 'file' part
        if 'audio' not in request.files:
            return "No file part"
        
        file = request.files['audio']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            if request.form.get('encrypt'):
                # Encrypt the uploaded file
                encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{file.filename}')
                encrypt_file(filename, encrypted_filename, key)
                msg=f"File encrypted and saved as {encrypted_filename}"
            
            elif request.form.get('decrypt'):
                # Decrypt the uploaded file
                decrypted_filename = os.path.join(DECRYPTED_FOLDER, f'decrypted_{file.filename}')
                decrypt_file(filename, decrypted_filename, key)
                msg=f"File decrypted and saved as {decrypted_filename}"

    return render_template('audio.html', msg=msg)

@app.route('/pdf', methods=['GET', 'POST'])
def pdf():
    msg=''
    if request.method == 'POST':
        # Check if the post request has the 'file' part
        if 'pdf' not in request.files:
            return "No file part"
        
        file = request.files['pdf']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            if request.form.get('encrypt'):
                # Encrypt the uploaded file
                encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{file.filename}')
                encrypt_file(filename, encrypted_filename, key)
                msg= f"File encrypted and saved as {encrypted_filename}"
            
            elif request.form.get('decrypt'):
                # Decrypt the uploaded file
                decrypted_filename = os.path.join(DECRYPTED_FOLDER, f'decrypted_{file.filename}')
                decrypt_file(filename, decrypted_filename, key)
                msg= f"File decrypted and saved as {decrypted_filename}"

    return render_template('pdf.html', msg=msg)

@app.route('/image', methods=['GET', 'POST'])
def image():
    msg=''
    if request.method == 'POST':
        # Check if the post request has the 'file' part
        if 'image' not in request.files:
            return "No file part"
        
        file = request.files['image']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            if request.form.get('encrypt'):
                # Encrypt the uploaded file
                encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{file.filename}')
                encrypt_file(filename, encrypted_filename, key)
                msg= f"File encrypted and saved as {encrypted_filename}"
            
            elif request.form.get('decrypt'):
                # Decrypt the uploaded file
                decrypted_filename = os.path.join(DECRYPTED_FOLDER, f'decrypted_{file.filename}')
                decrypt_file(filename, decrypted_filename, key)
                msg= f"File decrypted and saved as {decrypted_filename}"

    return render_template('image.html', msg=msg)

@app.route('/docx', methods=['GET', 'POST'])
def docx():
    msg=''
    if request.method == 'POST':
        # Check if the post request has the 'file' part
        if 'docx' not in request.files:
            return "No file part"
        
        file = request.files['docx']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            if request.form.get('encrypt'):
                # Encrypt the uploaded file
                encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{file.filename}')
                encrypt_file(filename, encrypted_filename, key)
                msg= f"File encrypted and saved as {encrypted_filename}"
            
            elif request.form.get('decrypt'):
                # Decrypt the uploaded file
                decrypted_filename = os.path.join(DECRYPTED_FOLDER, f'decrypted_{file.filename}')
                decrypt_file(filename, decrypted_filename, key)
                msg= f"File decrypted and saved as {decrypted_filename}"

    return render_template('docx.html', msg=msg)

@app.route('/xlsx', methods=['GET', 'POST'])
def xlsx():
    msg=''
    if request.method == 'POST':
        # Check if the post request has the 'file' part
        if 'xlsx' not in request.files:
            return "No file part"
        
        file = request.files['xlsx']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            if request.form.get('encrypt'):
                # Encrypt the uploaded file
                encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{file.filename}')
                encrypt_file(filename, encrypted_filename, key)
                msg= f"File encrypted and saved as {encrypted_filename}"
            
            elif request.form.get('decrypt'):
                # Decrypt the uploaded file
                decrypted_filename = os.path.join(DECRYPTED_FOLDER, f'decrypted_{file.filename}')
                decrypt_file(filename, decrypted_filename, key)
                msg= f"File decrypted and saved as {decrypted_filename}"

    return render_template('xlsx.html', msg=msg)

@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    return send_file(os.path.join(folder, filename), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
