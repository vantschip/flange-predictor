import streamlit as st
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Voorspellingsfunctie

def predict_flange_flatness(max_displacement, min_displacement):
    beta_0 = -0.8951  # Intercept
    beta_1 = 1.1585  # Coëfficiënt max angular displacement
    beta_2 = -1.3687  # Coëfficiënt min angular displacement
    
    return beta_0 + (beta_1 * max_displacement) + (beta_2 * min_displacement)

# Streamlit UI
st.title("Flange Flatness Predictor")

st.write("Voer waarden in voor de maximale en minimale Angular Displacement om een voorspelling te krijgen van de Flange Flatness.")

# Inputvelden
max_displacement = st.number_input("Max TOC Angular Displacement [mm]", value=-5.5, step=0.1)
min_displacement = st.number_input("Min TOC Angular Displacement [mm]", value=-6.5, step=0.1)

# Voorspelling berekenen
if st.button("Voorspel Flange Flatness"):
    predicted_flatness = predict_flange_flatness(max_displacement, min_displacement)
    st.write(f"**Voorspelde Flange Flatness: {predicted_flatness:.2f} mm**")
    
    # Tolerantiecontrole
    if predicted_flatness > 2.5:
        st.warning("Waarschuwing: De voorspelde Flange Flatness is buiten de tolerantie!")
    else:
        st.success("De voorspelde Flange Flatness ligt binnen de tolerantie.")
    
    # Grafische visualisatie
    fig, ax = plt.subplots()
    ax.scatter([max_displacement], [predicted_flatness], color='red', label='Voorspelde Flange Flatness')
    ax.set_xlabel("Max TOC Angular Displacement [mm]")
    ax.set_ylabel("Voorspelde Flange Flatness [mm]")
    ax.set_title("Relatie tussen TOC Angular Displacement en Voorspelde Flange Flatness")
    ax.legend()
    st.pyplot(fig)
