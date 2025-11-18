class Solution{
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val graph = mutableMapOf<Int, MutableList<Int>>()
        for (node in 0 until numCourses){
            graph.put(node, mutableListOf())
        }
        for (edge in prerequisites){
            graph.get(edge[1])!!.add(edge[0])
        }
        println(graph)
        //return true
        val visited = mutableSetOf<Int>()
        val currentStack = mutableSetOf<Int>()
        fun cycleDetect(start: Int): Boolean{
            if (start in visited) return true
            if (start in currentStack) return false
            currentStack.add(start)
            for (neighbour in graph[start]!!){
                if (! cycleDetect(neighbour)) return false
            }
            visited.add(start)
            currentStack.remove(start)
            return true
        }
        for (node in 0 until numCourses){
            if(!cycleDetect(node)) return false
        }
        return true
    }
}
fun main(){
    val obj = Solution()
    obj.canFinish(5, arrayOf(intArrayOf(1,2), intArrayOf(3,4), intArrayOf(1,4), intArrayOf(4,2)))
}