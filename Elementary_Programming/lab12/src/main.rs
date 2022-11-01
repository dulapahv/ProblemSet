use std::env;
use std::fmt;
use std::fmt::Error;
use std::fmt::Formatter;

pub trait Display {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}

#[derive(Copy, Clone, Debug)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Copy, Clone, Debug)]
pub struct LatLong {
    ns: f64,
    ew: f64,
}

impl fmt::Display for LatLong {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut ewc = 'E';
        if self.ew < 0.0 {
            ewc = 'W';
        }
        let mut nsc = 'N';
        if self.ns < 0.0 {
            nsc = 'S';
        }
        write!(f, "({}{}, {}{})", self.ew, ewc, self.ns, nsc)
    }
}

struct Manager {
    name: String,
    age: u8,
    staff_list: Vec<String>,
    location: LatLong,
}

struct Worker {
    name: String,
    age: u8,
    location: LatLong,
}

struct SoftEng {
    name: String,
    age: u8,
    location: LatLong,
    skills: Vec<String>,
}

pub trait Employee {
    fn get_name(&self) -> String;
    fn get_age(&self) -> u8;
    fn get_location(&self) -> LatLong;
    fn get_staff_list(&self) -> Vec<String>;
    fn get_skills(&self) -> Vec<String>;
}

impl fmt::Display for Manager {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Manager: {}, age: {}, location: {}, staff: {:?}",
            self.name, self.age, self.location, self.staff_list
        )
    }
}

impl fmt::Display for Worker {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Worker: {}, age: {}, location: {}",
            self.name, self.age, self.location
        )
    }
}

impl fmt::Display for SoftEng {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "SoftEng: {}, age: {}, location: {}, skills: {:?}",
            self.name, self.age, self.location, self.skills
        )
    }
}

fn main() {
    println!("Traits examples");
    let mut p1 = Point { x: 0.0, y: 0.0 };
    let mut p2 = Point { x: 1.0, y: 1.0 };
    p2 = p1;
    println!("p1 = {:?}", p1);
    println!("p2 = {:?}", p2);

    let pos = LatLong {
        ew: 102.0,
        ns: 14.3,
    };
    println!("Pos {} ", pos);

    println!("Traits examples");
    let mut p1 = Point { x: 0.0, y: 0.0 };
    let mut p2 = Point { x: 1.0, y: 1.0 };
    p2 = p1;
    println!("p1 = {:?}", p1);
    println!("p2 = {:?}", p2);

    //use employee trait
    let m = Manager {
        name: String::from("John"),
        age: 30,
        staff_list: vec![String::from("Alice"), String::from("Bob")],
        location: LatLong {
            ew: 102.0,
            ns: 14.3,
        },
    };
    let w = Worker {
        name: String::from("Alice"),
        age: 20,
        location: LatLong {
            ew: 102.0,
            ns: 14.3,
        },
    };
    let s = SoftEng {
        name: String::from("Bob"),
        age: 25,
        location: LatLong {
            ew: 102.0,
            ns: 14.3,
        },
        skills: vec![String::from("Rust"), String::from("C++")],
    };

    println!("m = {}", m);
    println!("w = {}", w);
    println!("s = {}", s);
}
