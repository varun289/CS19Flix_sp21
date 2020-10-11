models.py:

    class MyModel(models.Model):
        field1 = models.CharField(max_length=40, blank=False, null=False)
        field2 = models.CharField(max_length=60, blank=True, null=True)

forms.py:

    class MyModelForm(forms.ModelForm):  # extending ModelForm, not Form as before
        class Meta:
            model = MyModel

views.py:

    def create_a_my_model(request):
        if request.method == 'POST':
            form = MyModelForm(request.POST)
            if form.is_valid():
                # save the model to database, directly from the form:
                my_model = form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
                # alternatively:
                # my_model = form.save(commit=False)  # create model, but don't save to database
                # my.model.something = whatever  # if I need to do something before saving it
                # my.model.save()
        else:        
            form = MyModelForm()
        context_data = {'form': form}
        return HttpResponse('templtate.html', context_data)
