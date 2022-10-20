from django.shortcuts import render
from matplotlib.style import context
import plotly.express as px
from chart1.forms import DateForm
from chart1.models import Turbit

def chart(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
   
    tt= Turbit.objects.all()
    
    if start:
        tt = tt.filter(dt__gte=start)
    if end:
        tt = tt.filter(dt__lte=end)

    fig=px.scatter(
        y=[c.power for c in tt ],
        x=[c.wind for c in tt ],
        title="Power vs Wind speed",
        labels={'x':"Wind speed(m/s)",'y':"Power(kW)"}
        
    )
    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
    })
    chart=fig.to_html()
    context={'chart': chart,'form':DateForm()}
    return render(request,'chart1/chart1.html',context)
    