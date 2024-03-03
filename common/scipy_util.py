from scipy import stats, optimize, interpolate, fftpack
import numpy as np

class ScipyUtil:
	@staticmethod
	def calculate_statistics(data):
		return stats.describe(data)

	@staticmethod
	def calculate_normal_distribution_pdf(x, mean, std_dev):
		return stats.norm.pdf(x, mean, std_dev)

	@staticmethod
	def optimize_function(func, initial_guess):
		return optimize.minimize(func, initial_guess)

	@staticmethod
	def interpolate_data(x, y, new_x):
		f = interpolate.interp1d(x, y)
		return f(new_x)

	@staticmethod
	def calculate_fft(data):
		return fftpack.fft(data)

	@staticmethod
	def calculate_ifft(data):
		return fftpack.ifft(data)

	@staticmethod
	def solve_linear_system(A, b):
		return np.linalg.solve(A, b)

	@staticmethod
	def calculate_eigenvalues_and_eigenvectors(A):
		return np.linalg.eig(A)

	@staticmethod
	def calculate_inverse_matrix(A):
		return np.linalg.inv(A)

	@staticmethod
	def calculate_determinant(A):
		return np.linalg.det(A)

	@staticmethod
	def calculate_rank(A):
		return np.linalg.matrix_rank(A)

	@staticmethod
	def calculate_svd(A):
		return np.linalg.svd(A)

	@staticmethod
	def calculate_pca(data):
		mean = np.mean(data, axis=0)
		data_centered = data - mean
		U, S, Vt = np.linalg.svd(data_centered)
		return U, S, Vt