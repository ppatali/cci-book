using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ArrayStrings;
using Xunit;

namespace ArrayStrings.Tests
{
    public class StringCompressionTests
    {
        [Fact]
        public void NoCompression()
        {
            Assert.Equal("abc", StringCompression.compress("abc"));
        }
        [Fact]
        public void NoCompressionWithRepeat()
        {
            Assert.Equal("aabc", StringCompression.compress("aabc"));
        }
        [Fact]
        public void CompressionWithRepeats()
        {
            Assert.Equal("a2b1c5a3", StringCompression.compress("aabcccccaaa"));
        }
    }
}
