# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
# на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения
# оптимального  решения.

# Вариант 5. Предприятие может предоставить работу по одной специальности 2 женщинам, по другой - 2 мужчинам,
# по третьей - 2 работникам независимо от пола. Сформировать все возможные варианты заполнения вакантных мест,
# если имеются 6 претендентов: 3 женщины и 3 мужчины.

import time
from itertools import combinations
# Претенденты с характеристиками (имя, опыт, уровень квалификации)
women = [
    {'name': 'Ж1', 'experience': 4, 'qualification': 7},
    {'name': 'Ж2', 'experience': 6, 'qualification': 9},
    {'name': 'Ж3', 'experience': 5, 'qualification': 8}
]
men = [
    {'name': 'М1', 'experience': 5, 'qualification': 6},
    {'name': 'М2', 'experience': 10, 'qualification': 8},
    {'name': 'М3', 'experience': 3, 'qualification': 7}
]

# Вариант 1: Алгоритмический метод с ограничениями и целевой функцией
print("\nВариант 1: Алгоритмический")
start_time = time.time()
all_combinations_manual = []
for women_pair in combinations(women, 2):
    # Проверяем, удовлетворяет ли каждая женщина в паре условию : минимум 5 лет опыта
    if all(p['experience'] >= 5 for p in women_pair):
        remaining_women = [w for w in women if w not in women_pair]
        for men_pair in combinations(men, 2):
            remaining_men = [m for m in men if m not in men_pair]
            remaining = remaining_women + remaining_men
            # Целевая функция — сумма квалификации на специальности 2 - критерий оптимальности
            total_qualification = sum(p['qualification'] for p in men_pair)
            all_combinations_manual.append({
                'специальность 1': [p['name'] for p in women_pair],
                'специальность 2': [p['name'] for p in men_pair],
                'специальность 3': [p['name'] for p in remaining],
                'total_qualification': total_qualification
            })
end_time = time.time()
# Поиск оптимального решения — максимальная квалификация на специальности 2
best_manual = max(all_combinations_manual, key=lambda x: x['total_qualification'])
print(f"Всего комбинаций (алгоритмический): {len(all_combinations_manual)}")
for idx, combo in enumerate(all_combinations_manual, 1):
    print(f"{idx}. {combo}")
print(f"\nЛучшая комбинация (алгоритмический): {best_manual}")
print(f"Время выполнения (алгоритмический): {end_time - start_time:.6f} секунд\n")

# Вариант 2: С помощью функций Питона с ограничениями и целевой функцией
print("\nВариант 2: Через itertools")
start_time = time.time()
all_combinations_itertools = []
for w_comb in combinations(women, 2):
    # Условие минимум 5 лет опыта
    if all(p['experience'] >= 5 for p in w_comb):
        rem_w = [w for w in women if w not in w_comb]
        for m_comb in combinations(men, 2):
            rem_m = [m for m in men if m not in m_comb]
            rem = rem_w + rem_m
            # Целевая функция — квалификация на специальности 2
            total_qualification = sum(p['qualification'] for p in m_comb)
            all_combinations_itertools.append({
                'специальность 1': [p['name'] for p in w_comb],
                'специальность 2': [p['name'] for p in m_comb],
                'специальность 3': [p['name'] for p in rem],
                'total_qualification': total_qualification
            })
end_time = time.time()
best_itertools = max(all_combinations_itertools, key=lambda x: x['total_qualification'])
print(f"Всего комбинаций (itertools): {len(all_combinations_itertools)}")
for idx, combo in enumerate(all_combinations_itertools, 1):
    print(f"{idx}. {combo}")
print(f"\nЛучшая комбинация (itertools): {best_itertools}")
print(f"Время выполнения (itertools): {end_time - start_time:.6f} секунд")