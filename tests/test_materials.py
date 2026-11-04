import unittest
from materials_science_solver import materials

class TestMaterials(unittest.TestCase):

    def test_CrystalLattice_init(self):
        lattice = materials.CrystalLattice("diamond", dimensions=3, symmetry_group="T_d")
        self.assertEqual(lattice.name, "diamond")
        self.assertEqual(lattice.dimensions, 3)
        self.assertEqual(lattice.symmetry_group, "T_d")

    def test_CrystalLattice_repr(self):
        lattice = materials.CrystalLattice("diamond", dimensions=3, symmetry_group="T_d")
        self.assertEqual(repr(lattice), "CrystalLattice(name='diamond', dimensions=3, symmetry_group='T_d')")

    def test_Alloy_init(self):
        lattice = materials.CrystalLattice("diamond", dimensions=3, symmetry_group="T_d")
        alloy = materials.Alloy("steel", [lattice])
        self.assertEqual(alloy.name, "steel")
        self.assertEqual(len(alloy.crystal_lattices), 1)
        self.assertEqual(alloy.crystal_lattices[0].name, "diamond")

    def test_Alloy_repr(self):
        lattice = materials.CrystalLattice("diamond", dimensions=3, symmetry_group="T_d")
        alloy = materials.Alloy("steel", [lattice])
        self.assertEqual(repr(alloy), "Alloy(name='steel', crystal_lattices=[CrystalLattice(name='diamond', dimensions=3, symmetry_group='T_d')])")

    def test_Property_init(self):
        property1 = materials.Property("density", 7.9)
        self.assertEqual(property1.name, "density")
        self.assertEqual(property1.value, 7.9)

    def test_Property_repr(self):
        property1 = materials.Property("density", 7.9)
        self.assertEqual(repr(property1), "Property(name='density', value=7.9)")

if __name__ == "__main__":
    unittest.main()
