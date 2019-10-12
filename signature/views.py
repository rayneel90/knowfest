from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.views import View
from django.shortcuts import redirect, render, HttpResponse
from .serializer import SignInputSerializer
from .models import SignInput, SignOutput
from .tasks import check_cust, SignatureCheck
from glob import glob
class SignAPIView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = SignInputSerializer
    def post(self, requests):
        serializer = SignInputSerializer(data=requests.data)
        if serializer.is_valid():
            input = serializer.save()
            status = check_cust(input.cust_id)
            if status == "Success":
                checker = SignatureCheck(input.cust_id)
                score, decision = checker.verify_sig(.9, input.image.path)
            else:
                score, decision = None, None
            resp = SignOutput(input=input, status=status, authentic=decision,
                                    score=score)
            resp.save()
            return redirect('sign:output', model=resp.id)
        else:
            return Response(serializer.errors)


class SignOutputView(View):
    def get(self, request, model):
        sign_output = SignOutput.objects.get(id=model)
        sign_input = sign_output.input
        samples = list(enumerate(glob('media/sample/{}/*'.format(sign_input.cust_id))))
        samples = [samples[i:i+4] for i in range(0, len(samples), 4)]
        return render(request, 'sign_output.html', {'input': sign_input, 'output': sign_output, 'samples': samples})
        # sign_input = SignInput.objects,get(id)