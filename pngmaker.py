val = "89504e470d0a1a0a0000000d49484452000000630000006301"
converted = bytes.fromhex(val)

import sys
sys.stdout.buffer.write(converted)
