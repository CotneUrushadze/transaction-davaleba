from django.core.management import BaseCommand
from shop.models import *
from faker import Faker
from django.db.models import F
from django.db import transaction


faker = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):


#N!
        self.random_bulk(100)

    def random_bulk(self, num):
        items = []
        for _ in range(num):
            categoryitem = Category.objects.get(id=1)
            item = Item(name = faker.word(), price = 5, category = categoryitem)
            items.append(item)
        Item.objects.bulk_create(items)


    #     self.random_notbulk(100)

    # def random_notbulk(self, num):
    #     for _ in range(num):
    #         categoryitem = Category.objects.get(id=1)
    #         item = Item(name = faker.word(), price = 5, category = categoryitem)
    #         item.save()


#N2
    #     self.price_up()

    # def price_up(self):
    #     Item.objects.filter(id__gt=500).update(price = F('price') * 1.1)
        

#N3
        # Item.objects.filter(price__lt=50).delete()


#N4
        # for _ in range(1, 11):
        #     category = Category.objects.create(name = 'for niggers')
        #     item = Item.objects.create(name = 'KFC', category = category)

        
        # with transaction.atomic():
        #             for _ in range(1, 11):
        #                 category = Category.objects.create(name = 'for niggers')
        #                 item = Item.objects.create(name = 'KFC', category = category)
