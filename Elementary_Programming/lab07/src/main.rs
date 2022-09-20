fn main() {
	/* 1 */
	let mut n = 2; // Add `mut` to make it mutable
	n = n + 5;

	/* 2 */
	let m = 10;
	let x: f64 = 1.0;
	let x10 = x * m as f64; //cast m to f64

	/* 3 */
	const N: usize = 10; // const is a keyword
	let narray: [i32; N]; // 3a: N is const

	/* 4 */
	const M: usize = 10;
	let mut marray: [f32; M] = [0.0; M];
	for i in 0..M {
		marray[i] = rand::random::<f32>();
	}

	/* 5 */
	fn calcmean(array: &[f32]) -> f32 {
		let mut sum = 0.0;
		for i in 0..array.len() {
			sum += array[i];
		}
		sum / array.len() as f32
	}
	println!("{}", calcmean(&marray));

	/* 6 */
	let mut count = 0;
	for i in 0..M {
		if marray[i] < 0.25 {
			count += 1;
		}
	}

	/* 7 */
	let m = 20.0;
	let x: f64 = 1.0;
	{
		let x10_2 = x / m;
	}
	//println!("{}% is {}", 1 / m, x10_2); // x10_2 is limited in the scope above

	//8: Different operation (multiply and divide)

	/* 9 */
	println!("f32 max: {}", std::f32::MAX);
	println!("f32 min: {}", std::f32::MIN);
	println!("f64 max: {}", std::f64::MAX);
	println!("f64 min: {}", std::f64::MIN);

	/* 10 */
	struct Optimism {
		name: String,
		expectedSalary: f32,
		probability: f32,
	}

	/* 10a */
	let opt = Optimism {
		name: String::from("Nadeko Sengoku"),
		expectedSalary: 100000.0,
		probability: 0.5,
	};

	/* 10b */
	fn init_optimism(name: String, expectedSalary: f32, probability: f32) -> Optimism {
		Optimism {
			name: name,
			expectedSalary: expectedSalary,
			probability: probability,
		}
	}
	let opt2 = init_optimism("Shinobu Oshino".to_string(), 100000.0, 0.5);

	/* 11 */
	struct Coordinate {
		lat: f32,
		long: f32,
	}

	/* 11a */
	const DegSym: char = '\u{00B0}';

	/* 11b */
	impl Coordinate {
		fn print(&self) {
			let direction: char = if self.lat > 0.0 { 'N' } else { 'S' };
			println!(
				"{}{}{}, {}{}{}",
				self.lat.abs(),
				DegSym,
				if self.lat > 0.0 { 'N' } else { 'S' },
				self.long.abs(),
				DegSym,
				if self.long > 0.0 { 'E' } else { 'W' }
			);
		}
	}

	/* 12 */
	let mut coordsvec: Vec<Coordinate> = Vec::new();

	/* 12a */
	let mut lat = 0.0;
	let mut long = 0.0;

	for _ in 0..4 {
		for _ in 0..4 {
			coordsvec.push(Coordinate {
				lat: lat,
				long: long,
			});
			lat += 0.01;
		}
		lat = 0.0;
		long += 0.01;
	}

	/* 12b */
	for i in 0..4 {
		for j in 0..4 {
			coordsvec[i * 4 + j].print();
		}
		println!();
	}

	/* 12c */
	for i in 0..4 {
		for j in 0..4 {
			coordsvec[i * 4 + j] = Coordinate {
				lat: 0.0,
				long: 0.0,
			};
			coordsvec[i * 4 + j].print();
		}
		println!();
	}

	/* 13 */
	struct Point {
		x: f64,
		y: f64,
	}

	impl Point {
		fn distance(&self, other: &Point) -> f64 {
			((self.x - other.x).powi(2) + (self.y - other.y).powi(2)).sqrt() //magnificent google formula
		}
	}

	struct Polygon {
		points: Vec<Point>,
	}

	/* 14 */
	impl Polygon {
		fn perimeter(&self) -> f64 {
			let mut sum: f64 = 0.0;
			for i in 0..self.points.len() {
				sum += self.points[i].distance(&self.points[(i + 1) % self.points.len()]);
			}
			sum
		}
	}

	/* 15 */
	let name = "Nozomu Itoshiki";
	let thainame = "โนโซมุ อิโตชิกิ";
	let japname = "糸色望";

	/* 16 */
	struct Person {
		name: String,
		age: u8,
	}

	let nozomu = Person {
		name: String::from(name),
		age: 25,
	};

	/* 17 */
	fn find_char(s: &str, c: char) -> i32 {
		for (i, ch) in s.chars().enumerate() {
			if ch == c {
				return i as i32;
			}
		}
		-1
	}
}
