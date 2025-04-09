// https://leetcode.com/problems/fizz-buzz/
public class FizzBuzz {
    class Solution {
        public List<String> fizzBuzz(int n) {
            List<String> answer = new ArrayList<>(n);

            for (int i = 1 ; i <=n ; i++){
                boolean divby3 = i % 3 == 0;
                boolean divby5 = i % 5 == 0;

                if(divby3 && divby5)
                    answer.add("FizzBuzz");
                else if (divby3)
                    answer.add("Fizz");
                else if (divby5)
                    answer.add("Buzz");
                else
                    answer.add(String.valueOf(i));
            }
            return answer;
            /advch\
        }
    }
}
