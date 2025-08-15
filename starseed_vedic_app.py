import datetime
from flatlib.chart import Chart
from flatlib.geopos import GeoPos

# Survey questions for starseed traits
STARSEED_QUESTIONS = [
    "Do you feel a strong connection to the stars?",
    "Do you have recurring dreams about space or other planets?",
    "Do you feel different from those around you?",
    # ...more questions
]

# Bloodline indicators
BLOODLINE_QUESTIONS = [
    "Is there a history of psychic abilities in your family?",
    "Any ancestral legends about celestial origins?",
    # ...more questions
]

def get_birth_data():
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    birth_time = input("Enter your birth time (HH:MM): ")
    birth_place = input("Enter your birth place (City, Country): ")
    # For demo, use fixed coordinates. In production, use geocoding.
    geo = GeoPos('40n42', '74w00')  # NYC example
    dt = birth_date + ' ' + birth_time
    return dt, geo

def generate_vedic_chart(dt, geo):
    chart = Chart(dt, geo)
    # Extract relevant Vedic astrology info (nakshatras, houses, etc.)
    # For demo, print Sun sign
    sun = chart.get('SUN')
    print(f"Your Sun Sign: {sun.sign}")
    return chart

def ask_questions(questions):
    responses = []
    for q in questions:
        ans = input(q + " (yes/no): ")
        responses.append(ans.lower() == 'yes')
    return responses

def analyze_starseed_traits(responses):
    score = sum(responses)
    if score > len(responses) // 2:
        return "Likely a Starseed"
    else:
        return "Possible Earth Origin"

def analyze_bloodline(responses):
    score = sum(responses)
    if score > len(responses) // 2:
        return "Bloodline Starseed Indicators Present"
    else:
        return "No Strong Bloodline Indicators"

def main():
    print("Welcome to the Vedic-Starseed-Bloodline Analyzer")
    dt, geo = get_birth_data()
    chart = generate_vedic_chart(dt, geo)
    
    print("\nStarseed Survey:")
    starseed_responses = ask_questions(STARSEED_QUESTIONS)
    starseed_result = analyze_starseed_traits(starseed_responses)

    print("\nBloodline Survey:")
    bloodline_responses = ask_questions(BLOODLINE_QUESTIONS)
    bloodline_result = analyze_bloodline(bloodline_responses)

    print("\n--- Combined Profile ---")
    print(f"Astrology Chart: {chart}")
    print(f"Starseed Analysis: {starseed_result}")
    print(f"Bloodline Analysis: {bloodline_result}")

if __name__ == "__main__":
    main()