# Lab 13: Filtering, Sorting, and Merging DataFrames

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("=== Lab 13: Filtering, Sorting, and Merging DataFrames ===\n")

# -------------------------------------------------------
# Task 1: Create Sample Data
# -------------------------------------------------------

print("Creating sample datasets...\n")

hospital_data = {
    'hospital_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'hospital_name': [
        'City General Hospital',
        'St. Mary Medical Center',
        'Regional Health System',
        'Community Hospital',
        'University Medical Center',
        'Memorial Hospital',
        'Sacred Heart Hospital',
        'Metro General'
    ],
    'bed_count': [450, 320, 680, 180, 520, 290, 410, 380],
    'patient_satisfaction': [4.2, 4.7, 3.9, 4.5, 4.1, 4.8, 4.3, 3.8],
    'emergency_services': [True, True, True, False, True, True, True, True],
    'specialty': [
        'General',
        'Cardiac',
        'Trauma',
        'Pediatric',
        'Research',
        'Geriatric',
        'Cardiac',
        'General'
    ]
}

location_data = {
    'hospital_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'city': [
        'New York',
        'Los Angeles',
        'Chicago',
        'Houston',
        'Phoenix',
        'Philadelphia',
        'San Antonio',
        'San Diego'
    ],
    'state': ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA'],
    'zip_code': ['10001', '90210', '60601', '77001', '85001', '19101', '78201', '92101'],
    'region': ['Northeast', 'West', 'Midwest', 'South', 'West', 'Northeast', 'South', 'West']
}

hospitals_df = pd.DataFrame(hospital_data)
locations_df = pd.DataFrame(location_data)

# Save CSV files
hospitals_df.to_csv("hospitals.csv", index=False)
locations_df.to_csv("locations.csv", index=False)

print("Sample CSV files created.\n")

# -------------------------------------------------------
# Task 2: Load CSV Files
# -------------------------------------------------------

hospitals = pd.read_csv("hospitals.csv")
locations = pd.read_csv("locations.csv")

print("Hospitals Dataset:")
print(hospitals.head(), "\n")

print("Locations Dataset:")
print(locations.head(), "\n")

# -------------------------------------------------------
# Task 3: Filtering Data
# -------------------------------------------------------

print("=== Filtering Examples ===\n")

large_hospitals = hospitals[hospitals['bed_count'] > 400]
print("Hospitals with more than 400 beds:")
print(large_hospitals[['hospital_name', 'bed_count']], "\n")

emergency_hospitals = hospitals[hospitals['emergency_services'] == True]
print("Hospitals with emergency services:")
print(emergency_hospitals[['hospital_name']], "\n")

high_satisfaction = hospitals[hospitals['patient_satisfaction'] > 4.5]
print("Hospitals with satisfaction > 4.5:")
print(high_satisfaction[['hospital_name', 'patient_satisfaction']], "\n")

# Multiple condition filtering
large_emergency = hospitals[
    (hospitals['bed_count'] > 300) &
    (hospitals['emergency_services'] == True)
]

print("Large hospitals with emergency services:")
print(large_emergency[['hospital_name', 'bed_count']], "\n")

# String filtering
general_hospitals = hospitals[hospitals['hospital_name'].str.contains("General")]
print("Hospitals containing 'General':")
print(general_hospitals[['hospital_name']], "\n")

# -------------------------------------------------------
# Task 4: Sorting Data
# -------------------------------------------------------

print("=== Sorting Examples ===\n")

sorted_by_beds = hospitals.sort_values("bed_count")
print("Sorted by bed count:")
print(sorted_by_beds[['hospital_name', 'bed_count']], "\n")

sorted_by_satisfaction = hospitals.sort_values("patient_satisfaction", ascending=False)
print("Sorted by patient satisfaction:")
print(sorted_by_satisfaction[['hospital_name', 'patient_satisfaction']], "\n")

sorted_multi = hospitals.sort_values(['specialty', 'bed_count'])
print("Sorted by specialty then bed count:")
print(sorted_multi[['hospital_name', 'specialty', 'bed_count']], "\n")

# -------------------------------------------------------
# Task 5: Merging DataFrames
# -------------------------------------------------------

print("=== Merging DataFrames ===\n")

inner_merge = pd.merge(hospitals, locations, on="hospital_id")
print("Inner Join Result:")
print(inner_merge[['hospital_name', 'city', 'state']], "\n")

left_merge = pd.merge(hospitals, locations, on="hospital_id", how="left")
print("Left Join Result:")
print(left_merge[['hospital_name', 'city', 'state']], "\n")

right_merge = pd.merge(hospitals, locations, on="hospital_id", how="right")
print("Right Join Result:")
print(right_merge[['hospital_name', 'city', 'state']], "\n")

outer_merge = pd.merge(hospitals, locations, on="hospital_id", how="outer")
print("Outer Join Result:")
print(outer_merge[['hospital_name', 'city', 'state']], "\n")

# -------------------------------------------------------
# Task 6: Combined Analysis
# -------------------------------------------------------

print("=== Combined Data Analysis ===\n")

complete_data = pd.merge(hospitals, locations, on="hospital_id")

filtered_data = complete_data[
    (complete_data['bed_count'] > 300) &
    (complete_data['emergency_services'] == True)
]

result = filtered_data.sort_values("patient_satisfaction", ascending=False)

print("Large hospitals with emergency services sorted by satisfaction:")
print(result[['hospital_name', 'city', 'bed_count', 'patient_satisfaction']], "\n")

# -------------------------------------------------------
# Task 7: Regional Statistics
# -------------------------------------------------------

analysis_data = pd.merge(hospitals, locations, on="hospital_id")

regional_stats = analysis_data.groupby('region').agg({
    'bed_count': ['mean', 'max', 'min'],
    'patient_satisfaction': ['mean', 'max', 'min'],
    'hospital_id': 'count'
}).round(2)

regional_stats.columns = ['_'.join(col) for col in regional_stats.columns]

print("Regional Hospital Statistics:")
print(regional_stats, "\n")

# -------------------------------------------------------
# Task 8: Summary Report
# -------------------------------------------------------

def create_hospital_report(hospitals_df, locations_df):

    merged_data = pd.merge(hospitals_df, locations_df, on='hospital_id')

    quality_hospitals = merged_data[merged_data['patient_satisfaction'] > 4.0]

    sorted_quality = quality_hospitals.sort_values('bed_count', ascending=False)

    summary_stats = {
        "total_hospitals": len(merged_data),
        "quality_hospitals": len(quality_hospitals),
        "avg_bed_count": merged_data['bed_count'].mean(),
        "avg_satisfaction": merged_data['patient_satisfaction'].mean(),
        "emergency_services": merged_data['emergency_services'].sum()
    }

    return sorted_quality, summary_stats


report, stats = create_hospital_report(hospitals, locations)

print("=== HOSPITAL REPORT ===")
print(f"Total Hospitals: {stats['total_hospitals']}")
print(f"Quality Hospitals (>4.0 satisfaction): {stats['quality_hospitals']}")
print(f"Average Bed Count: {stats['avg_bed_count']:.1f}")
print(f"Average Satisfaction: {stats['avg_satisfaction']:.2f}")
print(f"Hospitals with Emergency Services: {stats['emergency_services']}\n")

print("Top Quality Hospitals:")
print(report[['hospital_name', 'city', 'bed_count', 'patient_satisfaction']])
