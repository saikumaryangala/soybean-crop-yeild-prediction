from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
global scaler
def home(request):
    return render(request, 'index.html')

def getPredictions(Year,Loc_Id,W11,W12,W13,W14,W15,P9,P10,P11,S_surface1,S_surface2,S_surface3,S_surface4):
    model = pickle.load(open('DT.pkl', 'rb'))
    prediction = model.predict(np.array([[Year,Loc_Id,W11,W12,W13,W14,W15,P9,P10,P11,S_surface1,S_surface2,S_surface3,S_surface4]]))
    return (prediction[0])

def result(request):
    Year = float(request.GET['Year'])
    Loc_Id = float(request.GET[ 'Loc_Id'])
    W11 = float(request.GET[ 'W11'])
    W12 = float(request.GET[ 'W12'])
    W13 = float(request.GET[ 'W13'])
    W14 = float(request.GET[ 'W14'])
    W15 = float(request.GET[ 'W15'])
    P9 = float(request.GET[ 'P9'])
    P10 = float(request.GET['P10'])
    P11 = float(request.GET[ 'P11'])
    S_surface1 = float(request.GET[ 'S_surface1'])
    S_surface2 = float(request.GET[ 'S_surface2'])
    S_surface3 = float(request.GET[ 'S_surface3'])
    S_surface4 = float(request.GET[ 'S_surface4'])
    

    
    result = getPredictions(Year,Loc_Id,W11,W12,W13,W14,W15,P9,P10,P11,S_surface1,S_surface2,S_surface3,S_surface4)
    return render(request, 'result.html', {'result': result})