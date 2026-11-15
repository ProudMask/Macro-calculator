"""Educational revised Harris–Benedict calculator with explicit scenario assumptions."""
import argparse
import json
import math

ACTIVITY_FACTORS = {'sedentary': 1.2, 'lightly active': 1.375, 'moderately active': 1.55, 'very active': 1.725, 'extra active': 1.9}


def number(value, name):
    if isinstance(value, bool):
        raise ValueError(f'{name} must be a finite number')
    try:
        value = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f'{name} must be a finite number') from exc
    if not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    return value


def calculate_macros_and_calories(weight_kg, height_cm, age_years, sex, activity_level, protein_g_per_kg=2.2, fat_fraction=0.25):
    """Return unrounded estimates; macro parameters describe a scenario, not advice."""
    weight = number(weight_kg, 'weight_kg')
    height = number(height_cm, 'height_cm')
    age = number(age_years, 'age_years')
    protein_factor = number(protein_g_per_kg, 'protein_g_per_kg')
    fat_fraction = number(fat_fraction, 'fat_fraction')
    if weight <= 0 or height <= 0 or age < 18:
        raise ValueError('Weight and height must be positive; this calculator accepts adults aged 18 or above')
    if protein_factor < 0 or not 0 <= fat_fraction < 1:
        raise ValueError('Protein factor must be nonnegative and fat fraction must be in [0, 1)')
    if not isinstance(sex, str) or not isinstance(activity_level, str):
        raise ValueError('Sex and activity level must be strings')
    sex = sex.strip().casefold()
    activity_level = activity_level.strip().casefold()
    if sex not in {'male', 'female'}:
        raise ValueError('Select male or female to choose the published equation coefficients')
    if activity_level not in ACTIVITY_FACTORS:
        raise ValueError(f'Unknown activity level; choose from {list(ACTIVITY_FACTORS)}')
    if sex == 'male':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    calories = bmr * ACTIVITY_FACTORS[activity_level]
    protein = weight * protein_factor
    fat = calories * fat_fraction / 9
    carbs = (calories - protein * 4 - fat * 9) / 4
    if not all(math.isfinite(v) for v in (bmr, calories, protein, fat, carbs)) or bmr <= 0 or carbs < 0:
        raise ValueError('Inputs or macro assumptions produce an invalid energy allocation')
    return {'method': 'revised Harris-Benedict (Roza-Shizgal, 1984)', 'inputs': {'weight_kg': weight, 'height_cm': height, 'age_years': age, 'equation_sex': sex}, 'assumptions': {'activity_level': activity_level, 'activity_factor': ACTIVITY_FACTORS[activity_level], 'protein_g_per_kg': protein_factor, 'fat_fraction': fat_fraction}, 'bmr_kcal_per_day': bmr, 'estimated_tdee_kcal_per_day': calories, 'protein_g_per_day': protein, 'fat_g_per_day': fat, 'carbs_g_per_day': carbs}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--weight-kg', required=True, type=float)
    parser.add_argument('--height-cm', required=True, type=float)
    parser.add_argument('--age-years', required=True, type=float)
    parser.add_argument('--sex', required=True, choices=['male', 'female'])
    parser.add_argument('--activity', required=True, choices=list(ACTIVITY_FACTORS))
    parser.add_argument('--protein-g-per-kg', type=float, default=2.2)
    parser.add_argument('--fat-fraction', type=float, default=0.25)
    args = parser.parse_args()
    try:
        result = calculate_macros_and_calories(args.weight_kg, args.height_cm, args.age_years, args.sex, args.activity, args.protein_g_per_kg, args.fat_fraction)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
