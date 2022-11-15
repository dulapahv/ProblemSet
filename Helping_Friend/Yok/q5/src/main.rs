use std::fmt;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::io::Read;

#[derive(Debug)]
struct Pos {
    x: f64,
    y: f64,
}

#[derive(Debug)]
struct Manager {
    name: String,
    age: u32,
    staff_list: Vec<String>,
    pos: Pos,
}

#[derive(Debug)]
struct SoftEng {
    name: String,
    age: u32,
    skills: Vec<String>,
    pos: Pos,
}

#[derive(Debug)]
struct GraphicDesighner {
    name: String,
    age: u32,
    skills: Vec<String>,
    pos: Pos,
}

/*
Parse the following to struct, of either Manager, SoftEng, GraphicDesigner depending on Role

Role: Manager
Name: John Smith
Age: 35
StaffList: Bob Brown, Alice Green
Pos: 14.34567, 100.45675
*/

impl fmt::Display for Pos {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{},{}", self.x, self.y)
    }
}

impl fmt::Display for Manager {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "Role: Manager

Name: {}

Age: {}

StaffList: {}

Pos: {}",
            self.name,
            self.age,
            self.staff_list.join(", "),
            self.pos
        )
    }
}

impl fmt::Display for SoftEng {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "Role: SoftEng

Name: {}

Age: {}

Skills: {}

Pos: {}",
            self.name,
            self.age,
            self.skills.join(", "),
            self.pos
        )
    }
}

impl fmt::Display for GraphicDesighner {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "Role: GraphicDesighner

Name: {}

Age: {}

Skills: {}

Pos: {}",
            self.name,
            self.age,
            self.skills.join(", "),
            self.pos
        )
    }
}

fn main() {
    let mut f = File::open("input.txt").expect("file not found");
    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("something went wrong reading the file");

    let mut lines = contents.lines();

    let role = lines.next().unwrap();
    let name = lines.next().unwrap();
    let age = lines.next().unwrap();
    let pos = lines.next().unwrap();
    let pos = pos.split(", ").collect::<Vec<&str>>();
    let pos = Pos {
        x: pos[0].parse().unwrap(),
        y: pos[1].parse().unwrap(),
    };

    let mut staff_list = Vec::new();
    let mut skills = Vec::new();

    if role == "Manager" {
        let staff_list_str = lines.next().unwrap();
        staff_list = staff_list_str.split(", ").map(|s| s.to_string()).collect();
    } else if role == "SoftEng" {
        let skills_str = lines.next().unwrap();
        skills = skills_str.split(", ").map(|s| s.to_string()).collect();
    } else if role == "GraphicDesighner" {
        let skills_str = lines.next().unwrap();
        skills = skills_str.split(", ").map(|s| s.to_string()).collect();
    }

    if role == "Manager" {
        let manager = Manager {
            name: name.to_string(),
            age: age.parse().unwrap(),
            staff_list: staff_list,
            pos: pos,
        };
        println!("{}", manager);
    } else if role == "SoftEng" {
        let softeng = SoftEng {
            name: name.to_string(),
            age: age.parse().unwrap(),
            skills: skills,
            pos: pos,
        };
        println!("{}", softeng);
    } else if role == "GraphicDesighner" {
        let graphicdesighner = GraphicDesighner {
            name: name.to_string(),
            age: age.parse().unwrap(),
            skills: skills,
            pos: pos,
        };
        println!("{}", graphicdesighner);
    }
}
