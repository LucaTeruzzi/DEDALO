# DEDALO
 Device for Enhanced Dust Analyses with Light Obscuration sensors

# DEDALO: Device for Enhanced Dust Analyses with Light Obscuration sensors
============================================================================

###################################################################################################
###################################################################################################



               ###         #####           ###         ##    ##    ##      ##     ######
              ## ##        ##   ##        ## ##        ##   ##     ##      ##   ###
             ##   ##       ##   ##       ##   ##       ## ##       ##      ##    ###
            #########      #####        #########      ####        ##      ##      #####
           ##       ##     ##   ##     ##       ##     ##  ##      ##      ##          ##
          ##         ##    ##   ##    ##         ##    ##    ##     ###  ###         ####
         ##           ##   #####     ##           ##   ##     ##      ####      #######
    ___________________________________________________________________________________________

         #         #     ####  #####  ####         ####  ##### ##    #  ####  ###  ####
         #        # #   ##     #      #  ##       ##     #     # #   # ##    #   # #  ##
         #       #   #    #    ###    ###           #    ###   #  #  #   #   #   # ###
         #      ######     ##  #      #  #           ##  #     #   # #    ## #   # #  #
         ##### #      # ####   #####  #   #       ####   ##### #    ## ####   ###  #   #
    ___________________________________________________________________________________________



ABAKUS LASER SENSOR SOFTWARE ---- PYTHON 3.8, v 1.1.2  ©

EUROCOLD LAB, EUROPEAN COLD LABORATORY FACILITIES 
DEPARTMENT OF EARTH AND ENVIRONMENTAL SCIENCES, UNIVERSITY OF MILANO-BICOCCA (MILAN, ITALY)

Acknowledgment:
1) L. Teruzzi,   	      PhD in Physics, Astrophysics and Applied Physics, Department of Physics,
                 	      University of Milan (Milan, Italy)
2) C. Artoni,    	      engineering manager of the EuroCold Lab, Department of Earth and Environmental Sciences,
                 	      University of Milano-Biccoca (Milan, Italy)
3) L. Cremonesi, 	      research fellow, Department of Earth and Environmental Sciences,
                 	      University of Milano-Biccoca (Milan, Italy)

Further contributions:
1) C. Ravasio, 		   research fellow, Department of Earth and Environmental Sciences,
		     	            University of Milano-Biccoca (Milan, Italy)
2) M. A. C. Potenza, 	associate professor, Department of Physics, 
		     	            University of Milan (Milan, Italy)
3) B. Delmonte, 	      tenured assistant professor, Department of Earth and Environmental Sciences, 
                 	      University of Milano-Biccoca (Milan, Italy)
4) V. Maggi, 		      full professor, Department of Earth and Environmental Sciences, 
                 	      University of Milano-Biccoca (Milan, Italy)


###################################################################################################
###################################################################################################


In the following, each element in the right GUI interface is described:

• DATA AND INPUT PARAMETERS
- Path directory: path were the files (.txt, .dat) containing full data from Abakus
laser sensor, as read via serial port RS-232, are stored.
Files are structured as follows. The 2 heading rows contain the title (ABAKUS LASER SENSOR ----- 
PARTICLE SIZE DISTRIBUTION DATA), the name of the serial port connected to the user pc, 
the name of the software owned by the Abakus particle counter and its ID number and the noise levels
for each one of the 32 Abakus channels are retrieved (they should be measured in milliVolt).
Then, it is reported the delay time between two consecutive serial writing and reading operations
on serial port (default: 10 ms), the flow rate set on the peristaltic pump during the measurement (mL/min)
and its date and time.
Lastly, a table is created reporting the incremental index of the measurement (aka. the time measurement in seconds), 
the acquisition time (generally, half a second), the laser diode voltage, the RAM-buffer and the number of 
particle counts for each channel.

- Data file(s): file(s) name the user wants to analyze; this input can consist of
both a single name and a list of names, separated by a comma (" , "). File names can be written extensively by hand or 
can be selected in the specified repostory through the button 'Select' on the side as well. The
histograms in the firt three left panels are always referred to the first file specified in the
list, while for a comparison of all the input files the user can switch to the third
panel where their normalized histograms are shown. The aim of such a normalization is only to 
make the histograms correctly comparable at sight, dividing each column by the total number of countings.

