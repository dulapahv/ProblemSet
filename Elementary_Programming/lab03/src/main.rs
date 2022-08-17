use std::fs::File;
use std::io::Write;
use chrono::Local;
use chrono::DateTime;
use chrono::Utc;
use chrono::Datelike;
 5
fn main() {
    let example = "Example string";
    let unicode_example = "\u{0E01}\u{0E02}\u{0E31}\u{0E01}";
    println!("{}", unicode_example);
    write_my_name();
}

fn write_my_name() -> std::io::Result<()> {
    let mut f = File::create("name1.txt")?;
    let my_name = "\u{0e14}\u{0e38}\u{0e25}\u{0e1e}\u{0e48}\u{0e32}\u{0e2b}\u{0e4c}";
    let s_id: i64 = 650000011;
    let utc_here: DateTime<Utc> = Utc::now();
    let local: DateTime<Local> = Local::now();
    let year = utc_here.year();
    let e = if let Err(e) = write!(
        f,
        "My name: {}\nStudent ID: {}\nUTC here: {}\nLocal: {}\nYear: {}",
        my_name, s_id, utc_here, local, year
    ) {
        e
    } else {
        todo!()
    };
    Ok(())
}
