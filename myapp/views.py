from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.

def index(request):
	feature1 = Feature()
	feature1.id = 0
	feature1.name = "Fast"
	feature1.details = "our service is very quick"

	feature2 = Feature()
	feature2.id = 1
	feature2.name = "Easy to use and"
	feature2.details = "our service is very Easy to use"

	feature3 = Feature()
	feature3.id = 2
	feature3.name = "Reliable"
	feature3.details = "our service is Reliable"

	feature4 = Feature()
	feature4.id = 3
	feature4.name = "Affordable"
	feature4.details = "our service is very affordable"
	feature = [feature2,feature1,feature3,feature4]

	return render(request,"index.html", {'feature' : feature,})


# defining function for wordcounter
def counter(request):
	# checking if method is POST or not
	if request.method == 'POST':

		# taking text input
		text = request.POST['text']

		# checking weather text is empty
		# or not
		if text != '':

			# splitting the text and taking length
			# of that
			amount_of_word = len(text.split())

			# returning HTML page with data, if calculated
			# successfully
			return render(request, 'counter.html',
						{'amount': amount_of_word})

		else:
			# returning HTML page without data, if any
			# error occurs
			return render(request, 'counter.html', {'on': 'active'})

	else:
		# returning HTML page if request.method is not POST
		return render(request, 'counter.html', {'on': 'active'})



