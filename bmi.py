def calculate_bmi(weight, height, unit="imperial"):
    """Calculate BMI based on weight and height."""
    if unit == "metric":
        bmi = weight / (height ** 2)
    else:
        bmi = (weight * 703) / (height * height)
    return bmi

def lifestyle_index(bmi, stress_level, physical_activity, diet_quality, sleep_quality):
    """Calculate the Stress & Lifestyle Index based on various factors."""
    # Normalize input values for a combined index (adjust as necessary)
    normalized_stress = (10 - stress_level) / 10  # Inverted scale, lower stress is better
    normalized_physical_activity = physical_activity / 10  # Assuming max score of 10
    normalized_diet_quality = diet_quality / 10  # Assuming max score of 10
    normalized_sleep_quality = sleep_quality / 10  # Assuming max score of 10

    # Weighting factors (these can be adjusted based on importance)
    bmi_weight = 0.4
    stress_weight = 0.3
    activity_weight = 0.1
    diet_weight = 0.1
    sleep_weight = 0.1

    # Calculate the Stress & Lifestyle Index
    index = (bmi_weight * (bmi / 40)) + (stress_weight * normalized_stress) + \
            (activity_weight * normalized_physical_activity) + \
            (diet_weight * normalized_diet_quality) + \
            (sleep_weight * normalized_sleep_quality)
    
    return index

def main():
    """Main function to collect user input and display the results."""
    name = input("Enter your name: ")

    unit = input("Would you like to use metric or imperial units? ").lower()

    if unit == "metric":
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    else:
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))

    bmi = calculate_bmi(weight, height, unit)
    
    # Get additional input for stress and lifestyle
    stress_level = int(input("On a scale from 1 to 10, how stressed do you feel? (1 = least stressed, 10 = most stressed): "))
    physical_activity = int(input("On a scale from 1 to 10, how would you rate your physical activity level? (1 = low, 10 = high): "))
    diet_quality = int(input("On a scale from 1 to 10, how would you rate your diet quality? (1 = poor, 10 = excellent): "))
    sleep_quality = int(input("On a scale from 1 to 10, how would you rate your sleep quality? (1 = poor, 10 = excellent): "))

    lifestyle_idx = lifestyle_index(bmi, stress_level, physical_activity, diet_quality, sleep_quality)

    print(f"\n{name}, your BMI is {bmi:.2f}.")
    print(f"Your Stress & Lifestyle Index is {lifestyle_idx:.2f}.")

    # Feedback based on the index value
    if lifestyle_idx < 0.5:
        print("You're doing well! Keep maintaining a balanced lifestyle.")
    elif lifestyle_idx < 0.75:
        print("You're on the right track, but consider improving some aspects of your lifestyle.")
    else:
        print("It seems you may need to make some lifestyle changes. Consider consulting a health professional.")

if __name__ == "__main__":
    main()
