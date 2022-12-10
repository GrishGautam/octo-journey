from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'name' : 'grish',
        'age' : 23,
        'nationality' : "Nepali"
    }
    return render(request,"index.html")

from django.shortcuts import render


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



