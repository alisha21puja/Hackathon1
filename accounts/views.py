
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from django.urls import path, include
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Article,UserProfile

from django.contrib import messages
from django.views.generic import TemplateView
from .forms import ArticleForm



class AccountInfo(TemplateView):
	template_name = 'dashboard.html'
	def get(self,request):
		form = AccountForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = AccountForm(request.POST)
		if form.is_valid():
			text= form.cleaned_data['userType']
			form = AccountForm()

			return redirect('dashboard')
		args = {'form':form,'text':text }
		return render(request,'dashboard.html',{'form':form})
			

def indx(request):
	return  render(request,'login.html')


def dashboard(request):
	return  render(request,'dashboard.html')


def loginn(request):
	if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['password']
			user = auth.authenticate(username=email,password=password)
			# print(user)
			
			# print(key) #33
			if user is not None:
				key = user._get_pk_val()
				user_1 = list(UserProfile.objects.values_list('type_usr','id').filter(id=key).values('type_usr'))
				user_type = user_1[0]
				var=user_type['type_usr']

				if user_type['type_usr'] == 100 :
					auth.login(request,user)
					request.session['userid']=key
					return redirect('participantIndex')
					# return redirect('participantIndex')
				elif user_type['type_usr'] == 200 :
					auth.login(request,user)
					request.session['userid']=key
					return redirect('sponsorIndex')
				elif user_type['type_usr'] == 300 :
					auth.login(request,user)
					request.session['userid']=key
					return redirect('organiserIndex')
				else:
					messages.error(request,'invalid user type dectected contact admin')
					return render(request,'login.html',{'error':'invalid user type dectected contact admin'})

					# return redirect('login')
			else:
				# messages.error(request,'invalid credentials')
				return render(request,'login.html',{'error':'Invalid credentials'})
	else:
		return render(request,'login.html')


	"""
	if request.method=='POST':
		username = request.POST['email']
		password = request.POST['password']








		

		if username =='kapil.thakur9614@gmail.com' and password =='sachin123':
			user = auth.authenticate(username =username,password=password)
			if user is not None:
				auth.login(request,user)
				messages.success(request,'You are now loged in')
				return redirect('organiserIndex')
			else:
				auth.login(request,user)
				messages.success(request,'Credendtial are Wrong')
				return  render(request,'login.html')
				#messages.error(request,'invalidiuoiuuoi credential')
				#return  render(request,'login.html')
		elif username =='alwin.joseph@mca.christuniversity.in' and password =='sachin123':
			user = auth.authenticate(username =username,password=password)
			if user is not None:
				auth.login(request,user)
				messages.success(request,'You are now loged in')
				return redirect('participantIndex')
			else:
				messages.error(request,'invalid credential')
				return  render(request,'login.html')

		elif username =='alisha.singh@mca.christuniversity.in' and password =='sachin123':
			user = auth.authenticate(username =username,password=password)
			if user is not None:
				auth.login(request,user)
				messages.success(request,'You are now loged in')
				return redirect('sponsorIndex')
			else:
				messages.error(request,'invalid credential')
				return  render(request,'login.html')
		else:
				messages.error(request,'inhiuyvalid credential')
				return  render(request,'login.html')
	"""	



def logout(request):

	if request.method=='POST':
		auth.logout(request)
		messages.success(request,' You are now loged out')

		return redirect('home') 



def UserSelection(request,id):
	if request.method=='POST':

		reg= User.objects.get(id=id)
		pro=Profile()
		pro.userType = request.POST['useru']
		#reg.save(reg.userType)
		pro.user_id= reg   
		#pro.create(reg,userType=userType)
		#reg.update(reg.userType)
		pro.create(pro.userType,pro.user_id)
		pro.save()
		return  render(request,'base.html')
	else:
		return  render(request,'login.html')



	




def usertype(request,pk):
	lo=get_object_or_404(User, pk=pk)
	return  render(request,'usertype.html',{'lo':lo})


def helo(request):
	if request.method=='POST':
		user=User.object.get(email=signup.email)
		reg= Registration()
		reg.userType = request.POST['useru']
		reg.save()
		reg = User.objects.update(reg.userType)
		return  render(request,'base.html')
	else:
		return  render(request,'login.html')

		
def signup(request):
	if request.method=='POST':
		
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['confirmpassword']
		phone  = request.POST['phone']
		type_usr = request.POST['type_usr']

		#mobile  = request.POST['mobile']
		#userType = request.POST['usertype']

		if password == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request,"That username is taken")
				return  render(request,'login.html',{'errorr':'Username is already taken'})


				# return redirect('accounts')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request,"That email is been use")
					return  render(request,'login.html',{'errorr':'Email is in use '+email})


					return redirect('accounts')

				else:
					user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
					#auth.login(request,user)
					#messages.success(request,'You are now Loged in')
					user.save()
					key = user._get_pk_val()
					var = UserProfile(id=key,type_usr = type_usr,phone=phone)
					var.save()
					messages.success(request,'You are now registered in')
					return redirect('accounts')



		elif first_name=='':
			
			messages.error(request,'FirstName  field  is empty')

		elif last_name=='':
			messages.error(request,'Last Name field  is empty')

		elif username=='':
			messages.error(request,'Username field  is empty')


		elif email=='':
			messages.error(request,'Email field   is empty')


		elif password=='':
			messages.error(request,'Password is empty')

		elif password2=='':
			messages.error(request,'Confirm password field is empty')


		else:
			messages.error(request,'Password do not match')
			return redirect('accounts')


		
		

	else:
		return render(request,'base.html')



def logoutt(request):
	if request.method=='POST':

		try:
			user=User.objects.get(email=request.POST['email'])
			return render(request,'login.html',{'error':"User Name already registered  please Login!!"})

		except User.DoesNotExist:
			
			signup.firstName =request.POST['firstname']
			signup.firstName = request.POST['firstname']
			signup.lastName = request.POST['lastname']
			signup.email = request.POST['email']
			signup.password = request.POST['password']
			signup.confirmPassword = request.POST['confirmpassword']
			signup.mobile = request.POST['mobile']
			signup.userType =='Default'





			if signup.firstName=='':
				return render(request,'login.html', {'error':"Please Enter your First Name!"})
			elif signup.lastName =='' :
				return render(request,'login.html', {'error':"Please Enter your Last Name!"})
			elif signup.email=='':
				return render(request,'login.html', {'error':"Please Enter your Email Name!"})
			elif signup.password=='':
				return render(request,'login.html', {'error':"Please Enter your Password!"})
			elif signup.confirmPassword!=signup.password:
				return render(request,'login.html', {'error':"Your Password and confirmpassword are not correct!"})			
			elif signup.confirmPassword=='':
				return render(request,'login.html', {'error':"Please Enter your confirmpassword !"})
			elif signup.mobile=='':
				return render(request,'login.html', {'error':"Please Enter your mobile number !"})
			elif signup.userType=='':
				signup.userType='Default'
				signup.save()
			else:
				signup.userType =='Default'
				signup.save()




			 







			






			user = User.objects.create_user( signup.firstName,signup.password,usesignup.userType)

			return redirect('usertpe',pk=signup.id)

	render(request,'base.html')


def login(request):
	render(request,'base.html')
	