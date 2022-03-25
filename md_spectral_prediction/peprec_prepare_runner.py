import pandas as pd
from pandas import DataFrame
import os
import subprocess


def prepare_peprec(search_results_path: str,
        peprec_output_dir: str):

    searchResults = pd.read_json(search_results_path)
    peprec_df = searchResults_to_peprec(search_results_df=searchResults)

    os.makedirs(peprec_output_dir, mode=0o777, exist_ok=True)
    peprec_df.to_csv(os.path.join(peprec_output_dir, "search.peprec"),sep='\t', index=False)


def searchResults_to_peprec(search_results_df: DataFrame):
    peprec_initialise = search_results_df.loc[:,['sequence','charge']].drop_duplicates()
    peprec_initialise = peprec_initialise.rename(columns={"sequence":"peptide"})
    peprec_initialise["spec_id"] = peprec_initialise.index
    peprec_initialise["modifications"] = '-'
    peprec_initialise = peprec_initialise.loc[:,['spec_id','modifications','peptide','charge']]
    return peprec_initialise

def run_ms2pip(config_path: str, peprec_path: str):
    print("Running ms2pip predictions")
    command = [
    'ms2pip',
    '-c', config_path,
    ' ', peprec_path
    ]
    print(command)

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        print(output.decode("utf-8"))
        print("finished")
    except subprocess.CalledProcessError as e:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(e.output.decode("utf-8"))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        raise(e)

