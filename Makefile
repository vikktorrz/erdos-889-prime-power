CXX = g++
CXXFLAGS = -std=c++20 -O2 -Wall -Wextra

TARGET = /tmp/erdos-sieve
SOURCE = src/sieve.cpp

N ?= 1000000

.PHONY: all clean run

all:
	$(CXX) $(CXXFLAGS) $(SOURCE) -o $(TARGET)

run: all
	$(TARGET) $(N)

clean:
	rm -f $(TARGET)