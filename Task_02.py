from PIL import Image
import numpy as np

# Function to encrypt an image
def encrypt(path, key):
    # Open the image and convert it to RGB mode
    img = Image.open(path).convert('RGB')
    img_array = np.array(img)

    # Convert to a larger data type (e.g., int32) to handle the addition without overflow
    encrypted = (img_array.astype(np.int32) + key) % 256  # Add the key to each pixel value (mod 256 to stay within range)

    # Ensure the result is within the range of uint8
    encrypted = np.clip(encrypted, 0, 255).astype(np.uint8)

    # Create and save the encrypted image
    encrypted_imp = Image.fromarray(encrypted, 'RGB')
    encrypted_imp.save('encrypted_image.png')

    print("Image encrypted and saved as 'encrypted_image.png'.")

# Function to decrypt an image
def decrypt(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path).convert('RGB')
    encrypted_array = np.array(encrypted_img)

    # Decrypt by subtracting the key (mod 256)
    decrypted_array = (encrypted_array.astype(np.int32) - key) % 256

    # Ensure the result is within the range of uint8
    decrypted_array = np.clip(decrypted_array, 0, 255).astype(np.uint8)

    # Create and save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array, 'RGB')
    decrypted_img.save('decrypted_image.png')

    print("Image decrypted and saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    print("Simple Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        image_path = input("Enter the path of the image to encrypt: ")
        key = int(input("Enter an encryption key (integer): "))
        encrypt(image_path, key)

    elif choice == 2:
        encrypted_image_path = input("Enter the path of the encrypted image: ")
        key = int(input("Enter the decryption key (integer): "))
        decrypt(encrypted_image_path, key)

    else:
        print("Invalid choice! Exiting.")
