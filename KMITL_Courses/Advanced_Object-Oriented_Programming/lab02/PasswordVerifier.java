public class PasswordVerifier {
	private static int MINIMUM_PASSWORD_LENGTH = 6;

	public static boolean isMinimumLength(String str) {
		if (str.length() >= MINIMUM_PASSWORD_LENGTH) {
			return true;
		} else {
			return false;
		}
	}

	public static boolean hasUpperCase(String str) {
		if (str.matches(".*[A-Z].*")) {
			return true;
		} else {
			return false;
		}
	}

	public static boolean hasLowerCase(String str) {
		if (str.matches(".*[a-z].*")) {
			return true;
		} else {
			return false;
		}
	}

	public static boolean hasDigital(String str) {
		if (str.matches(".*[0-9].*")) {
			return true;
		} else {
			return false;
		}
	}

	public static boolean hasLegalChars(String str) {
		if (str.matches("^[a-zA-Z0-9_]+$")) {
			return true;
		} else {
			return false;
		}
	}

	public static boolean isValid(String str) {
		if (isMinimumLength(str) && hasUpperCase(str) && hasLowerCase(str) && hasDigital(str) && hasLegalChars(str)) {
			return true;
		} else {
			return false;
		}
	}
}
