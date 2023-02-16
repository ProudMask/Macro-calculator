# Macro and Calorie Calculator

This is a simple program written in Python that calculates your macros and calories based on your weight, age, gender, and activity level.

## Method

The program uses the Harris-Benedict equation to calculate your basal metabolic rate (BMR), which is the number of calories your body burns at rest. The equation takes into account your weight, age, and gender:

- For males: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)
- For females: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years)

Once your BMR is calculated, the program then multiplies it by a factor based on your activity level to determine your total daily energy expenditure (TDEE), which is the number of calories you need to maintain your current weight:

- Sedentary: little or no exercise, TDEE = BMR x 1.2
- Lightly active: light exercise or sports 1-3 days per week, TDEE = BMR x 1.375
- Moderately active: moderate exercise or sports 3-5 days per week, TDEE = BMR x 1.55
- Very active: hard exercise or sports 6-7 days per week, TDEE = BMR x 1.725
- Extra active: very hard exercise or sports, physical job or training twice per day, TDEE = BMR x 1.9
- Finally, the program calculates your macro needs based on the following guidelines:

- Protein: 2.2 grams of protein per kilogram of body weight
- Fat: 25% of calories from fat, 9 calories per gram of fat
- Carbs: remaining calories from carbs, 4 calories per gram of carb

## Usage

To use the program, simply run the Python script and follow the prompts to enter your weight, age, gender, and activity level. The program will then calculate your macro and calorie needs and print the results to the console.
```
python
Copy code
python macro_calculator.py
```

## Contributing
If you have any suggestions or improvements for the program, feel free to open an issue or submit a pull request.
