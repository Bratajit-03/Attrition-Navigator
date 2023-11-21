from flask import Flask, request, render_template
import pickle
import numpy as np

model = pickle.load(open("attrition_rate.pkl", 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == "POST":
        Age = int(request.form['Age'])
        BusinessTravel = request.form['BusinessTravel']
        DailyRate = int(request.form['DailyRate'])
        Department = request.form['Department']
        DistanceFromHome = request.form['DistanceFromHome']
        Education = request.form['Education']
        EducationField = request.form['EducationField']
        EnvironmentSatisfaction = request.form['EnvironmentSatisfaction']
        Gender = request.form['Gender']
        HourlyRate = request.form['HourlyRate']
        JobInvolvement = request.form['JobInvolvement']
        JobLevel = request.form['JobLevel']
        JobRole = request.form['JobRole']
        JobSatisfaction = request.form['JobSatisfaction']
        MaritalStatus = request.form['MaritalStatus']
        MonthlyIncome = request.form['MonthlyIncome']
        MonthlyRate = request.form['MonthlyRate']
        NumCompaniesWorked = request.form['NumCompaniesWorked']
        OverTime = request.form['OverTime']
        PercentSalaryHike = request.form['PercentSalaryHike']
        PerformanceRating = request.form['PerformanceRating']
        RelationshipSatisfaction = request.form['RelationshipSatisfaction']
        StockOptionLevel = request.form['StockOptionLevel']
        TotalWorkingYears = request.form['TotalWorkingYears']
        TrainingTimesLastYear = request.form['TrainingTimesLastYear']
        WorkLifeBalance = request.form['WorkLifeBalance']
        YearsAtCompany = request.form['YearsAtCompany']
        YearsInCurrentRole = request.form['YearsInCurrentRole']
        YearsSinceLastPromotion = request.form['YearsSinceLastPromotion']
        YearsWithCurrManager = request.form['YearsWithCurrManager']

        # BusinessTravel
        if BusinessTravel == "Travel_Rarely":
            BusinessTravel = 2
        elif BusinessTravel == "Travel_Frequently":
            BusinessTravel = 1
        else:
            BusinessTravel = 0

        # Department
        if Department == "Sales":
            Department = 2
        elif Department == "Research_&_Development":
            Department = 1
        else:
            Department = 0

        # Education
        if Education == "Below_College":
            Education = 1
        elif Education == "College":
            Education = 2
        elif Education == "Bachelor":
            Education = 3
        else:
            Education = 4

        # EducationField
        if EducationField == "Life_Sciences":
            EducationField = 1
        elif EducationField == "Other":
            EducationField = 4
        elif EducationField == "Medical":
            EducationField = 3
        elif EducationField == "Marketing":
            EducationField = 2
        elif EducationField == "Technical_Degree ":
            EducationField = 5
        else:
            EducationField = 0

        # EnvironmentSatisfaction
        if EnvironmentSatisfaction == "Low":
            EnvironmentSatisfaction = 1
        elif EnvironmentSatisfaction == "Medium":
            EnvironmentSatisfaction = 2
        elif EnvironmentSatisfaction == "High":
            EnvironmentSatisfaction = 3
        else:
            EnvironmentSatisfaction = 4

        # Gender
        if Gender == "Male":
            Gender = 1
        else:
            Gender = 0

        # JobInvolvement
        if JobInvolvement == "Low":
            JobInvolvement = 1
        elif JobInvolvement == "Medium":
            JobInvolvement = 2
        elif JobInvolvement == "High":
            JobInvolvement = 3
        else:
            JobInvolvement = 4

        # JobSatisfaction
        if JobSatisfaction == "Low":
            JobSatisfaction = 1
        elif JobSatisfaction == "Medium":
            JobSatisfaction = 2
        elif JobSatisfaction == "High":
            JobSatisfaction = 3
        else:
            JobSatisfaction = 4

        # JobRole
        if JobRole == "Human_Resorces":
            JobRole = 1
        elif JobRole == "Laboratory_Technician":
            JobRole = 2
        elif JobRole == "Manager":
            JobRole = 3
        elif JobRole == "Manufacturing_Director":
            JobRole = 4
        elif JobRole== "Research_Director":
            JobRole = 5
        elif JobRole == "Research_Scientist":
            JobRole = 6
        elif JobRole == "Sales_Executive":
            JobRole = 7
        elif JobRole == "Sales_Representative":
            JobRole = 8
        else:
            JobRole = 0

        # MaritalStatus
        if MaritalStatus == "Married":
            MaritalStatus = 1
        elif MaritalStatus == "Single":
            MaritalStatus = 2
        else:
            MaritalStatus = 0

        # OverTime
        if OverTime == "Yes":
            OverTime = 1
        else:
            OverTime = 0

        # RelationshipSatisfaction
        if RelationshipSatisfaction == "Low":
            RelationshipSatisfaction = 1
        elif RelationshipSatisfaction == "Medium":
            RelationshipSatisfaction = 2
        elif RelationshipSatisfaction == "High":
            RelationshipSatisfaction = 3
        else:
            RelationshipSatisfaction = 4

        # WorkLifeBalance
        if WorkLifeBalance == "Bad":
            WorkLifeBalance = 1
        elif WorkLifeBalance == "Good":
            WorkLifeBalance = 2
        elif WorkLifeBalance == "Better":
            WorkLifeBalance = 3
        else:
            WorkLifeBalance = 4
        

        input_features = np.array([Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager])


        prediction = model.predict([input_features])[0]

        if prediction == 0:
            prediction = "Based on the provided information, it appears that the employee is likely to remain with the company."
        else:
            prediction = "Based on the provided information, there is a high probability that the employee may consider leaving the company."


        return render_template("index.html", prediction=prediction )

    else:
        return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
