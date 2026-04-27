from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    profile = {
        "name": "Divyachandra R",
        "role": "Neuroengineer",

        "contact": {
            "phone": "+91-9361428183",
            "email": "divyachandradv@gmail.com",
            "linkedin": "https://www.linkedin.com/in/divya-chandra-r-969a911b2"
        },

        "about": [
    "My interest in neuroscience developed during my undergraduate years through self-directed exploration of emerging technologies.",

    "What began as curiosity gradually evolved into a clear direction, leading me to secure my first neuro internship at IIT and pursue a Master’s in Neuroengineering at TUM.",

    "Throughout this journey, I developed a strong interest in working with neuro-materials and exploring how they enable more tangible and dynamic interaction with the brain.",

    "Outside of academics, I value maintaining a balanced routine through fitness and creative downtime, which helps me stay consistent and focused while pursuing my long-term goals in neuroengineering."
],

        "education": [
            "Elite MSc. Neuroengineering | Technical University of Munich, Germany (2024 - 2026) | 2.5 CGPA",
            "Bachelors in Biomedical Engineering | SNS College of Technology, TamilNadu, India (2019 - 2023) | 9.12/10 CGPA",
            "Higher Secondary | Ananda Vidyalaya Matric. Hr. Sec School, Rajapalayam, Tamil Nadu (2019) | 81%"
        ],

        "experience": [
            {
                "title": "Master Thesis - Photonics Laboratory, NAIST, Japan (April 2026 - Present)",
                "description": "Designing emission filter patterns for cmos-image sensor; microfabricating it by clean room processes; characterize for biocompatibility and testing its performance through in-vivo or in-vitro brain imaging. ",
                "skills": ["Microfabrication", "cmos filter design", "biocompatibility testing", "Cadence virtuoso"]
    
            },
            {
                "title": "Intern - NeuroMaterials Lab, TUM, Germany (March 2025 - March 2026)",
                "description": "Electrochemical setup design for bottom mounted glass electrode & magnetic nanoparticle characterization for remanence effect with EIS",
                "skills": ["EIS experimentation", "Analysis of Impedence", "CAD modelling"],
                "drive": "https://drive.google.com/drive/folders/1K5HwTzNV4_eZM_NyZFkHNfVf6Rmh_kf-?usp=drive_link"
            },
            {
                "title": "Project Assistant - Computational Neuroscience Lab, IIT Madras (February 2024 – September 2024) ",
                "description": "Development of android application in kotlin aimed at collecting patients data of Parkinson’s disease through speech, walk pattern and the IGT(decision making) experiments, to apply data analysis in real-world healthcare challenges",
                "skills": ["Android studio", "Kotlin", "Data Analysis", "mobile hardware access", "working with pd patients"],
                "drive": "https://drive.google.com/drive/folders/12Ze97YOYhUpWGaA3m9CvrIWkXdTlQjLU?usp=drive_link"
            },
            {
                "title": "Research Intern - IIT Madras (May 2023 – January 2024) ",
                "description": "Real time detection of Heavy metals in various specimens via Bio-compatible electrodes using electrochemistry with deposition and voltammetry techniques",
                "skills": ["3-elctrode system", "voltammetry experiments", "electrochemistry" , "synthetic urine preparation"],
                "drive": "https://drive.google.com/drive/folders/1fz41Zx3OS9CyEOZPwSufnhmjgZCuO3yn?usp=drive_link"
            },
            {
                "title": "AR/VR Trainee - AllReal (March 2022 - April 2022)",
                "description": "Printing and designing 3D models for VR platform",
                "skills": ["Blender", "Fusion360"],
                "drive": "https://drive.google.com/drive/folders/1PUf_QYT2adyGKA89qduXCdqHTgCUMuiA?usp=drive_link"
            }
        ],

        "projects": [
            {
                "name": "Farmers Market - Neuro inspired system engineering module MSNE,TUM  ",
                "description": "Alternating Unilateral Reaching With Real Objects for Upper-Limb Rehabilitation After Hemiplegia. Alternating unilateral reaching with real objects for upper-limb rehabilitation after hemiplegia. A fun game asking the patient to sort the fruits and veggie in basket aiming at collecting their hand move data and cognition speed of noticing the hand and products to sort",
                "skills": ["embedded system","pygame designing","python"],
                "drive": "https://drive.google.com/drive/folders/1HYizwShqtUFD0_i9ImkRj9WB2x2trR6J?usp=drive_link"
                
            },
            {
                "name": "The perfect handshake - Neuro inspired system engineering module MSNE,TUM",
                "description": "Measuring confidence of handshake using Eskin built with pressure and imu sensors to be placed in glove like setup, finding difference between weak, strong, perfect handshake of the opponent allowing robot-human interaction more intuitive",
                "skills": ["vibrotactile actuators", "e-skin","signal classification","paper research", "team work"],
                "drive": "https://drive.google.com/drive/folders/18vc9JR6uY9kRWsA9VWYGWGKNXOhYIi-y?usp=drive_link"
            },
            {
                
                "name": " Multiple Disorder Detection by Gait Analysis using Machine Learning  - Bachelor thesis project",
                "description": "Real-time plantar and physiological data are acquired using multiple sensors interfaced with a microcontroller, and securely stored in the cloud for continuous monitoring. The collected data are analyzed through a KNN-based machine learning model via a web application, enabling accurate and early detection of gait abnormalities and related health conditions",
                "skills": ["Programming and Machine Learning", "embedded system","cloud"],
                "drive": "https://drive.google.com/drive/folders/1LKPVcRihxgflv1cFPMS5MED7NKph6ovZ?usp=drive_link"
            },
            {
                "name": "Automated IV Drip",
                "description": "Designed and developed an automated intravenous (IV) drip monitoring system using a load cell integrated with an IV stand. The system continuously measures fluid weight and processes data through an HX711 module and Arduino microcontroller to detect depletion levels. Implemented a real-time alert mechanism to notify healthcare providers when the IV fluid approaches empty, improving patient safety and reducing manual monitoring.",
                "skills": ["Arduino", "loadcell", "hardware coding"],
            }
        ],

        "publication": {
    "title": "Multiple Disorder Detection by Gait Analysis using Machine Learning",
    "link": "https://ijaem.net/issue_dcp/Literature%20review%20Onmultiple%20Disorder%20Detection%20by%20Gait%20Analysis%20Using%20Machine%20Learning.pdf"
},

        "languages": ["Tamil", "English"],

        "hobbies": ["Sketching","Reading"]
    }

    return render_template("index.html", profile=profile)


if __name__ == "__main__":
    app.run(debug=True)