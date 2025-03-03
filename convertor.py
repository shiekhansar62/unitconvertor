
# import streamlit as st 

# # Improved CSS styling
# st.markdown("""
#     <style>
#     body {
#         background-color: #1e1e2f;
#         color: white;
#     }
#     .stApp {
#         background: linear-gradient(135deg, #3e3e55, #5a5a80);
#         padding: 30px;
#         border-radius: 15px;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
#     }
#     h1 {
#         text-align: center;
#         font-size: 36px;
#         color: #ffffff;
#     }
#     .stButton>button {
#         background: linear-gradient(45deg, #0b5394, #351c75);
#         color: white;
#         font-size: 18px;
#         padding: 10px 20px;
#         border-radius: 10px;
#         transition: 0.3s;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
#         border: none;
#     }
#     .stButton>button:hover {
#         transform: scale(1.05);
#         background: linear-gradient(45deg, #92fe9d, #00c9ff);
#         color: black;
#     }
#     .result-box {
#         font-size: 20px;
#         font-weight: bold;
#         text-align: center;
#         background: rgba(255, 255, 255, 0.1);
#         padding: 50px;
#         border-radius: 10px;
#         margin-top: 20px;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
#     }
#     .footer {
#         text-align: center;
#         margin-top: 50px;
#         font-size: 14px;
#         color: #ffffff;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Title and description
# st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
# st.write("Easily convert between different units of length, weight, and temperature.")

# # Sidebar menu
# conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
# value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
# col1, col2 = st.columns(2)

# if conversion_type == "Length":
#     with col1:
#         from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
#     with col2:
#         to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
# elif conversion_type == "Weight":
#     with col1:
#         from_unit = st.selectbox("From", ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"])
#     with col2:
#         to_unit = st.selectbox("To", ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"])
# elif conversion_type == "Temperature":
#     with col1:
#         from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
#     with col2:
#         to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    
# # Conversion functions 
# def length_converter(value, from_unit, to_unit):
#     length_units = {
#         'Meters': 1, 
#         'Kilometers': 0.001, 
#         'Centimeters': 100, 
#         'Millimeters': 1000, 
#         'Miles': 0.000621371, 
#         'Yards': 1.09361, 
#         'Feet': 3.28084, 
#         'Inches': 39.3701
#     }
#     # Convert value to meters, then to target unit
#     return (value / length_units[from_unit]) * length_units[to_unit]

# def weight_converter(value, from_unit, to_unit):
#     weight_units = {
#         'Grams': 1, 
#         'Kilograms': 0.001, 
#         'Milligrams': 1000, 
#         'Pounds': 0.00220462, 
#         'Ounces': 0.035274
#     }
#     # Convert value to grams, then to target unit
#     return (value / weight_units[from_unit]) * weight_units[to_unit]

# def temp_converter(value, from_unit, to_unit):
#     # Convert to Celsius first
#     if from_unit == "Celsius":
#         celsius = value
#     elif from_unit == "Fahrenheit":
#         celsius = (value - 32) * 5/9
#     elif from_unit == "Kelvin":
#         celsius = value - 273.15

#     if to_unit == "Celsius":
#         return celsius
#     elif to_unit == "Fahrenheit":
#         return (celsius * 9/5) + 32
#     elif to_unit == "Kelvin":
#         return celsius + 273.15

# # Button for conversion 
# if st.button("🤖 Convert"):
#     if conversion_type == "Length":
#         result = length_converter(value, from_unit, to_unit)
#     elif conversion_type == "Weight":
#         result = weight_converter(value, from_unit, to_unit)
#     elif conversion_type == "Temperature":
#         result = temp_converter(value, from_unit, to_unit)

#     st.markdown(f"<div class='result-box'>Result: {result}</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='footer'>Developed by <a href='https://github.com/shiekhansar62' target='_blank'>shiekhansar62</a></div>", unsafe_allow_html=True)





import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    /* Outer container for the app */
    .outer-container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background: linear-gradient(135deg, #3e3e55, #5a5a80);
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 50px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Start outer container
st.markdown("<div class='outer-container'>", unsafe_allow_html=True)

# Title and description
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    
# Conversion functions 
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 
        'Kilometers': 0.001, 
        'Centimeters': 100, 
        'Millimeters': 1000, 
        'Miles': 0.000621371, 
        'Yards': 1.09361, 
        'Feet': 3.28084, 
        'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Grams': 1, 
        'Kilograms': 0.001, 
        'Milligrams': 1000, 
        'Pounds': 0.00220462, 
        'Ounces': 0.035274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    # Convert input to Celsius
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15

    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15

# Button for conversion 
if st.button("🤖 Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>Result: {result}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='footer'>Developed by <a href='https://github.com/shiekhansar62' target='_blank'>shiekhansar62</a></div>", unsafe_allow_html=True)

# End outer container
st.markdown("</div>", unsafe_allow_html=True)
