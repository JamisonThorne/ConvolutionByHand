class Identity_Kernel():
    def kernel(output):
        output[0][0] = 0
        output[0][1] = 0
        output[0][2] = 0
        output[1][0] = 0
        output[1][1] = 1
        output[1][2] = 0
        output[2][0] = 0
        output[2][1] = 0
        output[2][2] = 0
        return output