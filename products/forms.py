from django import forms
from .models import User,ProductModel,Account


# class Contact_us(forms.ModelForm):
#
#     def clean_phone(self):
#         phone = self.cleaned_data["phone"]
#         if phone:
#             if not phone.isnumeric():
#                 raise forms.ValidationError("شماره تلفن ، عددی نیست")
#             else:
#                 return phone
#
#
#     class Meta:
#         model = CommentModel
#         fields = ["message", "email", "phone"]
class Contact_us(forms.Form):

    body = forms.CharField(widget=forms.Textarea, required=True)
    name= forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True)
    def clean_name(self):
        name = self.cleaned_data["name"]
        if name:
            if  name.isnumeric():
                raise forms.ValidationError("شماره تلفن ، عددی نیست")
            else:
                return name
# class CommentForm(forms.ModelForm):
#     def clean_name(self):
#         name = self.cleaned_data["name"]
#         if name:
#             if len(name) < 3:
#                 raise forms.ValidationError("نام کوتاه است")
#             else:
#                 return name
#
#     class Meta:
#         model = CommentModel
#         fields = ["title","name", "message_positive_points","message_negative_points","message_text"]
#
class CommentForm(forms.Form):
    title=forms.CharField(max_length=250, required=True)
    # name=forms.CharField(max_length=250, required=True)
    message_positive_points=forms.CharField(max_length=250, required=True)
    message_negative_points=forms.CharField(max_length=250, required=True)
    message_text=forms.CharField(max_length=250, required=True)

    # def clean_name(self):
    #     name = self.cleaned_data["name"]
    #     if name:
    #         if len(name) < 3:
    #             raise forms.ValidationError("نام کوتاه است")
    #         else:
    #             return name





class SearchProduct(forms.Form):
    query = forms.CharField()

#
class CreateProductsForm(forms.ModelForm):
    image1=forms.ImageField(label="تصویر اول")
    image2=forms.ImageField(label="تصویر دوم")
    class Meta:
        model=ProductModel
        fields=["title","description"]



class LoginForm(forms.Form):
    username=forms.CharField(max_length=50 , required=True)
    password=forms.CharField(max_length=50 , required=True ,widget=forms.PasswordInput )




class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(max_length=120 , widget=forms.PasswordInput , label="password")
    password2=forms.CharField(max_length=120 , widget=forms.PasswordInput , label="repeat password")
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
    def clean_password2(self):
        cd=self.cleaned_data
        if cd["password"] != cd["password2"] :
            raise forms.ValidationError("مشابهه نیستند")
        return cd["password2"]

class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
class EditAccountForm(forms.ModelForm):
    class Meta:
        model=  Account
        fields=["user","date_of_birth","bio","job","photo"]