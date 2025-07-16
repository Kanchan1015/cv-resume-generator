## 📄 Resume Generator (Jinja2 + Streamlit + PDF)

A clean and flexible **Resume Generator** built using **Streamlit**, **Jinja2 templating**, and **WeasyPrint**. Users can fill out a form via web UI and download a beautifully styled resume as a **PDF file**.

> ⚠️ Note: The design system is still a **work in progress**. Further styling and template features are being added.

---

### 🧰 Tech Stack

| Tool          | Purpose                            |
| ------------- | ---------------------------------- |
| 🐍 Python     | Core language                      |
| 🔥 Streamlit  | Frontend web UI (forms + download) |
| 🎨 Jinja2     | HTML templating engine             |
| 🖨️ WeasyPrint | HTML to PDF conversion             |
| 🖌️ CSS        | Resume layout and design           |
| 📁 venv       | Python virtual environment         |

---

### 📁 Folder Structure

```
cv-generator/
├── app.py                  # Streamlit UI entrypoint
├── render.py               # Renders PDF using HTML + CSS
├── templates/
│   └── resume_template.html
├── static/
│   └── style.css
├── outputs/
│   └── resume.pdf
├── requirements.txt
└── README.md
```

---

### 🧪 Prerequisites

1. **Python 3.10+**
2. **Homebrew (macOS)** — required to install native libraries for WeasyPrint
3. **Recommended**: Create and use a Python **virtual environment**

---

### ⚙️ Setup Instructions

#### 1. Clone the Repo

```bash
git clone https://github.com/your-username/cv-generator.git
cd cv-generator
```

#### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Install WeasyPrint Native Dependencies (macOS)

```bash
brew install pango cairo gdk-pixbuf libffi
```

---

### 🚀 Running the App

From your activated venv:

```bash
python -m streamlit run app.py
```

Then open the app in your browser:

```
http://localhost:8501
```

---

### 🖨️ How It Works

1. User fills out personal info, education, experience, skills, etc.
2. Streamlit submits the form
3. The data is injected into a **Jinja2-based HTML template**
4. Styled HTML is converted into a **PDF file** using WeasyPrint
5. The resume is downloadable as `resume.pdf`

---

### 🎯 Features

✅ Streamlit UI for form-based data entry
✅ Jinja2 templating for easy customization
✅ Clean HTML structure with CSS styling
✅ PDF download with formatted content
🚧 More styling and real-time preview in development

---

### 📌 Known Limitations

- 💡 Resume layout design is currently basic and being improved
- 📸 Live PDF preview inside the browser is not yet available
- 🔄 Switching between multiple templates is not implemented
- 📄 DOCX export has been deprecated in favor of PDF

---

### 📅 Roadmap

- [ ] Add professional summary field
- [ ] Live resume preview inside Streamlit
- [ ] Multiple resume themes (modern, minimal, creative)
- [ ] Save/load JSON form data
- [ ] Deploy online (Streamlit Cloud / HuggingFace)

---

### 👤 Author

**Anbalagan Kanchan**
