from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


from todos import exceptions
from todos import models

def done(request, id, path_name, path_id=None):
    todo = get_object_or_404(models.Todo, id=id)
    todo.done = not todo.done
    try:
        todo.save(request.user)
    except exceptions.InvalidUserExcpetion as e:
        messages.add_message(request, messages.ERROR, _(str(e.message)))
        if path_id != None:
            url = reverse(path_name, args=[id])
        else:
            url = reverse(path_name)
        return HttpResponseRedirect(url)


    msg_done = _("done")
    msg_not_done = _("not done")
    msg_done_full = f'{todo.title}: {msg_done}!'
    msg_not_done_full = f'{todo.title}: {msg_not_done}!'


    if todo.done:
        messages.add_message(request, messages.SUCCESS, msg_done_full)
    else:
        messages.add_message(request, messages.WARNING, msg_not_done_full)

    if path_id != None:
        url = reverse(path_name, args=[id])
    else:
        url = reverse(path_name)
    return HttpResponseRedirect(url)