import os
import random
import sys

def generate_resume(index):
    return f"{index}. **Name:** {generate_name()}\n" \
           f"   - **Skills:** {generate_skills()}\n" \
           f"   - **Experience:** {generate_experience()}\n" \
           f"   - **Education:** {generate_education()}\n" \
           f"   - **References:** {generate_references()}\n" \
           f"   - **Volunteering:** {generate_volunteering()}\n" \
           f"   - **Contact Information:** {generate_contact_info()}\n" \
           f"   - **Projects:** {generate_projects()}\n\n"

def generate_name():
    return f"{random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack', 'Katherine', 'Leo', 'Mia', 'Nathan', 'Olivia', 'Patrick', 'Quinn', 'Rachel', 'Sam', 'Tina', 'Ulysses', 'Victoria', 'Walter', 'Xena', 'Yuki', 'Zane'])} {random.choice(['Johnson', 'Smith', 'Brown', 'Lee', 'Wang', 'Garcia', 'Patel', 'Kim', 'Davis', 'Singh', 'Chen', 'Jones', 'Nguyen', 'Gupta', 'Silva', 'Lee', 'Yamamoto', 'Rodriguez', 'Cruz', 'White', 'Lopez', 'Wu', 'Hernandez', 'Miller', 'Jackson', 'Kumar', 'Taylor', 'Gonzalez', 'Williams', 'Li', 'Smith', 'Kim', 'Sato', 'Gupta', 'Lopez', 'M체ller', 'Lee', 'Wang', 'Chen', 'Suzuki', 'Brown', 'Nguyen', 'Garcia', 'Patel', 'Jones', 'Kumar', 'Smith', 'Yamamoto', 'Rodriguez', 'Wu', 'L처pez', 'White', 'Silva', 'Cruz', 'Miller', 'Jackson', 'Nguyen', 'Lee', 'Lopez', 'Chen', 'Garcia', 'Smith', 'Kumar', 'Patel', 'Wang', 'Jones', 'Rodriguez', 'Wu', 'White', 'Taylor', 'L처pez', 'Silva', 'Cruz', 'Brown', 'Miller', 'Kumar', 'Jackson', 'Nguyen', 'Lee', 'Gupta', 'Kumar', 'Lopez', 'Chen', 'Jones', 'Wu', 'Rodriguez', 'Garcia', 'Patel', 'White', 'Taylor', 'L처pez', 'Silva', 'Cruz', 'Brown', 'Miller', 'Kumar', 'Jackson', 'Nguyen', 'Lee', 'Gupta'])}"

def generate_skills():
    return ", ".join(random.sample(['Java', 'Python', 'C#', 'JavaScript', 'HTML', 'CSS', 'SQL', 'React', 'Angular', 'Node.js', 'Vue.js', 'Machine Learning', 'Data Analysis', 'Graphic Design', 'Project Management', 'Agile', 'Git', 'Docker', 'Kubernetes', 'Swift', 'Android Development', 'iOS Development', 'UI/UX Design', 'Blockchain', 'Cybersecurity', 'Network Administration', 'Cloud Computing', 'DevOps', 'Big Data', 'IoT', 'AR/VR Development'], k=random.randint(3, 16)))

def generate_experience():
    return f"{random.choice(['Lead', 'Senior', 'Junior'])} {random.choice(['Developer', 'Engineer', 'Designer', 'Scientist', 'Analyst', 'Manager'])} at {generate_company()}"

def generate_company():
    return f"{random.choice(['TechCorp', 'InnoSolutions', 'DataExperts', 'CreativeMinds', 'CodeCrafters', 'TechInnovate', 'DigitalSolutions', 'InnovativeTech', 'DataInnovators', 'CreativeSolutions'])}"

def generate_education():
    return f"{random.choice(['Bachelor', 'Master', 'Ph.D.'])} in {random.choice(['Computer Science', 'Engineering', 'Data Science', 'Art', 'Physics', 'Business Administration'])} from {generate_university()}"

def generate_university():
    return f"{random.choice(['Tech University', 'Inno Institute', 'Data Science School', 'Creative Arts College', 'Physics Academy', 'Business School'])}"

def generate_references():
    return f"{generate_name()}, {generate_title()}, {generate_email()}\n" \
           f"{generate_name()}, {generate_title()}, {generate_email()}"

def generate_title():
    return random.choice(['CTO', 'CEO', 'Manager', 'Lead', 'Coordinator', 'Director', 'Engineer', 'Developer', 'Designer', 'Scientist', 'Analyst'])

def generate_email():
    return f"{generate_name().lower().replace(' ', '_')}@example.com"

def generate_volunteering():
    return f"{random.choice(['Coding for Charity', 'Tech Mentorship', 'Community Cleanup', 'Youth Education', 'Environmental Conservation', 'Social Justice Initiatives', 'Healthcare Support', 'Food Drive', 'Disaster Relief'])}"

def generate_contact_info():
    return f"{generate_email()}, {generate_location()}"

def generate_location():
    return f"{random.choice(['City', 'Town', 'Village'])}, {random.choice(['Techland', 'Innoville', 'Data City', 'Artopia', 'Scienceburg', 'Green Valley', 'Techtopia', 'Inno Haven', 'Data Haven', 'Innovation Meadows'])}"

def generate_projects():
    return f"{random.choice(['Developed', 'Led', 'Contributed to'])} the {random.choice(['Innovative', 'Revolutionary', 'Cutting-edge', 'Groundbreaking'])} " \
           f"{random.choice(['Project', 'App', 'System', 'Framework', 'Platform'])} for {random.choice(['Optimizing', 'Enhancing', 'Streamlining', 'Solving'])} {random.choice(['Business Processes', 'User Experience', 'Data Analysis', 'Problem-solving', 'Collaboration'])}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <upper_bound>")
        sys.exit(1)

    upper_bound = int(sys.argv[1])
    output_directory = "generatedResumes"
    os.makedirs(output_directory, exist_ok=True)

    for i in range(1, upper_bound + 1):
        output_file = os.path.join(output_directory, f"resume_{i}.txt")
        with open(output_file, "w") as file:
            file.write(generate_resume(i))

if __name__ == "__main__":
    main()