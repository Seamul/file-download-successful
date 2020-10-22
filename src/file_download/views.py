import os

from django.conf import settings
from django.http import HttpResponse


def file_download(request):
    quickbook_path = os.path.join(settings.MEDIA_ROOT, "documents", "Chart_of_Accounts.xlsx")

    with open(quickbook_path, 'rb') as file:
        context = file.read()

    response = HttpResponse(context, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="abc.xlsx"'

    return response
