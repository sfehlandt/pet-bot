from .models import Pet, Task

    def my_tasks(owner_id):
        print('Execute my_tasks')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        pet.my_tasks()

    def start_task(owner_id, task_id):
        print('Execute start_task')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        task = Task.objects.get(id=task_id)s
        pet.start_task(task)

    def finish_task(owner_id, task_id):
        print('Execute finish_task')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        task = Task.objects.get(id=task_id)
        pet.finish_task(task)

    def free_tasks(owner_id):
        print('Execute free_tasks')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        Task.free_tasks()

    def pet_status(owner_id):
        print('Execute pet_status')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        pet.get_status()

    def my_credits(owner_id):
        print('Execute my_credits')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        pet.my_credits()

    def use_credits(owner_id):
        print('Execute use_credits')
        return
        pet = Pet.objects.get(owner_id=owner_id)
        pet.use_credits()
