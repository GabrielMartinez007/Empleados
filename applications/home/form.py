# El archivo form se utilizar para modificar el funcionamiento de los formularios de django,
# el mismo es que interactua con los modelos y la vista para poder pintar la informacion
# en la template, aqui mismo se hacen validaciones y logicas para el funcionamiento de esos formularios.

from django import forms

from .models import Prueba

# Esta es una clase de formulario, la misma guarda un estilo de formulario, el archivo form puede tener
# mas de una clase y puede alimentar a infinidad de vistas.
class PruebaModels(forms.ModelForm):

    # La clase Meta es la que se encarga de lo visual de los formularios
    class Meta:
        model = Prueba
        fields = (
                  'titulo',
                  'subtitulo',
                  'cantidad',
        )
        # Los widgets son los que se encargan de embellecer los formularios.
        # widgets recibe un diccionario
        widgets = {
            # form.TextInpunt recibe un atributo llamado attrs
            'titulo': forms.TextInput(
                # attrs recibe un diccionario
                attrs={
                    'placeholder': "Ingrese texto aqui"
                }
            )
        }

    # Las funciones "clean" sirven para validar algun tipo de data, es la capa mas temprana de los formularios
    # antes de interactuar siquiera con las vistas la informacion agregada en cualquiera de los textbox se verifica
    # en este archivo.

    # en este caso voy a validar los valores ingresados en "cantidad" asi depurandolos antes de llegar a models y views.
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 10:
            raise forms.ValidationError("Ingrese un numero mayor a 10")

        return cantidad