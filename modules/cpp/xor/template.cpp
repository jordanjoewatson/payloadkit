#include <iostream>
#include <windows.h>
#include <iostream>

// DATA
unsigned char intArray[] = {{ intArray }};

unsigned char hexArray[] = {{ hexArray }};

unsigned char hexString[] = {{ hexString }}

void _xor(unsigned char* bytes, unsigned char* xorKey, int byteCount)
{
    int xorKeyCount = *(&xorKey + 1) - xorKey;
	xorKeyCount = {{ xorKeySize }};
    for (int i = 0 ; i < byteCount ; i++)
    {
        int keyItr = i % xorKeyCount;
        *bytes ^= xorKey[keyItr];
        bytes++;
    }
    return;
}

unsigned char* cptr;
cptr = intArray;
unsigned char key[] = {{ xorKeyHex }}
_xor(cptr, key, {{ xorKeySize }});
