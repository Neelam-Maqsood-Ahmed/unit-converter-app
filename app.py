# import streamlit as st

# st.title(" Unit Converter App")
# st.markdown("### Convert, Length, Weight and Time Instantly")
# st.write("Welcome!Select a category, enter the value and get converted result in real time")
# category = st.selectbox("Select Category", ["Length", "Weight", "Time"])


# def convert_units(category, value, unit):
#     if category == "length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
        
#         elif unit == "Weight":
#              if unit == "Kilograms to pounds":
#                  return value * 2.20462
#              elif category == "pounds to Kilogram":
#                  return value / 2.20462
             
#         elif unit == "Time":
#              if unit == "Seconds to Minutes":
#                  return value / 60
#              elif category == "Minutes to secondes":
#                  return value * 60
#              elif unit == "Minutes to Hours":
#                     return value / 60
#              elif unit == "Hours to Minutes":
#                     return value * 60
#              elif unit == "Hours to Days":
#                     return value / 24
#              elif unit == "Days to Hours":
#                     return value * 24
             

#              if category == "length":
#                   unit = st.selectbox("Select Unit", ["Kilometers to Miles", "Miles to Kilometers"])
#              elif category == "Weight":
#                     unit = st.selectbox("Select Unit", ["Kilograms to pounds", "pounds to Kilogram"])
#              elif category == "Time":
#                     unit = st.selectbox("Select Unit", ["Seconds to Minutes", "Minutes to secondes", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

# value = st.number_input("Enter Value to convert")
# if st.button("Convert"):
#     result = convert_units(category, value, unit)
#     st.success(f"Converted Value is {result}")
import streamlit as st  

st.title("Unit Converter App")  
st.markdown("### Convert Length, Weight, and Time Instantly")  
st.write("Welcome! Select a category, enter the value, and get the converted result in real time.")  

category = st.selectbox("Select Category", ["Length", "Weight", "Time"])  

def convert_units(category, value, unit):  
    if category == "Length":  
        if unit == "Kilometers to Miles":  
            return value * 0.621371  
        elif unit == "Miles to Kilometers":  
            return value / 0.621371  

    elif category == "Weight":  
        if unit == "Kilograms to Pounds":  
            return value * 2.20462  
        elif unit == "Pounds to Kilograms":  
            return value / 2.20462  

    elif category == "Time":  
        if unit == "Seconds to Minutes":  
            return value / 60  
        elif unit == "Minutes to Seconds":  
            return value * 60  
        elif unit == "Minutes to Hours":  
            return value / 60  
        elif unit == "Hours to Minutes":  
            return value * 60  
        elif unit == "Hours to Days":  
            return value / 24  
        elif unit == "Days to Hours":  
            return value * 24  

    return "Invalid conversion"  # Fallback case if no match is found  

# Define the unit options based on the category selected  
if category == "Length":  
    unit = st.selectbox("Select Unit", ["Kilometers to Miles", "Miles to Kilometers"])  
elif category == "Weight":  
    unit = st.selectbox("Select Unit", ["Kilograms to Pounds", "Pounds to Kilograms"])  
elif category == "Time":  
    unit = st.selectbox("Select Unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])  

value = st.number_input("Enter Value to Convert")  

if st.button("Convert"):  
    result = convert_units(category, value, unit)  
    st.success(f"Converted Value is {result:.2f}")  