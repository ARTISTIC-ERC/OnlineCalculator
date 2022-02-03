![artistic-erc](https://user-images.githubusercontent.com/50483699/86449612-b9113980-bd18-11ea-8ee0-ddd5cf7326a4.png)

THE ARTISTIC Project Online Calculator
========================================================

These codes allow reproducing the computational workflow available in the "online calculator" section of the ARTISTIC project computational portal (https://www.erc-artistic.eu/computational-portal/) through a user-friendly interface and previous free registration to the platform

The codes allow generating 3D slurry and electrode mesostructures linked to LIB electrode manufacturing processes and they should be run sequentially (first the slurry, then the drying and finally the calendering).

The codes account for the slurry phase ("Slurry" folder), its drying ("Drying" folder) and the electrode calendering ("Calendering" folder). The drying can be performed through two different models, the first one outputting homogeneous electrode mesostructures, and the second one reproducing additive migration and the associated electrode heterogeneities.

The codes have been developed to be launched in sequence and by using the same folder, meaning that you should first wait the end of the slurry simulation, then launch the drying in the same folder and finally running the calendering simulation.

The values of the force field parameters reported in the codes are the ones employed for the online calculator mentioned above.

The inputs that the user should specify (if any) should be reported in the associated user_inputs* file.

The script* files are specific for running these simulations in the Matrics computational cluster, but they are function to offer to the user the order in which the codes should be launched.

For more information, the interested readers are referred to the online calculator (https://www.erc-artistic.eu/computational-portal/calculator/online-calculator) and the read me files available for each step (slurry, drying and calendering).


License
========================================================

This project is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence.

If you use these codes for your own research, please cite the following papers:

https://chemistry-europe.onlinelibrary.wiley.com/doi/full/10.1002/batt.202000049

https://www.sciencedirect.com/science/article/pii/S240582972100427X

https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/batt.202100324

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5956353.svg)](https://doi.org/10.5281/zenodo.5956353)

Contact
========================================================

For any doubt or question please contact:
alejandro.franco@u-picardie.fr (Professor Alejandro A. Franco, PI of the ARTISTIC project)
