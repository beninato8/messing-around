/**************************************
 * 8 2 2017
 * GenMaze.java
 * @author  Nicholas Beninato
 *
 *      This program runs and gets the result of a python script to generate a random maze.
 *      The python script creates a text file and this class reads and returns the result
 *      An overloaded method is provided to create a random maze
 *          - You can create a maze with dimensions rows by cols
 *          - You can create a maze of random size set by min and max values for rows and cols
 **************************************/
import java.awt.Desktop;
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class GenMaze
{
    public static String [] genRandMaze(int cols, int rows)
    {
        return getMaze(cols, rows);
    }
    public static String [] genRandMaze(int minCol, int maxCol, int minRow, int maxRow)
    {

        int cols = ThreadLocalRandom.current().nextInt(minCol, maxCol + 1);
        int rows = ThreadLocalRandom.current().nextInt(minRow, maxRow + 1);
        return getMaze(cols, rows);
    }
    private static String [] getMaze(int cols, int rows)
    {
        String cmd = "python3 maze.py " + cols + " " + rows;
        // p(cmd);
        try
        {
            Process x = Runtime.getRuntime().exec(cmd);
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.err.println("Error waiting for file to be written");
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Error running python script");
            e.printStackTrace();
        }
        String [] maze = readLines(cols, rows);
        // p(Arrays.toString(maze));
        return maze;
    }
    private static void p(Object o)
    {
        System.out.println(o.toString());
    }
    private static String [] readLines(int num1, int num2)
    {
        num1 += 2;
        num2 += 2;
        FileReader fileReader = null;
        try 
        {
            fileReader = new FileReader("Maze_" + num1 + "x" + num2 + ".txt");        
        } catch (FileNotFoundException e) {
            System.err.println("Unable to find file:\n" + "Maze_" + num1 + "x" + num2 + ".txt");
            e.printStackTrace();
        }
        
        BufferedReader bufferedReader = new BufferedReader(fileReader);
        List<String> lines = new ArrayList<String>();
        String line = null;
        try
        {
            while ((line = bufferedReader.readLine()) != null) 
            {
                lines.add(line);
            }
            bufferedReader.close();
        } catch (IOException e) {
            System.err.println("Error reacing from file:\n" + "Maze_" + num1 + "x" + num2 + ".txt");
            e.printStackTrace();
        }
        return lines.toArray(new String[lines.size()]);
    }
}