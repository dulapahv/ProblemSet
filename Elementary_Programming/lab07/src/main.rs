use rand::Rng;
use std::io;

fn main() {
	//1
	let mut n = 2;
	n = n + 5; // n aint a mut, fixed

	//2
	let m = 10;
	let x: f64 = 1.0;
	let x10 = x * m as f64; //cast m to f64

	//3
	const N: usize = 10; //const is a keyword
	let narray: [i32; N]; //3a: N is const

	//4
	const M: usize = 10;
	let mut marray: [f32; M] = [0.0; M]; //4a: M is const
	for i in 0..M {
		marray[i] = rand::random::<f32>();
	}

	//5
	println!("{}", calcmean(&marray));

	//6
	let mut count = 0;
	for i in 0..M {
		if marray[i] < 0.25 {
			count += 1;
		}
	}
	//WHAT THE FUCK IS THIS

	//7
	let m = 20.0;
	let x: f64 = 1.0;
	{
		let x10 = x / m;
	}
	println!("{}% is {}", 1 as f64 / m, x10); //cannot divide int by f64. cast 1 as f64
											  //cyberpunk 2077 problem solving skills

	//8: Different operation (multiply and divide)

	//9
	println!("f32 max: {}", std::f32::MAX);
	println!("f32 min: {}", std::f32::MIN);
	println!("f64 max: {}", std::f64::MAX);
	println!("f64 min: {}", std::f64::MIN);

	//10a
	let opt = Optimism {
		name: String::from("Nadeko Sengoku"),
		expectedSalary: 100000.0,
		probability: 0.5,
	};
	let opt2 = initOptimism("Shinobu Oshino".to_string(), 100000.0, 0.5);

	//11
	let thatOneIntersection = Coordinate {
		lat: 13.7506,
		long: 100.7943,
	};

	//12
	let coordsvec: Vec<Coordinate> = Vec::new();
	//I'm not doing this shit
	//You should consult the others - Satoko

	let monogatariwall = Coordinate {
		lat: 13.743778,
		long: 100.534000,
	};
	monogatariwall.print();

	let trinitytestsite = Coordinate {
		lat: 33.677391091393474,
		long: -106.47528710243341,
	};
	trinitytestsite.print();
	//15
	let name = "Nozomu Itoshiki";
	let thainame = "โนโซมุ อิโตชิกิ";
	let japname = "糸色望";

	//16
	let nozomu = Person {
		name: String::from(name),
		age: 25,
	};
}

//11a
const DegSym: char = '\u{00B0}';

fn calcmean(array: &[f32]) -> f32 {
	//part of 5a
	let mut sum = 0.0;
	for i in 0..array.len() {
		sum += array[i];
	}
	sum / array.len() as f32
}

//10
struct Optimism {
	name: String,
	expectedSalary: f32,
	probability: f32,
}

//10b
fn initOptimism(name: String, expectedSalary: f32, probability: f32) -> Optimism {
	Optimism {
		name: name,
		expectedSalary: expectedSalary,
		probability: probability,
	}
}

//11
struct Coordinate {
	lat: f32,
	long: f32,
}

//11a
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

struct Point {
	x: f64,
	y: f64,
}

//13
struct Polygon {
	points: Vec<Point>,
}

impl Point {
	fn distance(&self, other: &Point) -> f64 {
		((self.x - other.x).powi(2) + (self.y - other.y).powi(2)).sqrt() //magnificent google formula
	}
}

//14
impl Polygon {
	fn perimeter(&self) -> f64 {
		let mut sum: f64 = 0.0;
		for i in 0..self.points.len() {
			sum += self.points[i].distance(&self.points[(i + 1) % self.points.len()]);
			//got the formula from google, not guaranteed to work
		}
		sum
	}
}

//16
struct Person {
	name: String,
	age: u8,
}

//17
fn checkIfCharIsIn(charac: char, string: String) -> bool {
	for c in string.chars() {
		if c == charac {
			return true;
		}
	}
	false
}
