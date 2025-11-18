class anagram{
    public static boolean isAnagram(String s, String t) {
        int[] counts1=new int[26];
        int[] counts2=new int[26];
        int a=97;
        char[] arrs=s.toCharArray();
        char[] arrt=t.toCharArray();
        
        for (int i=0;i<arrs.length;i++){
            counts1[(int) arrs[i]-a]++;
        }
        for (int j=0;j<arrt.length;j++){
            counts2[(int) arrt[j]-a]++;
        }
        for (int k=0;k<26;k++){
            if (counts1[k]!=counts2[k]) return false;
        }
        return true;
    }
    public static void main(String args[]){
        System.out.println(isAnagram("hi","ih"));
    }
}
