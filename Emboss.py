class Emboss_Kernel():
    def kernel(output):
        output[0][0] = -2
        output[0][1] = -1
        output[0][2] = 0
        output[1][0] = -1
        output[1][1] = 1
        output[1][2] = 1
        output[2][0] = 0
        output[2][1] = 1
        output[2][2] = 2
        return output