def calculate_macros_and_calories(weight, age, gender, activity_level):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * (weight/2.20462)) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * (weight/2.20462)) - (4.330 * age)
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    elif activity_level == "very active":
        calories = bmr * 1.725
    elif activity_level == "extra active":
        calories = bmr * 1.9
    protein = weight * 2.2 # 2.2 grams of protein per kilogram of body weight
    fat = calories * 0.25 / 9 # 25% of calories from fat, 9 calories per gram of fat
    carbs = (calories - (protein * 4) - (fat * 9)) / 4 # remaining calories from carbs, 4 calories per gram of carb
    return {
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs
    }
# Prompt user for information
weight = float(input("Enter your weight in kilograms: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ")
activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/extra active): ")
# Calculate macros and calories
result = calculate_macros_and_calories(weight, age, gender, activity_level)
# Print results
print("Calories: {:.2f}".format(result["calories"]))
print("Protein: {:.2f} grams".format(result["protein"]))
print("Fat: {:.2f} grams".format(result["fat"]))
print("Carbs: {:.2f} grams".format(result["carbs"]))
