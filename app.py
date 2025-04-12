import streamlit as st

# Initialisierungen
if "fan_mode" not in st.session_state:
    st.session_state.fan_mode = "Auto"
    st.session_state.relais_states = {
        "Lüfter 50%": "HIGH",  # Lüfter 50% (aus)
        "Lüfter 100%": "HIGH",  # Lüfter 100% (aus)
        "ECU Mainswitch": "HIGH",
        "Zündung": "HIGH",
        "Haldex": "HIGH",
        "Servolenkung": "HIGH",
        "Lüfter": "HIGH"
    }

    # Initialisieren der Labels für jedes Relais
    for relais in ["ECU Mainswitch", "Zündung", "Haldex", "Servolenkung", "Lüfter 50%", "Lüfter 100%", "Lüfter"]:
        st.session_state[f"{relais}_label"] = f"{relais} - Auto"
        st.session_state[f"{relais}_color"] = "red"

# Funktionslogik, um Relais zu schalten
def toggle_relay(relay_name):
    # Wenn beide Lüfter aus sind, gehe zurück zu Auto-Modus
    if st.session_state.relais_states["Lüfter 50%"] == "HIGH" and st.session_state.relais_states["Lüfter 100%"] == "HIGH":
        st.session_state.fan_mode = "Auto"
    
    # Wenn der Modus Auto ist, wechsle auf Manuell
    if st.session_state.fan_mode == "Auto":
        st.session_state.fan_mode = "Manuell"

    # Wechsel Relais-Zustand für Lüfter 50% oder Lüfter 100%
    if relay_name == "Lüfter 50%":
        st.session_state.relais_states["Lüfter 50%"] = "LOW" if st.session_state.relais_states["Lüfter 50%"] == "HIGH" else "HIGH"
        # Wenn Lüfter 50% eingeschaltet wird, Lüfter 100% ebenfalls auf Manuell setzen
        if st.session_state.relais_states["Lüfter 50%"] == "LOW":
            st.session_state.relais_states["Lüfter 100%"] = "LOW"
    elif relay_name == "Lüfter 100%":
        st.session_state.relais_states["Lüfter 100%"] = "LOW" if st.session_state.relais_states["Lüfter 100%"] == "HIGH" else "HIGH"
        # Wenn Lüfter 100% eingeschaltet wird, Lüfter 50% ebenfalls auf Manuell setzen
        if st.session_state.relais_states["Lüfter 100%"] == "LOW":
            st.session_state.relais_states["Lüfter 50%"] = "LOW"
    else:
        st.session_state.relais_states[relay_name] = "LOW" if st.session_state.relais_states[relay_name] == "HIGH" else "HIGH"

    update_button_state()

def update_button_state():
    # Lüfter 50% (Pin 26)
    if st.session_state.relais_states["Lüfter 50%"] == "LOW":
        st.session_state.fan1_label = f"Lüfter 50% (Manuell) - Ein"
        st.session_state.fan1_color = "green"
    else:
        st.session_state.fan1_label = f"Lüfter 50% (Auto) - Aus"
        st.session_state.fan1_color = "red"

    # Lüfter 100% (Pin 25)
    if st.session_state.relais_states["Lüfter 100%"] == "LOW":
        st.session_state.fan2_label = f"Lüfter 100% (Manuell) - Ein"
        st.session_state.fan2_color = "green"
    else:
        st.session_state.fan2_label = f"Lüfter 100% (Auto) - Aus"
        st.session_state.fan2_color = "red"

    # Für alle Relais-Buttons
    for name in ["ECU Mainswitch", "Zündung", "Haldex", "Servolenkung", "Lüfter"]:
        if st.session_state.relais_states[name] == "LOW":
            st.session_state[f"{name}_color"] = "green"
            st.session_state[f"{name}_label"] = f"{name} - Ein"
        else:
            st.session_state[f"{name}_color"] = "red"
            st.session_state[f"{name}_label"] = f"{name} - Aus"

# Benutzeroberfläche in Streamlit
st.title("Relais Steuerung (Web Version)")

# Anzeige der Buttons für alle Relais
col1, col2 = st.columns(2)

# Relais-Schaltflächen für alle Relais
with col1:
    for i, relais in enumerate(["ECU Mainswitch", "Zündung", "Haldex"]):
        st.button(st.session_state[f"{relais}_label"], key=relais, on_click=toggle_relay, args=(relais,))
        st.markdown(
            f"<div style='background-color:{st.session_state[f'{relais}_color']};width:50px;height:50px;border-radius:25px;'></div>",
            unsafe_allow_html=True,
        )

with col2:
    # Lüfter 50% und Lüfter 100% Buttons
    st.button(st.session_state["Lüfter 50%_label"], key="Lüfter 50%", on_click=toggle_relay, args=("Lüfter 50%",))
    st.markdown(
        f"<div style='background-color:{st.session_state['Lüfter 50%_color']};width:50px;height:50px;border-radius:25px;'></div>",
        unsafe_allow_html=True,
    )

    st.button(st.session_state["Lüfter 100%_label"], key="Lüfter 100%", on_click=toggle_relay, args=("Lüfter 100%",))
    st.markdown(
        f"<div style='background-color:{st.session_state['Lüfter 100%_color']};width:50px;height:50px;border-radius:25px;'></div>",
        unsafe_allow_html=True,
    )
