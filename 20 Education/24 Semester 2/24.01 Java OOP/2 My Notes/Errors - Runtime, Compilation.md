> [!toc] *Table of Contents*
> ```toc

## 1 Compilation Errors

## 2 Runtime Errors

### 2.1 Casting

- ==ALLOWED==: casting a child type to parent type: `Animal a1 = (Animal) cat1`
- ==NOT ALLOWED==: casting a parent type to child type: `Cat c1 = (Cat) animal1`
- ? Why is this not allowed? You would be able to **try to** invocate Cat's methods on an Animal object, or **try to** use Cat's attributes. This is a Runtime error.


