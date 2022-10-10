use std::f64::consts::PI;

const N: usize = 10;
const M: usize = 2;
const L: usize = 101;

fn lut_sin(lut: [f64; N], x: f64) -> f64 {
    let mut lower_s: f64 = 0.0;
    let mut upper_s: f64 = 0.0;

    let mut num_sin: f64 = 0.0;

    let mut lut_lib: [f64; N] = [0.0; N];
    let mut num: f64 = 0.0;

    for i in 0..N {
        lut_lib[i] = (lut[i] * PI / 180.0).sin();
        // num += 10.0;
    }
    let mut a = 0;
    // find sin
    for j in 0..N {
        if x <= lut[j] {
            if j > 0 {
                upper_s = lut[j];
                a = j;
                lower_s = lut[j - 1];
                break;
            }
        }
    }

    num_sin = lut_lib[a - 1] + (lut_lib[a] - lut_lib[a - 1]) * (x - lower_s) / (upper_s - lower_s);
    num_sin
}

// P'Unn
fn lut_cos(lut: [f64; N], x: f64) -> f64 {
    let mut lower_c: f64 = 0.0;
    let mut upper_c: f64 = 0.0;

    let mut num_cos: f64 = 0.0;
    let mut y: f64 = x;

    let mut lut_lib: [f64; N] = [0.0; N];
    let mut num: f64 = 0.0;

    for i in 0..N {
        lut_lib[i] = (lut[i] * PI / 180.0).cos();
        // num += 10.0;
    }
    //fins cos
    let mut b = 0;
    for j in 0..N {
        if y <= lut[j] {
            if j > 0 {
                upper_c = lut[j];
                b = j;
                lower_c = lut[j - 1];
                break;
            }
        }
    }
    num_cos = lut_lib[b - 1] + (lut_lib[b] - lut_lib[b - 1]) * (y - lower_c) / (upper_c - lower_c);
    num_cos
}

fn main() {
    let mut lut: [f64; N] = [0.0; N];
    let mut num: f64 = 0.0;

    let mut test: f64 = 0.0;
    let mut test_value: [f64; L] = [0.0; L];
    let mut test_sin: [f64; L] = [0.0; L];
    let mut test_cos: [f64; L] = [0.0; L];

    for i in 0..N {
        lut[i] = num;
        num += 90.0 / N as f64;
        // num += 10.0;
    }
    for i in 0..L {
        test_value[i] = test;
        // test += 90.0/L as f64;
        test += 8.0 as f64;
    }

    println!("");
    println!("angle\t\t\t|  sin_from_library\t|\tsin_from_interpolation\t|\tcos_from_library\t|\tcos_from_interpolation");
    println!("");

    // print table
    for k in 0..L {
        test_sin[k] = lut_sin(lut, test_value[k]);
        test_cos[k] = lut_cos(lut, test_value[k]);
        println!(
            "{:20.16}\t|{:20.16}\t|\t{:20.16}\t|\t{:20.16}\t|\t{:20.16}",
            test_value[k],
            (test_value[k] * PI / 180.0).sin(),
            test_sin[k],
            (test_value[k] * PI / 180.0).cos(),
            test_cos[k]
        );
    }

    // println!("{:?}",lut);
    // println!("{:?}",test_value);
    // println!(“x = {:20.16}”, x );

    // println!("{}", lut_sin(lut, 15.0));
    // println!("{}",(15.0*PI/180.0).sin());

    // println!("{:?}",test_sin);
    // println!("{}", lut_sin(lut, 63.234));
    // println!("{}",lut_sin(lut,test_value[0]));
    // println!("{}", test_value[1]);

    // for k in 0..L{
    //     test_cos[k] = lut_cos(lut, test_value[k]);
    //     println!("{}", test_cos[k]);
    // }
}
