import os
import hashlib
import secrets

# Hamming Distance Function
def hamming_distance(s1, s2):
    return sum(bin(x ^ y).count('1') for x, y in zip(bytes.fromhex(s1), bytes.fromhex(s2)))

print("🔐 Garuda Sentinel Project 4: Random vs Pseudo-Random Key Generation\n")

# Ask user for bit length (up to 256)
bit_length = int(input("Enter key bit length (max 256): "))
if bit_length > 256:
    bit_length = 256
byte_length = bit_length // 8

print("\n[1] Generating TRUE Random Key using os.urandom()...")
true_salt = os.urandom(16)
true_random = os.urandom(byte_length)
true_key = true_salt + true_random
final_true = hashlib.sha256(true_key).hexdigest()
print(f"✅ TRUE Random Key (SHA-256): {final_true}")

print("\n[2] Generating PSEUDO Random Key using secrets module...")
pseudo_salt = secrets.token_bytes(16)
pseudo_random = secrets.token_bytes(byte_length)
pseudo_key = pseudo_salt + pseudo_random
final_pseudo = hashlib.sha256(pseudo_key).hexdigest()
print(f"✅ PSEUDO Random Key (SHA-256): {final_pseudo}")

# Compare both
distance = hamming_distance(final_true, final_pseudo)
print(f"\n🔍 Hamming Distance between Keys: {distance} bits")
print("🔗 Higher distance indicates more randomness between the two keys.")

# Verdict Table
print("\n📊 Secure Comparison Table:")
print("| Feature             | True Random (os.urandom) | Pseudo Random (secrets)     |")
print("|---------------------|---------------------------|------------------------------|")
print("| Source              | Hardware entropy          | Python secure PRNG           |")
print("| Security Level      | 🔐 Maximum                | 🔐 Secure (cryptographic)     |")
print("| Repeatability       | ❌ No                     | ❌ No (without seeding)       |")
print("| Usage               | Keygen, IV, high-security | Passwords, tokens, auth keys |")

# Save to file
with open("random_keys_log.txt", "w") as f:
    f.write("TRUE RANDOM KEY (SHA-256):\n" + final_true + "\n\n")
    f.write("PSEUDO RANDOM KEY (SHA-256):\n" + final_pseudo + "\n")
    f.write("\nHamming Distance (bit-level): " + str(distance) + " bits\n")

print("\n📁 Keys and comparison details saved to 'random_keys_log.txt'")
