import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import scipy.fftpack
import pydicom

class CTUtil:
	@staticmethod
	def load_dicom_file(file_path):
		return pydicom.dcmread(file_path)

	@staticmethod
	def get_pixel_array(dicom):
		return dicom.pixel_array

	@staticmethod
	def display_image(image, cmap='gray'):
		plt.imshow(image, cmap=cmap)
		plt.show()

	@staticmethod
	def normalize_image(image):
		return (image - np.min(image)) / (np.max(image) - np.min(image))

	@staticmethod
	def rescale_image(image, slope, intercept):
		return image * slope + intercept

	@staticmethod
	def window_image(image, window_center, window_width):
		img_min = window_center - window_width // 2
		img_max = window_center + window_width // 2
		window_image = image.copy()
		window_image[window_image < img_min] = img_min
		window_image[window_image > img_max] = img_max
		return window_image

	@staticmethod
	def get_dicom_metadata(dicom, field):
		return getattr(dicom, field, None)

	@staticmethod
	def save_image_as_png(image, file_path):
		plt.imsave(file_path, image, cmap='gray')

	@staticmethod
	def apply_threshold(image, threshold):
		return (image > threshold).astype(np.uint8)

	@staticmethod
	def get_image_shape(image):
		return image.shape

	@staticmethod
	def resize_image(image, new_shape):
		return cv2.resize(image, new_shape, interpolation = cv2.INTER_LINEAR)

	@staticmethod
	def rotate_image(image, angle):
		return ndimage.rotate(image, angle, reshape=False)

	@staticmethod
	def flip_image(image, axis):
		return np.flip(image, axis)

	@staticmethod
	def crop_image(image, start_row, start_col, end_row, end_col):
		return image[start_row:end_row, start_col:end_col]

	@staticmethod
	def get_pixel_value(image, row, col):
		return image[row, col]

	@staticmethod
	def set_pixel_value(image, row, col, value):
		image[row, col] = value

	@staticmethod
	def apply_gaussian_filter(input, sigma):
		return scipy.ndimage.gaussian_filter(input, sigma)

	@staticmethod
	def apply_median_filter(input, size):
		return scipy.ndimage.median_filter(input, size)

	@staticmethod
	def apply_fourier_transform(input):
		return scipy.fftpack.fft2(input)

	@staticmethod
	def apply_inverse_fourier_transform(input):
		return scipy.fftpack.ifft2(input)

	@staticmethod
	def apply_radon_transform(input, theta=None):
		return scipy.radon(input, theta)

	@staticmethod
	def apply_inverse_radon_transform(input, theta=None):
		return scipy.iradon(input, theta)

	@staticmethod
	def apply_sobel_filter(input):
		return scipy.ndimage.sobel(input)

	@staticmethod
	def apply_laplace_filter(input):
		return scipy.ndimage.laplace(input)

	@staticmethod
	def apply_gabor_filter(input, frequency):
		return scipy.ndimage.gabor_filter(input, frequency)