class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for(int candy : candies) {
            if(max<candy)
                max = candy;
        }
        
        List<Boolean> hasMaxCandies = new ArrayList<Boolean>(candies.length);
        for(int i = 0; i < candies.length; i++) {
            hasMaxCandies.add((candies[i]+extraCandies >= max)?true:false);
        }
        return hasMaxCandies;
    }
}