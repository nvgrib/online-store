import random


def get_list_with_random_ids(model, count):
	all_ids = [item.id for item in model.objects.all()]
	random.shuffle(all_ids)
	return all_ids[:count]