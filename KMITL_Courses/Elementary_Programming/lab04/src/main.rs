use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

#[derive(Debug, Copy, Clone)]
struct Point {
   x: f64,
   y: f64,
  }

impl Point {
    fn new() -> Point {
        Point{x: 0.0, y: 0.0}
    }
}

fn length(d:[Point;2]) -> f64 {
	let dx = d[0].x - d[1].x;
	let dy = d[0].y - d[1].y;
	let dd = dx*dx + dy*dy;
	dd.sqrt()
}

/** ADD **/
fn angle(d:[Point;3]) -> f64 {
	let a = length([d[0], d[1]]);
	let b = length([d[1], d[2]]);
	let c = length([d[0], d[2]]);
	let cos_a = (b*b + c*c - a*a) / (2.0 * b * c);
	let cos_b = (a*a + c*c - b*b) / (2.0 * a * c);
	let cos_c = (a*a + b*b - c*c) / (2.0 * a * b);
	let acos_a = cos_a.acos();
	let acos_b = cos_b.acos();
	let acos_c = cos_c.acos();
	let angle = acos_a + acos_b + acos_c;
	angle
}

fn area(d:[Point;3]) -> f64 {
	let a = length([d[0], d[1]]);
	let b = length([d[1], d[2]]);
	let c = length([d[0], d[2]]);
	let s = (a+b+c)/2.0;
	let dd = s*(s-a)*(s-b)*(s-c);
	dd.sqrt()
}
/** === **/

#[derive(Debug, Copy, Clone)]
struct Triangle {
   name:[char;2],
   p : [Point;3],
  }

/****************** Add to this function *************************/
fn check_triangle(t:Triangle) {
	println!("\nMytriangle\n{:?}\n",t);
	let a = length([t.p[0], t.p[1]]);
	let b = length([t.p[1], t.p[2]]);
	let c = length([t.p[0], t.p[2]]);
	println!("Length: a = {:?}, b = {:?}, c = {:?}", a, b, c);
	let angle = angle(t.p);
	println!("Angle = {}",angle);
	let area = area(t.p);
	println!("Area = {}",area);
	println!("================================================================");
}

/****************** Read .. and understand later  *************************/
fn read_triangles( s:String ) -> u64 {
	
	print!("File contains:\n{}",  s);
        let lines:Vec<&str> = s.split('\n').collect();
	let n_lines = lines.len();
	println!("s has {} lines", n_lines );
	let mut n_tri:u64 = 0;
	for j in 0..n_lines {
		let t_set:Vec<&str> = lines[j].split(' ').collect();
		let n_tokens = t_set.len();
		if n_tokens < 6 { break; }
		println!("t_set[{}] has {} tokens", j, n_tokens );
		for k in 0..n_tokens-1 { print!(" {}:{}", k, t_set[k]); }
		println!();
		let label = t_set[0];
		print!("T {}: ", label);
		let mut k1:usize = 1;
		let mut ps = [Point::new();3];
		for m in 0..3 { 
			print!(" {}, ", t_set[k1] );
			let x: f64 = t_set[k1].parse().unwrap(); 
			k1 = k1 + 1;
			let y: f64 = t_set[k1].parse().unwrap(); 
			print!("Point ({},{}) ", x, y );
			k1 = k1 + 1;
			// let p = Point{x:x,y:y};
			ps[m] = Point{x:x,y:y};
			}
		let namej = ['A','A'];
		let tj = Triangle{name:namej,p:ps };
		check_triangle(tj);
		n_tri += 1;
		println!();
	}
	n_tri
}

fn main() {
    // Create a path to the desired file
    let path = Path::new("triangles.txt");
    let display = path.display();

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    let mut n_t:u64 = 0;
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        // Ok(_) => print!("{} contains:\n{}", display, s),
        Ok(_) => { n_t = read_triangles(s); }
    }
    println!("{} triangles read", n_t);
    // `file` goes out of scope, and the "hello.txt" file gets closed
}
