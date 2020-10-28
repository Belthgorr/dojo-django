from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class decToRoma(APIView):

    def get(serlf, request,number, format=None):
     
        numeros = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerales = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        entero = number
        numeral =''
        i=0

        while entero >0:
            for _ in range(entero // numeros[i]):
                numeral+= numerales[i]
                entero -= numeros[i]

            i +=1
        return Response({numeral})


