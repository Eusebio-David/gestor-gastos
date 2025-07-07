from django import forms 

class ContactoForm(forms.Form):

   

    nombre = forms.CharField(label='nombre', required=True, widget=forms.TextInput(attrs={
        'class':"block w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget transition duration-200",
        'placeholder':"Tu nombre"
    }))
    apellido = forms.CharField(label="apellido", required=True, widget=forms.TextInput(attrs={
        'class':"block w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget transition duration-200",
        'placeholder':"Tu apellido"
    }))
    email =forms.EmailField(label="email", required=True, widget=forms.EmailInput(attrs={
        'class':"block w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget transition duration-200",
        'placeholder':"tu@email.com"
    }))
    telefono = forms.IntegerField(label="Teléfono", required=False, widget=forms.NumberInput(attrs={
        'class':"block w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget transition duration-200",
        'placeholder':"+1 (555) 123-4567"
    }))
    contenido = forms.CharField(label="contenido", required=True,
                                widget=forms.Textarea(attrs={
                                    "rows":"6",
                                    "class":"block w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget resize-none transition duration-200",
                                    "placeholder":"Describe tu consulta o problema en detalle..."
                                }))