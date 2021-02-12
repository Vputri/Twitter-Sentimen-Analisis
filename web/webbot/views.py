from django.shortcuts import render
import joblib

def index(request):
    return render(request, 'webbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')
    filename = '/home/vika/sentimen analisis/web/webbot/pipeline.sav'
    loaded_model = joblib.load(filename)
    pred = loaded_model.predict([query])
    if (pred == [1]) :
        ans = 'negatif'
    elif (pred == [2]):
        ans = 'positif'
    else:
        ans = 'Nothing'

    return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
