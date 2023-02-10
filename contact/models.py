from django.db import models

class ContactBook(models.Model):
    image = models.FileField(_("Avatar Image"),)
    mobile_number = models.CharField(_("Mobile Number"), max_length=11)
    email = models.EmailField(_("user Email"), max_length=254)
    label = models.CharField(_("label"), max_length=50)
    person_name = models.CharField(_("person Name"), max_length=50)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)



    class Meta:
        verbose_name = _("ContactBook")
        verbose_name_plural = _("ContactBooks")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("ContactBook_detail", kwargs=("pk": self.pk))
