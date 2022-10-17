// #[derive(Debug)]
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
    range: (u32, u32),
    name: String,
}

fn main() {
    // let mut input = String::new();
    // std::io::stdin().read_line(&mut input).expect("Read Faiiled");

    let mut my_vec = vec![
        EeachLang {
            lang: Language::Thai,
            range: (0x0E00, 0x0E7F),
            name: "Thai".to_string(),
        },
        EeachLang {
            lang: Language::Arabic,
            range: (0x0600, 0x06FF),
            name: "Arabic".to_string(),
        },
        EeachLang {
            lang: Language::Tagalog,
            range: (0x1700, 0x171F),
            name: "Tagalog".to_string(),
        },
        EeachLang {
            lang: Language::Chinese,
            range: (0x4E00, 0x9FFF),
            name: "Chinese".to_string(),
        },
        EeachLang {
            lang: Language::Japanese,
            range: (0x3040, 0x309F),
            name: "Japanese".to_string(),
        },
        EeachLang {
            lang: Language::Burmese,
            range: (0x1000, 0x109F),
            name: "Burmese".to_string(),
        },
        // EeachLang{lang:Language:: French, range: (0x00A8,0x00B8, 0x005E, 0x02CB, 0x02CA, 0x00C6, 0x0152), name "French"},
        EeachLang {
            lang: Language::Korea,
            range: (0x1100, 0x11FF),
            name: "Korea".to_string(),
        },
        EeachLang {
            lang: Language::English,
            range: (0x0041, 0x007A),
            name: "English".to_string(),
        },
        // EeachLang{lang:Language:: Spanish, range: (0x00BF, 0x00A1, 0x00D1), name:  "Spanish".to_string()},
        EeachLang {
            lang: Language::Other,
            range: (0x00, 0x10FFFF),
            name: "Other".to_string(),
        },
    ];
    // println!("{:?}", my_vec);
    let mut a: Language = Language::Thai;
    let mut b = "".to_string();
    a = find_lang('ก', &my_vec);
    b = tell_lang(&a, &my_vec);
    println!("{}", b)
}

//d.Build a function which, given a unicode value,
//scans the table and finds out to which language that character belong -
//returning the enumerated type.

fn find_lang(c: char, table: &Vec<EeachLang>) -> Language {
    let mut char_lang: Language = Language::Thai;
    for i in table {
        if c as u32 >= i.range.0 && c as u32 <= i.range.1 {
            char_lang = i.lang;
            break;
        }
    }
    char_lang
}

// given a language, returns a string describing it.
fn tell_lang(each_lang: &Language, table: &Vec<EeachLang>) -> String {
    let mut name_lang = "".to_string();
    for i in table {
        if each_lang == &i.lang {
            name_lang = i.name.clone();
            break;
        }
    }
    name_lang
}

// fn main() {
//     let mut char = String::new();
//     println!("Enter a character: ");
//     std::io::stdin()
//         .read_line(&mut char)
//         .expect("Failed to read line");
//     let char = char.trim().chars().next().unwrap();

//     match char {
//         'a'..='z' => println!("English"),
//         'A'..='Z' => println!("English"),
//         'ء'..='ي' => println!("Arabic"),
//         'ا'..='ە' => println!("Arabic"),
//         'ぁ'..='ん' => println!("Japanese"),
//         'ァ'..='ヶ' => println!("Japanese"),
//         'ㄱ'..='ㅎ' => println!("Korean"),
//         _ => println!("Unknown"),
//     }
// }
