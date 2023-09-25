
# DEDALO: Device for Enhanced Dust Analyses with Light Obscuration sensors


# Introduction 

DEDALO is an open-source Python-based GUI software that allows to operate an in-line SPOS instrument and further analyze the data by compensating for the refractive index value, according
to the specific sample composition. In addition, DEDALO also recovers the numeric concentration of the sample, which is not provided by the instrument. The algorithm computes 𝐶ext analytically with
Mie scattering theory [1, 2]; smoothing functions are then introduced as in traditional instruments. The general workflow is sketched in the following:

#
<p align="center">
<img src="https://github.com/LucaTeruzzi/DEDALO/assets/83271765/7470415b-6055-449f-bcb2-59418f6ea3d5" width=50% height=50%>
</p>

#

The core of the DEDALO algorithm is a pre-computed extinction cross-section look-up-table (LUT) obtained by varying particle diameter and refractive index and calculating the 𝐶ext values through Mie theory. The use of the LUT saves a considerable amount of computational resources, avoiding to calculate the Mie functions everytime.

DEDALO allows the user to operate the SPOS instrument in-line, only requiring the value of the flow rate as an input. During the measurement, the algorithm shows the instantaneous (1 s
integration time) and the time-integrated PSD, as well as the instantaneous numeric concentration of the sample. A continuous monitoring of the working parameters is provided. Each instantaneous
PSD and the time-integrated one are written into a file, together with some statistical markers such as the PSD mode diameter and the distribution quantiles. They are formatted both as spreadsheets
and as text files, complying with most data visualization tools.

Being written in Python 3.10, the algorithm can run on all operative systems without compatibility issues.

# Documentation

This README gives a brief overview of the key information required to install and run the software.

## Package setup

To run the script on his own laptop or PC, the user first need to install the specified Python
packages:

• numpy ≥ 1.21, matplotlib ≥ 3.6.2 and math (default packages);

• pyserial, for setting the serial communication through the RS232 port between the SPOS instrument and the PC;

• PyQt5, pyqtgraph, qtwidgets required for the graphical user interface;

• termcolor;

• pandas;

• os-sys ≥ 2.1.4;

• scipy ≥ 1.9.3 (optimize, interpolate), needed for computing the instrumental calibration
curve;

• miepython, for computations regardig Mie scattering parameters (eg. scattering and extinction cross sections);

• openpyxl, for exporting data in xlsx files.

To do so, after installing Python3 and pip3, you can just copy and paste the following line in the
command line:
```
pip3 install numpy≥1.21, matplotlib≥3.6.2, os-sys≥2.1.4, pyserial, PyQt5, pyqtgraph, qtwidgets, termcolor, scipy≥1.9.3, miepython, openpyxl, pandas
```
Otherwise, you can run the setup.py script in the ”setup” folder by typing:
```
python3 setup.py
```

## How to use

The algorithm is designed to be extremely user-friendly and can be run dircetly from command line by typing:

```
python3 spos_main.py
```

or by just double clicking on the executbale version (Windows only) spos_main.pyw.
The following GUI interface is displayed:

<img src="https://github.com/LucaTeruzzi/DEDALO/assets/83271765/a67adbd8-fb8c-4091-9c7e-3ef9f4aed760" width=100% height=100%>

# Contributions

New issues and pull requests are welcomed. 

# Citation

If you use this code in a publication, please cite: 

L. Teruzzi, L. Cremonesi and M.A.C. Potenza, "DEDALO: Device for Enhanced Dust Analyses with Light Obscuration sensors", J. Instrum. (in review)

# References

[1] C. van de Hulst, Light Scattering by Small Particles, Dover Publication Inc., New York (1981).

[2] C. F. Boren, D. R. Huffman, Absorption and Light Scattering by Small Particles, Wiley Science
Paperback Series, New York (1998).

# Permissions

This code is provided under a GNU GENERAL PUBLIC LICENSE and it is in active development. Collaboration ideas and pull requests generally welcomed. Please use the citations below to credit the builders of this repository.

Copyright (c) 2023 Luca Teruzzi
