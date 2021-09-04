using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;
using ArrayStrings;

namespace ArrayStrings.Tests
{
    public class StringRotationTests
    {
        [Fact]
        public void EqualString()
        {
            Assert.True(StringRotation.isRotation("abc", "abc"));
        }

        [Fact]
        public void Shift2String()
        {
            Assert.True(StringRotation.isRotation("abc", "cab"));
        }

        [Fact]
        public void NotRotationEqualString()
        {
            Assert.False(StringRotation.isRotation("abc", "cba"));
        }
        [Fact]
        public void SampleFromBook()
        {
            Assert.True(StringRotation.isRotation("waterbottle", "erbottlewat"));
        }
        [Fact]
        public void BothEmpty()
        {
            Assert.True(StringRotation.isRotation("", ""));
        }
        [Fact]
        public void OneNull()
        {
            Assert.False(StringRotation.isRotation(null, "erbottlewat"));
        }
        [Fact]
        public void UnequalLength()
        {
            Assert.False(StringRotation.isRotation("waterbottle", "water bottle"));
        }
    }
}
