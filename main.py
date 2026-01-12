def main():
    # 用列表存储5个学生的成绩
    score = [0, 0, 0, 0, 0]  # 初始化5个位置
    while True:
        print("\n===== 简单成绩分析系统 =====")
        print("1. 输入学生成绩")
        print("2. 显示最高分和最低分")
        print("3. 显示平均分")
        print("4. 显示所有成绩")
        print("5. 退出系统")
        print("===========================")
        # 用户选择功能
        ch = input("请选择功能 (1-5): ")
        if ch == "1":
            # 调用同学B写的函数
            score=inputgrade(score)
        elif ch == "2":
            # 调用同学C写的函数
            maxx,minn= maxmin(score)
            # 调用同学D写的函数
            xsmaxmin(maxx,minn)  
        elif ch == "3":
            # 调用同学C写的函数
            av= aver(score)
            # 调用同学D写的函数
            xsaver(av)
        elif ch == "4":
            # 调用同学D写的函数
            xsall(score)
        elif ch == "5":
            print("谢谢使用，再见！")
            break
            
        else:
            print("输入错误，请输入1-5的数字！")
# 启动程序
if __name__ == "__main__":
    main()
