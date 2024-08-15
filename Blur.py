class Blur_Kernel():
    def kernel(output):
        output[0][0] = 0.0625
        output[0][1] = 0.125
        output[0][2] = 0.0625
        output[1][0] = 0.125
        output[1][1] = 0.25
        output[1][2] = 0.125
        output[2][0] = 0.0625
        output[2][1] = 0.125
        output[2][2] = 0.0625
        return output