docker kill precise_trainer
docker rm precise_trainer
docker run \
        -v PATH_TO_DATASETS:/opt/precise/wake-words\
        -v PATH_TO_TRAINING_FOLDER:/opt/precise/training\
        --name precise_trainer  precise:0.3
