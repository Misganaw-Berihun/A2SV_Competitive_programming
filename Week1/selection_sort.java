// { Driver Code Starts
import java.util.*;

class GFG
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t>0)
		{
			int n = sc.nextInt();
			int arr[] = new int[n];
			for(int i=0;i<n;i++)
			{
				arr[i] = sc.nextInt();
			}

			Solution obj = new Solution();
			obj.selectionSort(arr, n);

			for(int i=0;i<n;i++)
		    	System.out.print(arr[i]+" ");
		    System.out.println();
			t--;
		}

	}
}
// } Driver Code Ends



/*
*My Solutuion
**/
class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        int minIdx = i ;

        for(int j = i + 1; j < arr.length; j++){
            if(arr[j] < arr[minIdx])
                minIdx = j;
        }
        return minIdx;
	}

	void selectionSort(int arr[], int n)
	{
	    //code here
	    for( int i = 0; i < n; i++){
	        int minIdx = select(arr,i);
	        int temp = arr[minIdx];
	        arr[minIdx] = arr[i];
	        arr[i] = temp;
	    }
	}
}