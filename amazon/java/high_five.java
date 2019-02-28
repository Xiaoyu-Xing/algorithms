import java.util.*;
class Result{
	int id;
	int value;
	public Result(int id, int value){
		this.id = id;
		this.value = value;
	}
}

// Time complexity, n is the review for each id, m is the id number, O(m*n + m*nlogn)
// space, O(m*n) or total number of element is the passed-in array
public class High_Five {
	public static Map<Integer, Double> getHighFive(Result[] results){
	Map<Integer, Double> map = new HashMap<>();
	//这里pValue的命名,就是每个person都有哪些value。
	Map<Integer, ArrayList<Integer>> pValue = new HashMap<>();
	//对照着ID把成绩塞给对应的人。
	for (Result res : results){
		int id = res.id;
		if (pValue.containsKey(id)){
			//这里curL表示current List
			ArrayList<Integer> curL = pValue.get(id);
			curL.add(res.value);
			pValue.put(id, curL);
		}
		else {
			ArrayList<Integer> curL = new ArrayList<>();
			curL.add(res.value);
			pValue.put(id, curL);
		}
	}
	for (Integer id : pValue.keySet()){
		ArrayList<Integer> list = pValue.get(id);
		//这里写法有些风骚了,就是懒的重写comparator
		Collections.sort(list);
		Collections.reverse(list);
		double value = 0;
		for (int k = 0; k < 5; k++){
			value += list.get(k);
		}
		value = value/5.0;
		map.put(id, value);
	}
	return map;
}
}

// Better, priority queue, n is average review in each id, m is number of id, time complexity O((n-5)*log5*m + m*5*log5)
// space: O(m*5)
public static Map<Integer, Double> getHighFive(Result[] results){
    Map<Integer, Double> result = new HashMap<>();
    Map<Integer, PriorityQueue<Integer>> map = new HashMap<>();
    for (Result res : results) {
        if (map.containsKey(res.id)) {
            PriorityQueue<Integer> heap = map.get(res.id);
            heap.offer(res.val);
            if (heap.size() > 5) {
                heap.poll();
            }
            map.put(res.id, heap);
        } else {
            PriorityQueue<Integer> heap = new PriorityQueue<>(new Comparator<Integer> () {
            	@Override
                public int compare (Integer i1, Integer i2) {
                    return i1 - i2;
                }
            });
            heap.offer(res.val);
            map.put(res.id, heap);
        }
    }
    for (Integer id : map.keySet()) {
        double sum = 0;
        PriorityQueue<Integer> heap = map.get(id);
        while (!heap.isEmpty()) {
            sum += map.get(id).poll();
        }
        sum /= 5.0d;
        result.put(id, sum);
    }
    return result;
}
