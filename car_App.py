import streamlit as st
import pickle
model=pickle.load(open('Car_pred.pkl','rb'))

def main():
    string="Car Price Predictor"
    st.set_page_config(page_title=string,page_icon=" ")
    st.title("Car Price Predictor")
    st.markdown("### Are you planning to sell your car !?\n#### so let's try evaluating the price")
    st.image(
        "https://imgd.aeplcdn.com/0x0/n/cw/ec/112947/wagon-r-2022-exterior-right-front-three-quarter-3.jpeg?isig=0",
        width=800,
    )
    st.write('')
    st.write('')
    years=st.number_input('In which year car was purchased?',1990,2021,step=1,key='year')
    years_old=2022-years
    present_price=st.number_input('What is the price of the car at the time of purchase? (In ₹lakhs)',0.0, 50.0, step=0.5,key='present_price')
    Kms_driven=st.number_input('What is the distance completed by car in kilometers?',0.0,5000000.0,step=500.0,key='Kms_driven')
    owner=st.radio("The number of owners the car had previously?",(0,1,2,3),key='owner')

    fuel_type_petrol=st.selectbox('What is the fuel type of the car?',('Petrol','Diesel','CNG'),key='fuel')
    if(fuel_type_petrol=='Petrol'):
        fuel_type_petrol=1
        fuel_type_Diesel=0
    elif(fuel_type_petrol=='Diesel'):
        fuel_type_petrol=0
        fuel_type_Diesel=1
    else:
        fuel_type_petrol=0
        fuel_type_petrol=0
    
    seller_type_individual=st.selectbox('Are you a dealer or an individual?',('Dealer','Individual'),key='dealer')
    if(seller_type_individual=='Individual'):
        seller_type_individual=1
    else:
        seller_type_individual=0

    Transmission_manual=st.selectbox('What is the transmission type?',('Manual','Automatic'),key='manual')
    if(Transmission_manual=='Manual'):
        Transmission_manual=1
    else:
        Transmission_manual=0
    
    if st.button("Estimate Price",key='predict'):
        try:
            Model=model
            prediction=Model.predict([[present_price, Kms_driven, owner, years_old,fuel_type_Diesel,fuel_type_petrol,seller_type_individual,Transmission_manual]])
            output=round(prediction[0],2)
            if output<0:
                st.warning("You will not be able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs".format(output))
        except:
                st.warning("Oops!! something went wrong\n Try again")

    

if __name__ == '__main__':
    main()
