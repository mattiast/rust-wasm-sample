From rust:1.70.0 as builder
RUN cargo install wasm-bindgen-cli
RUN rustup target add wasm32-unknown-unknown
RUN apt update && apt install -y wabt binaryen
WORKDIR /myapp
COPY ./Cargo.toml ./Cargo.toml
RUN mkdir src && touch src/lib.rs && cargo build --release --target=wasm32-unknown-unknown
COPY ./src ./src
RUN touch src/lib.rs && cargo build --release --target=wasm32-unknown-unknown
RUN wasm-bindgen ./target/wasm32-unknown-unknown/release/suvasmu.wasm --out-dir bg-out

From python:3.10
run pip install wasmer wasmer_compiler_cranelift
WORKDIR /myapp
copy --from=builder /myapp/bg-out/suvasmu_bg.wasm /myapp/suvasmu.wasm
env WASM_MODULE_PATH=/myapp/suvasmu.wasm
copy use.py .
cmd python use.py
