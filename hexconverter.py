import argparse
parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')
parser.add_argument('-i', '--input', help='Input file name', required=True)
parser.add_argument('-o', '--output', help='Output file name', required=True)
args = parser.parse_args()
ifile = args.input
ofile = args.output

with open(ifile, "rb") as f:
	with open(ofile, "wb") as g:
		byte = f.read(1)
		while byte:
			b = int.from_bytes(byte, byteorder='big')
			firstNib = b >> 4;
			truncNib = firstNib << 4;
			outByte = firstNib | truncNib;
			outByte = outByte.to_bytes(1, byteorder='big')
			g.write(outByte)
			byte = f.read(1)
	g.close()
f.close()
