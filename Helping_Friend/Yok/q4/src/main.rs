use std::fs::File;
use std::io::prelude::*;
use std::io::{self, BufRead};
use std::path::Path;

#[derive(Debug, Clone, Copy, PartialEq)]
enum Language {
    Thai,
    Arabic,
    Lao,
    Tagalog,
    Chinese,
    Japanese,
    Burmese,
    French,
    Korea,
    English,
    Spanish,
    Other,
}

#[derive(Debug, PartialEq)]
struct EeachLang {
    lang: Language,
    range: Vec<u32>,
    name: String,
}

#[derive(Debug, PartialEq)]
struct Count {
    lang: Language,
    count: u64,
}

fn main() {
    let mut my_vec = vec![
        EeachLang {
            lang: Language::Thai,
            range: vec![0x0E00, 0x0E7F],
            name: "Thai".to_string(),
        },
        EeachLang {
            lang: Language::Arabic,
            range: vec![0x0600, 0x06FF],
            name: "Arabic".to_string(),
        },
        EeachLang {
            lang: Language::Tagalog,
            range: vec![0x1700, 0x171F],
            name: "Tagalog".to_string(),
        },
        EeachLang {
            lang: Language::Chinese,
            range: vec![0x4E00, 0x9FFF],
            name: "Chinese".to_string(),
        },
        EeachLang {
            lang: Language::Japanese,
            range: vec![0x3040, 0x309F],
            name: "Japanese".to_string(),
        },
        EeachLang {
            lang: Language::Burmese,
            range: vec![0x1000, 0x109F],
            name: "Burmese".to_string(),
        },
        EeachLang {
            lang: Language::French,
            range: vec![0x00A8, 0x00B8, 0x005E, 0x02CB, 0x02CA, 0x00C6, 0x0152],
            name: "French".to_string(),
        },
        EeachLang {
            lang: Language::Korea,
            range: vec![0x1100, 0x11FF],
            name: "Korea".to_string(),
        },
        EeachLang {
            lang: Language::English,
            range: vec![0x0041, 0x007A],
            name: "English".to_string(),
        },
        EeachLang {
            lang: Language::Spanish,
            range: vec![0x00BF, 0x00A1, 0x00D1, 0x00F1],
            name: "Spanish".to_string(),
        },
        EeachLang {
            lang: Language::Other,
            range: vec![0x00, 0x10FFFF],
            name: "Other".to_string(),
        },
    ];

    let mut struct_vec = vec![
        Count {
            lang: Language::Thai,
            count: 0,
        },
        Count {
            lang: Language::Arabic,
            count: 0,
        },
        Count {
            lang: Language::Tagalog,
            count: 0,
        },
        Count {
            lang: Language::Chinese,
            count: 0,
        },
        Count {
            lang: Language::Japanese,
            count: 0,
        },
        Count {
            lang: Language::Burmese,
            count: 0,
        },
        Count {
            lang: Language::Korea,
            count: 0,
        },
        Count {
            lang: Language::English,
            count: 0,
        },
        Count {
            lang: Language::Other,
            count: 0,
        },
    ];

    // let mut loop_count = 0;
    // let mut text = file();
    // for i in text.chars().into_iter(){
    //     let mut a:Language = Language::Thai;
    //     let mut c = i;
    //     a = find_lang(c, &my_vec);

    //     for k in 0..my_vec.len(){
    //         if a == my_vec[k].lang{
    //            for j in 0..struct_vec.len() - 1{
    //             if a == struct_vec[j].lang{
    //                 struct_vec[j].count += 1;
    //             }
    //            }
    //         }
    //     }
    // }

    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for (line_number, line) in lines.enumerate() {
            if let Ok(ref ip) = line {
                let mut text = ip;
                for i in text.chars().into_iter() {
                    let mut a: Language = Language::Thai;
                    let mut c = i;
                    a = find_lang(c, &my_vec);

                    for k in 0..my_vec.len() {
                        if a == my_vec[k].lang {
                            for j in 0..struct_vec.len() - 1 {
                                if a == struct_vec[j].lang {
                                    struct_vec[j].count += 1;
                                }
                            }
                        }
                    }
                }
                print!("Line {:?} : ", line_number + 1);
                for i in 0..struct_vec.len() - 1 {
                    if struct_vec[i].count > 0 {
                        print!("{:?} ({:?}) ", struct_vec[i].lang, struct_vec[i].count);
                    }
                }
                println!();
				
				for i in 0..struct_vec.len() - 1 {
					struct_vec[i].count = 0;
				}
            }
        }
    }

    // println!("{}", 'Ã±' as u32);
    // println!("{:?}", struct_vec);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

//d.Build a function which, given a unicode value,
//scans the table and finds out to which language that character belong -
//returning the enumerated type.

fn find_lang(c: char, table: &Vec<EeachLang>) -> Language {
    let mut char_lang: Language = Language::Thai;
    for i in table {
        if i.range.len() == 2 {
            if c as u32 >= i.range[0] && c as u32 <= i.range[1] {
                char_lang = i.lang;
                break;
            }
        } else {
            for j in 0..i.range.len() {
                if c as u32 == i.range[j] {
                    //println!("{}", i.range[j]);
                    char_lang = i.lang;
                    break;
                }
            }
        }
    }
    char_lang
}

// // given a language, returns a string describing it.
// fn tell_lang(each_lang: &Language, table: &Vec<EeachLang>) ->String{
//     let mut name_lang = "".to_string();
//     for i in table{
//         if each_lang == &i.lang{
//             name_lang = i.name.clone();
//             break
//         }
//     }
//     name_lang
// }

// fn file() -> String {
//      // Create a path to the desired file
//      let path = Path::new("input.txt");
//      let display = path.display();

//      // Open the path in read-only mode, returns `io::Result<File>`
//      let mut file = match File::open(&path) {
//          Err(why) => panic!("couldn't open {}: {}", display, why),
//          Ok(file) => file,
//      };

//      // Read the file contents into a string, returns `io::Result<usize>`
//      let mut s = String::new();
//     //  let mut n_t: u64 = 0;
//      match file.read_to_string(&mut s) {
//          Err(why) => panic!("couldn't read {}: {}", display, why),
//          // Ok(_) => print!("{} contains:\n{}", display, s),
//          Ok(_) => {
//             return s;
//          }
//      }

//      // `file` goes out of scope, and the "input.txt" file gets closed
// }

// fn format_output(table: Vec<Count>){
//     print
// }
