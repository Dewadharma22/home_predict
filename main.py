import streamlit as st

st.set_page_config(
    page_title="Streamlit App",
    page_icon=":guardsman:",  # You can use an emoji or a path to an image
    layout="wide",  # 'centered' or 'wide'
    initial_sidebar_state="expanded",  # 'auto', 'expanded', or 'collapsed'
)
st.title("Welcome to My Streamlit App")
st.write("This is a simple Streamlit application with a custom page configuration.")
# Add more content to the app
st.sidebar.header("Navigasi")
page = st.sidebar.radio(
    "Select a page",
    [ "About", "Contact", "Machine Learning", "Visualisasi" ]
)
st.write(f"You selected: {page}")

if page == "About":
    import about
    about.tampilkan_tentang_saya()
elif page == "Contact":
    import contact
    contact.tampilkan_kontak()
elif page == "Machine Learning":
    import model
    model.tampilkan_model()
else:
    import viz
    viz.tampilkan_visualisasi()