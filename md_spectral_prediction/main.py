import argparse
import os

from peprec_prepare_runner import prepare_peprec, run_ms2pip


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='Peptide Mapping Export', description='Run MS2 pip with search results')

    parser.add_argument("-s", "--search_results_path", dest='search_results_path',
                        help='Path to Mass Dynamics searchResults.json output')
                        

    parser.add_argument("-od", "--output_directory",
                        dest='output_directory', help='output directory')

    parser.add_argument("-c", "--config_ms2pip",
                        dest='config_ms2pip', help='config_ms2pip')

    args = parser.parse_args()

    print("Prepare peprec for ms2pip prediction.")
    prepare_peprec(
        search_results_path = args.search_results_path,
        peprec_output_dir = args.output_directory
    ) 
    peprec_file_path = os.path.join(args.output_directory, "search.peprec")
    print(f"Peprec ready: {peprec_file_path}")

