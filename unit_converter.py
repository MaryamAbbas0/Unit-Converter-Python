import streamlit as st

# Conversion factors for different categories
conversion_factors = {
    "Length": {
        "meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001, 
        "micrometer": 1e-6, "nanometer": 1e-9, "mile": 1609.34, "yard": 0.9144, 
        "foot": 0.3048, "inch": 0.0254, "nautical_mile": 1852
    },
    "Area": {
        "square_meter": 1, "square_kilometer": 1e6, "square_mile": 2.59e6, 
        "acre": 4046.86, "hectare": 10000
    },
    "Data Transfer Rate": {
        "bit_per_second": 1, "kilobit_per_second": 1000, "megabit_per_second": 1e6, "gigabit_per_second": 1e9
    },
    "Digital Storage": {
        "byte": 1, "kilobyte": 1024, "megabyte": 1024**2, "gigabyte": 1024**3, "terabyte": 1024**4
    },
    "Energy": {
        "joule": 1, "calorie": 4.184, "kilowatt_hour": 3.6e6
    },
    "Frequency": {
        "hertz": 1, "kilohertz": 1e3, "megahertz": 1e6, "gigahertz": 1e9
    },
    "Fuel Economy": {
        "kilometers_per_liter": 1, "miles_per_gallon": 0.4251  # Approx conversion factor
    },
    "Mass": {
        "gram": 1, "kilogram": 1000, "pound": 453.592, "ounce": 28.3495, "ton": 1e6
    },
    "Plane Angle": {
        "degree": 1, "radian": 57.2958
    },
    "Pressure": {
        "pascal": 1, "bar": 1e5, "psi": 6894.76, "atmosphere": 101325
    },
    "Speed": {
        "meter_per_second": 1, "kilometer_per_hour": 3.6, "mile_per_hour": 2.237
    },
    "Temperature": {
        "celsius": lambda x: x, 
        "fahrenheit": lambda x: (x * 9/5) + 32, 
        "kelvin": lambda x: x + 273.15
    },
    "Time": {
        "second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "year": 3.154e7
    },
    "Volume": {
        "liter": 1, "milliliter": 0.001, "cubic_meter": 1000, "gallon": 3.785
    }
}

# Function to convert units
def convert_units(value, from_unit, to_unit, category):
    try:
        if category in conversion_factors and from_unit in conversion_factors[category] and to_unit in conversion_factors[category]:
            if callable(conversion_factors[category][from_unit]):  # Special case for temperature
                return conversion_factors[category][from_unit](value)
            base_value = value * conversion_factors[category][from_unit]  # Convert to base unit
            return base_value / conversion_factors[category][to_unit]  # Convert to target unit
        else:
            return "Invalid conversion"
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("Unit Converter 🌼 by Maryam Abbas")
st.write("No more confusion, just smooth and easy conversions! 🎉")

st.subheader("Select the type of conversion:🔄")
selected_category = st.selectbox("Conversion type 📏", list(conversion_factors.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From unit", list(conversion_factors[selected_category].keys()))
with col2:
    to_unit = st.selectbox("To unit", list(conversion_factors[selected_category].keys()))

value = st.number_input("Enter the value to convert ✍️", min_value=0.0, format="%.2f")

if st.button("Convert 🔄"):
    result = convert_units(value, from_unit, to_unit, selected_category)
    st.success(f"{value} {from_unit} is equal to {result} {to_unit} ✅")
