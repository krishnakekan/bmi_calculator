
# let's data in dict i.e key, value pair in python, we can read json files using JSON module in python.

#pip install numpy
import numpy as np

data = [
  {
    'Gender': 'Male',
    'HeightCM': 171,
    'WeightKG': 96
  },
  {
    'Gender': 'Male',
    'HeightCM': 161,
    'WeightKG': 85
  },
  {
    'Gender': 'Male',
    'HeightCM': 180,
    'WeightKG': 77
  },
  {
    'Gender': 'Female',
    'HeightCM': 166,
    'WeightKG': 62
  },
  {
    'Gender': 'Female',
    'HeightCM': 150,
    'WeightKG': 70
  },
  {
    'Gender': 'Female',
    'HeightCM': 167,
    'WeightKG': 82
  }
]

def calculate_bmi(data):
    results = []
    for dat in data:
        try:
            res = {}
            bmi = dat['WeightKG']/(dat['HeightCM']/100)
            res['Gender'] = dat['Gender']
            res['BMI (kg/m2)'] = bmi
            #print(bmi)
        except KeyError as e:
            print(e)
        if bmi in np.arange(0,19.4):
            res['BMI Category'] = 'Underweight'
            res['Health risk'] = 'Malnutrition risk'

        elif bmi in np.arange(18.5,25.9):
            res['BMI Category'] = 'Normal weight'
            res['Health risk'] = 'Low risk'

        elif bmi in np.arange(25,30.9):
            res['BMI Category'] = 'Over weight'
            res['Health risk'] = 'Enhanced risk'

        elif bmi in np.arange(30,35.9):
            res['BMI Category'] = 'Moderately obese'
            res['Health risk'] = 'Medium risk'

        elif bmi in np.arange(35,40.9):
            res['BMI Category'] = 'Severely obese'
            res['Health risk'] = 'High risk'

        elif bmi > 40:
            res['BMI Category'] = 'Underweight'
            res['Health risk'] = 'Very High risk'

        if len(res) > 0:
            results.append(res)
    return results

result = calculate_bmi(data)
print(result)

    
        
        


    


    


