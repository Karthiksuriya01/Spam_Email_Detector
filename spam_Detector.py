import streamlit as st 
import pickle

model = pickle.load(open('spam123.pkl', 'rb'))
cv = pickle.load(open('vec.pkl','rb'))



def main():
        st.title("Email Spam Classification Application")
        st.write("This is a Machine Learning application to class")
        st.subheader("classification")
        user_input = st.text_area("Email an eamail to classify", height=1)
        if st.button("Classify"):
                if user_input:
                        data = [user_input]
                        print(data)
                        vec = cv.transform(data).toarray()
                        result = model.predict(vec)
                        if result[0] == 0:
                                st.success("This is Not a spam email")
                        else:
                                st.error("This is a spam email")
                else:
                        st.write("Please Enter an email to classify")  
main()