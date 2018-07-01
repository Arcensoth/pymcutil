# pymcutil
[![Master Build Status Badge]](https://travis-ci.org/Arcensoth/pymcutil)
[![Master Code Quality Badge]](https://app.codacy.com/project/Arcensoth/pymcutil/dashboard?branchId=4730158)
[![Master Code Coverage Badge]](https://app.codacy.com/project/Arcensoth/pymcutil/dashboard?branchId=4730158)

[![Dev Build Status Badge]](https://travis-ci.org/Arcensoth/pymcutil)
[![Dev Code Quality Badge]](https://app.codacy.com/project/Arcensoth/pymcutil/dashboard?branchId=4730157)
[![Dev Code Coverage Badge]](https://app.codacy.com/project/Arcensoth/pymcutil/dashboard?branchId=4730157)

An expressive Minecraft utility library revolving around data manipulation and generation.

The goal of this project is to provide a flexible suite of development tools for technical Minecraft players:

- No special syntax, keywords, or anything of the sort. This is just a Python library. You're free to do whatever you'd normally do in Python, importing only the modules you need to import.
- A complete, hierarchical set of [commands](./tests/command) and their subcommands, as well as frequently used [selectors](./tests/selector) and [positions](./tests/position) to go along with them.
- A thorough collection of game object and [data tags (NBT)](./tests/data_tag) representations, for things like [blocks](./tests/block), [items](./tests/item), and [entities](./tests/entity).
- Auto-completion, argument suggestion, and type validation for all representations - especially if you're using a capable IDE like PyCharm. No need to pull up the wiki just to make sure you've got the right NBT tag.
- Data file manipulation and generation, including deep reference searching and automatic dependency resolution.
    - Map several Minecraft functions and parameters to Python methods that spit out a name and a series of commands dependent on the parameters. All involved functions will be searched for dependencies and generated automatically.
    - This goes for any data file in general: loot tables to loot tables, advancements to advancements, advancements to loot tables, advancements to functions, and so on.

## Requirements
* [Python](https://www.python.org/) 3.6+

[Master Build Status Badge]: https://img.shields.io/travis/Arcensoth/pymcutil/master.svg?label=build
[Master Code Quality Badge]: https://img.shields.io/codacy/grade/b038637bf42e45558d2e3418aa10318b/master.svg?label=quality
[Master Code Coverage Badge]: https://img.shields.io/codacy/coverage/b038637bf42e45558d2e3418aa10318b/master.svg?label=coverage
[Dev Build Status Badge]: https://img.shields.io/travis/Arcensoth/pymcutil/dev.svg?label=dev+build
[Dev Code Quality Badge]: https://img.shields.io/codacy/grade/b038637bf42e45558d2e3418aa10318b/dev.svg?label=dev+quality
[Dev Code Coverage Badge]: https://img.shields.io/codacy/coverage/b038637bf42e45558d2e3418aa10318b/dev.svg?label=dev+coverage
