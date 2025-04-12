import streamlit as st

# Initialisierung des Status
if "fan_mode" not in st.session_state:
    st.session_state.fan_mode = "Auto"  # Beide Lüfter starten im Auto-Modus
    st.session_state.fan1_state = "HIGH"  # Lüfter 1 (aus)
    st.session_state.fan2_state = "HIGH"  # Lüfter 2 (aus)

# Funktionslogik, um Relais zu schalten
def toggle_fan_relay(relay_id):
    # Wenn beide Relais "Aus" sind, kehre zurück zu Auto-Modus
    if st.session_state.fan1_state == "HIGH" and st.session_state.fan2_state == "HIGH":
        st.session_state.fan_mode = "Auto"

    # Wenn Relais in "Auto" ist, wechsle auf "Manuell"
    if st.session_state.fan_mode == "Auto":
        st.session_state.fan_mode = "Manuell"

    # Steuerung der Relais
    if relay_id == 1:
        st.session_state.fan1_state = "LOW" if st.session_state.fan1_state == "HIGH" else "HIGH"
    elif relay_id == 2:
        st.session_state.fan2_state = "LOW" if st.session_state.fan2_state == "HIGH" else "HIGH"

    update_button_state()

def update_button_state():
    # Lüfter 1 (Pin 26)
    if st.session_state.fan1_state == "LOW":
        st.session_state.fan1_label = f"Lüfter 1 ({st.session_state.fan_mode}) - Ein"
        st.session_state.fan1_color = "green"
    else:
        st.session_state.fan1_label = f"Lüfter 1 ({st.session_state.fan_mode}) - Aus"
        st.session_state.fan1_color = "red"

    # Lüfter 2 (Pin 25)
    if st.session_state.fan2_state == "LOW":
        st.session_state.fan2_label = f"Lüfter 2 ({st.session_state.fan_mode}) - Ein"
        st.session_state.fan2_color = "green"
    else:
        st.session_state.fan2_label = f"Lüfter 2 ({st.session_state.fan_mode}) - Aus"
        st.session_state.fan2_color = "red"

# Benutzeroberfläche in Streamlit
st.title("Relais Steuerung (Web Version)")

# Buttons zum Steuern der Lüfter
col1, col2 = st.columns(2)

# Lüfter 1 (Pin 26)
with col1:
    st.button(st.session_state.fan1_label, key="fan_1", on_click=toggle_fan_relay, args=(1,))
    st.markdown(
        f"<div style='background-color:{st.session_state.fan1_color};width:50px;height:50px;border-radius:25px;'></div>",
        unsafe_allow_html=True,
    )

# Lüfter 2 (Pin 25)
with col2:
    st.button(st.session_state.fan2_label, key="fan_2", on_click=toggle_fan_relay, args=(2,))
    st.markdown(
        f"<div style='background-color:{st.session_state.fan2_color};width:50px;height:50px;border-radius:25px;'></div>",
        unsafe_allow_html=True,
    )

