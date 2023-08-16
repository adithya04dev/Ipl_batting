# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:43:12 2023

@author: adith
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle
#import sys
#sys.path.append('C:/Users/adith/Documents/ipl_app/streamlit_app')

from batsman import Batsman

with open('batting.pkl', 'rb') as f:
    bat = pickle.load(f)
    #result1=bat.calculate("RA Tripathi",[1,2,3],["Pace"],[2022])
    #print(result1['strike_rate'])

def main():
    # Title of the app
    st.title("IPL: Batter Stats")
    # Input for PlayerName
    player_names = bat.players
    # Input for PlayerName (dropdown)
    player_name = st.selectbox("Select Player Name", player_names)
    phases = st.multiselect("Select Phases ", ["Powerplay", "Middle1","Middle2","Slog"])
    # Input for Bowling type (dropdown)
    bowling_type = st.multiselect("Select Bowling Type(s)", ["Pace", "Spin"])
    # Input for Season (slider)
    start_year = 2016
    end_year = 2023
    selected_years = st.slider("Select Seasons", start_year, end_year, (start_year, end_year))
    ph1={'Powerplay':1,'Middle1':2,'Middle2':3,'Slog':4}
    
    overs=[ph1[phases[i]] for i in range(len(phases))]
    bowling_type=[bowling_type[i] for i in range(len(bowling_type))]
    Season=[i for i in range(selected_years[0],selected_years[1]+1)]
    
    
    # Display the selected inputs
    
    if st.button('Submit'):
        
        
        #st.write("Selected Player Name:", player_name)
        #st.write("Selected Bowling Type:", type(bowling_type[0]))  # Corrected indentation
        #st.write("Selected Phases:", len(phases))          
        #st.write("Selected Seasons:", selected_years[0], "to", selected_years[1])
        result1=bat.calculate(player_name,overs,bowling_type,Season)
        result2=bat.overall()
        st.write("Overall (All phases and bowlingt types ):")
        st.dataframe(result2)
        
        
        st.write("Phase wise breakdown:")
        st.dataframe(result1)
        
    
    
if __name__=='__main__':
    main()
