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
