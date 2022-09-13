use std::fs::File;
use std::io::BufRead;
use std::{fs, io};

struct freq_table_entry {
    letter: char,
    count: u64,
    frequency: f64,
}

// This function will update your freq_table ...
// maybe it needs an extra argument
fn unpack_text_line(line: String, table: &mut Vec<freq_table_entry>) -> u64 {
    let mut nc: u64 = 0;
    'chars: for c in line.chars() {
        'tablecheck: for i in 0..table.len() {
            if table[i].letter == c {
                nc += 1;
                table[i].count += 1;
                continue 'chars;
            }
        }
        table.push(freq_table_entry {
            letter: c,
            count: 1,
            frequency: 0.0,
        });
    }
    nc
}

fn read_text_line() -> String {
    print!("Text to be processed ");
    let mut buffer = String::new();
    let result = io::stdin().read_line(&mut buffer);
    eprintln!("Buffer ({}) [{}]", buffer.len(), buffer);
    buffer
}

// Some other useful functions, eg
// calc_fractions -- to calculate the fracctions for each letter
fn calc_fractions(table: &mut Vec<freq_table_entry>) {
    let mut total: u64 = 0;
    for i in 0..table.len() {
        total += table[i].count;
    }
    for i in 0..table.len() {
        table[i].frequency = (table[i].count as f64 / total as f64);
    }
}

// print_report - print table in readable form
fn print_report(table: &Vec<freq_table_entry>) {
    for i in table {
        println!(
            "{}\t{}\t{}\t{}",
            i.letter,
            i.letter.escape_unicode(),
            i.count,
            i.frequency
        );
    }
}

// add_summary - add useful summary - # useful chars, #other spaces, punctuation, non-Thai letter
fn add_summary(table: &Vec<freq_table_entry>) {
    let mut useful: u64 = 0;
    let mut other: u64 = 0;
    for i in table {
        if i.letter == ' '
            || i.letter == '.'
            || i.letter == ','
            || i.letter == '!'
            || i.letter == '?'
            || i.letter == '-'
            || i.letter == '('
            || i.letter == ')'
            || i.letter == '"'
            || i.letter == '\''
            || i.letter == ':'
            || i.letter == ';'
            || i.letter == '0'
            || i.letter == '1'
            || i.letter == '2'
            || i.letter == '3'
            || i.letter == '4'
            || i.letter == '5'
            || i.letter == '6'
            || i.letter == '7'
            || i.letter == '8'
            || i.letter == '9'
        {
            useful += i.count;
        } else {
            other += i.count;
        }
    }
    println!(
        "{} {} {}",
        useful,
        other,
        table.len() as u64 - useful - other
    );
}

//     Most frequent letter
fn most_frequent(table: &Vec<freq_table_entry>) {
    let mut max: u64 = 0;
    let mut max_letter: char = ' ';
    for i in table {
        if i.count > max {
            max = i.count;
            max_letter = i.letter;
        }
    }
    println!("{}\t{}\t{}", max_letter, max_letter.escape_unicode(), max);
}

fn read_lines(filename: &str) -> io::Result<io::Lines<io::BufReader<File>>> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    println!("Character Frequencies");
    let mut ix: u64 = 0;
    // Construct and empty table with vector
    let mut freq_table: Vec<freq_table_entry> = Vec::new();
    let infile = fs::File::open("test.txt").expect("Unable to open file");
    let lines = io::BufReader::new(infile).lines();
    // loop through the text
    for line in lines {
        let line = line.unwrap();
        eprintln!("Text [{}]", line);
        if line.len() == 0 {
            continue;
        } else {
            let nc = unpack_text_line(line, &mut freq_table);
            ix += 1;
        }
    }
    eprintln!("\n{} lines processed", ix);
    calc_fractions(&mut freq_table);
    print_report(&freq_table);
    most_frequent(&freq_table);
}
