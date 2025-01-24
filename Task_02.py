from PIL import Image
import numpy as np

def encrypt(path, key):
    
    img = Image.open(path).convert('RGB')
    img_array = np.array(img)

    
    encrypted = (img_array.astype(np.int32) + key) % 256  

  
    encrypted = np.clip(encrypted, 0, 255).astype(np.uint8)

    
    encrypted_imp = Image.fromarray(encrypted, 'RGB')
    encrypted_imp.save('encrypted_image.png')

    print("Image encrypted and saved as 'encrypted_image.png'.")


def decrypt(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path).convert('RGB')
    encrypted_array = np.array(encrypted_img)

   
    decrypted_array = (encrypted_array.astype(np.int32) - key) % 256

   
    decrypted_array = np.clip(decrypted_array, 0, 255).astype(np.uint8)

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
