import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Product Quality Analysis")
st.write("Upload the dataset")
upload=st.file_uploader(label="upload the file")
df=pd.read_csv(upload)
df
if st.checkbox("Click here to see the report"):
    
    phase1=df[df.mcu_phase==1]
    phase2=df[df.mcu_phase==2]
    phase3=df[df.mcu_phase==3]


    st.title("Production budget of phase1 film")

    fig = plt.figure(figsize = (20, 12))
    plt.bar(phase1.movie_title,phase1.production_budget)
    st.pyplot(fig)
    st.title("Worldwide box office of phase1 film")
    fig2=plt.figure(figsize=(20,12))
    plt.bar(phase1.movie_title,phase1.worldwide_box_office)
    st.pyplot(fig2)

    st.title("Production budget of phase2 film")
    fig3 = plt.figure(figsize = (20, 12))
    plt.bar(phase2.movie_title,phase2.production_budget)
    st.pyplot(fig3)
    st.title("Worldwide box office of phase2 film")
    fig4=plt.figure(figsize=(20,12))
    plt.bar(phase2.movie_title,phase2.worldwide_box_office)
    st.pyplot(fig4)

    st.title("Production budget of phase3 film")
    fig5 = plt.figure(figsize = (20, 12))
    plt.bar(phase3.movie_title,phase3.production_budget)
    st.pyplot(fig5)
    st.title("Worldwide box office of phase3 film")
    fig6=plt.figure(figsize=(20,12))
    plt.bar(phase3.movie_title,phase3.worldwide_box_office)
    st.pyplot(fig6)
    st.title("Audience_Score for phase1")

    fig7=plt.figure(figsize=(20,12))
    plt.pie(phase1.audience_score,labels=phase1.movie_title)
    st.pyplot(fig7)

    st.title("Audience_Score for phase2")
    fig8=plt.figure(figsize=(20,12))
    plt.pie(phase2.audience_score,labels=phase2.movie_title)
    st.pyplot(fig8)

    st.title("Audience_Score for phase3")
    fig9=plt.figure(figsize=(20,12))
    plt.pie(phase3.audience_score,labels=phase3.movie_title)
    st.pyplot(fig9)
    st.title("Raw data report")
    st.title("Highest box office product of marvel")    

    highest=df.iloc[:,[0,6,9]] 

    high=highest.sort_values(by=["worldwide_box_office"],ascending=False)
    high
    st.title("Highest opening product of marvel")
    opend=df.iloc[:,[0,7,9]] 

    opens=opend.sort_values(by=["opening_weekend"],ascending=False)
    opens

    st.title("best review product of marvel")
    pro=df.iloc[:,[0,4,9]] 

    product=pro.sort_values(by=["audience_score"],ascending=False)
    product
    st.title("Biggest_opening of phase1")
    fig10=plt.figure(figsize=(10,5))
    plt.bar(phase1.movie_title,phase1.opening_weekend)
    st.pyplot(fig10)
    st.title("Biggest_opening of phase2")
    fig11=plt.figure(figsize=(20,12))
    plt.bar(phase2.movie_title,phase2.opening_weekend)
    st.pyplot(fig11)
    st.title("Biggest_opening of phase3")
    fig11=plt.figure(figsize=(20,12))
    plt.bar(phase3.movie_title,phase3.opening_weekend)
    st.pyplot(fig11)






