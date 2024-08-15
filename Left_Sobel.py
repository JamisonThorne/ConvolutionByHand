class Left_Sobel_Kernel():
    def kernel(output):
        output[0][0] = 1
        output[0][1] = 0
        output[0][2] = -1
        output[1][0] = 2
        output[1][1] = 0
        output[1][2] = -2
        output[2][0] = 1
        output[2][1] = 0
        output[2][2] = -1
        return output
