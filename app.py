import streamlit as st
import pickle
import numpy as np

company_mapping = {
    "Acer": 0,
    "Apple": 1,
    "Asus": 2,
    "Chuwi": 3,
    "Dell": 4,
    "Fujitsu": 5,
    "Google": 6,
    "HP": 7,
    "Huawei": 8,
    "LG": 9,
    "Lenovo": 10,
    "MSI": 11,
    "Mediacom": 12,
    "Microsoft": 13,
    "Razer": 14,
    "Samsung": 15,
    "Toshiba": 16,
    "Vero": 17,
    "Xiaomi": 18
}

TypeName_mapping = {
    "Convertible": 0,
    "Gaming": 1,
    "Netbook": 2,
    "Notebook": 3,
    "Ultrabook": 4,
    "Workstation": 5
}

cpu_mapping = {
    "AMD Processor": 0,
    "Intel Core i3": 1,
    "Intel Core i5": 2,
    "Intel Core i7": 3,
    "Other Intel Processor": 4
}

Gpu_mapping = {
    "AMD": 0,
    "Intel": 1,
    "Nvidia": 2
}

os_mapping = {
    "Mac": 0,
    "Others/No OS/Linux": 1,
    "Windows": 2
}

with open("laptop.pkl", 'rb') as f:
    model = pickle.load(f)


def predict(company, laptop_type, ram, weight, touchscreen, ips, cpu, hdd, ssd, gpu, os):
    selected_company = company_mapping[company]
    selected_TypeName = TypeName_mapping[laptop_type]
    selected_cpu = cpu_mapping[cpu]
    selected_gpu = Gpu_mapping[gpu]
    selected_os = os_mapping[os]
    input_data = np.array(
        [[selected_company, selected_TypeName, int(ram), int(weight), int(touchscreen), int(ips), selected_cpu,
          int(hdd), int(ssd), selected_gpu, selected_os]])

    price =model.predict(input_data)[0]
    return price


if __name__ == "__main__":
    st.header("Laptop Price Prediction")
    col1, col2 = st.columns([2, 1])
    company = col1.selectbox("Select a Brand", list(company_mapping.keys()))

    # type of laptop
    laptop_type = col1.selectbox("Select a Type of Laptop", list(TypeName_mapping.keys()))

    # Ram
    ram_options = [2, 4, 8, 16, 32, 64]
    ram = col1.slider("RAM(in GB)", min_value=min(ram_options), max_value=max(ram_options), step=2, value=4)

    # weight
    weight = col1.number_input('Weight of the Laptop',
                               max_value=2.0,
                               min_value=1.0,
                               value=1.0,
                               step=0.1)

    # Touchscreen
    touchscreen = col1.selectbox('Touchscreen', ['No', 'Yes'])

    # IPS
    ips = col1.selectbox('IPS', ['No', 'Yes'])

    # cpu
    cpu = col1.selectbox("Select a CPU", list(cpu_mapping.keys()))

    hdd = col1.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

    ssd = col1.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

    gpu = col1.selectbox("Select a GPU", list(Gpu_mapping.keys()))

    os = col1.selectbox("Select a OS", list(os_mapping.keys()))

    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    result = predict(company, laptop_type, ram, weight, touchscreen, ips, cpu, hdd, ssd, gpu, os)
    submit_button = st.button("Submit")

    if submit_button:
        larger_text = f"<h2 style='color: red;'>The Predicted Laptop Price is : {result} rupees</h2>"
        st.markdown(larger_text, unsafe_allow_html=True)