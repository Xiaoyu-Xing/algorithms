// Kruskal + union find

import java.util.*

class Connection {
	String node1;
	String node2;
	int cost;
	public Connection(String a, String b, int c) {
		node1 = a;
		node2 = b;
		cost = c;
	}
}

public class CityConnections {
	private static int unionCount;
	public static ArrayList<Connection> getLowCost(ArrayList<Connection> connections) {
		if (connections == null || connections.size() == 0) {
			return new ArrayList<Connection>();
		}
		ArrayList<Connection> result = new ArrayList<>(); // Store result
		Map<String, Integer> map = new HashMap<>();
		Collections.sort(connections, new Comparator<Connection>() {
			@Override
			public int compare(Connection a, Connection b) {
				return a.cost - b.cost;
			}
		});

		unionCount = 0;
		for (Connection c : connections) {
			String a = c.node1;
			String b = c.node2;
			if (union(map, a, b)) { // connect them if not
				result.add(c);
			}
		}

		String check = connections.get(0).node1;
		int union = map.get(check);
		for (String s : map.keySet()) {
			if (map.get(s) != union) {
				return new ArrayList<Connection>();
			}
		}

		Collections.sort(connections, new Comparator<Connection>(){
			@Override
			public int compare(Connection a, Connection b) {
				if (a.node1.equals(b.node1)) {
					return a.node2.compareTo(b.node2);
				}
				return a.node1.compareTo(b.node1);
			}
		});
	}

}
public static boolean union(Map<String, Integer> map, String a, String b) {
	if (!map.containsKey(a) || !map.containsKey(b)) {
		map.put(a, unionCount);
		map.put(b, unionCount);
		unionCount++;
		return true;
	}
	if (!map.containsKey(a) && map.containsKey(b)) {
		map.put(a, map.get(b));
		return true;
	}
	if (map.containsKey(a) && !map.containsKey(b)) {
		map.put(b, map.get(a));
		return true;
	}
	// Both exist
	aID = map.containsKey(a);
	bID = map.containsKey(b);
	if (aID == bID) return false; // already connected
	for (String s : map.keySet()) {
		if (map.get(s) == bID) {
			map.put(s, aID);
		}
	}
	return true;
}