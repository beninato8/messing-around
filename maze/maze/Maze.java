public class Maze
{
    public static void main (String [] args)
    {
        String [] myMaze = GenMaze.genRandMaze(7, 12);
        for (int i = 0; i < myMaze.length; i++)
        {
            p(myMaze[i]);
        }
    }
    public static void p(Object o)
    {
        System.out.println(o);
    }
}