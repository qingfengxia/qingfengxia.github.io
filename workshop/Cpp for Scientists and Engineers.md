

### Schedule

Teaching: 60 min

Exercise:  120 min: ​     live coding session   example code provided

### Useful links
+ online poll (quiz)
+ shared document/link to example code/this slide

---

### Aimed audiences and Objectives

For **intermediate programmers with experience of at least one programming language**

Objective:  to improve the performance and robustness of the large scale software.

Part 1: Re-introduction of (modern) C++

+ numeric types in programming languages
+ safer scientific computation

[Part 2  New features since C++11](./modern_cpp_smart_pointers.html)

+ overviews of C++11, C++17 and C++20 features

+ smart pointers of C++11

part 3  design large scale software (yet completed)

- C++ wrapping for Python, or other interpreting languages

Part 4: Pitfalls of C++ (yet completed)

---

# I. Introduction to C++

## what is C++

Object oriented (OO) version of C, "C with [Classes](https://en.wikipedia.org/wiki/Class_(programming))"

A superset of C

but not the only extension of C:  objective-C, D, etc.

---
### then what is C language?
 C is born with Unix OS from Bell lab in early 1970s.

Nowadays, most operation systems (OS) is written in C, Linux kernel, the language to control OS

Many high level language runtime are written in C(Python)/C++(javascript)

Unique: Pointer (address to raw memory space) and full control memory

Power: assembly language can be embedded into C code

---
### C++ features over C
+ object oriented paradigm
+ generic programming by template  `std::vector<int> ints;`
+ `namespace` to avoid name clash
+ functional programming, `std::fuction, lambda`
+ exception (try-catch-finally)
+ RTTI: runtime type information, but not as powerful as Java/C#

---

## why C/C++ (pros)
+ fundamental: operation system, device driver
+ performance: compiling language as Fortran
+ versatile: Object-orientation, template/generalized, functional
+ vast third-party libraries
+ shared feature with C family languages: C#, Java, Objective-C, etc

+ suitable for large scale software design, HPC
e.g. CFD software Ansys Fluent from Fortran to C++
---
### Popularity of C and C++
<img src="./assets/tiobe_lang_rank_2019.png" width=75%>

The combination of C and C++ takes the lead in Tiobe rankings.

---

### C++ standards
+ C++ invented by Bjarne Stroustrup in 1985

+ The firs standard C++ 98,  standard library (STL) was not available

+ C++11 (modern C++) and C++17/C++20 have some exciting/modern features
  - `std::thread`, `std::function`, `lambda`, `std::tuple`, smart pointers, type traits
  - `filesystem`(C++17)

+ some can not wait for a better C++: *rust, go* are invented before C++11 published

  >  we will talk about features of modern C++ in the later sections

---

## why not C++ (Cons)

C++ grammar is too complicate: 

 - too many integer types, java has only unsigned types with fixed ranges
 - pointer, reference
 - confusing keyword `using` and `static`
 - polymorphic only apply to pointer/reference
 - no memory management / garbage collector like Python, Java, C#

Less productive:

+ less featured standard libraries, vs. python, Java, C#, etc
  however, C++ has lib and frameworks like boost, Qt

