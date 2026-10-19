from django.shortcuts import render

# Create your views here.

import os
import joblib
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

model_path = os.path.join(settings.BASE_DIR, 'salary_model.pkl')
model = joblib.load(model_path)

class PredictAPI(APIView):
    def post(self, request):
        exp = float(request.data.get('experience'))
        score = float(request.data.get('test_score'))
        prediction = model.predict([[exp, score]])[0]
        return Response({"predicted_salary": round(float(prediction), 2)})
