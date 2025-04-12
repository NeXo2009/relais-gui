import streamlit as st

# "GPIO"-Simulation
if "gpio" not in st.session_state:
    st.session_state.gpio = {
        22: "HIGH",
        27: "HIGH",
        5: "HIGH",
        6: "HIGH",
        26: "HIGH",
        25: "HIGH"
    }
    st.session_state.fan_state = "Auto"

relais_names = {
    22: "ECU Mainswitch",
    27: "Zündung",
    5: "Haldex",
    6: "Servolenkung",
    26: "Lüfter",
    25: "Licht"
}

st.title("Relais Steuerung (Simulation)")

for pin in st.session_state.gpio.keys():
    col1, col2 = st.columns([3, 1])

    with col1:
        if pin == 26:
            label = f"{relais_names[pin]} ({st.session_state.fan_state})"
        else:
            label = f"{relais_names[pin]}"

        state = st.session_state.gpio[pin]
        color = "green" if state == "LOW" else "red"
        if st.button(f"{label} - {'Ein' if state == 'LOW' else 'Aus'}", key=pin):
            if pin == 26:
                st.session_state.fan_state = "Manuell" if st.session_state.fan_state == "Auto" else "Auto"
            st.session_state.gpio[pin] = "HIGH" if state == "LOW" else "LOW"

    with col2:
        st.markdown(
            f"<div style='background-color:{color};width:50px;height:50px;border-radius:25px;'></div>",
            unsafe_allow_html=True
        )
