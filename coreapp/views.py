from django.shortcuts import render
from joblib import load
from sklearn.ensemble import RandomForestClassifier
import os

# # Get the directory of the current Python module (__file__ is the path of the current module)
# current_directory = os.path.dirname(__file__)

# # # Construct the path to the trained model file
# model_file_path = os.path.join(current_directory, 'trained_rf_model.joblib')

# # # Load the trained model
# trained_rf_model = load(model_file_path)
# print("Model File Path:", model_file_path)





def Home(request):
        return render(request, 'coreapp/base.html')


def predict_human_development_level(gender_inequality_index, maternal_mortality_ratio, adolescent_birth_rate,
                                    women_parliament_seats, female_secondary_education, male_secondary_education,
                                    female_labour_force, male_labour_force):
    # Construct input data as a dictionary or a pandas DataFrame
    input_data = {
        'Gender Inequality Index': gender_inequality_index,
        'Maternal mortality ratio': maternal_mortality_ratio,
        'Adolescent birth rate': adolescent_birth_rate,
        'Share of seats in parliament (% held by women)': women_parliament_seats,
        'F_secondary_educ': female_secondary_education,
        'M_secondary_educ': male_secondary_education,
        'F_Labour_force': female_labour_force,
        'M_labour_force': male_labour_force
    }

    # Make prediction using the loaded model
   


def predict_view(request):
    if request.method == 'POST':
        gender_inequality_index = float(request.POST.get('gender_inequality_index'))
        maternal_mortality_ratio = float(request.POST.get('maternal_mortality_ratio'))
        adolescent_birth_rate = float(request.POST.get('adolescent_birth_rate'))
        women_parliament_seats = float(request.POST.get('women_parliament_seats'))
        female_secondary_education = float(request.POST.get('female_secondary_education'))
        male_secondary_education = float(request.POST.get('male_secondary_education'))
        female_labour_force = float(request.POST.get('female_labour_force'))
        male_labour_force = float(request.POST.get('male_labour_force'))
        
        prediction = predict_human_development_level(gender_inequality_index, maternal_mortality_ratio,
                                                     adolescent_birth_rate, women_parliament_seats,
                                                     female_secondary_education, male_secondary_education,
                                                     female_labour_force, male_labour_force)
        # Pass the prediction result to the template or handle it as needed
        return render(request, 'coreapp/result.html', {'prediction': prediction})
    else:
        # Render the form template for user input
        return render(request, 'coreapp/predict.html')

