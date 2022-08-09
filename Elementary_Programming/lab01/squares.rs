fn main() {
    println!("Squares!");
    for n in 1..100 {
       let x = n as f64;
       let sqrt_x:f64 = x.sqrt();
       let xx:f64 = sqrt_x * sqrt_x;
       print!("{} ", x);
       if x == xx {
	println!(" OK");
	}
       else {
        let dx = x - xx;
	print!("{}", dx);
	println!(" diff");
	}
    }
}
