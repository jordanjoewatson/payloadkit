
$bytes = [System.IO.File]::ReadAllBytes("C:\\Users\\jord\\Desktop\\iexplore.exe")
$bytes2 = [System.Byte[]]::CreateInstance([System.Byte], $bytes.count)



for($i=0; $i -lt $bytes.count ; $i++)
{
    $bytes2[$i] = $bytes[$i] -bxor 0x6A
}

echo $bytes[-1]
echo $bytes2[-1]
$b = [bool]($bytes -eq $bytes2)
echo $b


for($i=0; $i -lt $bytes.count ; $i++)
{
    $bytes2[$i] = $bytes2[$i] -bxor 0x6A
}

$c = [bool]($bytes -eq $bytes2)
echo $c

echo $bytes[-1]
echo $bytes2[-1]

echo $bytes.count

echo $bytes2.count 

for($i=0; $i -lt $bytes.count ; $i++)
{
    if ( $bytes[$i] -ne $bytes2[$i] )
    {
        Write-Output "Error"
    }
}


$EncodedText =[Convert]::ToBase64String($Bytes)
$EncodedText

# actual working stuff to submit from here, above is just test code

# PowerShell encoded payload base64

# PowerShell decode Base64 to byte array
[System.Convert]::FromBase64String("U29tZSBEYXRh")
[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($EncodedText))

# PowerShell encoded payload base16

# PowerShelk decode base16 to byte array

# PowerShell byte array
[byte[]] $byte_array = 65,66,67,90

[byte[]] $another_array = 0x41, 0x42, 0x43, 0x5A


# PowerShell XOR Function
function xor {
    Param(
        [parameter(Mandatory=$true)]
        [Byte[]]
        $byteArray 
    )

    Param(
        [parameter(Mandatory=$true)]
        [Byte]
        $xorValue 
    )

    for($i=0; $i -lt $bytes.count ; $i++)
    {
        $bytes[$i] = $bytes[$i] -bxor $xorValue 
    }

    return $bytes
}
