class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> s =new ArrayList<>();
        for(int i = 1; i <= n; i++){
            s.add(fBuzz(i));
        }
        return s;
    }

    private String fBuzz(int n){
        if(n %3 == 0 && n % 5==0)
            return "FizzBuzz";
        else if(n % 3 == 0)
            return "Fizz";
        else if(n % 5 == 0)
            return "Buzz";
        else
            return Integer.toString(n);
    }
}
