#Ne pas oublier de changer le module à importer
from stat_mediane import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
([1,6,7],6.),\
([1,7,6],6.),\
([1,3,3,6],3.),\
([1,3,4,6],3.5),\
([6,1,4,3],3.5),\
([2622, 7122, 8535, 6288, 4574, 4540, 4683, 4950, 789, 6774, 5310, 7555, 4826, 9453, 1765, 8164, 5939, 1775, 9144, 2742, 3863, 9268, 4055, 6366, 1718, 4444, 3023, 5793, 2689, 1253, 8790, 3268, 7510, 501, 3309, 6251, 6644, 1878, 2881, 9439, 3031, 8250, 424, 1014, 6548, 7754, 1985, 9619, 5588, 4684, 601, 7427, 3745, 2185, 1124, 5213, 7775, 4737, 2628, 5940, 2704, 8067, 5556, 6435, 8952, 5921, 4345, 5537, 4813, 4846, 5985, 5169, 2671, 3092, 3582, 858, 4135, 8700, 4032, 9629, 4474, 5659, 4324, 1643, 9649, 6796, 3557, 6882, 4718, 8258, 6040, 1308, 1973, 4470, 1870, 7902, 6187, 3565, 2440, 8037, 3683, 3227, 5251, 5285, 2740, 9995, 8353, 1594, 4245, 2499, 9739, 2584, 5049, 4895, 3340, 2025, 7678, 6536, 7006, 8545, 5348, 4070, 5704, 3489, 140, 9551, 6947, 2261, 9552, 7977, 3172, 2830, 8631, 5284, 2775, 9741, 2204, 7047, 9282, 3187, 646, 3538, 2251, 4440, 4798, 2942, 1459, 1536, 2417, 5129, 9875, 4116, 9676, 1360, 4425, 5862, 8659, 876, 9075, 5450, 373, 1766, 958, 3058, 944, 8694, 5885, 1949, 4951, 2291, 8148, 9375, 6572, 6621, 8392, 1621, 6604, 4647, 2507, 9455, 9881, 7510, 3421, 1365, 3545, 5238, 4216, 4667, 9218, 8043, 2621, 6233, 8941, 6086, 7568, 7431, 9389, 4238, 7288, 5866, 4369, 8331, 6900, 4305, 6959, 4148, 8287, 8242, 7493, 6814, 1398, 3922, 6012, 6273, 189, 4202, 8632, 6634, 8715, 7624, 103, 3080, 6847, 578, 7058, 7052, 797, 8127, 4126, 7499, 8263, 5875, 9767, 7718, 5337, 260, 1483, 7661, 4688, 4062, 4831, 5819, 604, 4065, 3172, 3855, 2298, 7259, 8320, 3330, 863, 1921, 9172, 6633, 1103, 7720, 717, 4543, 6706, 3665, 4142, 7841, 6775, 950, 1960, 1809, 2118, 9733, 5932, 9972, 8912, 6763, 7781, 6042, 5507, 509, 9376, 241, 111, 7796, 4000, 8085, 2522, 5416, 9403, 3872, 4152, 7059, 842, 1964, 3990, 7239, 7433, 3796, 5993, 2454, 8136, 4012, 7302, 7543, 4503, 9135, 8365, 2644, 1635, 3093, 1710, 9120, 2621, 9257, 100, 7662, 5357, 2679, 6289, 5079, 4919, 6704, 8235, 7616, 3516, 6463, 6139, 3906, 1875, 1703, 2932, 5903, 3739, 1362, 9205, 1990, 3788, 3825, 6256, 4118, 2364, 4206, 4673, 2562, 3870, 5745, 124, 5154, 8477, 6020, 3801, 7430, 8559, 5830, 4825, 4924, 4642, 3962, 1690, 8175, 5409, 2611, 2410, 868, 949, 8647, 6686, 2359, 4874, 5909, 140, 5715, 371, 9406, 3175, 9112, 4733, 5001, 7696, 2137, 1712, 9997, 8206, 8212, 3185, 3706, 1514, 6069, 4271, 832, 5598, 1956, 5081, 8337, 5428, 6854, 2038, 7354, 5213, 4159, 9413, 481, 6418, 979, 1436, 5077, 3739, 9584, 1143, 9270, 7724, 4161, 4225, 8047, 3581, 5351, 918, 7477, 7570, 1393, 1480, 9183, 9842, 856, 7655, 2983, 8190, 6864, 9499, 7656, 5335, 6653, 3804, 9043, 4597, 4246, 5137, 321, 606, 3760, 2535, 7974, 3256, 861, 9933, 2653, 4063, 6270, 6570, 3027, 856, 4302, 1007, 4439, 1015, 8211, 4757, 2844, 3408, 9431, 1062, 5570, 4460, 6489, 2095, 2091, 1926, 9833, 5863, 3980, 1164, 9595, 4987, 606, 4162, 7535, 1630, 8636, 7839, 503, 3047, 5276, 324, 9739, 8701, 849, 5080, 5779, 8685, 2237, 8709, 3286, 9788, 2546, 822, 9362, 236, 5982, 1070, 8254, 1225, 8410, 5194, 2105],4828.5)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(float(count1)) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
