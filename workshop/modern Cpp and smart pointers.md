Modern C++ feature

## new features in C++11

C++11 (modern C++) and C++17/C++20 have some exciting/modern features

- `std::thread`,  `std::atomic<>` `std::mutex, std::future` portable multi-threading 

-  `std::function`, `lambda`
-  Rvalue reference `T&&` value appears at the right of an assign statement.`std::move` semantics

- `std::tuple`,  read only container with different types, just as in Python

  `auto t = std::make_tuple("name", 1999, 320.12, false);`
  can be used to pack and pass multiple parameters to functions, a light-weight data class

- type safe `enum class E`,  prevent implicit conversion from enum value to integer

- smart pointers, `nulltpr`(type safe version of NULL in C language) 

- type traits,  compiling time type operation in template programming

----
### new features in C++11 (continued)
- auto `auto got = myset.find (input);` like javascript `var v=...`, instead of
`std::unordered_set<std::string>::const_iterator got = myset.find (input);`
- `unordered_set, unordered_multiset, unordered_map, unordered_multimap`
- standardised *Attribute*  `[[ noreturn ]] void f() {};`
- `std::array<int, 10>` instead of `int[10]` to behave STL container `std::vector`
- range based for `for(const auto& v: vector) {}`    like Python `for v in vector`
- regular expression, random number generation, time and date standard libraries

---
### new features in C++11 (continued)
- new keywords: `override`, `final`, just like Java and C#
- `default` and `delete`
`Constructor()=default;  // use the compiler generated default constructor` 

```cpp
   pure_virtual_function() = delete;  
   // instead weird  `pure_virtual_function()=0;`
   // can also delete copy constructor
  A(const A&) = delete;
  A& operator=(const A&) = delete;
```

---

- `explicit` to prevent implicit 
```cpp
    struct B {
      explicit operator bool() const { return true; }
    };

    B b;
    if (b); // OK calls B::operator bool()
    bool bb = b; // error, compiler will not consider B::operator 
```

---

### New features in C++17

- C++14 is a minor update/bugfix to C++11
- `filesystem`(C++17), finally a cross-platform implementation
    based on boost filesystem, it is available for system without C++17 compiler
- `std::optional`:   a value that may or may not be present

- `std::string_view`:  read-only non-owning reference to string types, python slicing
- `std::byte`:  a new type support only bitwise operation, instead of `unsigned char`
   for safer embedded programming, to deal with control and status registgers

- Structured bindings: 

  `const auto& [name, year] = std::make_tuple("John", 1999);`
---


### `std::any`  to hold single value of any type
Previously,  type erased data can only be saved as `void*`  with type info lost

It is also based on boost library,  now in C++ standard header `<utility>`

  ```cpp
  std::any x = 1;  // int type auto deducted
  x.has_value() // == true
  assert(typeid(int) == x.type());  // type() return const type_info&
  std::any_cast<int>(x) // == 1
  double d = std::any_cast<int>(x); // get int value and assign to double
  double d = std::any_cast<double>(x);  // runtime error: bad_any_cast
  
  std::any_cast<int&>(x) = 10; // reference extracted, but not pointer
  std::any_cast<int>(x) // == 10
  ```

A modifiable type-safe container holding any different type can be implemented.

---

### `std::variant` a type safe  C `union`

Different from `std::any` , `std::variant` has only limited predefined types

```cpp
  std::variant<int, std::string, double> v {12};
  std::get<int>(v); // == 12
  v="12";  // std::get<std::string>(v)  
```

see more examples

https://github.com/AnthonyCalandra/modern-cpp-features

---

### New features in C++20

+ deprecate raw pointer, `volatile`, `regsiter`

+ `import module A` instead of/as well as header `#include <A>`

+ `concept`, see <https://en.cppreference.com/w/cpp/header/concepts>

+ coroutines,    `co_wait`,`co_return`, `co_yield`        related to   `async` in python, JavaScript, C#

