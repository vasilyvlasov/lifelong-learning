__author__ = 'vvlasov'

print '%x' % (int("20814804c1767293b99f1d9cab3bc3e7", 16) ^ int("00000000000000000100000000000000", 16) ^ \
              int("00000000000000000500000000000000", 16))