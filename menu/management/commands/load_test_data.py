from django.core.management.base import BaseCommand
from menu.models import FoodCategory, Food


class Command(BaseCommand):
    help = 'Загружает тестовые данные для меню'

    def handle(self, *args, **options):
        self.stdout.write('Очищаем существующие данные...')
        Food.objects.all().delete()
        FoodCategory.objects.all().delete()

        self.stdout.write('Создаем категории...')
        cat1 = FoodCategory.objects.create(name_ru='Напитки', order_id=10)
        cat2 = FoodCategory.objects.create(name_ru='Выпечка', order_id=20)
        cat3 = FoodCategory.objects.create(name_ru='Скрытая категория', order_id=30)

        self.stdout.write('Создаем блюда...')
        
        # Напитки (опубликованные)
        tea = Food.objects.create(
            category=cat1, code=1, internal_code=100,
            name_ru='Чай', description_ru='Чай 100 гр',
            cost=123.00, is_publish=True
        )
        cola = Food.objects.create(
            category=cat1, code=2, internal_code=200,
            name_ru='Кола', description_ru='Кола',
            cost=123.00, is_publish=True
        )
        sprite = Food.objects.create(
            category=cat1, code=3, internal_code=300,
            name_ru='Спрайт', description_ru='Спрайт',
            cost=123.00, is_publish=True
        )
        baikal = Food.objects.create(
            category=cat1, code=4, internal_code=400,
            name_ru='Байкал', description_ru='Байкал',
            cost=123.00, is_publish=True
        )
        # Напитки (опубликованные)
        dobriy = Food.objects.create(
            category=cat1, code=5, internal_code=500,
            name_ru='Добрый кола', description_ru='Добрый кола',
            cost=123.00, is_publish=False
        )

        # Выпечка (опубликованные)
        Food.objects.create(
            category=cat2, code=6, internal_code=600,
            name_ru='Круассан', description_ru='Свежий круассан',
            cost=250.00, is_publish=True
        )

        # Скрытая категория (неопубликованные)
        Food.objects.create(
            category=cat3, code=7, internal_code=700,
            name_ru='Блюдо is_publish=False', description_ru='Не для всех',
            cost=999.00, is_publish=False
        )

        # Дополнительные товары (Чай + Кола)
        tea.additional.add(cola)

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))
        self.stdout.write(f'Категорий: {FoodCategory.objects.count()}')
        self.stdout.write(f'Блюд: {Food.objects.count()}')
