import streamlit as st

st.title("Halaman Penarikan")

# Formulir
with st.form("Penarikan"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0, step=1000)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    submit_botton = st.form_submit_button(label="Penarikan")

    if submit_botton and jumlah >= 50000 :
        st.session_state["total_semua"].append({
            "Tipe" : "Penarikan",
            "jumlah" : jumlah
        })
        st.success("Penarikan Uang Berhasil")
    else:
        st.error("Penarikan Gagal")