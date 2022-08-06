$envVar = [System.Environment]::GetEnvironmentVariable('{{ key }}')
$xorKey = "{{ xorkey }}"

$encoding = [system.Text.Encoding]::UTF8
$xorBytes = $encoding.GetBytes($xorKey) 
$envVarBytes = $encoding.GetBytes($envVar) 


# PowerShell XOR Function
function xor ($bytes, $xorValue) {

    for($i=0; $i -lt $bytes.Length ; $i++)
    {
        $keyItr = $i % $xorValue.Length;
        $bytes[$i] = $bytes[$i] -bxor $xorValue[$keyItr]
    }

    return $bytes
}

[String]$encoded = "{{ encoded }}"
[byte[]] $encoded = [System.Convert]::FromBase64String($encoded)
[byte[]] $decoded = xor $encoded $xorBytes

$equal = $true

for ($i = 0; $i -lt $decoded.length; $i++) {
  if ($decoded[$i] -ne $envVarBytes[$i] ) {
    $equal = $false
    break
  }
}

if($equal) {
  write-host "do cool shit"
}
else {
  write-host "you should exit"
}