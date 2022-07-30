Dim intArray As Variant
intArray = Array({{ intArray }})

Dim hexArray As Variant
hexArray = Array({{ hexArray }})

' ENCODED BASE64 PAYLOAD
Dim encodedShellcode As String 
encodedShellcode = {{ base64EncodedPayload }}

' ENCODED BASE16 PAYLOAD
Dim encodedShellcode As String 
encodedShellcode = {{ base16EncodedPayload }}

' EVERYTHING AFTER HERE IS GARBAGE

# opentechtips.com/base64-encoder-and-decoder-algorithm-from-scratch-in-python
Function base64Decode(String s) As Dim()
    if s[-2:] == "==":
        s = s[0:-2] + "AA"
        padding = 2
    elif s[-1:] == "=":
        s = s[0:-1] + "A"
        padding = 1
    else:
        padding = 0

    while i = 0 < len(s):
        d = 0
        for j in range(0,4,1):
            d += base64chars.index(s[i]) << (18 - j * 6)
            i += 1

        decoded += chr (d >> 16) & 255

        decoded += chr (d >> 8) & 255

        decoded += chr (d & 255)

    decoded = decoded[0:len(decoded) - padding]

    print(decoded)
End Function 



Function xor(Dim() bytes, Dim() xorKey) As Dim()
    Dim byteCount As Int
    byteCount = UBound(bytes) - LBound(bytes) + 1
    Dim xorKeyCount;
    xorKeyCount = UBound(bytes) - LBound(bytes) + 1
    Dim keyItr as Int 
    
    For i = 1 To byteCount
        keyItr = i % xorKeyCount;
        bytes(i) = bytes(i) Xor xorKey(keyItr)
    Next i

    xor = bytes
End Function

Dim bytes() as Byte 

' TODO
' 1. Base64 decryption function
' 2. Base16 decryption function
' 3. Test Int, Hex, Base64, Base16