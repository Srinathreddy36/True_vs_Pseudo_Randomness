# 🔐 Garuda-Randomness-Showdown

A hands-on cryptography project to compare **True Randomness** (`os.urandom`, `secrets`) vs **Pseudo-Randomness** (`random` with seed). This project visualizes entropy strength, uniqueness, and cryptographic security of random number generation methods.

---

## 📘 Overview

This project demonstrates:
- How `os.urandom()` and `secrets` generate cryptographically secure random numbers.
- How `random.seed()` with `random.getrandbits()` is **not** suitable for secure systems.
- How entropy, salt, nonce, and bit-length affect randomness and key uniqueness.

---

## 🧠 Concepts Covered

- **Entropy & Nonce** generation
- **True Randomness** (cryptographic): `os.urandom`, `secrets`
- **Pseudo-Randomness** (predictable): `random` with seed
- **Bit-Length Analysis** (e.g. 128, 192, 256 bits)
- **Uniqueness Comparison**
- **Secure vs Insecure RNG**

---

## 🧪 How It Works

1. User inputs desired **bit length** (up to 256 bits).
2. Generates:
   - **True Random Key** using `secrets.token_bytes()` and `os.urandom()`.
   - **Pseudo-Random Key** using `random.seed()` and `random.getrandbits()`.
3. Computes SHA3-256 hash of both keys (salted).
4. Shows comparison:
   - Bit strength
   - Nonce usage
   - Hash uniqueness
   - Security notes

---

## ✅ Status

🧩 Completed Core Logic  
🔒 Aligned with Serious Cryptography - Chapter 1  
🛠️ Ready for Portfolio & GitHub

---

## 📎 Author

**Srinath Reddy**  
Cybersecurity Student | Garuda Sentinel Founder  
GitHub: [@Srinathreddy36](https://github.com/Srinathreddy36)

---

## 🛡️ Part of Garuda Sentinel Mission

> "Every bit of randomness counts. This project reflects Garuda's vigilance in separating secure from insecure — byte by byte."

---

## 🚀 Next Steps

- Add entropy analysis graph
- Visual UI with PyQt/Tkinter for key generation
- Export comparison report (PDF/CSV)

---
