import streamlit as st
import numpy as np
import pandas as pd
from prediction import predict_15Z_offshore

def main():

  st.title('Cape Canaveral Severe Weather Probability Tool')
  st.markdown('This is to be used on summer days with OFFSHORE FLOW')
  

  st.header('Sounding Parameters from 15Z')
  col1, col2 = st.columns(2)
  with col1:
    Thompson_Index = st.number_input('Thompson Index (KI - LI)', -30.0, 60.0, step = 0.1, format= "%.1f")
    RH = st.number_input('700-500mb Average RH', 0, 100, step=1)
    PWAT = st.number_input('PWAT (inches)', 0.00, 5.00, step = 0.01, format = "%.01f")
    Thompson_Index = st.number_input('WINDEX', 0.0, 100.0, step = 0.1, format= "%.1f")
    Wet_Bulb_Zero = RH = st.number_input('Wet Bulb Zero Level (ft)', 0, 30000, step=1)
  with col2:
    #wind_average = st.slider('1000-700mb Average U-Wind Component', -40.0, 40.0, 0.5)
    wind_direction_1000_850 = st.number_input('1000-850mb Average Wind Direction', 0, 360, step = 1)
    wind_speed_1000_850 = st.number_input('1000-850mb Average Wind Speed in kts', 0.0, 100.0, step= 0.1, format= "%.1f")
    wind_direction_850_500 = st.number_input('850-500mb Average Wind Direction', 0, 360, step = 1)
    wind_speed_850_500 = st.number_input('850-500mb Average Wind Speed in kts', 0.0, 100.0, step= 0.1, format= "%.1f")
    
  if st.button('Probability of Severe Weather Today'):
    #result = predict(np.array([[Thompson_Index, wind_average]]))

    u_wind_average_1000_850 = wind_speed_1000_850 * np.cos(np.deg2rad(270-wind_direction_1000_850))
    v_wind_average_1000_850 = wind_speed_1000_850 * np.sin(np.deg2rad(270-wind_direction_1000_850))
    u_wind_average_850_500 = wind_speed_850_500 * np.cos(np.deg2rad(270-wind_direction_850_500))

    #result = predict(np.array([[Thompson_Index, wind_average, RH]]))
    #result_limited = predict_limited(np.array([[Thompson_Index, wind_average, RH]]))
    #result_str = str(int(result[0])) + '%'
    #st.header('Version 1.0')
    #st.header(str(int(result[0])) + '%')
    result_15Z_offshore = predict_15Z_offshore(np.array([[Thompson_Index, RH, PWAT, WINDEX, u_wind_average_1000_850, v_wind_average_1000_850, u_wind_average_850_500, Wet_Bulb_Zero]]))  
    st.header('Severe Weather Probability: ')
    st.header(str(int(result_15Z_offshore[0])) + '%')


if __name__=='__main__': 
    main()
  



