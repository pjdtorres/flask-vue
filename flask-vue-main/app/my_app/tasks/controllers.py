from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask.views import View
# from my_app.tasks.models import Task
from my_app.tasks import operations

# Deja la regla solo como '/' o como '/list'
taskRoute = Blueprint('taskRoute', __name__, url_prefix="/tasks")

task_list = ['task1', 'task2', 'task3']
class ListView(View):
    init_every_request = False

    def __init__(self, template) -> None:
        self.template = template

    def dispatch_request(self):
        # 1. Primeiro, vais buscar os objetos à base de dados
        tasks = operations.getAll()
        # 2. Ordena a lista pelo atributo ID
        tasks.sort(key=lambda x: x.id)
        
        # 2. Agora extraímos apenas o ID e o Nome para o print de teste
        # Supondo que o teu modelo tem os atributos 'id' e 'name' (ou 'nombre')
        lista_info = [(t.id, t.name) for t in tasks]
        print(f"Dados carregados: {lista_info}")
        
        # Obtém o número da página da URL, padrão é 1
        page = request.args.get('page', 1, type=int)
        
        # 2. Chama a tua função que está no operations.py
        # Recomendo usar per_page=5 para testares logo a navegação entre páginas
        pagination = operations.pagination(page=1, per_page=5)

        # 3. Print de depuração no Cmder para veres os IDs desta página específica
        print(f"Página: {pagination.page} | IDs: {[t.id for t in pagination.items]}")
    
        # 3. Passas a lista completa para o template
        return render_template(self.template, tasks=tasks)

# Nueva clase para crear tareas
class CreateView(View):
    methods = ['GET', 'POST']

    def __init__(self, template) -> None:
        self.template = template

    def dispatch_request(self):
        if request.method == 'POST':
            new_task = request.form.get('task', '').strip()
            if new_task:
                operations.create(new_task)
            return redirect(url_for('taskRoute.list'))

        return render_template(self.template)

# Nueva clase para atualizar tareas
class UpdateView(View):
    methods = ['GET', 'POST']

    def __init__(self, template) -> None:
        self.template = template

    def dispatch_request(self, id):
        # 1) Buscar no banco
        task_obj = operations.getById(id)
        if not task_obj:
            abort(404)

        # 2) Se for POST, atualizar no banco
        if request.method == "POST":
            name = request.form.get("task", "").strip()
            if name:
                operations.update(id, name)
                return redirect(url_for("taskRoute.list"))

        # 3) Se for GET, mandar o objeto para o template
        return render_template(self.template, id=id, task=task_obj)


class DeleteView(View):
    methods = ['POST']

    def dispatch_request(self, id):
        ok = operations.delete(id)
        if not ok:
            abort(404)
        return redirect(url_for('taskRoute.list'))


# --- REGISTRO DE RUTAS ---

# Lista de tareas
taskRoute.add_url_rule('/', view_func=ListView.as_view('list', template='dashboard/tasks/index.html'))

# Ruta para nueva tarea (¡Esta es la que falta!)
taskRoute.add_url_rule('/create/', view_func=CreateView.as_view('create', template='dashboard/tasks/create.html'))

# Registro de la ruta (asegúrate de que coincida con el nombre 'update')
taskRoute.add_url_rule(
    '/update/<int:id>', 
    view_func=UpdateView.as_view('update', template='dashboard/tasks/update.html')
)

taskRoute.add_url_rule(
    '/delete/<int:id>', 
    view_func=DeleteView.as_view('delete')
)
