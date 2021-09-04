using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ArrayStrings
{
    public class StringRotation
    {
        public static bool isRotation(string s1, string s2)
        {
            if (string.IsNullOrEmpty(s1) && string.IsNullOrEmpty(s2))
                return true;
            else if (string.IsNullOrEmpty(s1) || string.IsNullOrEmpty(s2))
                return false;
            else if (s1 == s2)
                return true;
            else if (s1.Length != s2.Length)
                return false;

            if ((s1 + s1).Contains(s2))
                return true;
            else
                return false;
        }
    }
}
