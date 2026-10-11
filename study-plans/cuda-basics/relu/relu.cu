#include <cuda_runtime.h>

__global__ void relu_kernel(const float* input, float* output, int N) {
    // Store N element-wise results in output; this kernel returns no value.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N) {
        if (input[i] > 0) {
            output[i] = input[i];
        }
        else {
            output[i] = 0;
        }
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    relu_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}