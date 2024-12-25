import streamlit as st

st.title("Halaman Dashboard")
st.image("1.jpg", caption="Treasure")

# fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(t["jumlah"]
                       for t in st.session_state ["total_semua"]
                       if t ["Tipe"] == "Menabung")  #st,session_state untuk menyimpan data sementara
    total_penarikan = sum(t["jumlah"]
                       for t in st.session_state ["total_semua"]
                       if t ["Tipe"] == "Penarikan")  #st,session_state untuk menyimpan data sementara
    saldo = total_nabung - total_penarikan

    return total_nabung, total_penarikan, saldo

total_semua = st.session_state["total_semua"]
total_nabung, total_penarikan, saldo = total()

st.metric("Total Tabungan", f"Rp. {total_nabung}")
st.metric("Total Penarikan", f"Rp. {total_penarikan}")
st.metric("Sisa Saldo", f"Rp. {saldo}")
