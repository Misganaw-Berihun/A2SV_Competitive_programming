class Solution {
    public int[][] kClosest(int[][] points, int k) {

        int[][] kMaxDist = new int[k][points[0].length];
        double maxSqDistance;
        double currSqDistance;

        int minIndex;

        for(int i = points.length - 1; i > 0; i--){
            minIndex = i;
            minSqDistance =  Math.pow(points[i][0] , 2.0) +  Math.pow(points[i][1],2.0) ;

            //finding the smallest distances and puting them at the end
            for(int j = i - 1; j >= 0; j--){
                currSqDistance = Math.pow(points[j][0] , 2.0) + Math.pow(points[j][1],2.0) ;
                    if(minSqDistance > currSqDistance){
                        minIndex = j;
                        minSqDistance = currSqDistance;
                    }
                }

            swap(points,minIndex, i);
        }

        int kthIdx = 0;
        for(int idx = points.length - k ; idx < points.length ; idx++){
            kMaxDist[kthIdx++] = points[idx];
        }

        return kMaxDist;
    }

    public void swap(int [][] points, int idx1, int idx2){
        int [] temp = points[idx1];
        points[idx1] = points[idx2];
        points[idx2] = temp;
    }
}
