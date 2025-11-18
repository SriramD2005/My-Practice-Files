import java.util.*;
class sliding_window {
    public static int characterReplacement(String s, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        int a = 'A';
        int l=0, r=0, res=0;
        while (r<s.length()){
            
            int nch = s.charAt(r);
            nch -= a;
            freq.put(nch,1+freq.getOrDefault(nch, 0));
            int max=0;
            for (Map.Entry<Integer,Integer> entry : freq.entrySet()){
                if (max<entry.getValue()){
                    max = entry.getValue();
                }
            }
            if (r-l+1-max<=k){
                int x = r-l+1-max;
                res =Math.max(r-l+1,res);
                System.out.println(s.charAt(r));
                System.out.println("valid:"+x);
                System.out.println(res);

                r++;
            }
            else{
                int num = s.charAt(l);
                num-=a;
                freq.put(num,freq.get(num)-1);
                l++;
            }
        }
        return res;
    }
    public static void main(String args[]){
        String s = "AABABBA";
        System.out.println(sliding_window.characterReplacement(s, 1));
    }
}
