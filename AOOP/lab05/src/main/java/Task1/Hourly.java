/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Task1;

/**
 *
 * @author boonjv
 */
public class Hourly extends Employee {

    private int hoursWorked;
 //-----------------------------------------------------------------
    // Sets up this hourly employee using the specified information.
    //-----------------------------------------------------------------

    public Hourly(String eName, String eAddress, String ePhone,
            String socSecNumber, double rate) {
        super(eName, eAddress, ePhone, socSecNumber, rate);
        hoursWorked = 0;
    }
 //-----------------------------------------------------------------
    // Adds the specified number of hours to this employee's
    // accumulated hours.
    //-----------------------------------------------------------------

    public void addHours(int moreHours) {
        hoursWorked += moreHours;
    }
 //-----------------------------------------------------------------
    // Computes and returns the pay for this hourly employee.
    //-----------------------------------------------------------------

    public double pay() {
        double payment = payRate * hoursWorked;
        hoursWorked = 0;
        return payment;
    }
 //-----------------------------------------------------------------
    // Returns information about this hourly employee as a string.
    //-----------------------------------------------------------------

    public String toString() {
        String result = super.toString();
        result += "\nCurrent hours: " + hoursWorked;
        return result;
    }
}
