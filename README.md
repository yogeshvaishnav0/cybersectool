# Cyber Security Web Platform

A web-based tool designed for **Cyber Security students and analysts**, running on **Linux (Kali Linux recommended)** and accessible via browser on localhost.

---

## 🔧 Tools Included

### 1. Google Dorking Tool
A single-page Google dorking utility with two sections:

#### • Basic Mode
- Category-based predefined Google dorks
- User keyword input
- Automatic redirect to Google search

#### • Advanced Mode
- Keyword-based dork generation
- File type and category selection
- Generates Google dork queries for manual use
- No auto-redirect (professional OSINT practice)

Both modes are available on the **same page using tabs (JavaScript)**.

---

### 2. Image Analyzer Tool
Uses **ExifTool (pre-installed in Kali Linux)** to analyze images.

#### Features:
- Image upload via browser
- Extract full metadata
- AI Image Detection (Beta)
  - Detects possible AI-generated images based on metadata
  - Supports sources like OpenAI, Google AI, Midjourney, Stable Diffusion
- OR logic:
  - Metadata only
  - AI detection only
  - Both together

⚠️ AI detection is metadata-based and experimental.

---

## 🛠 Requirements

- Linux OS (Kali Linux recommended)
- Python 3
- ExifTool (`/usr/bin/exiftool`)
- Flask

---

## 🚀 Installation & Run

```bash
git clone <your-repo-url>
cd cyber_platform
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
