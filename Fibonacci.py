import java.util.Scanner;

public class LabProgram {
   
   public static int fibonacci(int n) {
      if (n < 0) return -1;
      if (n == 0) return 0;
      
      int a = 0, b = 1;
      for (int i = 1; i < n; ++i) {
         int sum = a + b;
         a = b;
         b = sum;
      }
      return b;
      
   }
   
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int startNum;
      
      startNum = scnr.nextInt();
      System.out.println("fibonacci(" + startNum + ") is " + fibonacci(startNum));
   }
}
