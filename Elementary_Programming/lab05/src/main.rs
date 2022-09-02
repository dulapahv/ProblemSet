// use chrono::prelude::*;
// use chrono::{DateTime,Local};
use std::time::{Duration, Instant};

#[derive(Debug, Copy, Clone)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Debug, Copy, Clone)]
struct Circle {
    origin: Point,
    radius: f64,
}
/******************************************************************************/
#[derive(Debug, Copy, Clone)]
struct Square {
    origin: Point,
    side: f64,
}
/******************************************************************************/
fn time_diff_nsecs(t0: Instant) -> f64 {
    let duration = t0.elapsed();
    let d_nsecs = duration.as_nanos();
    d_nsecs as f64
}

const N: usize = 20000;

fn time_array(n: usize) -> f64 {
    // // Initialize array
    // let p0 = Point { x: 0.0, y: 0.0 };
    // let mut c0 = Circle {
    //     origin: p0,
    //     radius: 1.0,
    // };
	// let mut c1 = Square {
	// 	origin: p1,
	// 	side: 1.0,
	// };
    // let mut v_array: [Circle; N] = [c0; N];
    // let t0 = Instant::now();
    // for j in 0..N {
    //     v_array[j] = c0;
    //     c0.radius *= 1.001;
    // }
    // let duration = time_diff_nsecs(t0);
    // println!("Start {:?} Time to initialize array {:?}", t0, duration);
    // duration as f64
	// Initialize array

	let p0 = Point { x: 0.0, y: 0.0 };
	let mut c0 = Square {
		origin: p0,
		side: 1.0,
	};
	let mut v_array: [Square; N] = [c0; N];
	let t0 = Instant::now();
	for j in 0..N {
		v_array[j] = c0;
		c0.side *= 1.001;
	}
	let duration = time_diff_nsecs(t0);
	println!("Start {:?} Time to initialize array {:?}", t0, duration);
	duration as f64
}

fn access_array(n: usize) -> f64 {
	// Initialize array
	let p0 = Point { x: 0.0, y: 0.0 };
	let mut c0 = Square {
		origin: p0,
		side: 1.0,
	};
	let mut v_array: [Square; N] = [c0; N];
	for j in 0..N {
		v_array[j] = c0;
		c0.side *= 1.001;
	}
	let t0 = Instant::now();
	for j in 0..N {
		let c = v_array[j];
		let r = c.side;
	}
	let duration = time_diff_nsecs(t0);
	println!("Start {:?} Time to access array {:?}", t0, duration);
	duration as f64
}

fn time_vector(n: usize) -> f64 {
    // // Initialize vector
    // let p0 = Point { x: 0.0, y: 0.0 };
    // let mut c0 = Circle {
    //     origin: p0,
    //     radius: 1.0,
    // };
    // let mut v_objects: Vec<Circle> = Vec::with_capacity(50);
    // let t0 = Instant::now();
    // // println!("Start {:?}", t0 );
    // for j in 0..n {
    //     v_objects.push(c0);
    //     c0.radius *= 1.001;
    // }
    // let duration = time_diff_nsecs(t0);
    // println!("Start {:?} Time to initialize array {:?}", t0, duration);
    // duration as f64

	// Initialize vector
    let p0 = Point { x: 0.0, y: 0.0 };
    let mut c0 = Square {
        origin: p0,
        side: 1.0,
    };
    let mut v_objects: Vec<Square> = Vec::with_capacity(50);
    let t0 = Instant::now();
    // println!("Start {:?}", t0 );
    for j in 0..n {
        v_objects.push(c0);
        c0.side *= 1.001;
    }
    let duration = time_diff_nsecs(t0);
    println!("Start {:?} Time to initialize array {:?}", t0, duration);
    duration as f64
}

/* get average time to access/element Point/Square struct by using vector */
fn access_vector(n: usize) -> f64 {
	let p0 = Point { x: 0.0, y: 0.0 };
	let mut c0 = Square {
		origin: p0,
		side: 1.0,
	};
	let mut v_objects: Vec<Square> = Vec::with_capacity(50);
	let t0 = Instant::now();
	// println!("Start {:?}", t0 );
	for j in 0..n {
		v_objects.push(c0);
		c0.side *= 1.001;
	}
	let duration = time_diff_nsecs(t0);
	println!("Start {:?} Time to initialize array {:?}", t0, duration);
	duration as f64
}



fn main() {
    println!("Vectors - Performance and Timing");
    // let p0 = Point { x: 0.0, y: 0.0 };
    // let mut c0 = Circle {
    //     origin: p0,
    //     radius: 1.0,
    // };
    // let mut v_objects: Vec<Circle> = Vec::new();

	let p0 = Point { x: 0.0, y: 0.0 };
    let mut c0 = Square {
        origin: p0,
        side: 1.0,
    };
    let mut v_objects: Vec<Square> = Vec::new();

    let t_per_array = time_array(N);
    println!(
        "Array {} elements total {} ns mean {} ns/elem",
        N,
        t_per_array,
        (t_per_array) / (N as f64)
    );
	let a_per_array = access_array(N);
	println!(
		"Array access {} elements total {} ns mean {} ns/elem",
		N,
		a_per_array,
		(a_per_array) / (N as f64)
	);
    let t_per_vector = time_vector(N);
    println!(
        "Vector {} elements total {} ns mean {} ns/elem",
        N,
        t_per_vector,
        t_per_vector / (N as f64)
    );
	let a_per_vector = access_vector(N);
	println!(
		"Vector access {} elements total {} ns mean {} ns/elem",
		N,
		a_per_vector,
		(a_per_vector) / (N as f64)
	);
}
