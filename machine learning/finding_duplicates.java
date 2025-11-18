import java.util.HashMap;

public class finding_duplicates {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> counts=new HashMap<>();
        for (int i : nums){
            counts.put(i,0);
        }
        for (int j:nums){
            if (counts.get(j)>0) return true;
        }return false;
    }
}

    
