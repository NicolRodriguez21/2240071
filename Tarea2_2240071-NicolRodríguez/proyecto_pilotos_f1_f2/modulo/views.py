from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PilotoForm
from .models import Piloto


@login_required
def piloto_lista(request):
    pilotos = Piloto.objects.filter(usuario=request.user)

    busqueda = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '').strip()
    escuderia = request.GET.get('escuderia', '').strip()

    if busqueda:
        pilotos = pilotos.filter(
            Q(nombre__icontains=busqueda)
            | Q(nacionalidad__icontains=busqueda)
            | Q(escuderia__icontains=busqueda)
        )

    if categoria in ('F1', 'F2'):
        pilotos = pilotos.filter(categoria=categoria)

    if escuderia:
        pilotos = pilotos.filter(escuderia__icontains=escuderia)

    escuderias = (
        Piloto.objects.filter(usuario=request.user)
        .order_by('escuderia')
        .values_list('escuderia', flat=True)
        .distinct()
    )

    paginator = Paginator(pilotos, 6)
    pagina = paginator.get_page(request.GET.get('page'))

    return render(
        request,
        'modulo/piloto_lista.html',
        {
            'pagina': pagina,
            'busqueda': busqueda,
            'categoria_seleccionada': categoria,
            'escuderia_seleccionada': escuderia,
            'escuderias': escuderias,
            'total_filtrado': paginator.count,
        },
    )


@login_required
def piloto_detalle(request, pk):
    piloto = get_object_or_404(
        Piloto,
        pk=pk,
        usuario=request.user,
    )
    return render(
        request,
        'modulo/piloto_detalle.html',
        {'piloto': piloto},
    )


@login_required
def piloto_crear(request):
    if request.method == 'POST':
        formulario = PilotoForm(request.POST)

        if formulario.is_valid():
            piloto = formulario.save(commit=False)
            piloto.usuario = request.user
            piloto.save()
            messages.success(
                request,
                'El piloto se creó correctamente.',
            )
            return redirect('piloto_detalle', pk=piloto.pk)
    else:
        formulario = PilotoForm()

    return render(
        request,
        'modulo/piloto_formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Añadir piloto',
            'accion': 'Crear piloto',
        },
    )


@login_required
def piloto_editar(request, pk):
    piloto = get_object_or_404(
        Piloto,
        pk=pk,
        usuario=request.user,
    )

    if request.method == 'POST':
        formulario = PilotoForm(request.POST, instance=piloto)

        if formulario.is_valid():
            formulario.save()
            messages.success(
                request,
                'Los cambios se guardaron correctamente.',
            )
            return redirect('piloto_detalle', pk=piloto.pk)
    else:
        formulario = PilotoForm(instance=piloto)

    return render(
        request,
        'modulo/piloto_formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Editar piloto',
            'accion': 'Guardar cambios',
            'piloto': piloto,
        },
    )


@login_required
def piloto_eliminar(request, pk):
    piloto = get_object_or_404(
        Piloto,
        pk=pk,
        usuario=request.user,
    )

    if request.method == 'POST':
        nombre = piloto.nombre
        piloto.delete()
        messages.success(
            request,
            f'El piloto {nombre} se eliminó correctamente.',
        )
        return redirect('piloto_lista')

    return render(
        request,
        'modulo/piloto_confirmar_eliminar.html',
        {'piloto': piloto},
    )
