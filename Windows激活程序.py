try:
    import os
    import time
    class activation:
        def __init__(self):
            upk = "start slmgr.vbs /upk"
            ipk = "start slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX"
            skms = "start slmgr.vbs /skms zh.us.to"
            ato = "start slmgr.vbs /ato"
            xpr = "start slmgr.vbs /xpr"
            self.upk = upk
            self.ipk = ipk
            self.skms = skms
            self.ato = ato
            self.xpr = xpr
        def welcome(self):
            print('''
欢迎使用Windows激活程序，请确保您以管理员身份运行该程序并完全按照指示操作！。
版本：V1.0.0
作者：杂[Five Gallon]
发布日期：2023年4月7日

Copyright © 2023
                  ''')
            os.system("pause")
            os.system("cls")
        def up(self):
            print("正在卸载产品密钥")
            print("请在提示窗口出现后在继续")
            os.system(self.upk)
            os.system("pause")
            os.system("cls")
        def ip(self):
            print("正在安装产品密钥")
            print("请在提示窗口出现后在继续")
            os.system(self.ipk)
            os.system("pause")
            os.system("cls")
        def sk(self):
            print("正在设置密钥管理服务计算机名称")
            print("请在提示窗口出现后在继续")
            os.system(self.skms)
            os.system("pause")
            os.system("cls")
        def at(self):
            print("正在激活系统（此步时间可能较长，请耐心等待！）")
            print("请在提示窗口出现后在继续")
            os.system(self.ato)
            os.system("pause")
            os.system("cls")
        def check(self):
            print("正在检测...")
            os.system(self.xpr)
            time.sleep(5)
            os.system("pause")
except:
    print("程序运行时遇到错误！")
else:
    print("系统初始化成功！")
    main = activation()
    main.welcome()
    main.up()
    main.ip()
    main.sk()
    main.at()
    main.check()