import pandas as pd
import numpy as np


def standardize(x):
    return (x - x.mean()) / x.std()


penguins = pd.read_csv("penguins-raw.csv")


def setup_penguins(penguins):
    # focus on columns of interest
    focus = [
        "Species",
        "Island",
        "Sex",
        "Culmen Length (mm)",
        "Culmen Depth (mm)",
        "Flipper Length (mm)",
        "Body Mass (g)",
    ]
    simplified = penguins[focus]

    # simplify column names
    edited_columns = [
        "species",
        "island",
        "sex",
        "culmen_length",
        "culmen_depth",
        "flipper_length",
        "body_mass",
    ]
    simplified.columns = edited_columns

    # simplify species names
    species = simplified["species"].unique()
    simple_species_dict = {x: x.split(" ")[0].lower() for x in species}
    simplified = simplified.assign(
        species=lambda x: x["species"].map(simple_species_dict)
    )

    # downcase other string factors
    simplified = simplified.assign(island=lambda x: x.island.str.lower())
    simplified = simplified.assign(sex=lambda x: x["sex"].str.lower())

    # create columns with standardized variables for numerics
    simplified = simplified.assign(
        **{i + "_std": (lambda x: standardize(x[i])) for i in simplified.columns[3:]}
    )

    # drop rows with missing values
    simplified.isna().sum()
    simplified = simplified.dropna(axis=0)
    return simplified
