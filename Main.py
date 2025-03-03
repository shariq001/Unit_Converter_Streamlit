import streamlit as st

# Streamlit Page Configuration for SEO
st.set_page_config(
    page_title="Unit Converter | Muhammad Shariq", page_icon="♾️", layout="wide",  
)

st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #FFB200;
        }
        .sub-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #1ABC9C;
        }
        .date {
            text-align: center;
            color: gray;
            font-size: 16px;
        }
        .stButton>button {
            width: 100%;
            background-color: #FFB200;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #D99A00;
        }
        .result {
            font-size: 22px;
            font-weight: bold;
            color: #E74C3C;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Heading
st.markdown("<div class='title'>GIAIC - Unit Converter App</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Created By Muhammad Shariq</div>", unsafe_allow_html=True)
st.markdown("<div class='date'>Dated: 3 | 3 | 2025</div>", unsafe_allow_html=True)
st.divider()
# --------------------------------------------------------------------------------

conversion_type = st.selectbox("Select Physical Quantity Type!", ["Frequency", "Length", "Mass", "Pressure", "Speed", "Temperature", "Time"])
# Defining the Physical Quantities and storinng in a variable.

# ------------------------------------------------------------------------------



# mapping list is used to define the units in a key value pairs for each conversion types based on their units and sub units
units = {
    "Frequency": ["Hertz", "Kilohertz"],
    "Length": ["Nanometer", "Micrometer", "Millimeter", "Centimeter", "Meter", "Kilometer"],
    "Mass": ["Milligram", "Gram", "Kilogram", "Pound"],
    "Pressure": ["Pascal", "Torr"],
    "Speed": ["Metre per second", "Kilometer per hour", "Mile per hour"],
    "Temperature": ["Celsius", "Fahreinheit", "Kelvin"],
    "Time": ["Millisecond","Second", "Minute", "Hour",]
}

# ------------------------------------------------------------------------------

col1, col2 = st.columns(2) # For improved UI

# Select box input for Unit 1
with col1:
    unit1 = st.selectbox("Choose unit to convert from", units[conversion_type])
    # Selectbox input for Unit to convert from
    
# Select box input for Unit 2
with col2:   
    unit2 = st.selectbox("Choose unit to convert to", units[conversion_type])
    # Selectbox input for Unit to convert to

# -----------------------------------------------------------------------------

col3, col4 = st.columns(2) # For Improved UI

with col3:
    value = st.number_input("Enter value", min_value=0.0)
    # Number Input for Value to be converted

# -----------------------------------------------------------------------------

# Defining convertion values and operations to perform calculations based on the unit. def keyword is used to define a function.

# Frequency Conversions
def convert_frequency(value, unit1, unit2):
    conversions = {
        ("Hertz", "Kilohertz"): value / 1000,
        ("Kilohertz", "Hertz"): value * 1000,
    }
    return conversions.get((unit1, unit2), None)

# --------------------------------------------------------------------------------

# Length Conversions
def convert_length(value, unit1, unit2):
    conversions = {
        # Nanometer conversion
        ("Nanometer", "Micrometer"): value / 1000,
        ("Micrometer", "Nanometer"): value * 1000,
        
        ("Nanometer", "Millimeter"): value / 1000000,
        ("Millimeter", "Nanometer"): value * 1000000,
        
        ("Nanometer", "Centimeter"): value / 10000000,
        ("Centimeter", "Nanometer"): value * 10000000,
        
        ("Nanometer", "Meter"): value / 1000000000,
        ("Meter", "Nanometer"): value * 1000000000,
        
        ("Nanometer", "Kilometer"): value / 1000000000000,
        ("Kilometer", "Nanometer"): value * 1000000000000,
        
        # ----------- Micro Meter Conversions
        
        ("Micrometer", "Millimeter"): value / 1000,
        ("Millimeter", "Micrometer"): value * 1000,
        
        ("Micrometer", "Centimeter"): value / 10000,
        ("Centimeter", "Micrometer"): value * 10000,
        
        ("Micrometer", "Meter"): value / 1000000,
        ("Meter", "Micrometer"): value * 1000000,
        
        ("Micrometer", "Kilometer"): value / 1000000000,
        ("Kilometer", "Micrometer"): value * 1000000000,
        
        # ------------ Milli Meter conersions
        ("Millimeter", "Centimeter"): value / 10,
        ("Centimeter", "Millimeter"): value * 10,
        
        ("Millimeter", "Meter"): value / 1000,
        ("Meter", "Millimeter"): value * 1000,
        
        ("Millimeter", "Kilometer"): value / 1000000,
        ("Kilometer", "Millimeter"): value * 1000000,
        
        # ------------- Centimeter conversion
        
        ("Centimeter", "Meter"): value / 100,
        ("Meter", "Centimeter"): value * 100,
        
        ("Centimeter", "Kilometer"): value / 100000,
        ("Kilometer", "Centimeter"): value * 100000,
        
        # ------------- Meter conversions
        ("Meter", "Kilometer"): value / 1000,
        ("Kilometer", "Meter"): value * 1000,
        
    }
    return conversions.get((unit1, unit2), None)

# --------------------------------------------------------------------------------

# Mass Conversions
def convert_mass(value, unit1, unit2):
    conversions = {
        # ------------------- Milligram Conversions
        ("Milligram", "Gram"): value / 1000,
        ("Gram", "Milligram"): value * 1000,
        
        ("Milligram", "Kilogram"): value / 1000000,
        ("Kilogram", "Milligram"): value * 1000000,
        
        ("Milligram", "Pound"): value / 453600,
        ("Pound", "Milligram"): value * 453600,
        
        #--------------- Gram Conversion
        ("Gram", "Kilogram"): value / 1000,
        ("Kilogram", "Gram"): value * 1000,
        
        ("Gram", "Pound"): value / 453.6,
        ("Pound", "Gram"): value * 453.6,
        
        # --------------- Kilogram Conversion
        ("Kilogram", "Pound"): value / 2.205,
        ("Pound", "Kilogram"): value * 2.205,
    }
    return conversions.get((unit1, unit2), None)

# -----------------------------------------------------------------------

# Pressure Conversions
def convert_pressure(value, unit1, unit2):
    conversions = {
        ("Pascal", "Torr"): value / 133.3,
        ("Torr", "Pascal"): value * 133.3,
    }
    return conversions.get((unit1, unit2), None)

# ------------------------------------------------------------------

# Speed Conversions
def convert_speed(value, unit1, unit2):
    conversions = {
        ("Metre per second", "Kilometer per hour"): value * 3.6,
        ("Kilometer per hour", "Metre per second"): value / 3.6,
        
        ("Metre per second", "Mile per hour"): value * 2.237,
        ("Mile per hour", "Metre per second"): value / 2.237,
        
        ("Mile per hour", "Kilometer per hour"): value * 1.609,
        ("Kilometer per hour", "Mile per hour"): value / 1.609,
    }
    return conversions.get((unit1, unit2), None)

# ----------------------------------------------------------------------

# Temperature Conversions
def convert_temp(value, unit1, unit2):
    conversions = {
        ("Celsius", "Fahreinheit"): (value * 9/5) + 32,
        ("Fahreinheit", "Celsius"): (value - 32) * 5/9,
        
        ("Celsius", "Kelvin"): value + 273.15,
        ("Kelvin", "Celsius"): value - 273.15,
        
        ("Kelvin", "Fahreinheit"): (value - 273.15) * 9/5 + 32,
        ("Fahreinheit", "Kelvin"): (value - 32) * 5/9 + 273.15,
    }
    return conversions.get((unit1, unit2), None)

# --------------------------------------------------------------------

# Time Conversions
def convert_time(value, unit1, unit2):
    conversions = {
        # ----------------------- Millisecond Conversion
        ("Millisecond", "Second"): value / 1000,
        ("Second", "Millisecond"): value * 1000,
        
        ("Millisecond", "Minute"): value / 60000,
        ("Minute", "Millisecond"): value / 60000,
        
        ("Millisecond", "Hour"): value / 3600000,
        ("Hour", "Millisecond"): value / 3600000 ,
        
        # ---------------------- Second Conversions
        ("Second", "Minute"): value / 60,
        ("Minute", "Second"): value * 60,
        
        ("Second", "Hour"): value / 3600,
        ("Hour", "Second"): value * 3600,
        
        # ---------------------- Minute Conversions
        ("Minute", "Hour"): value / 60,
        ("Hour", "Minute"): value * 60,
    }
    return conversions.get((unit1, unit2), None)

# --------------------------------------------------------------------------------

# Conversion Button with logic and convert functionality
if st.button("Convert"):
    if value > 0:  # Ensure the number is greater than zero
        result = None

        if conversion_type == "Frequency":
            result = convert_frequency(value, unit1, unit2)
        elif conversion_type == "Length":
            result = convert_length(value, unit1, unit2)
        elif conversion_type == "Mass":
            result = convert_mass(value, unit1, unit2)
        elif conversion_type == "Pressure":
            result = convert_pressure(value, unit1, unit2)
        elif conversion_type == "Speed":
            result = convert_speed(value, unit1, unit2)
        elif conversion_type == "Temperature":
            result = convert_temp(value, unit1, unit2)
        elif conversion_type == "Time":
            result = convert_time(value, unit1, unit2)
            
            
        # Making sure the resulted is printed.
        with col4:
            if result is not None:
                st.success(f"Converted Value: {result}")
            else:
                st.warning("Conversion not available for the selected units.")
    else:
        st.warning("Enter a valid number greater than 0")
        
# Footer
st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>© 2025 Muhammad Shariq - All Rights Reserved</p>", unsafe_allow_html=True)
