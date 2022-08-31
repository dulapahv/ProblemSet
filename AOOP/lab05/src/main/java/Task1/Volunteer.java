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
public class Volunteer extends StaffMember {
 //-----------------------------------------------------------------
    // Sets up a volunteer using the specified information.
    //-----------------------------------------------------------------

    public Volunteer(String eName, String eAddress, String ePhone) {
        super(eName, eAddress, ePhone);
    }
 //-----------------------------------------------------------------
    // Returns a zero pay value for this volunteer.
    //-----------------------------------------------------------------

    public double pay() {
        return 0.0;
    }
}
