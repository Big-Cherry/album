# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: scripts.rpy
#  description: (story scripts) Game starts from here
#  Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

# 全局属性定义区：

default dunhuang_value = 0

# 特殊图像

image black = Solid("#000")

# 常用转场

define phototake = Fade(0.1, 0.0, 0.1)

# 游戏在此开始。

label start:
    
    # 开始东极岛故事线
    jump dj_start
