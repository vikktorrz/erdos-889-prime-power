CXX = g++
CXXFLAGS = -std=c++20 -O2 -Wall -Wextra

TARGET = /tmp/erdos-sieve
SOURCE = src/sieve.cpp

.PHONY: all clean run

all:
	$(CXX) $(CXXFLAGS) $(SOURCE) -o $(TARGET)

run:
	$(TARGET) 1000000

clean:
	rm -f $(TARGET)
