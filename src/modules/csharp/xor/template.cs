using System;
using System.IO;
using System.Text;

// Hello World! program
namespace HelloWorld
{
    class Hello {         
        static void Main(string[] args)
        {
            string path = "C:\\Users\\jord\\Desktop\\iexplore.exe";
            byte[] readText = File.ReadAllBytes(path);

            string encodedStr = Convert.ToBase64String(readText);
            byte[] inputStr = Convert.FromBase64String(encodedStr);
            
            System.Console.WriteLine(inputStr == readText);
            for(int i = 0; i < readText.Length; i++) 
            {
                System.Console.WriteLine(i);
                if (inputStr[i] != readText[i])
                {
                    System.Console.WriteLine("ERROR");
                }
            }
        }
    }
}

// CSharp

// CSharp encoded payload base64
string base64encodedPayload = "";

// CSharp decode Base64 to byte array
using System.Text;
byte[] inputStr = Convert.FromBase64String(encodedStr);

// CSharp encoded payload base16
string base16encodedPayload = "";

// CSharp decode base16 to byte array

// CSharp byte array
byte[] arr1 = { 0, 100, 120, 210, 255};

byte[] arr1 = { 0x1, 0x00, 0xFA, 0xFE, 0xFF};

// CSharp XOR Function
