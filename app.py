import streamlit as st

st.set_page_config(page_title="CV Generator", layout="centered")

st.title("📄 CV / Resume Generator")

st.markdown("Fill in your details below to generate a professional resume in Word format.")

if "generated_file" not in st.session_state:
    st.session_state.generated_file = None

with st.form("cv_form"):
    # --- Personal Details ---
    st.subheader("👤 Personal Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")

    # --- Education ---
    st.subheader("🎓 Education")
    education = []
    for i in range(1, 4):
        st.markdown(f"**Education #{i}**")
        degree = st.text_input(f"Degree/Program #{i}", key=f"degree_{i}")
        institution = st.text_input(f"Institution #{i}", key=f"institution_{i}")
        start = st.text_input(f"Start Year #{i}", key=f"start_{i}")
        end = st.text_input(f"End Year #{i}", key=f"end_{i}")
        if degree and institution and start and end:
            education.append({
                "degree": degree,
                "institution": institution,
                "start": start,
                "end": end
            })

    # --- Work Experience ---
    st.subheader("💼 Work Experience")
    experience = []
    for i in range(1, 4):
        st.markdown(f"**Job #{i}**")
        title = st.text_input(f"Job Title #{i}", key=f"title_{i}")
        company = st.text_input(f"Company #{i}", key=f"company_{i}")
        start = st.text_input(f"Start Date #{i}", key=f"job_start_{i}")
        end = st.text_input(f"End Date #{i}", key=f"job_end_{i}")
        desc = st.text_area(f"Description (bullet points, one per line) #{i}", key=f"desc_{i}")

        if title and company and start and end and desc:
            description = [line.strip() for line in desc.split("\n") if line.strip()]
            experience.append({
                "title": title,
                "company": company,
                "start": start,
                "end": end,
                "description": description
            })

    # --- Projects ---
    st.subheader("💻 Projects")
    projects = []
    for i in range(1, 4):
        st.markdown(f"**Project #{i}**")
        proj_title = st.text_input(f"Project Title #{i}", key=f"proj_title_{i}")
        proj_desc = st.text_area(f"Project Description #{i}", key=f"proj_desc_{i}")
        tech_stack = st.text_input(f"Technologies Used (comma-separated) #{i}", key=f"proj_tech_{i}")
        link = st.text_input(f"Project Link (optional) #{i}", key=f"proj_link_{i}")
        if proj_title and proj_desc and tech_stack:
            projects.append({
                "title": proj_title,
                "description": proj_desc,
                "technologies": [t.strip() for t in tech_stack.split(",") if t.strip()],
                "link": link
            })

    # --- Skills ---
    st.subheader("🧠 Skills")
    skills_input = st.text_input("List your skills (comma-separated)")
    skills = [s.strip() for s in skills_input.split(",") if s.strip()]

    # --- Extras: Languages & Certifications ---
    st.subheader("🌍 Languages & Certifications")
    languages_input = st.text_input("Languages Known (comma-separated)")
    certifications_input = st.text_input("Certifications (comma-separated)")
    extras = {
        "languages": [l.strip() for l in languages_input.split(",") if l.strip()],
        "certifications": [c.strip() for c in certifications_input.split(",") if c.strip()]
    }

    # --- Submit Button ---
    submitted = st.form_submit_button("Generate Resume")

    if submitted:
        data = {
            "personal": {
                "name": name,
                "email": email,
                "phone": phone,
                "linkedin": linkedin,
                "github": github
            },
            "education": education,
            "experience": experience,
            "projects": projects,
            "skills": skills,
            "extras": extras
        }

        output_path = "outputs/resume_streamlit.docx"
        generate_docx(data, filename=output_path)
        st.session_state.generated_file = output_path
        st.success("Resume generated successfully!")

# --- Download Button (outside form) ---
if st.session_state.generated_file:
    with open(st.session_state.generated_file, "rb") as f:
        st.download_button("⬇️ Download Resume", f, file_name="resume.docx")