+ better support of `cosntexpr` in `numeric`, `std::string, std::vector`

  


---

+ cross-platform `<bit>` operation and `endian` support
+ `<ranges>`  ,`std::span` 

+ `std::source_location`  insread of C macro `__FILE__` and `__LINE__`
+ `std::format()` think about Python format,  `printf()`

not released yet, but feature complete in July 2019

 see wiki <https://en.wikipedia.org/wiki/C%2B%2B20>



---

### Beyond C++20

Some features/proposal/TS has been postponed to the next release

contracts

networking 

meta class

reflection

---

### feature detection macros

`<version>` header in C++20, to detect whether a feature is available in this compiler

```cpp
#if __cpp_coroutines
	// do something with coroutine featrue
#endif
```

A version number macro has been available even before C++11

```
#if __cplusplus < 201402L
/// make `make_unique()` in C++14 available for C++11
/// solution from <https://stackoverflow.com/questions/17902405/how-to-implement-make-unique-function-in-c11>
#endif
```

---

### C++17  `__has_include()`

```cpp
#if __has_include(<filesystem>)
	#  include <filesystem>
	#  define have_filesystem 1
	namespace fs = std::filesystem;
#elif __has_include(<experimental/filesystem>)
	#  include <experimental/filesystem>
	#  define have_filesystem 1
	namespace fs = std::experimental::filesystem;
#elif __has_include(<boost/filesystem.hpp>)
	#  include <boost/filesystem.hpp>
	#  define have_filesystem 1
	namespace fs = boost::filesystem;
#else
	#  define have_filesystem 0
#endif
```



---

## Smart pointers of C++11

**Benefits**

- no need to use `new` and `delete`, the latter one is easily forgotten.

  Creating raw pointer by`new` will be deprecated in C++20

- safely passing data around

  return from function, and passed as parameter into another function

- exception safety: avoid memory leakage, even in exceptional code path

  what happen after exception happen?  delete object held in this scope before exit  this scope
  
- thread-safe, type `std::atomic_share_ptr<>` is introduced in C++20

---

### new smart pointer types

- `unique_ptr`: high performance as quick as raw pointer, 

`release()` will give up the responsibility of delete object.

- `shared_ptr`: if passed as parameter into and return out of functions.

  ---

- `scoped_ptr`: If used in local function, avoid memory and resource leakage if exception is called

- `weak_ptr`:  its lock() method essentially upgrades the `weak_ptr` to a `shared_ptr`

- `atomic_shared_ptr,  atomic_weak_ptr`, are introduced in C++20 to assist thread safety

> do remember to include the header file `<memory>` otherwise error
>
> `std::shared_ptr<>` 



### avoid pointer/reference by `shared_ptr`

+ To avoid copy for performance reason, share editable data.

+ Java, Python objects  (but not primitive type like integer) are passed by reference (in effect)

  + internally, objects has reference counting

+ Reference in c++ is a syntax sugar for pointer
  + slightly safer, which must be initialized and not NULL. 
  + If the referred object is deleted, use the reference cause runtime error!
  
  `shared_ptr`
  
  - implemented by reference counting, an well-established pattern
  - safe to use in multi-thread parallel programming (`std::atomic_share_ptr` of C++20)

---

### pass and return `shared_ptr` from function

`const shared_ptr<Const T>&` instead of `const T&`, `const T*` for read only input parameter

> here the reference of `shared_ptr<Const T>` to avoid copy, although the cost is small

