import binsearch as bsearch
import unittest
import random


class KnownValues(unittest.TestCase):
    knownValues = (((10, 20, 30), 20), 1),
    (((10, 20, 30), 30), 2),
    (((10, 20, 30), 5), None),
    (((10, 30, 50, 60, 70), 50), 2),
    (((10, 20, 30, 40, 70, 80), 80), 5),
    (((10, 20, 30, 50, 60, 90), 30), 2),
    (((10, 30, 50, 80, 90), 30), 1),
    (((10, 40, 50, 60, 70, 80, 90, 100), 100), 7),
    (((20, 30, 40, 60, 70), 20), 0),
    (((30, 40, 50, 60), 5), None),
    (((10, 20, 30, 30, 30), 30), 2),
    (((10, 20, 30, 30, 30, 30), 30), 2),
    (((20, 20, 20, 20), 20), 1),
    (((20, 20, 20, 20, 20, 20), 20), 2),
    (((10, 20, 30, 40, 50, 50, 60), 30), 2)

    def testBinKnownValue(self):
        """binarysearch should give known result with known input"""
        for v, idx in self.knownValues:
            result = bsearch.binsearch(list(v[0]), v[1])
            if idx is None:
                self.assertEqual(idx, result)
            else:
                self.assertEqual(v[0][idx], v[0][result])


class SanityCheck(unittest.TestCase):
    def testIInNLength(self):
        l = []
        for i in range(10, 11, 1):
            dataList = [j for j in range(i-10, i)]
            idx = random.randint(0, 9)
            value = dataList[idx]
            l.append(((dataList, dataList[idx]), idx))
        i = bsearch.binsearch(dataList, value)
        self.assertLessEqual(i, len(dataList))

    def testvalueEqualKey(self):
        l = []
        for i in range(10, 11, 1):
            dataList = [j for j in range(i-10, i)]
            idx = random.randint(0, 9)
            value = dataList[idx]
            l.append(((dataList, dataList[idx]), idx))
            i = bsearch.binsearch(dataList, value)
            self.assertEqual(value, dataList[idx])

    def testreturnNone(self):
        l = []
        for i in range(10, 11, 1):
            dataList = [j for j in range(i-10, i)]
            idx = random.randint(0, 9)
            value = dataList[idx]
            l.append(((dataList, dataList[idx]), idx))
            i = bsearch.binsearch(dataList, value)
            if i == "None":
                self.assertGreater(i, len(dataList))


class FailureCheck(unittest.TestCase):
    def testFailure(self):
        self.assertRaises(bsearch.InvalidArgument,
                          bsearch.binsearch, "InvalidArgument", 2)


if __name__ == "__main__":
    unittest.main()
