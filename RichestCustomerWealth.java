public class RichestCustomerWealth {
    class Solution {
        public int maximumWealth(int[][] accounts) {
            int maxWealthSoFar = 0;

            for(int[] customer : accounts){
                int currentCustomerWealth = 0;

                for (int bank : customer){
                    currentCustomerWealth += bank;
                }

                maxWealthSoFar = Math.max(currentCustomerWealth,maxWealthSoFar);
            }
            return maxWealthSoFar;
        }
    }

}
