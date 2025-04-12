import streamlit as st

# Initialisierungen
if "fan_mode" not in st.session_state:
    st.session_state.fan_mode = "Auto"
    st.session_state.fan1_state = "HIGH"  # Lüfter 1 (aus)
    st.session_state.fan2_state = "HIGH"  # Lüfter 2 (aus)
    st.session_state.relais_states = {"Lüfter 1": "HIGH", "Lüfter 2": "HIGH", "ECU Mainswitch": "HIGH",
                                      "Zündung": "HIGH", "Haldex": "HIGH", "Servolenkung": "HIGH", "Lüfter": "HIGH", "Licht": "HIGH"}

relais_names = ["ECU Mainswitch", "Zündung", "Haldex", "Servolenkung", "Lüfter 1", "Lüfter 2"]

# Funktionslogik, um Relais zu schalten
def toggle_relay(relay_name):
    # Wenn beide Lüfter aus sind, gehe zurück zu Auto-Modus
    if st.session_state.relais_states["Lüfter 1"] == "HIGH" and st.session_state.relais_states["Lüfter 2"] == "HIGH":
        st.session_state.fan_mode = "Auto"
    # Wenn der Modus Auto ist, wechsle auf Manuell
    if st.session_state.fan_mode == "Auto":
        st.session_state.fan_mode = "Manuell"

    # Wechsel Relais-Zustand für Lüfter 1 oder 2
    if relay_name == "Lüfter 1":
        st.session_state.relais_states["Lüfter 1"] = "LOW" if st.session_state.relais_states["Lüfter 1"] == "HIGH" else "HIGH"
    elif relay_name == "Lüfter 2":
        st.session_state.relais_states["Lüfter 2"] = "LOW" if st.session_state.relais_states["Lüfter 2"] == "HIGH" else "HIGH"
    else:
        st.session_state.relais_states[relay_name] = "LOW" if st.session_state.relais_states[relay_name] == "HIGH" else "HIGH"

    update_button_state()

def update_button_state():
    # Lüfter 1 (Pin 26)
    if st.session_state.relais_states["Lüfter 1"] == "LOW":
        st.session_state.fan1_label = f"Lüfter 1 ({st.session_state.fan_mode}) - Ein"
        st.session_state.fan1_color = "green"
    else:
        st.session_state.fan1_label = f"Lüfter 1 ({st.session_state.fan_mode}) - Aus"
        st.session_state.fan1_color = "red"

    # Lüfter 2 (Pin 25)
    if st.session_state.relais_states["Lüfter 2"] == "LOW":
        st.session_state.fan2_label = f"Lüfter 2 ({st.session_state.fan_mode}) - Ein"
        st.session_state.fan2_color = "green"
    else:
        st.session_state.fan2_label = f"Lüfter 2 ({st.session_state.fan_mode}) - Aus"
        st.session_state.fan2_color = "red"

    # Für alle Relais-Buttons
    for name in relais_names:
        if st.session_state.relais_states[name] == "LOW":
            st.session_state[f"{name}_color"] = "green"
            st.session_state[f"{name}_label"] = f"{name} - Ein"
        else:
            st.session_state[f"{name}_color"] = "red"
            st.session_state[f"{name}_label"] = f"{name} - Aus"

# Benutzeroberfläche in Streamlit
st.title("Relais Steuerung (Web Version)")

# Anzeige der Buttons für alle Relais
col1, col2, col3 = st.columns(3)

# Relais-Schaltflächen für alle Relais
with col1:
    for i, relais in enumerate(relais_names[:3]):
        st.button(st.session_state[f"{relais}_label"], key=relais, on_click=toggle_relay, args=(relais,))
        st.markdown(
            f"<div style='background-color:{st.session_state[f'{relais}_color']};width:50px;height:50px;border-radius:25px;'></div>",
            unsafe_allow_html=True,
        )

with col2:
    for i, relais in enumerate(relais_names[3:6]):
        st.button(st.session_state[f"{relais}_label"], key=relais, on_click=toggle_relay, args=(relais,))
        st.markdown(
            f"<div style='background-color:{st.session_state[f'{relais}_color']};width:50px;height:50px;border-radius:25px;'></div>",
            unsafe_allow_html=True,
        )

with col3:
    for i, relais in enumerate(relais_names[6:]):
        st.button(st.session_state[f"{relais}_label"], key=relais, on_click=toggle_relay, args=(relais,))
        st.markdown(
            f"<div style='background-color:{st.session_state[f'{relais}_color']};width:50px;height:50px;border-radius:25px;'></div>",
            unsafe_allow_html=True,
        )
