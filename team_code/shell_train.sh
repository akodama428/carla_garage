#!/bin/bash

export CARLA_ROOT="/home/atsushi/DriveLM/pdm_lite/carla/CARLA_Leaderboard_20"
export WORK_DIR="/home/atsushi/carla_garage"
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla
# export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.14-py3.7-linux-x86_64.egg
export SCENARIO_RUNNER_ROOT=${WORK_DIR}/scenario_runner
export LEADERBOARD_ROOT=${WORK_DIR}/leaderboard
export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":${PYTHONPATH}
export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":${PYTHONPATH}

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/anaconda3/lib

export OMP_NUM_THREADS=8  # Limits pytorch to spawn at most num cpus cores threads
export OPENBLAS_NUM_THREADS=1  # Shuts off numpy multithreading, to avoid threads spawning other threads.
#torchrun --nnodes=1 --nproc_per_node=1 --max_restarts=1 --rdzv_id=42353467 --rdzv_backend=c10d train.py --id train_id_000 --batch_size 8 --setting all --root_dir ~/code/leaderboard2_human_data/database/training_v0_2023_11_23 --logdir ~/code/leaderboard2_human_data/training_runs/debug --use_controller_input_prediction 1 --use_wp_gru 1 --use_discrete_command 1 --use_tp 1 --continue_epoch 1 --cpu_cores 8 --num_repetitions 1
torchrun --nnodes=1 --nproc_per_node=1 --max_restarts=1 --rdzv_id=$SLURM_JOB_ID --rdzv_backend=c10d \
    train.py --id train_id_003 --crop_image 1 --use_velocity 1 --seed 2 --epochs 31 --batch_size 5 --lr 0.0003 --setting all \
    --root_dir /home/atsushi/DriveLM/pdm_lite/log_root \
    --logdir /home/atsushi/carla_garage/team_code/pretrained_models/all_towns \
    --use_controller_input_prediction 1 --use_wp_gru 0 --use_discrete_command 1 --use_tp 1 --tp_attention 0 --continue_epoch 0 \
    --load_file /home/atsushi/carla_garage/team_code/pretrained_models/all_towns/model_0030_2.pth \
    --cpu_cores 8 --num_repetitions 1 \
    --crop_bev_height_only_from_behind 1 --lidar_resolution_height 256 --dataset_cache_name dataset_cache_256 

# /home/geiger/gwb791/code/leaderboard2_human_data/database/training_v3_oldtowns_2024_04_10
#--root_dir /home/geiger/gwb791/code/leaderboard2_human_data/database/training_v3_oldtowns_2024_04_10 /mnt/qb/work/geiger/gwb438/leaderboard2_human_data/database/expert_v3_dataset_2024_04_10 \ 
