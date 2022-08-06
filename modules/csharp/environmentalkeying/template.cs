string envVar = Environment.GetEnvironmentVariable("{{ key }}");
String xorKey = "{{ xorkey }}";
byte[] xorBytes = Encoding.ASCII.GetBytes(xorKey);
byte[] envVarBytes = Encoding.ASCII.GetBytes(envVar);

string encoded = "{{ encoded }}";
byte[] encoded = Convert.FromBase64String(encoded);
byte[] encoded = { {{ byteArrayInt }} };
byte[] encoded = { {{ byteArrayHex }} };

// CSharp XOR Function
static byte[] xor(byte[] bs, byte[] key)
{
    int keyItr = 0;
    for(int i = 0 ; i < bs.Length ; i++)
    {
        keyItr = i % key.Length;
        bs[i] ^= key[keyItr];
    }

    return bs;
}

byte[] decoded = xor(encoded, xorBytes);
string decodedString = Encoding.ASCII.GetString(decoded);

if(envVar == decodedString) {
    Console.WriteLine( "do cool shit");
}
else {
    Console.WriteLine( "you should exit");
}


