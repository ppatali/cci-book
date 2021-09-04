using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ArrayStrings
{
    public class StringCompression
    {
        public static string compress(string str)
        {
            if (string.IsNullOrEmpty(str))
                return str;

            int repeatCount = 0;
            StringBuilder compressedStr = new StringBuilder(str.Length);

            for (int i = 0; i < str.Length; i++)
            {
                repeatCount++;
                if ((i + 1) == str.Length || str[i] != str[i+1])
                {
                    compressedStr.Append(str[i]).Append(repeatCount);
                    repeatCount = 0;
                }
            }

            if (str.Length <= compressedStr.Length)
                return str;
            else
                return compressedStr.ToString();
        }
    }
}
