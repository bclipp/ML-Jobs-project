from ml_jobs.utils.data_prep.get_train_test_split import get_train_test_split
from ml_jobs.utils.extract.get_table import get_table
from ml_jobs.utils.management.setup_experiment import setup_experiment
from ml_jobs.utils.model.train_sales import train_sales


def build_sales_model():
    """
    fill in
    """
    # spark = SparkSession \
    #    .builder \
    #    .appName("Schema App") \
    #    .getOrCreate()

    gold_sales = get_table("sales")
    model_data = get_train_test_split(gold_sales)
    experiment = setup_experiment("/Users/bclipp21@gmail.com/", "chapter_12", "1.2")
    train_sales(model_data)


if __name__ == "__main__":
    build_sales_model()
