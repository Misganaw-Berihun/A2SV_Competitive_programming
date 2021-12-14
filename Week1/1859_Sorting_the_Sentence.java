class Solution {
    public String sortSentence(String s) {
         String [] strArr = s.split(" ");
        String [] sortedArr = new String[strArr.length];

        int wPos;
        int idx;
        for(int i = 0; i < strArr.length; i++){
          idx = strArr[i].length() - 1; //find index of digit
          wPos = strArr[i].charAt(idx) - '0' - 1;//convert the char index to int then subtract 1

          //store the value of substring without digit at sortedArr at index one minus postion number
          sortedArr[wPos] = strArr[i].substring(0,idx);
        }

        String sortedSentence = "";
        for(String str: sortedArr){
            sortedSentence += ( str + " ");
        }
        idx = sortedSentence.length() - 1;
        sortedSentence = sortedSentence.substring(0, idx); // removing the last space character

        return sortedSentence;
    }
}
