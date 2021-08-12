using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ArrayStrings
{
    public class IsUnique
    {
        public static bool check(string s)
        {
            //Assumption: 
            //1. string only contains ASCII chars in total 128

            if (string.IsNullOrEmpty(s)) return true;
            if (s.Length > 128) return false;
            
            const int TOTAL_UNIQUE_CHARS = 128;
            bool[] charCounts = new bool[TOTAL_UNIQUE_CHARS];
            foreach(char c in s)
            {
                if (charCounts[c])
                    return false;
                else
                    charCounts[c] = true;
            }

            return true;
        }
    }
}
