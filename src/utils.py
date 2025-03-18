def get_user_input():
    user_input = input("请输入控制指令 (前进: w, 后退: s, 左转: a, 右转: d, 左自旋: q, 右自旋: e, 停止: x): ")
    return user_input.strip().lower()