`shared_ptr<T>`,  instead of  `T&`, ``T*`  for if data will be modified, 

In asyn programming, the reference may point to destroyed memory, leading to access violation. 



return value will be automatically optimized by compiler. move semantics

`return make_shared(T);`  the T obj is new/created from heap, which will survive after the function returned. 

---

### keep only one copy of data by `unique_ptr`

https://www.modernescpp.com/index.php/c-core-guidelines-passing-smart-pointer

(c) Passing `unique_ptr` by value means “sink.”

```cpp
auto p=std::make_unique<T>();
f(p);  //  `f(std::make_unique<T> p)` consuming the unique pointer
// now p is empty, the pointed object T has been released after return from f(p)
```

(d) Passing `unique_ptr` by reference is for in/out `unique_ptr` parameters.

---

### Return only value type of smart pointers

Starting from C++17, compiler will do **Return Value Optimization (RVO)** , even the tiny cost of copying smart pointer itself will be optimized out;

returning `std::shared_ptr` by reference doesn't properly increment the reference count, which opens up the risk of deleting something at the wrong time.

returning a `unique_ptr<>` can be proper, compiler will use move semantic to give the memory management to the caller `unique_ptr<T> p = create_obj();`

<https://www.internalpointers.com/post/move-smart-pointers-and-out-functions-modern-c>

---

#### pass shared smart pointers as function parameter

```
### passed by raw pointer is fine, but should be avoided 
You should never do fancy tricks with pointers and references you get() from smart pointers: don't delete them, don't create new smart pointers out of them, or more generally: don't mess with their ownership. Whenever a function returns a raw pointer/reference or take it as parameter, you should consider it as owned by someone else, somewhere else in the code base. You can definitely operate on it but the ownership still belongs to the smart pointer that originally returned the raw pointer/reference to its dynamically-allocated resource.

### pass by value for shared_ptr, pass by value for unique_ptr is not possible
### pass by reference to manipulate the ownership

Pass *by reference* when the function is supposed to modify the ownership of *existing* smart pointers. More specifically:

- pass a non-`const` reference to `std::unique_ptr` if the function might modify it, e.g. delete it, make it refer to a different object and so on. Don't pass it as `const` as the function can't do anything with it: see (6) and (7) instead;
- the same applies to `std::shared_ptr`, but you can pass a `const`  reference if the function will only read from it (e.g. get the number  of references) or it will make a local copy out of it and share  ownership;
- I didn't find a real use case for passing `std::weak_ptr` by reference so far. Suggestions are welcome :)
```

https://www.internalpointers.com/post/move-smart-pointers-and-out-functions-modern-c

### be careful to common errors using smart pointers

<https://www.acodersjourney.com/top-10-dumb-mistakes-avoid-c-11-smart-pointers/>

Mistake # 6 : Deleting the raw pointer used by the `shared_ptr` !  ACCESS_VILOTATION

**Advice**

   do not mix raw and smark pointer,  create object by `std::make_shared<T>()` 

Recommendation: If you’re not using make_shared to create the shared_ptr , at least create the object managed > by the smart pointer in the same line of code – like :  ` shared_ptr<T>(new T())`



Extending [std::make_shared()](https://en.cppreference.com/w/cpp/memory/shared_ptr/make_shared) to support arrays in C++20

---

#### `make_shared(T)` or `shared_ptr<T>(new T())`

[std::make_unique](https://github.com/AnthonyCalandra/modern-cpp-features#stdmake_unique)  is the recommended way to create instances of `std::unique_ptr`s due to the following reasons:

- Avoid having to use the `new` operator and code prepetitoin, and merge two memory allocation. Momery allocation is costly in computation time, so merge the tiny memory usage (3 poiters size) with the target object can make 
- Most importantly, it provides exception-safety. Suppose we were calling a function `foo` like so:

```cpp
foo(std::unique_ptr<T>{new T{}}, function_that_throws(), std::unique_ptr<T>{new T{}});
```

---

### thread safety of smart pointers

`shared_ptr<T>` by no chance provide threading safety on the resource (T object). Even the *reference count* ++/--is NOT thread-safe, if `ref` is not atomic operation. 

`atomic_shared_ptr`,  `atomic_weak_ptr` are introduced in C++20

#### STL iterator is pointer `typedef`

 may be invalidated during insertion

---


