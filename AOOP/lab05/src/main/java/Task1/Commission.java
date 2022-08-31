/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Commission extends Hourly {
    private double totalSales;
    private double commissionRate;
    
    public Commission(String eName, String eAddress, String ePhone,
            String socSecNumber, double rate, double commissionRate) {
        super(eName, eAddress, ePhone, socSecNumber, rate);
        this.commissionRate = commissionRate;
    }
    
    public void addSales (double totalSales) {
        this.totalSales += totalSales;
    }
    
    @Override
    public double pay() {
        double payment = super.pay() + (totalSales * commissionRate);
        totalSales = 0;
        return payment;
    }
    
    @Override
    public String toString() {
        String result = super.toString();
        result += "\nTotal Sales: " + totalSales;
        return result;
    }
}
