import streamlit as st

# Initialisierung des Status
if "fan_mode" not in st.session_state:
    st.session_state.fan_mode = "Auto"
    st.session_state.fan1_state = "HIGH"  # Lüfter 1 Relais (aus)
    st.session_state.fan2_state = "HIGH"  # Lüfter 2 Relais (aus)

# Funktionslogik, um Relais zu schalten
def toggle_fan_relay(relay_id):
    # Wenn beide Lüfter "Aus" sind, gehe zurück in den "Auto"-Modus
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

# Benutzeroberfläche in Streamlit
st.title("Relais Steuerung (Web Version)")

col1, col2 = st.columns(2)

for i, relay in enumerate([1, 2]):
    state = (
        "LOW"
        if (relay == 1 and st.session_state.fan1_state == "LOW")
        or (relay == 2 and st.session_state.fan2_state == "LOW")
        else "HIGH"
    )
    label = f"Lüfter {relay} ({st.session_state.fan_mode}) - {'Ein' if state == 'LOW' else 'Aus'}"
    color = "green" if state == "LOW" else "red"

    with (col1 if relay == 1 else col2):
        if st.button(label, key=f"fan_{relay}"):
            toggle_fan_relay(relay)

        # Relaisstatus anzeigen
        st.markdown(
            f"<div style='background-color:{color};width:50px;height:50px;border-radius:25px;'></div>",
            unsafe_allow_html=True,
        )
