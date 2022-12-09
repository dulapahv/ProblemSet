/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package Task1;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

import javax.swing.*;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class DrawApp {
    //Your application window

    private static JFrame frame;

    //Where you can draw stuff
    private static JPanel canvas;

    //Where your pen colour changing buttons will reside
    private static JPanel colorPalette;

    //Your default pen color. You will change this when different pen colour buttons are clicked.
    private static Color currentColor = Color.BLACK;

    //The last recorded x,y positions of your mouse
    private static int lastMouseX, lastMouseY;

    public static void createAndShowGUI() {
        //Step 1:
        //a. Create the window with the title you want and set this to the JFrame frame.
        //b. Give your window a preferred size using methods provided by JFrame
        frame = new JFrame("Draw Application");
        frame.setSize(750, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        //Step 2a:
        //a. Make a JPanel for your canvas
        canvas = new JPanel();
        //b. Give your canvas a preferred size
        canvas.setPreferredSize(new Dimension(750, 400));
        //c. Set your canvas's background colour
        canvas.setBackground(Color.WHITE);
        //d. Add your canvas JPanel to your JFrame window
        frame.add(canvas);
        //Step 2b:
        //a. Make the JPanel to hold the colour palette
        colorPalette = new JPanel();
        //b. Add your colour palette JPanel to your window
        frame.add(colorPalette, BorderLayout.SOUTH);
        //Step 3:
        //a. Make each of your pen colour buttons
        JButton red = new JButton("Red");
        JButton orange = new JButton("Orange");
        JButton yellow = new JButton("Yellow");
        JButton green = new JButton("Green");
        JButton blue = new JButton("Blue");
        JButton indigo = new JButton("Indigo");
        JButton purple = new JButton("purple");
        JButton black = new JButton("Black");
        JButton white = new JButton("White");
        //b. Then add it to your palette JPanel
        colorPalette.add(red);
        colorPalette.add(orange);
        colorPalette.add(yellow);
        colorPalette.add(green);
        colorPalette.add(blue);
        colorPalette.add(indigo);
        colorPalette.add(purple);
        colorPalette.add(black);
        colorPalette.add(white);
        //add event listener for mouse clicks to the JFrame
        frame.addMouseListener(
                new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                //Step 4:
                //get the last positions of your mouse cursor
                lastMouseX = e.getX();
                lastMouseY = e.getY();
            }
        }
        );

        //add event listener for mouse movement to the JFrame
        frame.addMouseMotionListener(
                new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
                //Step 5:
                //a. get the JFrame's graphics context
                Graphics g = frame.getGraphics();
                //b. get the current mouse cursor's position
                int x = e.getX();
                int y = e.getY();
                //c. set the graphics context's drawing color to your current pen color
                g.setColor(currentColor);
                //d. using the graphics context's "pen", draw a line from your last mouse position to your current one
                g.drawLine(lastMouseX, lastMouseY, x, y);
                //e. then set your last position to your current one
                lastMouseX = x;
                lastMouseY = y;
            }
        }
        );

        //Step 6: Add action listeners to each of your color buttons
        // someButton.addActionListener
        // (
        // new ActionListener()
        // {
        // public void actionPerformed(ActionEvent e) 
        // {  
        // set pen colour
        // }
        // }
        // );
        red.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.RED;
            }
        }
        );
        orange.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.ORANGE;
            }
        }
        );
        yellow.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.YELLOW;
            }
        }
        );
        green.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.GREEN;
            }
        }
        );
        blue.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.BLUE;
            }
        }
        );
        indigo.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.CYAN;
            }
        }
        );
        purple.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.MAGENTA;
            }
        }
        );
        black.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.BLACK;
            }
        }
        );
        white.addActionListener(
                new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = Color.WHITE;
            }
        }
        );

        //Step 7: Display the window. Simply uncommenting the code below
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    //Don't worry about this, it works.
    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(
                new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        }
        );
    }
}
