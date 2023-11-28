"""
Collection of auxiliary utility functions for graph-dock

"""
import pandas as pd
import random
import os
import candle_lib 


# Command line parameters

additional_definitions = [
   {
       'name':'input_dir',
        'type': str,
        'help':'input data directory'
    },
    {
        'name':'output_dir',
        'type': str,
        'help':'network structure of shared layer'
    },
    {
        'name':'training_index_file',
        'type': str,
        'help':'index file for training set [numpy array]'
    },
        {
        'name':'training_index_file',
        'type': str,
        'help':'index file for training set [numpy array]'
    }
    {
        'name':'training_index_file',
        'default' : 'training.idx'
        'type': str,
        'help':'index file for training set [numpy array]'
    },
    {
        'name':'validation_index_file',
        'default' : 'validation.idx' ,
        'type': str,
        'help':'index file for validation set [numpy array]',
    },
    {
        'name':'testing_index_file',
        'default' : 'testing.idx' ,
        'type': str,
        'help':'index file for testiing set [numpy array]',
    },
    {
        'name':'data',
        'default' : 'data.parquet' ,
        'type': str,
        'help':'data file',
    }
]

required = [
    # 'data_url',
    # 'train_data',
    # 'test_data',
    # 'model_name',
    # 'conv',
    # 'dense',
    # 'activation',
    # 'out_act',
    # 'loss',
    # 'optimizer',
    # 'feature_subsample',
    # 'metrics',
    # 'epochs',
    # 'batch_size',
    # 'drop',
    # 'classes',
    # 'pool',
    # 'save'
]

class CLI(candle.Benchmark):

    def set_locals(self):
        """Functionality to set variables specific for the benchmark
        - required: set of required parameters for the benchmark.
        - additional_definitions: list of dictionaries describing the additional parameters for the
        benchmark.
        """

        if required is not None:
            self.required = set(required)
        if additional_definitions is not None:
            self.additional_definitions = additional_definitions


def preprocess_data(
    sample_size=50000,
    partition_ratios=[0.8, 0.1, 0.1],
    raw_data_path=os.path.join(
        "./", "data", "d4_table_name_smi_energy_hac_lte_25_title.csv"
    ),
    output_path=os.path.join("./", "data", "d4_dock_data_500k.csv"),
):
    """
    Formats data from docking data given by Lyu et al (classical docking) paper
    into format expected by training script.

    Parameters
    ----------
    sample_size : int
        Size of train+val+test sample
    partition_ratios : List[int]
        Ratios for training, validation, testing, respectively
    raw_data_path : os.path
        Location of raw data
    output_path : os.path
        Location of output data
    """
    n = sum(1 for line in open(raw_data_path)) - 1
    skip_r = sorted(random.sample(range(1, n + 1), n - sample_size))
    df = pd.read_csv(raw_data_path, skiprows=skip_r)
    df = df.drop(["hac"], axis=1)
    # create partitions
    partitions = (
        ["train"] * int(partition_ratios[0] * sample_size)
        + ["val"] * int(partition_ratios[1] * sample_size)
        + ["test"] * int(partition_ratios[2] * sample_size)
    )

    # deal with int rounding
    while len(partitions) != sample_size:
        partitions.append("train")

    random.shuffle(partitions)
    df["partition"] = partitions
    df.to_csv(output_path)

def initialize_parameters():
    cfg = CLI(
        "./config/
        ",  # this is the path to this file needed to find default_model.txt
        "graph-dock.default.cfg",  # name of the default_model.txt file
        "pytorch",  # framework, choice is keras or pytorch
        prog="graph-dock",  # basename of the model
        desc="some description",
    )

    # return the parameter dictionary built from
    # config file and overwritten by any
    # matching comand line parameters.
    gParameters = candle.finalize_parameters(
        cfg
    )  

    return gParameters

def main():
    params = initialize_parameters()
    scores = run(params)
    print(params["data_dir"])

    # demonstrating a list
    for i, value in enumerate(params["dense"]):
        print("dense layer {} has {} nodes".format(i, value))

    preprocess_data()

if __name__ == "__main__":
    preprocess_data()




