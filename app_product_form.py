import streamlit as st 

st.title("Product Form")

st.sidebar.header("Add New Product")


product_name=st.sidebar.text_input("Enter Product Name")

category=st.sidebar.selectbox("category",["Electronics","Clothing","Groceries","Books","Accessories"])

price=st.sidebar.number_input("Enter Price: ",0, 500, 250)

if st.sidebar.button("Add Product"):
    
    if product_name.strip()=="":
        st.error("Please add the details")
        
    else:
        st.success("Prodcut Added Successfully")
        
        st.subheader("Product details")
        
        st.write(f"Product name:{product_name}")
        st.write(f"category:{category}")
        st.write(f"price:{price}")
        