qa_tree = [
	{
		'question': 'Инструмент электрический или ручной?',
		'answers': [
			{
				'name': 'Электрический',
				'next_index': 1
			},
			{
				'name': 'Ручной',
				'next_index': 9
			}
		]
	},
	{
		'question': 'Назначение инструмента?',
		'answers': [
			{
				'name': 'Сверлить',
				'next_index': 2
			},
			{
				'name': 'Пилить/Строгать',
				'next_index': 5
			}
		]
	},
	{
		'question': 'Сверление с ударом или без?',
		'answers': [
			{
				'name': 'С ударом',
				'next_index': 3
			},
			{
				'name': 'Без удара',
				'next_index': 4
			}
		]
	},
	{
		'final': True,
		'answer': 'Перфоратор'
	},
	{
		'final': True,
		'answer': 'Дрель'
	},
	{
		'question': 'Основная рабочая деталь?',
		'answers': [
			{
				'name': 'Диск',
				'next_index': 6
			},
			{
				'name': 'Цепь',
				'next_index': 7
			},
			{
				'name': 'Фреза',
				'next_index': 8
			}
		]
	},
	{
		'final': True,
		'answer': 'Циркулярная пила'
	},
	{
		'final': True,
		'answer': 'Цепная пила'
	},
	{
		'final': True,
		'answer': 'Электрорубанок'
	},
	{
		'question': 'Предназначен для того, чтобы ... гвозди?',
		'answers': [
			{
				'name': 'Забивать',
				'next_index': 10
			},
			{
				'name': 'Вытаскивать',
				'next_index': 11
			}
		]
	},
	{
		'final': True,
		'answer': 'Молоток'
	},
	{
		'final': True,
		'answer': 'Клещи'
	}
]


def read_user_input(msg='', possible_answers=[]):
	print(msg)
	print('\n'.join([
		'%d. %s' % (i + 1, possible_answers[i]['name']) for i in range(len(possible_answers))
	]))

	is_correct_input = False
	index = ''
	while not is_correct_input:
		try:
			index = int(input()) - 1
			is_correct_input = 0 <= index < len(possible_answers)
			if not is_correct_input:
				print('Введенный номер должен быть больше нуля и меньше номера последнего варианта ответа')
		except:
			print('Некорректный ввод. Введите номер одного из предложенных вариантов')

	return index


def next_step(step=0):
	node = qa_tree[step]

	if 'final' in node:
		print('Ответ:', node['answer'])
		return

	index = read_user_input(
		node['question'],
		node['answers']
	)

	next_step(node['answers'][index]['next_index'])


next_step(0)