 #!/bin/bash

export CARLA_ROOT="/home/atsushi/DriveLM/pdm_lite/carla/CARLA_Leaderboard_20"
export WORK_DIR="/home/atsushi/carla_garage"
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla
export SCENARIO_RUNNER_ROOT=${WORK_DIR}/scenario_runner
export LEADERBOARD_ROOT=${WORK_DIR}/leaderboard
export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":${PYTHONPATH}

# export TEAM_AGENT="/home/atsushi/carla_garage/team_code/data_agent.py"
# export TEAM_AGENT="/home/atsushi/carla_garage/team_code/sensor_agent.py"
export TEAM_AGENT="/home/atsushi/carla_garage/team_code/plant_agent.py"
export TEAM_CONFIG="/home/atsushi/carla_garage/team_code/pretrained_models/all_towns"

# export ROUTES=$LEADERBOARD_ROOT/data/routes_devtest.xml
export ROUTES=$LEADERBOARD_ROOT/data/longest6.xml
export ROUTES_SUBSET=0
export REPETITIONS=1
export REPETITION=0
# export DIRECT=1

export DEBUG_CHALLENGE=1
export VISU_PLANT=1
export CHALLENGE_TRACK_CODENAME=MAP
export CHECKPOINT_ENDPOINT="${LEADERBOARD_ROOT}/results.json"
export RECORD_PATH="/home/atsushi/carla_garage/logs"
export SAVE_PATH="/home/atsushi/carla_garage/logs"
export RESUME=0

export TOWN=Town12

# Make sure any previously started Carla simulator instance is stopped
# Sometimes calling pkill Carla only once is not enough.
pkill Carla
pkill Carla
pkill Carla

term() {
  echo "Terminated Carla"
  pkill Carla
  pkill Carla
  pkill Carla
  exit 1
}
trap term SIGINT

# Function to handle errors
handle_error() {
  pkill Carla
  exit 1
}

# Set up trap to call handle_error on ERR signal
trap 'handle_error' ERR

# Start the carla server
export CARLA_SERVER=${CARLA_ROOT}/CarlaUE4.sh
export PORT=2000
sh ${CARLA_SERVER} -carla-streaming-port=0 -carla-rpc-port=${PORT} &
sleep 20 # on a fast computer this can be reduced to sth. like 6 seconds
echo 'Port' $PORT

python3 ${LEADERBOARD_ROOT}/leaderboard/leaderboard_evaluator_local.py \
--routes=${ROUTES} \
--routes-subset=${ROUTES_SUBSET} \
--repetitions=${REPETITIONS} \
--track=${CHALLENGE_TRACK_CODENAME} \
--checkpoint=${CHECKPOINT_ENDPOINT} \
--debug-checkpoint=${DEBUG_CHECKPOINT_ENDPOINT} \
--agent=${TEAM_AGENT} \
--agent-config=${TEAM_CONFIG} \
--debug=${DEBUG_CHALLENGE} \
--record=${RECORD_PATH} \
--resume=${RESUME}