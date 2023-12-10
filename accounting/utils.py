import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y):
    plt.figure(figsize=(7, 4))
    plt.bar(x, y, color =['#262046', '#66333e'], edgecolor='#bd95cd')
    plt.title('Доходы и расходы', color="violet")
    plt.tick_params(axis='y', colors="violet")
    plt.tick_params(axis='x', colors="violet")
    plt.style.use('dark_background')
    graph = get_graph()
    return graph

def get_plot1(x, y):
    plt.figure(figsize=(7, 4))
    plt.bar(x, y, color =['#262046', '#7d5683', '#66333e', '#3399cc'], edgecolor='#bd95cd')
    plt.title('Расходы по дате', color="violet")
    plt.tick_params(axis='y', colors="violet")
    plt.tick_params(axis='x', colors="violet")
    plt.style.use('dark_background')
    graph = get_graph()
    return graph



menuout = [{'title': "Главная", 'url_name': 'index'}, 
               {'title': "Приложение", 'url_name': 'wallets'}]
    


