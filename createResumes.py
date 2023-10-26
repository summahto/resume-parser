# Read the content of the input file
with open('randomResumes.txt', 'r') as file:
    content = file.readlines()

# Initialize variables to keep track of resumes
resume_number = 1
current_resume = []

# Iterate through the content and extract resumes
for line in content:
    line = line.strip()
    if line.startswith("**Name:**"):
        # If a new resume is encountered, save the previous one to a new file
        if current_resume:
            with open(f'resume_{resume_number}.txt', 'w') as output_file:
                output_file.writelines(current_resume)
            resume_number += 1
            current_resume = []

    # Append the current line to the current_resume
    current_resume.append(line + '\n')

# Save the last resume to a file
if current_resume:
    with open(f'resume_{resume_number}.txt', 'w') as output_file:
        output_file.writelines(current_resume)

print("Resumes have been extracted into separate text files.")
