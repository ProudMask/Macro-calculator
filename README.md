# Macro and Calorie Calculator

An educational formula calculator with explicit units, reproducible examples, and validated inputs. Uses the 1984 revised Harris–Benedict coefficients to estimate resting energy, applies an activity factor, then illustrates a configurable macro allocation. No third-party packages are required; use Python 3.10 or later.

## Run

```bash
python macros_calc.py --weight-kg 80 --height-cm 180 --age-years 30 --sex male --activity sedentary
python -m unittest discover -s tests -v
```

Use quotes for activity names with spaces, for example `--activity 'moderately active'`. The CLI prints JSON with input units, assumptions, estimated energy, and macro quantities. Importing the module does not prompt for input or run calculations.

## Calculation

- Male equation: `88.362 + 13.397*weight_kg + 4.799*height_cm - 5.677*age_years`
- Female equation: `447.593 + 9.247*weight_kg + 3.098*height_cm - 4.330*age_years`

The sex parameter selects the published equation coefficients. Estimated daily energy is the equation output multiplied by the chosen activity factor. These factors are inherited heuristic assumptions from the original project, not parameters fitted or validated here:

| Activity scenario | Factor |
| --- | --- |
| sedentary | 1.2 |
| lightly active | 1.375 |
| moderately active | 1.55 |
| very active | 1.725 |
| extra active | 1.9 |

The inherited defaults of 2.2 g/kg protein and 25% energy from fat are **illustrative scenario inputs, not individualized recommendations**. Change them with `--protein-g-per-kg` and `--fat-fraction`. Fat uses 9 kcal/g; protein and carbohydrate use 4 kcal/g. Carbohydrate receives the remaining energy. Impossible negative carbohydrate allocations are rejected rather than clipped to zero.

## Worked examples

| Synthetic inputs | Equation result (kcal/day) |
| --- | --- |
| 80 kg, 180 cm, age 30, male | 1853.632 |
| 60 kg, 165 cm, age 30, female | 1383.683 |

The first example at factor 1.2 yields estimated daily energy of 2224.3584 kcal. Tests check both examples and that energy allocated to macros reconciles with the energy estimate. These are arithmetic checks, not evidence of predictive accuracy.

## Fix and limitations

The original code incorrectly used weight divided by 2.20462 in the height term. Height is now a required independent input in centimeters; weight is kilograms. This changes the Python function signature to `calculate_macros_and_calories(weight_kg, height_cm, age_years, sex, activity_level, ...)` and replaces interactive prompts with explicit CLI options.

The calculator accepts finite positive height/weight and adult ages, validates choices, and rejects invalid allocations. Mathematical validity does not imply clinical applicability. Estimates are not measured metabolism, an individualized meal plan, or clinical advice. There is no trained model or validation dataset in this repository.

## Source

Roza AM, Shizgal HM (1984). [The Harris Benedict equation reevaluated: resting energy requirements and the body cell mass](https://pubmed.ncbi.nlm.nih.gov/6741850/). DOI: 10.1093/ajcn/40.1.168. [Full paper](https://zakboekdietetiek.nl/wp-content/uploads/2015/06/roza-1984.pdf).