- Save path: path were the result files (.txt, .dat) of the subsequent data analysis are saved.
This kind of file is generally structured as follows.
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
Average laser diode voltage:
Avergae RAM-buffer voltage:
Flow rate:  
Particles detected:
Total particles concentration:
Counts distribution peaked @: (as a function of particle diameters)
Counts distribution average:
Counts distribution average (arithmetical):
Time-average # counts:
Time std. deviation # counts:
Time-median # counts:
First quantile # counts (in time):
Third quantile # counts (in time):
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
Some differences on the results written on the file may depend on which kind of data the user is consindering (raw data, 
extinction-calibration corrected data or updated (aka. restriceted on x axis) data).

- Save name: name specified by the user (WITHOUT any extension, they are set automatically inside
the script) for saving.

- Flow rate: measured in mL/min, it is the flow rate set on the peristaltic pump
during the CFA measurement.  
The flow rate must be specified by the user before the measurement with the Abakus particle counter starts.

- Delay time: time between two consecutive serial writing and serial reading operations on the 
serial port. This delay time is only effective in LIVE mode, while the Abakus laser sensor is measuring.
Default value is 80 ms.

- Skip heading lines: number of heading rows to skip before preforming the analysis.
These lines consist of a series of information concerning the measurement
previously performed with the Abakus laser sensor (Date and time of the acquisition,
software version, noise levels and so on).
Default value is 38.

- Acquisition time: measured in seconds, it is the specific period the user wants
to analyze.
This input line is useful if the user wants to perform a comparison (in the last plotting panel) of more 
than one measurement: specifically, it allows to select ammong all the input file specified by the user only 
those "longer" than [acquisition time] seconds.

- Date: date and starting time of the measurement, saved also in the heading lines of the file.

- Buttons:
* Live: this button allows to swich between two different operating modes of
the software: if "Live" is OFF, when the "Run" button is selected the GUI
application reads all the input paramter previously defined and performs the
analysis of a pre-recorded data file. On the contrary, if the "Live" button is
ON the software performs a real time analysis during the continuous flow
measurement, plotting the corresponding histograms and saving data on file.
* Run: this button starts the (serial reading and) analysis according to the
option selected by "Live".
* Save: this button allows the user to save all the results, also shown in the
"Concentration and counting results from Abakus" output window, on a
.txt od .dat file; the path to the correct directory and the file name are the ones
specified before.
* Pause: this button pauses the measurement; when pressed another time, the measurement
restarts without losing previous data.
* Stop: this button stops the current measurement, disconnects the Abakus laser
sensor and closes the saving file.

- Concentration bar: status bar to monitor the number of counts and hence the sample concentration. A sort of colormap
has been implemented so that when the concentration is low the statua bar is green (single particle and scattering condition)
while while the concentration is getting higher the status bar changes color from green to red gradually.

- Abakus running: check if the instrument in working properly by changing its
color from red to green; if a problem of any kind is detected, the label becomes
red again.
* iteration time: measured in milliseconds, it measures the time the acquisition took 
effectively (consindering the serial writing and reading operations, the delay times set during the acquisition, 
the time needed for printing the results on the GUI window and saving them on file, and so on).
Usually, it is about 0.5 seconds.

- Sensor alarm: check if the laser diode voltage is being measured correctly by changing
its color from red to green; if any problem is detected or if the regulating voltage
exceeds 7000 mV, the label becomes red again.
* laser diode voltage: measured in mV, it is the regulation voltage of the laser
diode inside the instrument; it is a very important parameter, since if the
voltage exceeds 8000 mV (V), the sensor must be switched off immediately
and cleaned up.

- RAM-buffer alarm: check if the RAM-buffer voltage is being measured correctly by changing
its color from red to green; if any problem is detected or if the regulating voltage
exceeds 7000 mV, the label becomes red again.
* RAM-buffer voltage: measured in mV, it is the regulation voltage of the instrument RAM-buffer;
in order to work and measure properly, it must be greater than 2.4 V.

# ----------------------------------------------------------------------------------------------- #

• CONCENTRATION AND COUNTING RESULTS FROM ABAKUS
In non-LIVE mode, in this output window results are shown concerning the total number of particles detected by the Abakus,
the total particle concentration and the partial concentrations for each channel as well.
As for the time evolution plot, here the average numer of counts, the median and the first and third quantile 
are reported as well.
In LIVE mode, here are reported the first serial commands sent to the Abakus particle counter (for getting 
the software version, the noise levels and the number of channels) and then, each second, are printed in three columns 
the acquisition time, the increment in particle countings and the total number of particles detected so far.

