"""
Module containing data structures and constants for materials science.

This module defines the core data structures used throughout the Materials Science Constraint Solver,
including CrystalLattice, Alloy, and Property. It also includes a set of predefined constants.
"""

class CrystalLattice:
    """
    Represents a crystal lattice with its properties.

    Attributes:
        name (str): The name of the lattice.
        dimensions (int): The number of dimensions in the lattice.
        symmetry_group (str): The symmetry group of the lattice.
    """

    def __init__(self, name: str, dimensions: int, symmetry_group: str):
        """
        Initializes a CrystalLattice instance.

        Args:
            name (str): The name of the lattice.
            dimensions (int): The number of dimensions in the lattice.
            symmetry_group (str): The symmetry group of the lattice.
        """
        self.name = name
        self.dimensions = dimensions
        self.symmetry_group = symmetry_group

    def __repr__(self) -> str:
        return f"CrystalLattice(name='{self.name}', dimensions={self.dimensions}, symmetry_group='{self.symmetry_group}')"


class Alloy:
    """
    Represents an alloy with its properties.

    Attributes:
        name (str): The name of the alloy.
        crystal_lattices (list[CrystalLattice]): A list of CrystalLattice instances that make up the alloy.
    """

    def __init__(self, name: str, crystal_lattices: list):
        """
        Initializes an Alloy instance.

        Args:
            name (str): The name of the alloy.
            crystal_lattices (list[CrystalLattice]): A list of CrystalLattice instances that make up the alloy.
        """
        self.name = name
        self.crystal_lattices = crystal_lattices

    def __repr__(self) -> str:
        return f"Alloy(name='{self.name}', crystal_lattices={self.crystal_lattices})"


class Property:
    """
    Represents a property of the material.

    Attributes:
        name (str): The name of the property.
        value (float): The value of the property.
    """

    def __init__(self, name: str, value: float):
        """
        Initializes a Property instance.

        Args:
            name (str): The name of the property.
            value (float): The value of the property.
        """
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"Property(name='{self.name}', value={self.value})"


# Predefined constants
LATTICE_CONSTANTS = {
    "diamond": {"dimensions": 3, "symmetry_group": "T_d"},
    "face-centered-cubic": {"dimensions": 3, "symmetry_group": "O_h"},
    # Add more lattice types as needed
}

PROPERTY_TYPES = ["density", "melting_point", "hardness"]  # Add more property types as needed

# Example usage:
lattice = CrystalLattice("diamond", **LATTICE_CONSTANTS["diamond"])
alloy = Alloy("steel", [lattice])
property1 = Property("density", 7.9)
print(lattice)  # Output: CrystalLattice(name='diamond', dimensions=3, symmetry_group='T_d')
print(alloy)    # Output: Alloy(name='steel', crystal_lattices=[CrystalLattice(name='diamond', dimensions=3, symmetry_group='T_d')])
print(property1)  # Output: Property(name='density', value=7.9)
