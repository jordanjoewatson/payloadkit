#include <iostream>
#include <windows.h>
#include <iostream>

// DATA
unsigned char intArray[] = {{ intArray }};

unsigned char hexArray[] = {{ hexArray }};

unsigned char hexString[] = {{ hexString }}

void rot13(unsigned char* bytes, int byteCount)
{
    for (int i = 0 ; i < byteCount ; i++)
    {
        *bytes = (*bytes - 13) % 256;
        bytes++;
    }
    return;
}

unsigned char* cptr;
cptr = intArray;
rot13(cptr, {{ payloadSize }});
