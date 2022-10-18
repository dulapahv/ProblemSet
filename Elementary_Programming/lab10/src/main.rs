use std::f64::consts::PI;
use std::time::{Duration, Instant};

const MAX_POWER: u64 = 12;
const PI2: f64 = 2.0 * PI;
const BASE: u64 = 4;

fn time_diff_secs(t0: Instant) -> f64 {
    let duration = t0.elapsed();
    let d_secs = (duration.as_secs() as f64) + (duration.subsec_nanos() as f64) * 1e-9;
    d_secs
}

fn empty_loop(n: u64) -> f64 {
    let mut sum: f64 = 0.0;
    for _j in 0..n {
        let x: f64 = (rand::random::<f64>()) * PI2;
        sum += x;
    }
    let mean = sum / (n as f64);
    mean
}

fn real_loop(n: u64) -> f64 {
    let mut sum: f64 = 0.0;
    // Fill in something here
    for _j in 0..n {
        let x: f64 = (rand::random::<f64>()) * PI2;
        sum += x.sin();
    }
    let mean = sum / (n as f64);
    mean
}

fn print_time(t_secs: f64, n: u64) {
    print!("T {:8.3} s t {:6.1} ns ", t_secs, t_secs * 1.0e9 / (n as f64));
}

fn sin_series(x: f64, n: u64) -> f64 {
    let x2: f64 = x * x;
    // Fill in something here
    let mut divisor: u64 = 1;
    let mut sum: f64 = 0.0;
    let mut xn = x;
    let mut f: u64 = 2;
    let mut sign: bool = true;
    let mut term = x;
    for _j in 0..n {
        if sign {
            sum += term;
        } else {
            sum -= term;
        }
        xn = xn * x2;
        divisor = divisor * f * (f + 1);
        f += 2;
        term = xn / (divisor as f64);
        sign = !sign;
    }
    sum
}
fn main() {
    println!("Accurate timing");
    let mut n: u64 = 1;
    for j in 1..MAX_POWER {
        let mut t0 = Instant::now();
        let mut mean = empty_loop(n);
        let loop_time = time_diff_secs(t0);
        print!("{:3} {:9} ", j, n);
        print_time(loop_time, n);
        print!("m {:8.4} ", mean);

        // Now time the loop with some real code in it
        t0 = Instant::now();
        mean = real_loop(n);
        let real_time = time_diff_secs(t0);
        print_time(real_time, n);
        let act_time: f64 = real_time - loop_time;
        print_time(act_time, n);
        println!(" {:8.4}", mean);

        n = n * BASE;
    }

    for n_angles in 0..8 {
        let xd: f64 = 15.0 * (n_angles as f64);
        let x = PI * (xd / 180.0);
        print!("{:5.1} {:8.4} {:10.6}", xd, x, x.sin());
        for k in 1..10 {
            let sx = sin_series(x, k);
            print!("{:10.6} ", sx);
        }
        println!();
    }
}
