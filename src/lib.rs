use rand::Rng;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Jutska {
    pub x: f32,
    pub y: u64,
}

#[wasm_bindgen]
pub fn my_add(j: &mut Jutska) -> u64 {
    let y = j.y;
    j.y += 1;
    y
}

#[wasm_bindgen]
pub fn new_jutska() -> Jutska {
    let mut rng: rand_pcg::Pcg64 = rand_seeder::Seeder::from(123).make_rng();
    let x: f32 = (0..10000).map(|_| rng.gen::<f32>()).sum();
    Jutska { x, y: 5 }
}

#[wasm_bindgen]
pub fn eat_jutska(j: Jutska) -> f32 {
    j.x
}