# ----------------------------------------------------------------------------------------------- #

• ERROR, WARNINGS AND SYSTEM MESSAGES
In this output window are visualized warnings and/or error messages occurred during the software running.
They can be like 'ERROR', 'WARNING', 'Saving...'.

# ----------------------------------------------------------------------------------------------- #

• FIXED SETTINGS
- Size range and resolution: diameter range the instrument can measure, from 1 up to 7.2 microns, and difference 
in diameter that the Abakus laser sensor can resolve; in our case, it is equal to 200 nm.
- Noise levels (for each channel): noise levels measured by the Abakus laser sensor
itself before the measurement starts.
They should correspond to voltage (mV) noise of the instrument itself. They are ininfluent on the proper measurement.

# ----------------------------------------------------------------------------------------------- #

• APPROXIMATIONS
Simply here is specified that the Abakus sensor work in spherical
approximation, as already stated before in Chapter 1; this allows to derive a straighforward
relation between the extinction cross-section (which is the physical parameter
properly measured by the Abakus laser sensor) and the extinction diameter of the
equivalent sphere:
σ = (π·d^2)/4
Moreover, this physical quantity is also linked to the scattering amplitude (precisely, its real part) as
σ = (4π/k^2)*Re{S(0)},       with k = 2π/λ, λ the wavelength


###################################################################################################
###################################################################################################


Instead, on the left GUI interface the user can find six sections that can be selected by
the corresponding button on top and some informations of software and serial communication with the Abakus
laser sensor:

• SOFTWARE AND SERIAL PORTS
- Serial port: serial port(s) available for connecting the Abakus laser sensor to the user pc.

- Show serial monitor (button): this button allows the user to show a serial monitor, specifically
tailored to control the serial communication between the user pc and the intrument.
On this monitor the user can control the input and output strings/hex/bytes every second continuously.

- Software version: the software version registred on the Abakus particle counter.

# ----------------------------------------------------------------------------------------------- #

• Histogram: # counts vs d: the panel shows the historam related to the file (or the
first file, if more than one are listed) specified in the "Data file(s)" input line. The
y-axis reports the number of counts for each channel (aka, each extinction diameter).

• Histogram: # counts vs σ ext: same as before, but as a function of the extinction cross-section.

• Histogram: # counts vs Re{S(0)}: same as before, but as a function of the real part of the 
scattering amplitude.

• Time evolution: the panel shows the time-histogram related to the file (or the first
file, if more than one are listed) specified in the "Data file(s)" input line. Here, on
the y-axis the user can read the total number of counts registered by the Abakus
laser sensor every second (x-axis).
A dashed black line also highlight the average number of counts during the measurement.

• Voltage monitor (laser diode and RAM): the panel shows the behaviour of the laser diode
voltage and the RAM-buffer voltage of the devide during the measurement.

• Normalized cumulative distribution(s): the panel shows a comparison between
the histograms of all the files in the "Data file(s)" input line, properly normalized in
order to be compared correctly.

# ----------------------------------------------------------------------------------------------- #

In the lower part, three additional buttons may help the user performing data analysis (in non-LIVE mode).

- Update plot: moving the two vertical lines in the plots, this button allows the user to select and analyze only
the specificed subset of data.

- Correct data (extinction calibration): this button allows to show on the above plots the data corrected on the calibration curve.
At the same time, a pop-up window is shown where the 'corrected' results are stored.

- View calibration curve: this button creates two different plots.
The first one shows the measured particle diameters as a function of the true dimeters certified by the manufacturer; on this 
plot are also shown the bisector where the two diameters coincide and the Mie theoretical curve for the extinction diameter.
The second figure refers to the proper calibration curve, which has to be considered as the function such that the measured
diameter divided by the calibration function is the extinction diameter.


###################################################################################################
###################################################################################################


SOFTWARE VERSIONING

• Major version 1.0.0 -------- released on XX/XX/XXXX


###################################################################################################
###################################################################################################


For more informations on the classes, funtions and methods used to achieve this software,
plase have a look at Appendix B of the 'CFA datasheet' file in the corresponding repository.
If you still have some doubts, questions or suggestions for making the software better and
nicer, feel free to contact Luca Teruzzi:
• Phone number:     +39 334 9801058
• Office:           +39 02 6448 2074
• Mail:             luca.teruzzi@unimib.it
				                luca.teruzzi@unimi.it


###################################################################################################
###################################################################################################

