fn main() {
    let arr_1: [f64; 3] = [3.5, -100000.0, 0.0];

    for i in arr_1.iter() {
        println!("{}", i);
    }

    for i in 0..arr_1.len() {
        println!("{}", arr_1[i]);
    }
}
