from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image and convert it to RGB mode
    image = Image.open(image_path).convert('RGB')
    np_image = np.array(image, dtype=np.uint8)  # Ensure the array is of type uint8
    # Encrypt the image by applying a simple mathematical operation
    encrypted_image = (np_image.astype(np.uint16) + key) % 256  # Use uint16 to prevent overflow
    # Convert the encrypted image array back to an image
    encrypted_image = Image.fromarray(encrypted_image.astype('uint8'), 'RGB')
    # Save the encrypted image
    encrypted_image_path = 'encrypted_image.png'
    encrypted_image.save(encrypted_image_path)

    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image and convert it to RGB mode
    encrypted_image = Image.open(encrypted_image_path).convert('RGB')
    np_encrypted_image = np.array(encrypted_image, dtype=np.uint8)  # Ensure the array is of type uint8
    # Decrypt the image by reversing the mathematical operation
    decrypted_image = (np_encrypted_image.astype(np.uint16) - key) % 256  # Use uint16 to prevent overflow
    # Convert the decrypted image array back to an image
    decrypted_image = Image.fromarray(decrypted_image.astype('uint8'), 'RGB')
    # Save the decrypted image
    decrypted_image_path = 'decrypted_image.png'
    decrypted_image.save(decrypted_image_path)

    return decrypted_image_path

# Usage example
if __name__ == "__main__":
    # Define the path to the image and the encryption key
    image_path = r"C:\Users\Meghana\PycharmProjects\encryptor\img.jpg"  # Replace with the path to your image
    key = 50  # You can choose any integer value as the key
    # Encrypt the image
    encrypted_image_path = encrypt_image(image_path, key)
    print(f"Encrypted image saved at: {encrypted_image_path}")
    # Decrypt the image
    decrypted_image_path = decrypt_image(encrypted_image_path, key)
    print(f"Decrypted image saved at: {decrypted_image_path}")
