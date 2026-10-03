import unittest
from quantization_lab.records import Record, frontier
from quantization_lab.names import infer_quantization
from quantization_lab.analysis import quality_floor


def rec(quant, memory, load, prompt, tps, score):
    return Record("family", quant, quant, "local", memory, memory, load, prompt, tps, 3, score, 8192)


class Tests(unittest.TestCase):
    def test_quant_name(self):
        self.assertEqual(infer_quantization("model-Q4_K_M.gguf"), "Q4_K_M")

    def test_dominated_row_removed(self):
        a = rec("Q4", 4, 2, 1, 40, .8)
        b = rec("Q5", 5, 3, 2, 30, .7)
        self.assertEqual(frontier([a, b]), [a])

    def test_quality_floor(self):
        rows = [rec("Q4",4,2,1,40,.7), rec("Q8",8,4,2,20,.9)]
        self.assertEqual([x.quant for x in quality_floor(rows, .8)], ["Q8"])


if __name__ == "__main__":
    unittest.main()
