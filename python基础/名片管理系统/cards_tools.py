# 记录所有的名片列表
card_list=[]

def show_menu():
	 '''
	 显示菜单
	 ''' 
	 print('*'*50)
	 print('欢迎使用[名片管理系统]V1.0.')
	 print('')
	 print('1. 新增名片')
	 print('2. 显示全部')
	 print('3. 查询名片')
	 print('')
	 print('0. 退出系统')
	 print('*'*50)

def new_card():
	print('-'*50)
	print('新增名片')
	# 提示用户添加名片信息
	name_str = input('请输入姓名:')
	phone_str = input('请输入电话号码:')
	QQ_str = input('请输入QQ号:')
	email_str = input('请输入邮箱:')
	# TODO 将用户添加的信息保存为一个字典
	card_dict = {'name':name_str,'phone':phone_str,'QQ':QQ_str,'email':email_str} 
	# 将字典添加到列表中
	card_list.append(card_dict)
	print(card_list)
	# 提示用户添加成功
	print('添加 %s 名片成功。' % name_str)


def show_all():
	print('-'*50)
	print('显示全部')
	# 判断是否存在名片记录
	if len(card_list) == 0:
		print('目前没有任何名片记录，请使用新增.')
		return 

	# 打印表头
	for name in ['姓名','电话','QQ','邮箱']:
		print(name,end='\t\t')
	print('')
	print("="*50)
	for card_dict in card_list:
		print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'],card_dict['phone'],card_dict['QQ'],card_dict['email']))

def search_card():
	print('-'*50)
	print('搜索名片')
	# 提示用户输入要搜索的姓名
	find_name = input('请输入要搜索的姓名:')

	#变量名片列表，查询要搜索的名字，如果没有找到，需要提示用户
	for card_dict in card_list:
		if card_dict['name'] == find_name:
			print('姓名\t\t电话\t\tQQ\t\temail')
			print("="*50)
			print('找到了')
			print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'],card_dict['phone'],card_dict['QQ'],card_dict['email']))

			# 针对找到的名片执行修改和删除操作
			deal_card(card_dict)
			break
	else:
		print('抱歉没有找到 %s ' % find_name)


def deal_card(find_dict):
	print(find_dict)
	action_str = input('请选择要执行的操作  '
						'[1]修改 [2]删除 [0]返回上级菜单: ')
	if action_str == '1':
		find_dict['name'] = input_card_info(find_dict['name'],'姓名[回车不修改]')
		find_dict['phone'] = input_card_info(find_dict['name'],'电话[回车不修改]')
		find_dict['QQ'] = input_card_info(find_dict['name'],'QQ[回车不修改]')
		find_dict['email'] = input_card_info(find_dict['name'],'email[回车不修改]')
		print('修改名片成功')
	elif action_str == '2':
		
		card_list.remove(find_dict)
		print('删除名片成功')
	else:
		pass

def input_card_info(dict_value,tip_message):

	# 提示用户输入内容
	result_str = input(tip_message)

	# 针对用户输入的信息进行判断，如果是用户输入的内容，直接返回结果
	if len(result_str) >0:
		return result_str

	# 如果用户没有输入内容，返回字典中原有的值
	else:
		return dict_value
