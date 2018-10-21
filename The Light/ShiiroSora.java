import java.util.Scanner;

public class ShiiroSora {


    public static void main(String args[]){
        int i;
        int max=0;
        System.out.println("People entered: ");
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();

    for (i=0;i<x;i++){
        System.out.println("Times: ");
        Scanner sc = new Scanner(System.in);
        int a1=sc.nextInt();
        int a2=sc.nextInt();
        if (max<a2-a1){
            max=a2-a1+1;
        }



    }
    System.out.println("Max: "+ max);
    }
}
