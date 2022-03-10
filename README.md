# Edge-Detection

Tools and Libraries:
● Python 3.8.8
● OpenCV (conda install -c conda-forge opencv)
● Argparse

Implementation Details:
1. Grayscale: Conversion to grayscale will reduce the number of
channels therefore, reduces the computational requirements.

2. Denoising: To remove the noise from the image, we can apply a filter
to the image in order to smooth it. The four common filters available
for noise removal are following,

● Averaging Filter: Averages all the pixels under the kernel area
and replaces the central element.

● Median Filter: Each pixel in an image gets multiplied by the
Gaussian Kernel.

● Gaussian Filter: This is a non-linear filtering technique that
takes a median of all the pixels under the kernel area and
replaces the central component with this median value.

● Bilateral Filter (default): This function can be applied to reduce
noise while keeping the edges sharp.

3. Thresholding: For every pixel, the same threshold value is applied.
If the pixel value is smaller than the threshold, it is set to 0, otherwise
it is set to a maximum value. Here, we have used a binary
thresholding which will convert the image into black and white.

4. Canny Edge Detection: uses a multi-stage algorithm which includes

a.Gaussian filtering 

b.Finding the intensity gradient of the image

c.Non-maximum suppression 

d.Double thresholding 

e.Edge tracking by hysteresis.

Possible Improvement:

Noise removal near edges could be
improved by computing customized kernels as per requirement.
