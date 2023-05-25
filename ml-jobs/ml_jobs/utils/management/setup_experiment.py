"""
fill me in
"""


def setup_experiment(base, name, version):
    """
    fill me in
    """
    experiment = mlflow.create_experiment(
        f"{base}/{name}/experiments/", tags={"version": "1.0", "env": "DEV"}
    )
    model_path = f"{base}/{name}/experiments/model"
