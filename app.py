import streamlit as st

# Title of the app
st.title("📏 Unit Converter App")
st.subheader("Easily convert between different units!")

# Sidebar menu
conversion_type = st.sidebar.radio("Choose a conversion type:", ["Length", "Weight", "Temperature"])

# ---------------- Length Converter ----------------
def length_converter():
    st.header("📏 Length Converter")
    units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371, "Feet": 3.28084}
    
    amount = st.number_input("Enter length:", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From:", list(units.keys()))
    to_unit = st.selectbox("To:", list(units.keys()))

    if st.button("Convert"):
        result = amount * (units[to_unit] / units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

# ---------------- Weight Converter ----------------
def weight_converter():
    st.header("⚖️ Weight Converter")
    units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    
    amount = st.number_input("Enter weight:", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From:", list(units.keys()))
    to_unit = st.selectbox("To:", list(units.keys()))

    if st.button("Convert"):
        result = amount * (units[to_unit] / units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

# ---------------- Temperature Converter ----------------
def temperature_converter():
    st.header("🌡 Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

    amount = st.number_input("Enter temperature:", value=0.0)
    from_unit = st.selectbox("From:", temp_units)
    to_unit = st.selectbox("To:", temp_units)

    if st.button("Convert"):
        result = None
        if from_unit == to_unit:
            result = amount
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (amount * 9/5) + 32
            elif to_unit == "Kelvin":
                result = amount + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (amount - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (amount - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = amount - 273.15
            elif to_unit == "Fahrenheit":
                result = (amount - 273.15) * 9/5 + 32
        
        st.success(f"{amount} {from_unit} = {result:.2f} {to_unit}")

# Execute the selected conversion function
if conversion_type == "Length":
    length_converter()
elif conversion_type == "Weight":
    weight_converter()
elif conversion_type == "Temperature":
    temperature_converter()

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
