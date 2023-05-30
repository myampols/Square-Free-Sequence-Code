#include <iostream>

using namespace std;

const int BASE = 256;
const int MODULUS = 101;

int hashExtend(char c, int prevHash){
  int result = (prevHash * BASE + int(c)) % MODULUS;
  if (result >= 0){
      return result;
  }
  return (result + MODULUS) % MODULUS;
}

int hashShift(char cAdd, char cRem, int prevHash, int power){
  int result = (BASE * (prevHash - (int(cRem) * power)) + int(cAdd)) % MODULUS;
  if (result >= 0){
      return result;
  }
  return (result + MODULUS) % MODULUS;
}


bool squareAtLastCharWithHash(string s){
  int hashLeft = 0;
  int posRight = 0;
  int hashRight = 0;
  int power = 1;
  int len_s = s.length();
  for (int suffixLength = 2; suffixLength < len_s + 1; suffixLength += 2)
  {
    char c = s[len_s - suffixLength / 2];
    hashRight = hashExtend(c, hashRight);
    posRight += 1;
    char cAdd = s[len_s - suffixLength + 1];
    char cExt = s[len_s - suffixLength];
    if (suffixLength == 2){
      hashLeft = hashExtend (cExt, hashLeft);
    }
    else{
      int hashShifted = hashShift(cAdd, c, hashLeft, power);
      hashLeft = hashExtend(cExt, hashShifted);
      power = power * BASE;
    }
    if (hashLeft == hashRight) {
      return true;
    }
  }
  return false;
}

void test (string s){
    if (squareAtLastCharWithHash(s)){
      cout << s << " has square suff" << endl;
  }
  else {
      cout << s << " does not have square suff" << endl;
  }
}


int main()
{
  test("abac");
  test("abaca");
  test("abacc");
  test("abacabac");
  test("abacaba");
  test("abacbac");
  test("abacac");
  return 1;
}
