// CSharp encoded payload base64
string base64EncodedPayload = {{ base64EncodedPayload }};




// CSharp decode Base64 to byte array
using System.Text;
byte[] shellcode = Convert.FromBase64String(base64EncodedPayload);




// CSharp encoded payload base16
string base16EncodedPayload = {{ base16EncodedPayload }};




// CSharp decode base16 to byte array
using System.Globalization;
static byte[] base16ToByteArray(string base16String)
{
    byte[] shellcode = new byte[base16String.Length / 2];
    for (int index = 0; index < shellcode.Length; index++)
    {
        string byteValue = base16String.Substring(index * 2, 2);
        shellcode[index] = byte.Parse(byteValue, NumberStyles.HexNumber, CultureInfo.InvariantCulture);
    }

    return shellcode;
}

byte[] shellcode = base16ToByteArray(base16EncodedPayload);




// CSharp byte array
byte[] byteArrayInt = { {{ byteArrayInt }} };

byte[] byteArrayHex = { {{ byteArrayHex }} };




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


byte[] byteKey = Encoding.ASCII.GetBytes({{ key }});
byte[] shellcode = xor(encodedByteArray, byteKey);
