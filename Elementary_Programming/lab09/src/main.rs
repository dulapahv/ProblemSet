fn main() {
    /*
    A.	Take the supplied text, read it (using stdin is recommended)
    */

    /* Read from stdin */
    // let mut input = String::new();
    // std::io::stdin().read_line(&mut input).expect("Failed to read line");

    /* Read from a file */
    // add later along the lab
    let mut input = String::new();
    let mut file = std::fs::File::open("input.txt").expect("Failed to open file");
    std::io::Read::read_to_string(&mut file, &mut input).expect("Failed to read file");

    /*
    a.	You should build an enumerated type containing readable labels for each language.
    */
    #[derive(Copy, Clone, Debug, PartialEq, Eq)]
    enum Language {
        English,
        Thai,
        Japanese,
        Chinese,
        Korean,
        Burmese,
        ASCII,   // add later along the lab
        Unicode, // add later along the lab
    }

    /*
    b.	Create a struct containing the enumerated type, the range of unicodes
    used by that language and a string used to print the name of that language.
    */
    struct LanguageInfo {
        language: Language,
        range: (u32, u32),
        name: String,
    }

    /*
    c.	Build a table containing entries for these structs.
    */
    let languages = vec![
        LanguageInfo {
            language: Language::English,
            range: (0x20, 0x7E),
            name: "English".to_string(),
        },
        LanguageInfo {
            language: Language::Thai,
            range: (0x0E00, 0x0E7F),
            name: "Thai".to_string(),
        },
        LanguageInfo {
            language: Language::Japanese,
            range: (0x3040, 0x309F),
            name: "Japanese".to_string(),
        },
        LanguageInfo {
            language: Language::Chinese,
            range: (0x4E00, 0x9FFF),
            name: "Chinese".to_string(),
        },
        LanguageInfo {
            language: Language::Korean,
            range: (0xAC00, 0xD7AF),
            name: "Korean".to_string(),
        },
        LanguageInfo {
            language: Language::Burmese,
            range: (0x1000, 0x109F),
            name: "Burmese".to_string(),
        },
        LanguageInfo {
            // add later along the lab
            language: Language::ASCII,
            range: (0x00, 0x7F),
            name: "ASCII".to_string(),
        },
        LanguageInfo {
            // add later along the lab
            language: Language::Unicode,
            range: (0x00, 0x10FFFF),
            name: "Unicode".to_string(),
        },
    ];

    /* Check point A(c) */

    /*
    d.	Build a function which, given a unicode value, scans the table and finds
    out to which language that character belong - returning the enumerated type.
    */
    fn get_language(c: char, languages: &Vec<LanguageInfo>) -> Language {
        for language in languages {
            if c as u32 >= language.range.0 && c as u32 <= language.range.1 {
                return language.language;
            }
        }
        panic!("No language found for character {}", c);
    }

    /* Check point A(d) */

    /*
    e.	You will need another function which, given a language, returns a string describing it.
    */
    fn get_language_name(language: Language, languages: &Vec<LanguageInfo>) -> String {
        for lang in languages {
            if lang.language == language {
                return lang.name.clone();
            }
        }
        panic!("No language found for language {:?}", language);
    }

    /* Check point A(e) */

    /*
    a)	Make an initial table which contains some expected unicodes
    */
    // No need?
    // let mut table = vec![
    //     (0x20, 0x7E, Language::English),
    //     (0x0E00, 0x0E7F, Language::Thai),
    //     (0x3040, 0x309F, Language::Japanese),
    //     (0x4E00, 0x9FFF, Language::Chinese),
    //     (0xAC00, 0xD7AF, Language::Korean),
    //     (0x1000, 0x109F, Language::Burmese),
    //     (0x00, 0x7F), // Language::ASCII),
    //     (0x00, 0x10FFFF), // Language::Unicode),
    // ];

    /* Check point B(a) */

    /*
    b)	Read the test file, scan the table to find initially known languages (skip them) and list unicodes for languages not yet known.
    */
    // No need?
    // for c in input.chars() {
    //     let language = get_language(c, &languages);
    //     let mut found = false;
    //     for entry in &table {
    //         if entry.2 == language {
    //             found = true;
    //             break;
    //         }
    //     }
    //     if !found {
    //         let mut start = c as u32;
    //         let mut end = c as u32;
    //         for c in input.chars() {
    //             let language = get_language(c, &languages);
    //             if language == language {
    //                 end = c as u32;
    //             } else {
    //                 break;
    //             }
    //         }
    //         table.push((start, end, language));
    //     }
    // }

    /*
    c)	Use the output from this program to look up remaining unicodes and add more entries to your table.
    */
    // WHAT?!?!
    // table.push((0x00A0, 0x00FF, Language::English));
    // table.push((0x0E80, 0x0EFF, Language::Thai));
    // table.push((0x30A0, 0x30FF, Language::Japanese));
    // table.push((0x3400, 0x4DBF, Language::Chinese));

    /* Check point B(c) */

    /*
    d)	Repeat until all characters in the test file are assigned to a language.
    */
    // Isn't it done in B(b)?

    /*
    C.	Now write a program which reads the test file and produces a report, showing, for each line, which languages were used in that line and how many characters from that language were found. (Work out which type to use to create this report!)
        So your report might look like:

        Line 1: Thai (10), ASCII (4)
        Line 2: Chinese (11), Japanese (4), ASCII (10), …..
        Line 3: ….
    */
    for (i, line) in input.lines().enumerate() {
        let mut counts = std::collections::HashMap::new();
        for c in line.chars() {
            let language = get_language(c, &languages);
            let name = get_language_name(language, &languages);
            *counts.entry(name).or_insert(0) += 1;
        }
        let mut report = String::new();
        for (name, count) in counts {
            report.push_str(&format!("{} ", name));
            report.push_str(&format!("({}), ", count));
        }
        // remove last 2 characters (", ") from report String
        report.pop();
        report.pop();
        println!("Line {}: {}", i + 1, report);
    }
}
