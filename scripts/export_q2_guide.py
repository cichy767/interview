"""Build only the Q2 AWS data platform scenario guide and its review previews."""

from export_q2_materials import export_guides


if __name__ == "__main__":
    export_guides(include_general=False)
