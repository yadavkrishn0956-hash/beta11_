#!/usr/bin/env python3
"""
Medical Report Generator
Generates realistic fake medical reports for testing
"""

import random
from datetime import datetime, timedelta

# Sample data
PATIENTS = [
    {"name": "Rajesh Kumar", "abha": "12-3456-7890-1234", "age": 45, "gender": "Male"},
    {"name": "Priya Sharma", "abha": "12-3456-7890-5678", "age": 32, "gender": "Female"},
    {"name": "Amit Patel", "abha": "12-3456-7890-9012", "age": 28, "gender": "Male"},
    {"name": "Sneha Reddy", "abha": "12-3456-7890-3456", "age": 35, "gender": "Female"},
]

HOSPITALS = ["Apollo Hospital", "Fortis Hospital", "Max Hospital", "AIIMS", "Medanta"]
DOCTORS = ["Dr. Sharma", "Dr. Patel", "Dr. Reddy", "Dr. Singh", "Dr. Gupta"]

# Lab Report Templates
LAB_TESTS = {
    "Blood Sugar": lambda: random.randint(80, 140),
    "Hemoglobin": lambda: round(random.uniform(12.0, 16.0), 1),
    "Cholesterol": lambda: random.randint(150, 220),
    "Blood Pressure": lambda: f"{random.randint(110, 140)}/{random.randint(70, 90)}",
    "WBC Count": lambda: round(random.uniform(4.0, 11.0), 1),
    "RBC Count": lambda: round(random.uniform(4.5, 5.5), 1),
}

def generate_lab_report(patient):
    """Generate a lab report"""
    report = f"""
╔════════════════════════════════════════════════════════════════╗
║                    LABORATORY REPORT                           ║
║                   {random.choice(HOSPITALS):<40}║
╚════════════════════════════════════════════════════════════════╝

PATIENT INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name:           {patient['name']}
ABHA ID:        {patient['abha']}
Age/Gender:     {patient['age']} years / {patient['gender']}
Date:           {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Report ID:      LAB-{random.randint(10000, 99999)}

DOCTOR INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Attending:      {random.choice(DOCTORS)}
Department:     Pathology

TEST RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    for test, generator in LAB_TESTS.items():
        value = generator()
        status = "Normal" if random.random() > 0.2 else "Borderline"
        report += f"{test:<20} {str(value):<15} [{status}]\n"
    
    report += """
INTERPRETATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall health parameters are within acceptable ranges.
Minor variations noted in some parameters.
Recommend follow-up consultation with physician.

RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Continue current medication as prescribed
• Maintain healthy diet and regular exercise
• Follow-up test recommended in 3 months
• Stay hydrated and monitor symptoms

VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status:         Verified & Digitally Signed
Lab Technician: {random.choice(['Ramesh', 'Suresh', 'Kavita', 'Anita'])}
Verified By:    {random.choice(DOCTORS)}

╔════════════════════════════════════════════════════════════════╗
║  This is a digitally generated report from MediTrust AI       ║
║  For verification, visit: https://meditrust.ai/verify         ║
╚════════════════════════════════════════════════════════════════╝
"""
    return report

def generate_prescription(patient):
    """Generate a prescription"""
    medications = [
        ("Metformin 500mg", "2x daily after meals", "30 days"),
        ("Aspirin 75mg", "1x daily morning", "30 days"),
        ("Vitamin D3", "1x weekly", "12 weeks"),
        ("Paracetamol 500mg", "As needed for fever", "10 days"),
    ]
    
    selected_meds = random.sample(medications, k=random.randint(2, 4))
    
    report = f"""
╔════════════════════════════════════════════════════════════════╗
║                    MEDICAL PRESCRIPTION                        ║
║                   {random.choice(HOSPITALS):<40}║
╚════════════════════════════════════════════════════════════════╝

