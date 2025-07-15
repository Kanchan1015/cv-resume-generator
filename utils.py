def collect_user_data():
    print("🔹 Let's start with your personal details:\n")
    
    personal = {
        "name": input("Full Name: "),
        "email": input("Email: "),
        "phone": input("Phone Number: "),
        "linkedin": input("LinkedIn URL: "),
        "github": input("GitHub URL: ")
    }

    print("\n🔹 Let's enter your education details:\n")
    
    education = []
    while True:
        degree = input("Degree / Program: ")
        institution = input("Institution Name: ")
        start = input("Start Year: ")
        end = input("End Year: ")

        education.append({
            "degree": degree,
            "institution": institution,
            "start": start,
            "end": end
        })

        more = input("Do you want to add another education entry? (yes/no): ").strip().lower()
        if more != 'yes':
            break

        print("\n🔹 Let's enter your work experience details:\n")

    experience = []
    while True:
        title = input("Job Title: ")
        company = input("Company Name: ")
        start = input("Start Date (e.g., Jan 2022): ")
        end = input("End Date (e.g., Present or Dec 2023): ")

        print("Enter job description bullet points (press Enter twice to finish):")
        description = []
        while True:
            point = input("- ")
            if point.strip() == "":
                break
            description.append(point)

        experience.append({
            "title": title,
            "company": company,
            "start": start,
            "end": end,
            "description": description
        })

        more = input("Do you want to add another job? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    
    print("\n🔹 Let's enter your project details:\n")

    projects = []
    while True:
        title = input("Project Title: ")
        description = input("Short Description: ")
        tech = input("Technologies Used (comma-separated): ")
        link = input("Project Link (GitHub/Live URL, optional): ")

        projects.append({
            "title": title,
            "description": description,
            "technologies": [t.strip() for t in tech.split(",") if t.strip()],
            "link": link
        })

        more = input("Do you want to add another project? (yes/no): ").strip().lower()
        if more != 'yes':
            break


    print("\n🔹 Let's enter your skills:\n")
    skills_input = input("Enter your skills (comma-separated): ")
    skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]

    print("\n🔹 Extras: Languages & Certifications\n")
    languages_input = input("Languages Known (comma-separated): ")
    certifications_input = input("Certifications (comma-separated): ")

    extras = {
        "languages": [lang.strip() for lang in languages_input.split(",") if lang.strip()],
        "certifications": [cert.strip() for cert in certifications_input.split(",") if cert.strip()]
    }

        # Return all collected data in a dictionary
    return {
        "personal": personal,
        "education": education,
        "experience": experience,
        "projects": projects,
        "skills": skills,
        "extras": extras
    }

   

