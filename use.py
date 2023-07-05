from wasmer import engine, Store, Module, Instance, Function, ImportObject
from wasmer_compiler_cranelift import Compiler
import os

store = Store(engine.Universal(Compiler))
module = Module(store, open(os.environ["WASM_MODULE_PATH"], "rb").read())


def thro(x: int, y: int) -> None:
    print("thro", x, y)


throfu = Function(store, thro)
throfu.type.params
io = ImportObject()
io.register("./suvasmu_bg.js", {"__wbindgen_throw": throfu})
instance = Instance(module, io)

j = instance.exports.new_jutska()
print(instance.exports.my_add(j))
print(instance.exports.my_add(j))
print(instance.exports.eat_jutska(j))
