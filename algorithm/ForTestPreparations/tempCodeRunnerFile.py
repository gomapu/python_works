    # 1からW_intまでの値について、総和がその値に一致するかを判定
    for w in range(1, W_int+1):
        #総和ができる(関数がTrueを返す)ときカウント+1
        if(func(N_int, w, N_list, memo)):
            count += 1