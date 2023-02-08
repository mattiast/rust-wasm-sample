from wasmer import engine, wat2wasm, Store, Module, Instance, Function, ImportObject
from wasmer_compiler_cranelift import Compiler

store = Store(engine.Universal(Compiler))
module = Module(store, open("juba/suvasmu_bg.wasm", "rb").read())


def thro(x: int, y: int) -> None:
    print("thro", x, y)


throfu = Function(store, thro)
throfu.type.params
io = ImportObject()
io.register("wbg", {"__wbindgen_throw": throfu})
instance = Instance(module, io)

j = instance.exports.luomus()
print(instance.exports.my_add(j))
print(instance.exports.my_add(j))
print(instance.exports.tema(j))
