import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    fun solution(n: Int, k: Int, enemy: IntArray): Int {
        var N = n
        var K = k
        var cleared: PriorityQueue<Int> = PriorityQueue<Int>(Collections.reverseOrder())
        var answer: Int = 0
        var cur: Int = 0
        while(N >= 0 && cur < enemy.size){
            N -= enemy[cur]
            cleared.offer(enemy[cur])
            if(N < 0 && K > 0){
                N += cleared.poll()
                K -= 1
            }
            if (N >= 0){
                cur += 1
            }
        }
        return cur
    }
}