PATIENT INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name:           {patient['name']}
ABHA ID:        {patient['abha']}
Age/Gender:     {patient['age']} years / {patient['gender']}
Date:           {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Prescription:   RX-{random.randint(10000, 99999)}

DOCTOR INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Attending:      {random.choice(DOCTORS)}
Specialization: General Medicine
Registration:   MCI-{random.randint(100000, 999999)}

DIAGNOSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{random.choice(['Type 2 Diabetes Mellitus', 'Hypertension', 'Vitamin D Deficiency', 'Mild Fever'])}

MEDICATIONS PRESCRIBED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    for i, (med, dosage, duration) in enumerate(selected_meds, 1):
        report += f"\n{i}. {med}\n"
        report += f"   Dosage:   {dosage}\n"
        report += f"   Duration: {duration}\n"
    
    report += """
INSTRUCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Take medications as prescribed
• Do not skip doses
• Avoid alcohol consumption
• Follow-up appointment in 2 weeks
• Contact immediately if side effects occur

NEXT APPOINTMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Date: {(datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')}
Time: 10:00 AM

VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Digital Signature: {random.choice(DOCTORS)}
License Verified:  ✓

╔════════════════════════════════════════════════════════════════╗
║  This is a digitally generated prescription                    ║
║  Valid for 30 days from date of issue                          ║
╚════════════════════════════════════════════════════════════════╝
"""
    return report

def generate_xray_report(patient):
    """Generate an X-Ray report"""
    findings = random.choice([
        "No abnormalities detected. Lung fields clear. Heart size normal.",
        "Mild opacity in left lower lobe. Possible early infection. Recommend follow-up.",
        "Clear lung fields. No fractures detected. Normal cardiac silhouette.",
    ])
    
    report = f"""
╔════════════════════════════════════════════════════════════════╗
║                    RADIOLOGY REPORT (X-RAY)                    ║
║                   {random.choice(HOSPITALS):<40}║
╚════════════════════════════════════════════════════════════════╝

PATIENT INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name:           {patient['name']}
ABHA ID:        {patient['abha']}
Age/Gender:     {patient['age']} years / {patient['gender']}
Date:           {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Study ID:       XR-{random.randint(10000, 99999)}

EXAMINATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type:           Chest X-Ray (PA View)
Indication:     Routine checkup / Cough
Technique:      Digital Radiography

FINDINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{findings}

IMPRESSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{random.choice(['Normal chest X-ray', 'Mild abnormality detected', 'Follow-up recommended'])}

RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Clinical correlation advised
• Follow-up imaging if symptoms persist
• Consult with treating physician

VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Radiologist:    {random.choice(DOCTORS)}
Verified:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

╔════════════════════════════════════════════════════════════════╗
║  This is a digitally generated radiology report                ║
║  For queries, contact radiology department                     ║
╚════════════════════════════════════════════════════════════════╝
"""
    return report

def main():
    """Generate sample reports"""
    print("Medical Report Generator")
    print("=" * 70)
    print("\n1. Lab Report")
    print("2. Prescription")
    print("3. X-Ray Report")
    print("4. Generate All")
    
    choice = input("\nSelect report type (1-4): ")
    
    patient = random.choice(PATIENTS)
    
    if choice == "1":
        report = generate_lab_report(patient)
        filename = f"Lab_Report_{patient['name'].replace(' ', '_')}.txt"
    elif choice == "2":
        report = generate_prescription(patient)
        filename = f"Prescription_{patient['name'].replace(' ', '_')}.txt"
    elif choice == "3":
        report = generate_xray_report(patient)
        filename = f"XRay_Report_{patient['name'].replace(' ', '_')}.txt"
    elif choice == "4":
        # Generate all types
        for i, patient in enumerate(PATIENTS[:3]):
            reports = [
                (generate_lab_report(patient), f"Lab_Report_{patient['name'].replace(' ', '_')}.txt"),
                (generate_prescription(patient), f"Prescription_{patient['name'].replace(' ', '_')}.txt"),
                (generate_xray_report(patient), f"XRay_Report_{patient['name'].replace(' ', '_')}.txt"),
            ]
            for report, fname in reports:
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(report)
                print(f"✓ Generated: {fname}")
        print("\n✅ All reports generated successfully!")
        return
    else:
        print("Invalid choice!")
        return
    
    # Save single report
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Report generated: {filename}")
    print("\nPreview:")
    print("=" * 70)
    print(report[:500] + "...")

if __name__ == "__main__":
    main()
