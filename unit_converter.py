import streamlit as st
from pint import UnitRegistry

# Pint registry for unit conversions
ureg = UnitRegistry()

# Categories and Units
categories = {
    "Length": ["kilometer", "meter", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch", "nautical_mile"],
    "Area": ["square_meter", "square_kilometer", "square_mile", "acre", "hectare"],
    "Data Transfer Rate": ["bit_per_second", "kilobit_per_second", "megabit_per_second", "gigabit_per_second"],
    "Digital Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "Energy": ["joule", "calorie", "kilowatt_hour"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["kilometers_per_liter", "miles_per_gallon"],
    "Mass": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Plane Angle": ["degree", "radian"],
    "Pressure": ["pascal", "bar", "psi", "atmosphere"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day", "week", "year"],
    "Volume": ["liter", "milliliter", "cubic_meter", "gallon"]
}

# Function to convert units using Pint
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("Unit Converter ❄️ by Maryam")
st.write("No more confusion, just smooth and easy conversions! 🎉")

st.subheader("Select the type of conversion:🔄")
selected_category = st.selectbox("Conversion type 📏", list(categories.keys()))

# Arrange 'From unit' and 'To unit' in the same row
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From unit", categories[selected_category])
with col2:
    to_unit = st.selectbox("To unit", categories[selected_category])

value = st.number_input("Enter the value to convert ✍️", min_value=0.0, format="%.2f")

if st.button("Convert 🔄"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} is equal to {result} {to_unit} ✅")
