class product_except_self {
    public static int[] productExceptSelf(int[] nums) {
        //int last=nums[nums.length-1];
        int rev[]=new int[nums.length];
        rev[nums.length-1]=1;
        int prev;
        for (int i=nums.length-2;i>=0;i--){
            prev=rev[i+1];
            rev[i]=prev*nums[i+1];

    }prev=1;
    System.out.println("res:");
        int res[]=new int[nums.length];
        for (int j=0;j<nums.length;j++){
            res[j]=prev*rev[j];
            prev*=nums[j];
            }
        return res;
}  
public static void main(String args[]){
    int x[]={1,2,3,4,5,6};
    int res[]=product_except_self.productExceptSelf(x);
    //for (int i : product_except_self.productExceptSelf(x)){
        //System.out.println(i+' ');
    //}
    for (int k=0;k<res.length;k++){
        System.out.print(res[k]+" ");
    }
    
}
}