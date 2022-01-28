![artistic-erc](https://user-images.githubusercontent.com/50483699/86449612-b9113980-bd18-11ea-8ee0-ddd5cf7326a4.png)

THE ARTISTIC Project Online Calculator
========================================================

These codes allow reproducing the computational workflow available in the "online calculator" section of the ARTISTIC project computational portal (https://www.erc-artistic.eu/computational-portal/) through a user-friendly interface and previous free registration to the platform

The codes allow generating 3D slurry and electrode mesostructures linked to LIB electrode manufacturing processes and they should be run sequentially (first the slurry, then the drying and finally the calendering).

The codes account for the slurry phase ("Slurry" folder), its drying ("Drying" folder) and the electrode calendering ("Calendering" folder). The drying can be performed through two different models, the first one outputting homogeneous electrode mesostructures, and the second one reproducing additive migration and the associated electrode heterogeneities.

The codes have been developed to be launched in sequence and by using the same folder, meaning that you should first wait the end of the slurry simulation, then launch the drying in the same folder and finally running the calendering simulation.

The values of the force field parameters reported in the codes are the ones employed for the online calculator mentioned above.

The inputs that the user should specify (if any) should be reported in the associated user_inputs* file.

For more information, the interested readers are referred to the online calculator (https://www.erc-artistic.eu/computational-portal/calculator/online-calculator) and the read me files available for each step (slurry, drying and calendering).

License
========================================================

This project is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence.

This project received funding from the European Union’s Horizon 2020 research and innovation program for the funding support through the European Research Council (grant agreement 772873, “ARTISTIC” project, PI: Prof. Alejandro A. Franco).

If you use these codes for your own research, please cite the following papers:

T. Lombardo, J.B. Hoock, E.N. Primo, A.C. Ngandjong, M. Duquesnoy, A.A. Franco. Accelerated Optimization Methods for Force-Field Parametrization in Battery Electrode Manufacturing Modeling, Batteries & Supercaps 3(8) (2020) 721, https://doi.org/10.1002/batt.202000049.

A.C. Ngandjong, T. Lombardo, E.N. Primo, M. Chouchane, A. Shodiev, O. Arcelus, A.A. Franco. Investigating electrode calendering and its impact on electrochemical performance by means of a new discrete element method model: Towards a digital twin of Li-Ion battery manufacturing, 485 (2021) 229320, https://doi.org/10.1016/j.jpowsour.2020.229320.

T. Lombardo, A.C. Ngandjong, A. Belhcen, A.A. Franco. Carbon-Binder Migration: A Three-Dimensional Drying Model for Lithium-ion Battery Electrodes, Energy Storage Materials, 43 (2021) 337, https://doi.org/10.1016/j.ensm.2021.09.015.

T. Lombardo, F. Caro, A.C. Ngandjong, J.B. Hoock, M. Duquesnoy, J.C. Delepine, A. Ponchelet, S. Doison, A.A. Franco. The ARTISTIC Online Calculator: Exploring the Impact of Li-ion Battery Electrode Manufacturing Parameters Interactively through your Browser, Batteries & Supercaps (2022) https://doi.org/10.1002/batt.202100324.

Contact
========================================================

For any question please contact:
alejandro.franco@u-picardie.fr (Professor Alejandro A. Franco, PI of the ARTISTIC project)
