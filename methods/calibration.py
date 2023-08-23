############################################################################################################################################################
############################################################################################################################################################

# Program name: calibration.py
# Author: Luca Teruzzi, PhD in Physics, Astrophysics and Applied Physics, University of Milan, Milan (IT)
#         EuroCold Lab, Department of Earth and Environmental Sciences, University of Milano-Bicocca, Milan (IT)
# Date: 01 May 2022 (last modified)
# Objective: Abakus laser sensor calibration
# Description: This Python script aims at computing the instrumental calibration curve for Abakus laser sensor.
#              From a practical standpoint, some measurements were performed with colloidal suspensions of calibrated polystirene nanoparticles (known refractive index
#              @ 670 nm) with variable diameters of 1.0, 1.5, 2.0, 2.9, 3.75, 5.0 and 5.75 μm.
#              The calibration procedure is based on Mie scattering theroy for perfectly spherical and homogeneous particles: the optical extinction cross section
#              is computed and the resulting curve is inverted in terms of the (extinction) diameter.
#              Then, a comparison in made between the measured diameters and the theoretical ones: their ratios defines the desired calibration curve, that is 
#              the function for which the measured diameter divided by the calibration function corresponds exactly to the extinction diameter.
#              The calibration curve is retireved through a polynomial fit and saved on a text file for future analyses.

############################################################################################################################################################
############################################################################################################################################################


import numpy as np, math as m, matplotlib.pyplot as plt, miepython, sys                                 # Import the required libraries
from scipy.interpolate import interp1d
from miepython import *


############################################################################################################################################################
############################################################################################################################################################


x = np.linspace(1, 15, 600)                                                                             # x range for computation
x_plot = np.linspace(0, 10, 200)

wavelength= 0.67                                                                                        # Abakus wavelength
n_med = 1.33                                                                                            # Water refractive index @ specified wavelength
n_p = np.sqrt((1.4435*wavelength*wavelength)/(wavelength*wavelength - 0.020216) + 1)                    # Polystirene refractive index @ specified wavelength
wavelength = wavelength/n_med                                                                           # Wavelength correction on the medium refractive index
Q_ext, Q_sca, Q_back, g = mie(n_p/1.33, 2*m.pi*(x/2)/wavelength)                                        # Mie computation
sigma_ext = Q_ext*(x/2)**2                                                                              # Extinction cross-section
d_ext = np.sqrt(2*sigma_ext)                                                                            # Extinction diameter (spherical approximation)

d_interpolation = interp1d(x, d_ext, fill_value='extrapolate')

true_diameter_2021 = np.array([1.50, 1.80, 2.00, 3.78, 5.10, 5.49, 10])                                 # True samples diameters
meas_diameter_2021 = np.array([2.50, 2.80, 3.10, 4.00, 5.80, 6.40, 11])                                 # Measured diameters
y_dev_2021 = np.array([0.165, 0.165, 0.110, 0.130, 0.098, 0.100, 0.1])                                  # Error on measured diameters
ratio_2021 = meas_diameter_2021/d_interpolation(true_diameter_2021)                                     # Ration between the measured diameter and the theoretical prediction
                                                                                                        # rom Mie scattering theory

fit_coefficients, cov_matrix = np.polyfit(meas_diameter_2021, ratio_2021, 4, full=False, cov=True)      # Fit parameters and covariance matrix for calibration curve
calibration_curve = np.poly1d(fit_coefficients)
calibration_curve_lower, calibration_curve_upper = np.poly1d(fit_coefficients - 0.05*np.sqrt(np.diag(cov_matrix))), np.poly1d(fit_coefficients + 0.05*np.sqrt(np.diag(cov_matrix)))

f = plt.figure(figsize=(8, 6))                                                                          # Plot(s) for data visualization
plt.suptitle('Abakus calibration curve --- pt. 1', size=16, y=0.97) 
f.subplots_adjust(left=0.095, right=0.975, top=0.93, bottom=0.105)
ax = f.add_subplot(111)
ax.loglog(x, x, 'b--', linewidth=3, label='d$_{meas}$ = d$_{nom}$')
ax.loglog(x, d_ext, 'r-', linewidth=3, label='d$_{ext}$')
ax.loglog(true_diameter_2021, meas_diameter_2021, 'k*', linewidth=None, markersize=10, label='2021')
ax.errorbar(true_diameter_2021, meas_diameter_2021, yerr=y_dev_2021, ecolor='k', elinewidth=1.2, capsize=3, errorevery=1, linestyle='None')
ax.set_ylabel('Measured diameter [$\mu$m]', fontsize=12)
ax.set_xlabel('Nominal diameter [$\mu$m]', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.legend(loc='upper left')

f1 = plt.figure(figsize=(8, 6))
plt.suptitle('Abakus calibration curve --- pt. 2', size=16, y=0.97) 
f1.subplots_adjust(left=0.13, right=0.975, top=0.93, bottom=0.105)
ax1 = f1.add_subplot(111)
ax1.plot(x_plot, calibration_curve(x_plot), 'g-', linewidth=3, label='best fit')
ax1.plot(x_plot, calibration_curve_lower(x_plot), 'g-', linewidth=0.5); ax1.plot(x_plot, calibration_curve_upper(x_plot), 'g-', linewidth=0.5)
ax1.fill_between(x_plot, calibration_curve_upper(x_plot), calibration_curve_lower(x_plot), color='g', alpha=0.3, label='1σ deviation')
ax1.plot(meas_diameter_2021, ratio_2021, '^', linewidth=None, markersize=10, markeredgecolor='k', markeredgewidth=2, markerfacecolor='None', label='2021')
ax1.errorbar(meas_diameter_2021, ratio_2021, yerr=y_dev_2021/d_interpolation(true_diameter_2021), ecolor='k', elinewidth=2, capsize=4, errorevery=1, linestyle='None')
ax1.set_ylabel('Measured diameter / extinction diameter', fontsize=12)
ax1.set_xlabel('Measured diameter [$\mu$m]', fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
plt.legend(loc='upper left', ncol=2)

plt.show()

current_directory = sys.argv[1]
file = open(current_directory+'_calibration/calibration_curve.txt', 'w')                    # Save data on .txt file for future analyses
for i in range(0, len(x_plot)):
    file.write(str(x_plot[i])+'\t'+str(calibration_curve(x_plot[i]))+'\t'+str(calibration_curve_lower(x_plot[i]))+'\t'+str(calibration_curve_upper(x_plot[i]))+'\n')  
file.close()


############################################################################################################################################################
############################################################################################################################################################
