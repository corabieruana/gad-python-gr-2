from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)  #daca metoda e POST se creaza un form pt inregistrare cream cu acele informatii post
		if form.is_valid():
			form.save()    	#IMPORTANT! se salveaza utilizatorul in bd (in django admin)
			username = form.cleaned_data.get('username')  #the validated form data will be in cleaned_data dictionary
			messages.success(request, f'Contul a fost creat pentr {username}! Acum te poti loga!')
			return redirect('login')
	else:
		form = UserRegisterForm()   #empty form

	return render(request, 'users_app/register.html', {'form':form})


@login_required   #se numeste decorator si functia urmatoare se executa doar daca utilizatorul este logat
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)  #instance=request.user ca sa completeze by default fieldul de user cu numele utilziatorului curent
		p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Informatiile contului au fost actualizate!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user) 
		p_form= ProfileUpdateForm(instance=request.user.profile)


	context={            #dictionar cheie:valoare      cheile vor fi variabilele ce vor fi accesate din template
		'u_form': u_form,  
		'p_form':p_form
	}
	return render(request, 'users_app/profile.html',context)