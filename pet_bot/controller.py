from .models import Pet, Task

def find_pet(owner_id):
    try:
        pet = Pet.objects.get(owner_id=owner_id)
        return pet
    except:
        raise ValueError('Id: ' + str(owner_id) + ' does not correspond to a valid user')

def find_task(task_id):
    try:
        task = Task.objects.get(id=task_id)
        return task
    except:
        raise ValueError('Task of id = ' + str(task_id) + ' does not correspond to a valid Task')

def my_tasks(owner_id):
    pet = find_pet(owner_id)
    return pet.my_tasks()

def start_task(owner_id, task_id):
    pet  = find_pet(owner_id)
    task = find_task(task_id)
    if task.status != Task.PENDING:
        return 'No se puede comenzar la tarea '+ task.name +' ya que no se encuentra pendiente'
    elif task.pet:
        if task.pet != pet:
            return 'No se puede comenzar la tarea '+ task.name +' ya que se encuentra tomada por el usuario '+ task.pet.name
        else:
            return 'La tarea '+ task.name +' ya se encuentra tomada por este usuario'
    else:
        task.pet = pet
        task.mark_as_doing()
        return 'Tarea comenzada con éxito, termínala para ganar '+ str(task.credits) +' créditos'

def finish_task(owner_id, task_id):
    pet  = find_pet(owner_id)
    task = find_task(task_id)
    if task.status != Task.DOING:
        return 'No se puede terminar la tarea '+ task.name +' ya que no se encuentra en progreso'
    elif task.pet != pet:
        return 'No se puede terminar la tarea '+ task.name +' ya que no se encuentra tomada por el usuario '+ pet.owner_name
    else:
        pet.available_credits = pet.available_credits + task.credits
        pet.save()
        task.pet = None
        task.mark_as_done()
        return 'Tarea terminada con éxito, ganaste '+ str(task.credits) +' créditos!'

def free_tasks(owner_id = None):
    free_tasks = list(Task.objects.filter(pet = None))
    return free_tasks

def pet_status(owner_id):
    pet  = find_pet(owner_id)
    return pet.state

def my_credits(owner_id):
    pet = find_pet(owner_id)
    return pet.available_credits

def use_credits(owner_id):
    pet = find_pet(owner_id)
    response = pet.use_credits()
    if response == False:
        return 'No tiene suficientes créditos para ayudar a su mascota. Pruebe haciendo más tareas!'
    else:
        return 'Buena!! Tu masctoa está Ok nuevamente!! Keep up the hard work!'

def random_bad_state(owner_id, credits):
    pet = find_pet(owner_id)
    return pet.random_bad_state(credits)
