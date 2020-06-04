# python 画图

## 1.二维

1. 说明

   - 工具包

     ```python
     import matplotlib.pyplot as plt
     from matplotlib import font_manager
     # 在jupyter中需要添加下面的语句
     %matplotlib inline
     %config InlineBackend.figure_format = 'svg'
     ```

   - 中文标签

     ```python
     # windws和linux设置字体的放
     # font = {'family' : 'MicroSoft YaHei',
     #         'weight': 'bold',
     #         'size': 'larger'}
     # matplotlib.rc("font",**font)
     # matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")
     
     #另外一种设置字体的方式
     my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
     
     ```

     - 在需要中文的地方使用`fontproperties=my_font`调用，在图例中使用`prop=my_font`
     
   - latex

   - ```python
     plt.title(r"$\nu=0.2,\gamma=0.02$")
     ```

     

2. 基础设置

   - 设置图片大小
   
     ```python
    plt.figure(figsize=(20,8),dpi=80)
     ```
   
   - 设置x轴的刻度
   
   - ```python
     #调整x轴的刻度
     _xtick_labels = ["10点{}分".format(i) for i in range(60)]
     _xtick_labels += ["11点{}分".format(i) for i in range(60)]
     #取步长，数字和字符串一一对应，数据的长度一样
     plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font) #rotaion旋转的度数
     ```
   
   - 添加描述信息
   
   - ```python
     plt.xlabel("时间",fontproperties=my_font)
     plt.ylabel("温度 单位(℃)",fontproperties=my_font)
     plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)
     ```
   
   - 绘制网格
   
   - ```python
     plt.grid(alpha=0.1,linestyle=':')
     ```
   
   - 添加图例
   
   - ```python
     plt.legend(·,loc="upper left")
     ```
     
   - 保存图片
   
   - ```python
     plt.savefig(figname,bbox_inches='tight')
     ```
   
     
   
3. 普通画图

   ```python
   plt.plot(x,y_1,label="自己",color="#F08080")
   plt.plot(x,y_2,label="同桌",color="#DB7093",linestyle="--",alpha=0.2,)
   ```

4. 散点图

   ```python
   def my_scatter(x, y, x_str=None, y_str=None):
       plt.figure()
       plt.scatter(x, y, marker="o")
       plt.xlabel(x_str)
       plt.ylabel(y_str)
       plt.show()
   ```

5. 包裹面图

   - 以OCSVM为例

     ```python
     clf = svm.OneClassSVM(nu=0.2, kernel="rbf", gamma=0.02)
     clf.fit(Data)
     xx, yy = np.meshgrid(np.linspace(-15, 15, 500), np.linspace(-15, 15, 500))
     Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
     Z = Z.reshape(xx.shape)
     # plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
     a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
     # plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
     plt.scatter(Data[:,0],Data[:,1],edgecolors='k')
     plt.xlabel('x')
     plt.title(r"$\nu=0.2,\gamma=0.02$")
     plt.ylabel('y')
     plt.show()
     ```

   - 标准函数

   - ```python
     def my_counter(Data, clf, x_str, y_str):
         """
         画二维的包裹面
         :param Data:二维数据(n,2)
         :param clf:模型
         :param x_str:
         :param y_str:
         :return:
         """
         x = Data[:, 0]
         y = Data[:, 1]
         x_min = min(x)
         x_max = max(x)
         x_std = np.std(x)
         y_min = min(y)
         y_max = max(y)
         y_std = np.std(y)
         xx, yy = np.meshgrid(np.linspace((x_min - x_std), (x_max + x_std), 500),
                              np.linspace((y_min - y_std), (y_max + y_std), 500))
         # xx, yy = np.meshgrid(np.linspace(-15, 15, 500), np.linspace(-15, 15, 500))
         Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
         Z = Z.reshape(xx.shape)
         # plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
         a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
         # plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
         plt.scatter(Data[:, 0], Data[:, 1], edgecolors='k')
         plt.xlabel(x_str)
         plt.title(r"$\nu=0.2,\gamma=0.02$")
         plt.ylabel(y_str)
         plt.show()
     ```

