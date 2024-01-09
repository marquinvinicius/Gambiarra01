import mysql.connector
from bokeh.plotting import figure, show
from random import randint
from bokeh.models import ColumnDataSource
from bokeh.colors import RGB

#banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='classicmodels',
)

cursor = conexao.cursor()
comando = '''
select country, count(country) from customers
group by country
having count(country) > 3
'''
cursor.execute(comando)

#capitando os dados
resultado = cursor.fetchall()
paises = [r[0] for r in resultado]
quantidade = list([r[1] for r in resultado])

#gambiarra iniciando

cor = [RGB(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(len(paises))]
fonte = ColumnDataSource(data=dict(paises=paises, quantidade=quantidade, color=cor))

p = figure(x_range=paises, plot_height=400, title='Gambiarra Master',
           toolbar_location=None, tools='')
#dados de baixo, tamanho, ferramentas
p.vbar(x='paises', top='quantidade', width=0.5, color='color',
           legend_field='paises', source=fonte)
#dados debaixo, eixo y, largura da barra, cor, legenda, e a fonte dos dados

#gambiarra dos estilos
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = 'Paises'
p.yaxis.axis_label = 'Usuarios por pais'
p.title.text_font_size = '16pt'
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'

show(p)
