use std::f64::consts::PI;

fn main() {
	/*
	1.	Build your look up table, lut: start with a small one, e.g. 10 entries
		for 0, 10, … , 90.  You can expand it to a much larger one later.
	2.	Fill it with values for sin( ) computed by the library function.
		Don’t forget to convert to radians 😊.
	*/
	let lut: [f64; 10] = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0];

	/*
	4.	Create another array of test values. If the test values are the same as
		the values used to created the table, then you will get a perfect
		answer, so make sure that your test values range from 0 to 90, but
		include some non-integer values, e.g.
		[0.0, 0.234, 5.456, 10.100, 19.34, …..]
	5.	A good test set includes some known values, e.g. 0, 30, 45, 60, so that
		you can quickly verify that your function is correct.
	*/
	let x: [f64; 10] = [
		0.0, 0.234, 5.456, 10.100, 19.34, 25.12, 0.0, 30.0, 45.0, 60.0,
	];

	/*
	6.	In a loop, compare the sin values computed from your function with the
		library one.
	7.	Print these differences as a table.
	8.	Note that for f64 values, the precision is ~1 in 10^16, so more than 16
		decimal digits in your report are just noise! Rust will allow you
		suppress them using println!(“x = {:20.16}, x ); which print only
		16 digits after the decimal point in a 20 character width field.
	*/
	let mut by_func: [f64; 10] = [0.0; 10];
	let mut by_lib: [f64; 10] = [0.0; 10];

	by_func = lut_sin(lut, x);

	for i in 0..x.len() {
		by_lib[i] = (x[i] * PI / 180.0).sin();
	}

	for i in 0..by_func.len() {
		println!(
			"x = {}\tsin(x) = {:20.16}\tlut_sin(x) = {:20.16}\tdiff = {:20.16}",
			x[i],
			by_lib[i],
			by_func[i],
			(by_lib[i] - by_func[i]).abs()
		);
	}
}

/*
3.	Create a function lut_sin(lut, x) that computes sin(x) by interpolation
	in your function.
*/
fn lut_sin(lut: [f64; 10], x: [f64; 10]) -> [f64; 10] {
	let mut upper: f64 = 0.0;
	let mut lower: f64 = 0.0;
	let mut arr: [f64; 10] = [0.0; 10];
	for i in 0..x.len() {
		for j in 0..lut.len() {
			if x[i] < lut[j] {
				lower = (lut[j - 1] * PI / 180.0).sin();
				upper = (lut[j] * PI / 180.0).sin();
				arr[i] = lower + (upper - lower) * (x[i] - lut[j - 1]) / (lut[j] - lut[j - 1]);
				break;
			}
		}
	}
	arr
}
