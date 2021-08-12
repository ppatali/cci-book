using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;
using ArrayStrings;

namespace ArrayStrings.Tests
{
    public class IsUniqueTests
    {
        [Fact]
        public void NotUnique()
        {
            Assert.False(IsUnique.check("aba"));
        }

        [Fact]
        public void UniqueNoSpaces()
        {
            Assert.True(IsUnique.check("abc"));
        }
        [Fact]
        public void UniqueTwoWords()
        {
            Assert.True(IsUnique.check("hey world"));
        }
        [Fact]
        public void SingleChar()
        {
            Assert.True(IsUnique.check("#"));
        }
        [Fact]
        public void UniqueCaseSensitive()
        {
            Assert.True(IsUnique.check("Check 123!"));
        }
        [Fact]
        public void NotUniqueLongString()
        {
            Assert.False(IsUnique.check("QuickBrownFox"));
        }
    }
}
