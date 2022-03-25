#  Spectral Library prediction at Mass Dynamics

This repository contains code to convert the Mass Dynamics Peptide Mapping workflow search results into the correct input format required to run [`ms2Pip`](https://github.com/compomics/ms2pip_c#peprec-file)


# Environment setup

```bash
./scripts/prepare.sh
```

# Get predictions using MS2pip and Mass Dynamics search results as input

```bash
python md_spectral_prediction/main.py --search_results_path test_data/searchResult.json --output_directory output_data --config_ms2pip config
```

# Plot predictions

