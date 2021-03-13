from django.shortcuts import render
import joblib

def index(request):
    return render(request, 'webbot/index.htm')

def bot_search(request):
    query = request.GET.get('query')
    filename = '/home/vika/sentimen analisis/results/vektor.sav'
    filename1 = '/home/vika/sentimen analisis/results/MNB3.sav'
    vektor = joblib.load(filename)
    model = joblib.load(filename1)
    result = model.predict(vektor.transform([query]))
    if (result == [2]) :
        ans = "negatif"
    elif (result == [1]) :
        ans = "positif"
    else:
        ans = 'Nothing'

    return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
