// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
public class NumberofStepstoReduceaNumbertoZero {
    class Solution {
        //test changes
        public int numberOfSteps(int num) {
            int steps=0;

            while(num > 0){
                if(num%2 == 0){
                    num = num/2;

                }
                else{
                    num = num-1;

                }
                steps++;
            }
            return steps;
        }
    }
}

