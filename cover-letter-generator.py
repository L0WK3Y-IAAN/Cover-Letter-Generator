from datetime import datetime
import os
import pathlib

os.system('cls' if os.name == 'nt' else 'clear')

save_path = pathlib.Path(__file__).resolve().parent
date = datetime.now()
date2= datetime.now()

name = input("Enter Full Name: ")
csz = input("Enter City, State and Zip: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")
previous_role = input("Previous Role: ")

generalInfo = name + "\n" + csz + "\nCell: " + phone + "\nE-Mail: " + email + date.strftime("%B %d, %Y\n\n") 


companyName = input("Name of company: ")
positionTitle = input("Title of position: ")
os.system('cls' if os.name == 'nt' else 'clear')


output = generalInfo.center(50) + companyName+"\n"+positionTitle+"\n"+date2.strftime("%m/%d/%y\n\n")+"Dear Hiring Manager,\nThroughout my career, I have contributed to positive business results through effective organization, prioritization, and follow through of key organizational projects. My strengths and qualifications are an ideal match to the " + positionTitle + " requirements and will bring immediate value to "+companyName+"."+"\nIn my former " + previous_role + " role, I exercise a calculated and methodical approach to problem solving. While I am independently motivated, I appreciate collective efforts and collaborate productively within group settings. Moreover, I am competent in my research and problem solving skills, with proficiency in analytical thinking. I have previous experience in the IT field as well as self studies. I am also a recent graduate of the Kenzie Academy coding bootcamp and have front-end web development experience. So this opportunity is especially exciting for me because I get to use my skills and talents to help benefit the company! Furthermore, my critical thinking, collaboration, and problem-solving abilities will serve to support your continued organizational efforts.\nTo illustrate the scope of my career history and professional competencies, please take a moment to review my enclosed resume. I am grateful for your evaluation of my credentials and subsequent response.\n\nSincerely, " + name


save_file = os.path.join(save_path, name + ".docx")
file = open(save_file,"w")
file.write(output)
file.close()

print(output)