fn main() {
    let mut _a:char = 'a';
    let mut in_pt:i32 = 0;
    let mut out_pt:i32 = 0;
    let _z:char = '\u{7FFF}';

    const EPS:f64 = 1.0e-5;

    print!("Calculate Pi!\n");
    let mut _n = 1;
    loop{
        // Generate two random numbers
        let x:f64 = rand::random();
        let y:f64 = rand::random();
        // Calculate distance of (x,y) from origin
        let d2:f64 = ( x*x + y*y ).sqrt();
        // Is this point inside the unit circle?
        if d2 <= 1.00
        { in_pt+=1; }
        else
        { out_pt+=1; }
        // Calculate estimate of pi every 10000 trials
        if (_n % 10000) == 0 {
			
            let pi_est = 4.0 * (in_pt as f64)/ ((in_pt as f64) + (out_pt as f64));
            let diff = core::f64::consts::PI - pi_est;
            let sum = (x+y)/2.0;
            let deviation = (0.5-sum).abs();
            print!("{} {} {} ", _n, x, y);
            println!(" pi = {} {}", pi_est, diff);
            // Is the difference too large?
            let out_of_range = diff > EPS;
            let ok = diff > 0.0;
            let mut abs_diff = f64::abs(diff);
            print!("{} {} {} {}\n", out_of_range, ok, abs_diff, deviation);
            if abs_diff < EPS {
                println!("Pi value that led to a break: {}",pi_est);
                break;
            }
        }
        _n+=1;

    }
}
