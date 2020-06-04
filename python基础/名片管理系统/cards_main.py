#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import cards_tools
while True:
	
	# TODO 显示功能菜单
	cards_tools.show_menu()

	action_str=input('请选择希望执行的操作：')
	print('您选择操作是[%s]' % action_str)

	# 1,2,3 针对名片的操作
	if action_str in ['1','2','3']:
		# 新增名片 
		if action_str == '1':
			cards_tools.new_card()

		#显示全部
		if action_str == '2':
			cards_tools.show_all()

		#查询名片
		if action_str == '3':
			cards_tools.search_card()

		# pass

	# 0 退出系统
	elif action_str == '0':
		# 如果在程序编写时不，不希望立刻编写分支内容
		# 可以使用pass 关键字 作为一个占位符，保证程序的代码结构正确
		# pass
		print('欢迎再次使用名片管理系统。 ')
		break

 
	# 其他输入错误，提醒用户
	else:
		print('您输入的不正确，请重新输入。')