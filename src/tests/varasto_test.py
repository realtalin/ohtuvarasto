import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_negatiivinen = Varasto(-1, -1)
        self.varasto_liian_iso_alku_saldo = Varasto(10, 20)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.varasto_negatiivinen.tilavuus, 0.0)
    
    def test_uudella_varastolla_negatiivinen_alku_saldo(self):
        self.assertAlmostEqual(self.varasto_negatiivinen.saldo, 0.0)

    def test_liian_iso_alku_saldo(self):
        self.assertAlmostEqual(self.varasto_liian_iso_alku_saldo.saldo, 10)

    def test_negatiivisen_maaran_lisaaminen(self):
        self.varasto.lisaa_varastoon(-1)
        
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisaaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_maaran_ottaminen(self):
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_ottaminen_yli_saldon(self):
        saatu_maara = self.varasto.ota_varastosta(1)
        
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_varaston_tulostaminen(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")