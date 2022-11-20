#![allow(dead_code, unused_variables)]

use std::error::Error;

const NUM_BINS: usize = 10;
const GPSA_FILE: &str = "histogram/GPSA.csv";
const GPSB_FILE: &str = "histogram/GPSB.csv";
const DEG_LAT_IN_METER: f64 = 111_139.0;
const DEG_LONG_IN_METER: f64 = 107_963.0;

#[derive(Copy, Clone, PartialEq)]
struct GPS {
    lat: f64,
    long: f64,
}

impl std::fmt::Display for GPS {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(
            f,
            "GPS => Latitude = {}, Longitude = {}",
            self.lat, self.long
        )
    }
}

impl GPS {
    fn to_meter(&self) -> GPS {
        GPS {
            lat: self.lat * DEG_LAT_IN_METER,
            long: self.long * DEG_LONG_IN_METER,
        }
    }
    fn to_tuple(&self) -> (f64, f64) {
        (self.lat, self.long)
    }
}

fn load_data(file: &str) -> Result<Vec<GPS>, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_path(file)?;
    let mut gps_data = Vec::new();
    for result in rdr.records() {
        let record = result?;
        gps_data.push(GPS {
            lat: record[0].trim().parse()?,
            long: record[1].trim().parse()?,
        });
    }
    Ok(gps_data)
}

fn print_output(data: Vec<GPS>) {
    println!("======================================================");
    println!("Mean: {}", find_mean(&data));
    println!("Min: {}", find_min(&data));
    println!("Max: {}", find_max(&data));
    println!("Standard deviation: {}", find_std_dev(&data));
    println!("Standard error: {}", find_std_error(&data));
    println!("Standard error (meters): {}", find_std_error_meter(&data));
    println!("");
    println!(
        "Using conversion of 1 degree latitude to {} meters",
        DEG_LAT_IN_METER
    );
    println!(
        "Using conversion of 1 degree longitude to {} meters",
        DEG_LONG_IN_METER
    );
    println!(
        "Calculated 1 degree longitude is {} meters (not used in calculation)",
        calculate_deg_long_from_lat(&data)
    );
    println!("");
    println!(
        "Standard deviation (meters): {}",
        find_std_dev(&data).to_meter()
    );
    println!(
        "Standard error (meters): {}",
        find_std_error(&data).to_meter()
    );
    println!("");
    print_histogram(&data);
    println!("======================================================");
}

fn find_mean(data: &Vec<GPS>) -> GPS {
    let lat_mean = data.iter().map(|x| x.lat).sum::<f64>() / data.len() as f64;
    let long_mean = data.iter().map(|x| x.long).sum::<f64>() / data.len() as f64;
    GPS {
        lat: lat_mean,
        long: long_mean,
    }
}

fn find_min(data: &Vec<GPS>) -> GPS {
    let lat_min = data
        .iter()
        .map(|x| x.lat)
        .min_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap();
    let long_min = data
        .iter()
        .map(|x| x.long)
        .min_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap();
    GPS {
        lat: lat_min,
        long: long_min,
    }
}

fn find_max(data: &Vec<GPS>) -> GPS {
    let lat_max = data
        .iter()
        .map(|x| x.lat)
        .max_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap();
    let long_max = data
        .iter()
        .map(|x| x.long)
        .max_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap();
    GPS {
        lat: lat_max,
        long: long_max,
    }
}

fn find_std_dev(data: &Vec<GPS>) -> GPS {
    let lat_mean = find_mean(data).lat;
    let long_mean = find_mean(data).long;
    let lat_std_dev = (data.iter().map(|x| (x.lat - lat_mean).powi(2)).sum::<f64>()
        / (data.len() as f64 - 1.0))
        .sqrt();
    let long_std_dev = (data
        .iter()
        .map(|x| (x.long - long_mean).powi(2))
        .sum::<f64>()
        / (data.len() as f64 - 1.0))
        .sqrt();
    GPS {
        lat: lat_std_dev,
        long: long_std_dev,
    }
}

fn find_std_error(data: &Vec<GPS>) -> GPS {
    let lat_std_dev = find_std_dev(data).lat;
    let long_std_dev = find_std_dev(data).long;
    GPS {
        lat: lat_std_dev / (data.len() as f64).sqrt(),
        long: long_std_dev / (data.len() as f64).sqrt(),
    }
}

fn find_std_error_meter(data: &Vec<GPS>) -> GPS {
    let lat_std_err = find_std_error(data).lat;
    let long_std_err = find_std_error(data).long;
    GPS {
        lat: lat_std_err * DEG_LAT_IN_METER,
        long: long_std_err * DEG_LONG_IN_METER,
    }
}

fn calculate_deg_long_from_lat(data: &Vec<GPS>) -> f64 {
    return DEG_LAT_IN_METER * find_mean(data).lat.to_radians().cos();
}

fn calculate_bin_width(data: &Vec<GPS>) -> GPS {
    let lat_range = find_max(data).lat - find_min(data).lat;
    let long_range = find_max(data).long - find_min(data).long;
    return GPS {
        lat: lat_range / NUM_BINS as f64,
        long: long_range / NUM_BINS as f64,
    };
}

fn print_histogram(data: &Vec<GPS>) {
    let mut data = data.clone();
    data.sort_by(|a, b| a.lat.partial_cmp(&b.lat).unwrap());

    let lat_min = data[0].lat;
    let long_min = data[0].long;

    let bin_width = calculate_bin_width(&data);

    println!("Latitude histogram");
    let mut bin = Vec::new();
    for i in 0..NUM_BINS {
        bin.push((lat_min + i as f64 * bin_width.lat, 0));
    }
    for gps in &data {
        for i in 0..NUM_BINS {
            if gps.lat >= bin[i].0 && gps.lat < bin[i].0 + bin_width.lat {
                bin[i].1 += 1;
            }
        }
    }
    for i in 0..NUM_BINS {
        print!("{:>10.5} | ", bin[i].0);
        for _ in 0..bin[i].1 {
            print!("*");
        }
        println!("");
    }

    println!("Longitude histogram");
    let mut bin = Vec::new();
    for i in 0..NUM_BINS {
        bin.push((long_min + i as f64 * bin_width.long, 0));
    }
    for gps in data {
        for i in 0..NUM_BINS {
            if gps.long >= bin[i].0 && gps.long < bin[i].0 + bin_width.long {
                bin[i].1 += 1;
            }
        }
    }
    for i in 0..NUM_BINS {
        print!("{:>10.5} | ", bin[i].0);
        for _ in 0..bin[i].1 {
            print!("*");
        }
        println!("");
    }
}

fn main() {
    let data_a = load_data(GPSA_FILE);
    let data_b = load_data(GPSA_FILE);
    match data_a {
        Ok(data) => print_output(data),
        Err(e) => println!("Error: {}", e),
    }
    match data_b {
        Ok(data) => print_output(data),
        Err(e) => println!("Error: {}", e),
    }
}
