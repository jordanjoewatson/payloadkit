# Base64 encoded payload
$base64EncodedPayload = {{ base64EncodedPayload }}
$base64EncodedXORKey = {{ base64EncodedXORKey }}

# PowerShell decode Base64 to byte array
$shellcode = [System.Convert]::FromBase64String($base64EncodedPayload)

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

# PowerShell byte array
[byte[]] $intArray = {{ intArray }}

[byte[]] $hexArray = {{ hexArray }}


# PowerShell XOR Function
function xor {
    Param(
        [parameter(Mandatory=$true)]
        [Byte[]]
        $byteArray 
    )

    Param(
        [parameter(Mandatory=$true)]
        [Byte[]]
        $xorValue 
    )

    for($i=0; $i -lt $bytes.count ; $i++)
    {
        $keyItr = $i % $xorValue.Length;
        $bytes[$i] = $bytes[$i] -bxor $xorValue[$keyItr]
    }

    return $bytes
}

$xorStringValue = "{{ xorStringValue }}"
$xorIntArray = {{ xorIntArray }}
$xorHexArray = {{ xorHexArray }}

# XOR One liner
# $bytes is a byte array of the payload
# $xorValue is a byte array of the XOR key
for ($i=0; $i -lt $bytes.count ; $i++) {  $keyItr = $i % $xorValue.Length; $bytes[$i] = $bytes[$i] -bxor $xorValue[$keyItr] }