import streamlit as st
import pickle as pkl
st.title("Analyze Maks")
st.header("Here we analyze the mark.")
st.write("We indicates here")

with open("model.pkl","rb") as f:
    model=pkl.load(f)
    
hr=st.number_input("ENter number:")
btn=st.button("Click here")

pre=str(model.predict([[hr]])[0])

if btn:
    if hr:
        if 0<hr<10:
            
            st.success(f"You get your marks {pre[:5]}")
            pre=int(pre)
            if pre>33:
                st.success("Pass")
            else:
                st.success("fail")
        else:
            if hr<0:
                st.error("Hr can neven be negative.")
            else:
                st.success(f"You get your marks 100")
    else:
        st.error("Please enter the number first")