+ less productivity in regard of coding:
    on average, 50 lines of production code a day
   [The Programmer Productivity Paradox ](https://dzone.com/articles/programmer-productivity)
---

## C++ free course for beginner

[C++ from beginner to advance](C++ Tutorial from Basic to Advance) 9hr youtube course

[free 18 hr course on Udemy](https://www.udemy.com/course/free-learn-c-tutorial-beginners/?LSNPUBID=JVFxdTr9V80&ranEAID=JVFxdTr9V80&ranMID=39197&ranSiteID=JVFxdTr9V80-JvSaBsr8cDbph06Amjp0Hw)

## Try out c++ using  online compilers

There is a list of online compiler to try C++ in webbrowser

<https://arnemertz.github.io/online-compilers/>

Cppinsights: see how compiler do the compiling
<repl.it>: can save user's code snippet, as it is used in this lesseon

---


# II. Safer computation (numeric types)

## How crucial is the research software

space shuttle accidence, image

---

## the jungle of integer types

```cpp
//signed
char
short
int
long
long long
// and with their unsigned version
```
What is the size (in byte, unit of memory capacity) of `int` and `long` do you think?

<a href="https://repl.it/@qingfengxia/printcpptypesize">run example by online compiler</a>

---

### C++'s integer types depends on CPU, OS, even compiler

```cpp
// here we only consider 32 and 64bit OS
void*  // identifed from memory address pointer byte size
//signed and unsigned integer has the same length
char 1 byte
short  2 bytes
int     4 bytes
long   depends on OS, compiler settings
long long  8bytes
```
windows 64 bit, has `long` just 4 bytes, while on Linux 64 bit OS,  it is 8 bytes 

`size_t` returned by `sizeof` operator and  `std::vector.size()`, it is 64 bits on both `uint64_t` on 64 bit windows and Linux system, while 32 bit unsigned integer

---

### why limited size in memory?

In math, a number has unlimited range,  from -inf, to inf

In Python3, `int` type has no limit on integer range.

Why the primitive integer type use only fixed byte size? 

What is the impact (difference of python int and c++ int)?

---

### Numerical computation on CPU

`int a=1; int b=2; int c=a+b;`  

addition `a+b` takes only 1 CPU cycles to complete, if operands fit into register

![Numerical computation on CPU](images/ALU_demo.png)

---

### fixed width integer types in C and C++

**Java and C# has fixed byte size for integer type cross-platform!**

header `<cstdint>` has fixed width integer types,  `uint32_t` `int64_t` 

---

### numeric type in matlab

![Image result for numeric type in matlab](assets/matlab_numeric_types.png)

matlab `a = 1.0`   default to double type,  as C++ python, etc

Julia has the same integer and float pointer numeric types as C

---
### numeric types in other programming languages

note:  some languages does not need to specify type when decleare, but infering the type

`i=1`   i is double type in matlab, `auto i=1;`  in C++

```julia-repl
# 32-bit system:  julia> typeof(1)  Int32
# 64-bit system:  julia> typeof(1)  Int64
```

| language               | C/C++           | Fortran            | Java/C#         | javascript      | Julia         | Python3   | Matlab          |
| ---------------------- | --------------- | ------------------ | --------------- | --------------- | ------------- | --------- | --------------- |
| type                   | int             | integer            | int             | Number          | int           | int       | double          |
| upper and lower limits | -2^31 to 2^31-1 | -2^31 to 2^31-1    | -2^31 to 2^31-1 | -2^53 to 2^53-1 | like C `long` | unlimited | floating  point |
| byte in memory         | 4 depends       | default 4 (KIND=4) | fixed 4         | fixed 8         | 4 or 8        | >=24      | >=8             |

---
### deal with algorithm overflow

<https://www.pluralsight.com/blog/software-development/convert-unsigned-int-to-signed-int>

```cpp
#include <limits>    // for std::numeric_limits
#include <stdexcept> // for std::overflow_error

int SizeToInt(size_t u) {
    if (u > std::numeric_limits<int>::max())     {
        throw std::overflow_error(
            "size_t value cannot be stored in a variable of type int.");
    }
    return static_cast<int>(u);
}
```
actually CPU hardware can detect  the overflow/underflow error, but may be ignored by the programmer, see later section for disccusion

---
### arbitrary precision integer

Python 3 `int` type has arbitrary precision by default,  **no overflow concern!**

| Language | python    | C++         | Fortran | Java         | Julia                                                        | Matlab      |
| -------- | --------- | ----------- | ------- | ------------ | ------------------------------------------------------------ | ----------- |
| type     | int       | NA          |         | `BigInteger` | BigInt                                                       |             |
| support  | version 3 | third-party |         | Java SE 7    | [`Base.GMP`](https://docs.julialang.org/en/v1/base/numbers/#Base.GMP.BigInt) | third-party |
|          |           |             |         |              |                                                              |             |



---

## fixed point decimal

try this in Python`0.1 + 0.1 + 0.1 - 0.3`

equal interval, with the specified the precision.

> -99.99 to 99.99 with a step 0.01(precision)

fixed point decimal can be emulated by integer arithmatics, while it is not efficient to store value with a large range, therefore floating point is widely implemented in CPU.

In C++, it can be achieved by `std::ratio<integer, denominal>` . 

rational number in python , `Fraction(num, denom)`  

>  here `denominal = 100`, if 0.01(precision) is desired.



---



## float point number type 

### decimal (base 10) vs binary (base 2) floating point

+ *decimal* in Python/Java,  precisely map to human counting system, order=10

+ float point, is based on binary system, maybe not precise to represent *decimal*

  

---


![Image result for float point number](assets/Single-Precision-IEEE-754-Floating-Point-Standard.jpg)

![Image result for float point number](assets/FloatingPointNumber.jpg)

 exponent is 8-bit signed integer:   -128~127:     roughly maximum value:  $2^{127}$  or  $1.7 \times 10^{38}$

---

###  decimal (in human sense) type is absent in C/C++

wikipedia: 

python and java has library to support this `decimal` type, used in finance

Third-party C/C++ library

+  https://github.com/vpiotr/decimal_for_cpp  header only, using 8 byte storage for this type

+ **[Boost.Multiprecision](https://www.boost.org/doc/libs/1_66_0/libs/multiprecision/doc/html/index.html)**  gives 50 decimal digits

  ```cpp
  using boost::multiprecision::cpp_dec_float_50;
  cpp_dec_float_50 seventh = cpp_dec_float_50(1) / 7;
  std::cout.precision(std::numeric_limits<cpp_dec_float_50>::digits10);
  std::cout << seventh << std::endl;
  ```

  

---

### float point number types (binary)

<https://en.wikipedia.org/wiki/Double-precision_floating-point_format>,
IEEE754-2008 standard

- 16bit `half` precision, widely used in GPU

- 32bit single precision, `float`, at least 9 significant digits

- 64bit `double` precision, `double` for short in  C/C++

   1~17 significant digits (52 bits), 

   exponent is 11-bit signed integer:   -1023~1023

- 128-bit: Quadruple (binary128), barely any CPU support this natively

- `long double` depends on compiler implementation

  `double`  is a common/default in programming languages (Javascript, Python, Matlab)

---
### Arbitrary decimal float point support
General advice:  

+ use `double `precision (binary64) as possible,  multiplication and addition is fast (single CPU cycle)

* use `decimal` float point, as you choose to use arbitrary precision!

| Language | python       | C++             | Fortran | Java         | Julia    | Matlab          |
| -------- | ------------ | --------------- | ------- | ------------ | -------- | --------------- |
| type     | int          | NA              |         | `BigDecimal` | BigFloat | HPF             |
| support  | standard lib | third-party lib |         | Java SE 7    | built-in | third-party lib |
|          | primitive    |                 |         | Immutable    |          |                 |

---

## Implicit conversion (1) C language features
### dangerous integer type implicit conversion

It is crucial to know the types of your programming languages!

```cpp
void std_container_index_test(){
    std::vector<int> v;
    int index= 10;
    if (index < v.size()-1) // there is a compiler warning here
        std::cout << v[index];
}
```

<a href="https://repl.it/@qingfengxia/stdcontainerindextest"> run examle by online compiler</a>

---
### algorithmic promotion

+ safe from smaller type (smaller in byte size, range) to bigger type
   from `char -> short -> int ->long -> long long`
   from `unsigned int -> signed long long`

+ from `half->float->double->long double`

+ same width: `signed int -> unsigned int`, it is potentially dangerous!

   see example code in later section

+ `enum` is `int` if the underlying type is not explicitly specified

   see more details: <https://en.cppreference.com/w/cpp/language/implicit_conversion#Integral_promotion>

---
### numerical conversion
+ if there is no rule for promotion, it is an conversion
   -  e.g. floating–integral conversions
   - The programmer need to care about out of range, loss of precision

+ mixing of signed and unsigned integer of size byte size

  from `signed int -> unsigned long long`

```cpp
      int n = -1;
      unsigned int u = 1;
      std::cout << "Comparing signed and unsigned:\n"
                << " -1  < 1? " << (n < u) << '\n'
                << " -1  > 1? " << (n > u) << '\n';
```

  see example <https://en.cppreference.com/w/cpp/language/operator_comparison>



---
# III. Safer computation (third-party library)

## multiprecision integer and float points

to avoid overflow error

+ `boost::multiprecision`

 

---

## numerical type with safe range

### boost::Safe<integer_type>

https://www.boost.org/doc/libs/1_71_0/libs/safe_numerics/doc/html/tutorial/1.html

The type supports both infinities and NaN's. An infinity is generated whenever the result would overflow, and a NaN is generated for any mathematically undefined operation.



### safe range  

banking, int64 is sufficient

`safe_signed_range<-11, 11>`

---



Those special extended types use much more CPU cycles to complete, which is not accepted in large scale matrix operation. Insread, the most comptuation efficient hardware supported type, `double` will be used with careful consideration/design of **float point exception**

---

# IV. Safer computation (exception)

## Exception safety

4 levels of exception safety

+ ideal: no failure
+ strong: failure but rollback to previous condition, think about online banking transaction
+ basic: failure without resource leakage, important for server process
+ none: no guarantee, left program in a deterministic condition

There books/guidelines on write exception safety C++ code,

[C++ core guideline on exception](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#S-errors)



---

### some guideline from [SEI CERT C++ Coding Standard](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88046682)

[ERR54-CPP. Catch handlers should order their parameter types from most derived to least derived](https://wiki.sei.cmu.edu/confluence/display/cplusplus/ERR54-CPP.+Catch+handlers+should+order+their+parameter+types+from+most+derived+to+least+derived)

do you know why?

---
### exception change in C++11 and C++17

C++98:  defined a few standard exceptions in `<stdexception>` use then instead of throw int or string

  they are all derived from `std::exception` so it is easier to catch all derived exceptions

  https://en.cppreference.com/w/cpp/error/exception

C++11:  `current_exception` pointer, `nested_exception`

c++17:   exception specification changed,

 ` f() noexception(false)` instead of  `f() throw(std::logical_error)`

---
## exception/error in math computation

### integer underflow/overflow

- CPU set status register, which may be checked by C and C++

- C lib: `errno` set and clear by library function

  <https://www.gnu.org/software/libc/manual/html_node/Errors-in-Math-Functions.html>

  <https://en.cppreference.com/w/c/error/errno>

- C++ way to detect under/overflow

Note: know and detect your integer range in runtime

C has `LONG_MAX` macro, c++ has more general one `std::limits<long>::max()`

---

### float point exception and special values

Divied by zero (float point types)might be blocked by compiler at compiling time.

NaN,  +Inf, -Inf

```c
    printf("sqrt(-1) = %f\n", sqrt(-1));
    printf("DBL_MAX*2.0 = %f\n", DBL_MAX*2.0);
    printf("DBL_MAX*-2.0 = %f\n", DBL_MAX*-2.0);
```

those 3 special values operates with a valid number resulting in those special values

---

### setup float point exception check in C++

This is a C99 feature in header  `<cfenv>`

```cpp
    if(fetestexcept(FE_DIVBYZERO)) printf(" FE_DIVBYZERO");
    if(fetestexcept(FE_INEXACT))   printf(" FE_INEXACT");
    if(fetestexcept(FE_INVALID))   printf(" FE_INVALID");
    if(fetestexcept(FE_OVERFLOW))  printf(" FE_OVERFLOW");
    if(fetestexcept(FE_UNDERFLOW)) printf(" FE_UNDERFLOW");
    feclearexcept(FE_ALL_EXCEPT);
```

<https://en.cppreference.com/w/c/numeric/fenv/FE_exceptions>



---



## diagnostics tools to improve code safety

+ [Clang Power Tools](https://marketplace.visualstudio.com/items?itemName=vs-publisher-690586.ClangPowerTools), turn on compiler's all warning switches
+ cppchecker, lint, some other linting/checker tools
+ [SEI CERT C++ Coding Standard](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88046682), online reading

+ C++ Core guidelines checker (a plugin of visual studio)
+ etc.