## 2.三维

1. 工具包

   ```python
   from mpl_toolkits.mplot3d import Axes3D
   ```

2. 散点图

   ```python
   def plot_3d(x, y, z, x_str=None, y_str=None, z_str=None):
       ax = plt.subplot(projection='3d')  # 创建一个三维的绘图工程
       ax.scatter(x, y, z, c='r')  # 绘制数据点,颜色是红色
   
       ax.set_xlabel(x_str)
       ax.set_ylabel(y_str)
       ax.set_zlabel(z_str)  # 坐标轴
       # plt.draw()
       plt.show()
   ```
   
3. surface

   ```python
   def surface_plot(xx, yy, z, x_str, y_str, z_str, title_str):
       fig = plt.figure()
       ax = fig.add_subplot(111, projection='3d')  # 创建一个三维的绘图工程
       ax.plot_surface(xx, yy, z, cmap='rainbow')
       ax.scatter(X[:, 0], X[:, 1], y)
       ax.set_xlabel(x_str, fontproperties=my_font)
       ax.set_ylabel(y_str, fontproperties=my_font)
       ax.set_zlabel(z_str, fontproperties=my_font)  # 坐标轴
       plt.title(title_str, fontproperties=my_font)
       plt.show()
   ```

## 3.动态图

1. for 循环

   ```
   plt.figure()
   for i in range(1000):
       plt.clf()  # 清除图
       # plt.cla()  # 清除轴
       ·
       ·
       ·
       plt.pause(0.1)
   plt.pause(0)
   ```

## 4.  双轴图

1. 单张双轴图

   ```python
   fig, ax1 = plt.subplots()
   ax2 = ax1.twinx()
   ax1.set_xlabel('x')
   ax1.set_ylabel('y1')
   ax1.set_title('title')
   ax1.legend(loc=2)
   ax2.set_ylabel('y2')
   ax2.legend(loc=1)
   ax2.hist(data, bins=50, cumulative=True, normed=True, histtype='step', color='red', lw=2, label='hist') 
   plt.show()
   
   ```

2. 并列的双轴图

   ```python
   fig, ax = plt.subplots(1, 2, figsize=(20, 8))
   ax1 = ax[0]
   ax2 = ax1.twinx()
   ax1.hist(g_data, bins=bin_num, density=1)
   ax2.plot(x1, x1_list, 'r-')
   ax1.set_xlabel("粒径", fontproperties=my_font)
   ax1.set_ylabel("采样粒径分布百分比", fontproperties=my_font)
   ax2.set_ylabel("高斯分布", fontproperties=my_font)
   ax1.set_title("高斯", fontproperties=my_font)
   
   ax3 = ax[1]
   ax4 = ax3.twinx()
   ax4.plot(a, x3_list, 'r-')
   Width = (self.G_max - self.G_min) / bin_num
   x = np.arange(self.G_min, self.G_max, Width)
   x = x + 0.5 * Width
   
   ax3.bar(x, hist_data_mass_n, width=Width)
   ax3.set_xlabel("粒径", fontproperties=my_font)
   ax3.set_ylabel("采样质量分布百分比", fontproperties=my_font)
   ax4.set_ylabel("质量分布", fontproperties=my_font)
   
   _xticks_labels = ['{}'.format(i) for i in g_div]
   plt.xticks((x - 0.5)[::2], _xticks_labels[::2])
   ax3.set_title("质量分布", fontproperties=my_font)
   
   # fig.tight_layout()  # 调整整体空白
   plt.subplots_adjust(left=0.07, right=0.93, wspace=.25, hspace=0)  # 调整两个子图的间距和边缘距离
   plt.show()
   ```

   







