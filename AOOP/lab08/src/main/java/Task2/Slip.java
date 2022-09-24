/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Slip {

    private int slipId;
    private int width;
    private double slipLength;

    private static int numberOfSlips = 0;

    // static constants for default attribute values
    private static final int DEFAULT_WIDTH = 12;
    private static final int DEFAULT_SLIP_LENGTH = 25;

    // static constants for data validation
    private static final int MAXIMUM_NUMBER_OF_SLIPS = 50;
    private static final int VALID_SLIP_WIDTHS[] = {10, 12, 14, 16};

    // constructor with 3 parameters
    public Slip(int anId, int aWidth, double aSlipLength) throws Exception {

        // invoke setters to populate attributes
        setSlipId(anId);
        setWidth(aWidth);
        setSlipLength(aSlipLength);
        numberOfSlips++;
    }

    // constructor with 1 parameter
    public Slip(int anId) throws Exception {
        // invoke 3-parameter constructor with default width & slip values
        this(anId, DEFAULT_WIDTH, DEFAULT_SLIP_LENGTH);
    }

    // custom method to lease a Slip
    public double leaseSlip() {
        double fee;
        switch (width) {
            case 10:
                fee = 800;
                break;
            case 12:
                fee = 900;
                break;
            case 14:
                fee = 1100;
                break;
            case 16:
                fee = 1500;
                break;
            default:
                fee = 0;
        }
        return fee;
    }

    public double leaseSlip(double aDiscountPercent) {
        double fee = this.leaseSlip();
        double discountedFee = fee * (100 - aDiscountPercent) / 100;
        return discountedFee;
    }

    public void setSlipId(int andId) throws Exception {
        if (andId < 1 || andId > MAXIMUM_NUMBER_OF_SLIPS) {
            throw new Exception("Slip ID not between 1 & " + MAXIMUM_NUMBER_OF_SLIPS);
        } else {
            slipId = andId;
        }
    }

    public void setWidth(int aWidth) throws Exception {
        boolean validWidth = false;
        for (int i = 0; i < VALID_SLIP_WIDTHS.length && !validWidth; i++) {
            if (aWidth == VALID_SLIP_WIDTHS[i]) {
                validWidth = true;
            }
        }
        if (validWidth) {
            width = aWidth;
        } else {
            throw new Exception("Invalid Slip width");
        }
    }

    public void setSlipLength(double aSlipLength) {
        slipLength = aSlipLength;
    }

    public int getSlipId() {
        return slipId;
    }

    public int getWidth() {
        return width;
    }

    public double getSlipLength() {
        return slipLength;
    }

    public static int getNumberOfSlips() {
        return numberOfSlips;
    }

    @Override
    public String toString() {
        String info;
        info = "Slip: Id = "
                + getSlipId() + ", Width = " + getWidth() + ", Length = " + getSlipLength();
        return info;
    }
}
