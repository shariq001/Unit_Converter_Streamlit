import streamlit as st

# Streamlit Page Configuration for SEO
st.set_page_config(
    page_title="Unit Converter | Muhammad Shariq", page_icon="♾️", layout="wide",  
)

st.markdown("<h1 style='text-align: center; font-size: 40px; font-weight: bold; color: #FFB200'>GIAIC - Unit Converter App <i class='fa-brands fa-python'></i></h1>", unsafe_allow_html=True)
st.divider() # for a divider to separate sections

st.markdown("<h2 style=' font-weight: bold; color: #1ABC9C'>Created By Muhammad Shariq</h2>", unsafe_allow_html=True)

st.write("<p style=' color: gray'>Dated: 28 | 2 | 2025</p>", unsafe_allow_html=True)

# Creating a drop down menu for selecting the conversion type and the option is stored in a variable named conversion_type to use later.
conversion_type = st.selectbox("Select the Conversion Type!", ["Length", "Weight", "Temperature", "Time"])

# Defining convertion values and operations to perform calculations based on the unit. def keyword is used to define a function.

# Units for Length Conversions
def convert_length(value, unit):
    conversions = {
        "Meters to Feet": value * 3.28084,
        "Feet to Meters": value / 3.28084,
        "Kilometers to Miles": value * 0.621371,
        "Miles to Kilometers": value / 0.621371,
        "Centimeters to Inches": value * 0.393701,
        "Inches to Centimeters": value / 0.393701
    }
    return conversions[unit]

# Units for Weight Conversions
def convert_weight(value, unit):
    conversions = {
        "Kilograms to Pounds": value * 2.20462,
        "Pounds to Kilograms": value / 2.20462,
        "Gram to Kilograms": value / 1000,
        "Kilogram to Gram": value * 1000,
    }
    return conversions[unit]

# Units for Temperatures Conversions
def convert_temperature(value, unit):
    if unit == "Celsius to Fahrenheit":
        return (value * 9/5) + 32
    elif unit == "Fahrenheit to Celsius":
        return (value - 32) * 5/9
    elif unit == "Celsius to Kelvin":
        return (value + 273)
    elif unit == "Kelvin to Celsius":
        return (value - 273)
    
# Units for Time Conversions
def convert_time(value, unit):
    conversions = {
        "Seconds to Minutes": value / 60,
        "Minutes to Hours": value / 60,
        "Hours to Days": value / 24,
        "Days to Hours": value * 24
    }
    return conversions[unit]


# mapping list is used to define the units in a key value pairs for each conversion types based on their units
units = {
    "Length": ["Meters to Feet", "Feet to Meters", "Kilometers to Miles", "Miles to Kilometers", "Centimeters to Inches", "Inches to Centimeters"],
    "Weight": ["Kilograms to Pounds", "Pounds to Kilograms", "Gram to Kilograms", "Kilogram to Gram"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"],
    "Time": ["Seconds to Minutes", "Minutes to Hours", "Hours to Days", "Days to Hours"]
}

# Creating a drop down for selecting the sub unit for conversion.
unit = st.selectbox("Choose conversion", units[conversion_type])

# input field for user input of value (numbers only) to convert it into desired unit.
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Creating a button to process the conversion
if st.button("Convert"):
    if value > 0: # ensuring the number is not zero and should be greater.
        if conversion_type == "Length":
            result = convert_length(value, unit)
        elif conversion_type == "Weight":
            result = convert_weight(value, unit)
        elif conversion_type == "Temperature":
            result = convert_temperature(value, unit)
        elif conversion_type == "Time":
            result = convert_time(value, unit)

        st.success(f"Converted Value: {result:.2f}") # :.2f ensures the result is 2 decimal place.
    else:
        st.warning("Enter a valid number greater than or 0")