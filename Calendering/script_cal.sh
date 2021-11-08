#!/bin/sh
#SBATCH --job-name=lammps
#SBATCH --partition=normal                      # submission queue
#SBATCH --time=2-0:00:00                        # 1-1 means one day and one hour -> here 20min
#SBATCH --mail-type=END
##SBATCH --mail-user=alain.ngandjong@u-picardie.fr       #e-mail notification
#SBATCH --output=job_seq-%j.out         # if --error is absent, includes alsothe errors
#SBATCH --nodes=1      # 2 cpus
#SBATCH --ntasks-per-node=20
##SBATCH --cpus=10
#SBATCH --mem=15G                                # T-tera, G-giga, M-mega

##
==================================================================================
# this job run on 2 nodes with 28 cpus on each
##
==================================================================================

echo
"------------------------------------------------------------------------------"
echo "hostname                     =   $(hostname)"
echo "SLURM_JOB_NAME               =   $SLURM_JOB_NAME"
echo "SLURM_SUBMIT_DIR             =   $SLURM_SUBMIT_DIR"
echo "SLURM_JOBID                  =   $SLURM_JOBID"
echo "SLURM_JOB_ID                 =   $SLURM_JOB_ID"
echo "SLURM_NODELIST               =   $SLURM_NODELIST"
echo "SLURM_JOB_NODELIST           =   $SLURM_JOB_NODELIST"
echo "SLURM_TASKS_PER_NODE         =   $SLURM_TASKS_PER_NODE"
echo "SLURM_JOB_CPUS_PER_NODE      =   $SLURM_JOB_CPUS_PER_NODE"
echo "SLURM_TOPOLOGY_ADDR_PATTERN  =   $SLURM_TOPOLOGY_ADDR_PATTERN"
echo "SLURM_TOPOLOGY_ADDR          =   $SLURM_TOPOLOGY_ADDR"
echo "SLURM_CPUS_ON_NODE           =   $SLURM_CPUS_ON_NODE"
echo "SLURM_NNODES                 =   $SLURM_NNODES"
echo "SLURM_JOB_NUM_NODES          =   $SLURM_JOB_NUM_NODES"
echo "SLURMD_NODENAME              =   $SLURMD_NODENAME"
echo "SLURM_NTASKS                 =   $SLURM_NTASKS"
echo "SLURM_NPROCS                 =   $SLURM_NPROCS"
echo "SLURM_MEM_PER_NODE           =   $SLURM_MEM_PER_NODE"
echo "SLURM_PRIO_PROCESS           =   $SLURM_PRIO_PROCESS"
echo
"------------------------------------------------------------------------------"

# USER Commands

# special commands for openmpi/intel
#module load openmpi/intel-opa/gcc/64/1.10.4
#setenv SCRDIR /ARTISTIC/ELECTRODE_FABRICATION/SLURRY/ACTIVE_CBD/JOB_01/RUN_01/

module load openmpi/intel-opa/gcc
module load lammps

python3.6 Reformatting_cal_electrode.py

sleep 10

mpirun -mca btl ^openib -np $SLURM_NPROCS lmp_mpi < in_cal.run

python3.6 pores_cal.py

touch finish
# end of the USER commands

