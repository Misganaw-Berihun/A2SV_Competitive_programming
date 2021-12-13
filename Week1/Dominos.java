import java.util.Scanner;
public class Dominos{
  public static void main(String [] args){
    Scanner keyboard = new Scanner(System.in);
    int m,n,out;
    m = keyboard.nextInt();
    n = keyboard.nextInt();

    out = (m * n)/2;

    System.out.println(out);
  }
}
