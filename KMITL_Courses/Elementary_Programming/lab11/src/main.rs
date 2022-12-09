use std::io;
use std::io::Write;

#[derive(Debug)]
enum NumberFlags {
    Local,
    International,
    LikelyScammer,
    Special,
}

#[derive(Debug)]
struct TelephoneNumber {
    flags: Vec<NumberFlags>,
    number: String,
    idd_code: String,
    note: Option<String>,
}

#[derive(Debug)]
enum CreditCardProvider {
    Visa,
    MasterCard,
    AmericanExpress,
    Discover,
    DinersClub,
    JCB,
    Unknown,
}

#[derive(Debug)]
struct CreditCard {
    issuer: CreditCardProvider,
    number: String,
}

fn convert_to_ascii_number(number: &str) -> String {
    let mut ascii_number = String::new();
    for c in number.chars() {
        match c {
            '๐' => ascii_number.push('0'),
            '๑' => ascii_number.push('1'),
            '๒' => ascii_number.push('2'),
            '๓' => ascii_number.push('3'),
            '๔' => ascii_number.push('4'),
            '๕' => ascii_number.push('5'),
            '๖' => ascii_number.push('6'),
            '๗' => ascii_number.push('7'),
            '๘' => ascii_number.push('8'),
            '๙' => ascii_number.push('9'),
            _ => ascii_number.push(c),
        }
    }
    ascii_number
}

fn validate_card(number: &str) -> bool {
    let mut sum = 0;
    let mut alt = false;
    for c in number.chars().rev() {
        match c.to_digit(10) {
            Some(digit) => {
                let mut digit = digit;
                if alt {
                    digit *= 2;
                    if digit > 9 {
                        digit -= 9;
                    }
                }
                sum += digit;
                alt = !alt;
            }
            None => return false,
        }
    }
    sum % 10 == 0
}

fn parse_credit_card(number: &str) -> Result<CreditCard, String> {
    let number = number.trim();
    if !validate_card(number) {
        return Err("Invalid card number".to_string());
    }

    let mut issuer = CreditCardProvider::Unknown;

    if number.len() == 15 && number.starts_with("34") || number.starts_with("37") {
        issuer = CreditCardProvider::AmericanExpress;
    } else if number.len() == 16 && number.starts_with("51")
        || number.starts_with("52")
        || number.starts_with("53")
        || number.starts_with("54")
        || number.starts_with("55")
    {
        issuer = CreditCardProvider::MasterCard;
    } else if number.len() == 16 && number.starts_with("6011") {
        issuer = CreditCardProvider::Discover;
    } else if number.len() == 16 && number.starts_with("4") {
        issuer = CreditCardProvider::Visa;
    } else if number.len() == 16 && number.starts_with("36") {
        issuer = CreditCardProvider::DinersClub;
    } else if number.len() == 16 && number.starts_with("35") {
        issuer = CreditCardProvider::JCB;
    } else {
        issuer = CreditCardProvider::Unknown;
    }

    Ok(CreditCard {
        issuer: issuer,
        number: number.to_string(),
    })
}

fn parse_phone_number(number: &str) -> Result<TelephoneNumber, String> {
    let mut number = number.to_string();
    let mut idd_code = String::new();
    let mut flags: Vec<NumberFlags> = vec![];
    number = number.trim().to_string();

    number.retain(|c| !c.is_whitespace());

    if number.starts_with("+") {
        number.remove(0);

        let note = number.chars().skip(11).collect::<String>();
        if note.is_empty() {
            idd_code = number.chars().take(2).collect();
            number.drain(0..2);
        } else if note.chars().last().unwrap().is_numeric() {
            idd_code = number.chars().take(3).collect();
            number.drain(0..3);
        } else if note.chars().last().unwrap().is_alphabetic() {
            idd_code = number.chars().take(2).collect();
            number.drain(0..2);
        } else {
            return Err(String::from("Invalid number"));
        }
    } else {
        if number.starts_with("0") {
            number.remove(0);
            idd_code = "66".to_string();
        } else {
            return Err(String::from("Invalid number"));
        }
    }

    if idd_code == "66" {
        flags.push(NumberFlags::Local);
    } else {
        if idd_code == "657" {
            flags.push(NumberFlags::Local);
            flags.push(NumberFlags::LikelyScammer);
        } else {
            flags.push(NumberFlags::International);
        }
    }

    let note = number.chars().skip(9).collect::<String>();
    let note = if note.is_empty() {
        None
    } else {
        flags.push(NumberFlags::Special);
        number.truncate(9);
        Some(note)
    };

    Ok(TelephoneNumber {
        flags,
        number,
        idd_code,
        note,
    })
}

fn fancy_print_number(number: TelephoneNumber) {
    println!("Number: {}", number.number);
    println!("IDD Code: {}", number.idd_code);
    println!("Flags: {:?}", number.flags);
    if let Some(note) = number.note {
        println!("Note: {}", note);
    }
}

fn input_number() -> TelephoneNumber {
    let mut number = String::new();
    print!("Enter the telephone number: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut number)
        .expect("Failed to read line");
    let data = parse_phone_number(&number);
    //println!("Parsed number: {:?}", data);

    if data.is_err() {
        println!("Invalid number");
        input_number()
    } else {
        data.unwrap()
    }
}

fn input_credit_card() -> CreditCard {
    let mut number = String::new();
    print!("Enter the credit card number: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut number)
        .expect("Failed to read line");
    let data = parse_credit_card(&number);
    //println!("Parsed number: {:?}", data);

    if data.is_err() {
        println!("Invalid number");
        input_credit_card()
    } else {
        data.unwrap()
    }
}

fn main() {
    let number = input_number();
    fancy_print_number(number);
    let credit_card = input_credit_card();
    print!("{:?}", credit_card);
}
