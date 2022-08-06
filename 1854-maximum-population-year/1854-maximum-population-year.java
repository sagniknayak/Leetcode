class Solution {
    public int maximumPopulation(int[][] logs) {
        SortedSet<Integer> years = new TreeSet<Integer>();
        for(int[] log: logs)
            years.add(log[0]);
        Iterator<Integer> iter = years.iterator();
        int maxpop = 0, maxpopyear = 0;
        
        while(iter.hasNext()) {
            int pop = 0, year = iter.next();
            for(int[] log: logs) {
                if(log[0]<=year && year<log[1])
                    pop++;
            }
            if(pop>maxpop) {
                maxpop = pop;
                maxpopyear = year;
            }
        }
        return maxpopyear;
    }
}