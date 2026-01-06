import os
import subprocess
from flask import Flask, render_template, request, redirect
UPLOAD_FOLDER = "static/uploads"
EXIFTOOL_PATH = "/usr/bin/exiftool"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dorking", methods=["GET", "POST"])
def dorking():
    generated_query = None

    if request.method == "POST":
        mode = request.form.get("mode")

        if mode == "basic":
            category = request.form.get("category")
            keyword = request.form.get("keyword")

            dorks = {
                "passwords": 'filetype:txt "password"',
                "logs": 'filetype:log',
                "reports": 'filetype:pdf',
                "labs": '"cyber security lab"',
                "vuln": 'inurl:admin',
                "breach": 'filetype:zip "breach"'
            }

            query = f"{keyword} {dorks.get(category, '')}"
            return redirect("https://www.google.com/search?q=" + query)

        if mode == "advanced":
            keyword = request.form.get("adv_keyword")
            filetype = request.form.get("filetype")
            category = request.form.get("adv_category")

            parts = [keyword]

            if filetype:
                parts.append(f"filetype:{filetype}")

            category_map = {
                "website": "inurl:login",
                "password": '"password"',
                "database": "filetype:sql",
                "labs": '"cyber security lab"',
                "reports": "filetype:pdf"
            }

            if category in category_map:
                parts.append(category_map[category])

            generated_query = " ".join(parts)

    return render_template("dorking.html", generated_query=generated_query)

@app.route("/image-analyzer", methods=["GET", "POST"])
def image_analyzer():
    result = ""

    if request.method == "POST":
        image = request.files.get("image")
        extract_metadata = request.form.get("metadata")
        ai_detect = request.form.get("ai_detect")

        if image:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(image_path)

            metadata_output = ""

            if extract_metadata or ai_detect:
                cmd = [EXIFTOOL_PATH, image_path]
                process = subprocess.run(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                metadata_output = process.stdout

            # OR LOGIC
            if extract_metadata:
                result += "=== METADATA ===\n"
                result += metadata_output + "\n"

            if ai_detect:
                ai_sources = [
                    "OpenAI",
                    "ChatGPT",
                    "DALL-E",
                    "Google AI",
                    "Midjourney",
                    "Stable Diffusion"
                ]

                detected = False
                for src in ai_sources:
                    if src.lower() in metadata_output.lower():
                        result += f"=== AI IMAGE DETECTED ===\nSource: {src}\n"
                        detected = True
                        break

                if not detected:
                    result += "=== AI DETECTION ===\nNo AI source found in metadata\n"

            # Cleanup (optional but good)
            os.remove(image_path)

    return render_template("image_analyzer.html", result=result)

if __name__ == "__main__":
    print("[*] Cyber Security Platform Starting...")
    print("[*] Open: http://127.0.0.1:5000")
    app.run(debug=True)
