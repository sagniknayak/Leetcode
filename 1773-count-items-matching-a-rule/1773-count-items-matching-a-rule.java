class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int ctr = 0;
        int posi = 0;
        switch(ruleKey) {
            case "type":    posi = 0;
                            break;
            case "color":   posi = 1;
                            break;
            case "name":    posi = 2;
        }
        System.out.println(posi);
        for(List<String> item: items) {
            if(item.get(posi).equals(ruleValue))
                ctr++;
        }
        return ctr;
    }
}