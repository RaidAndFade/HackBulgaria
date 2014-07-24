import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;

import org.codehaus.jettison.json.JSONArray;
import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

public class AttendanceAggregator {
    public static void aggregateAttendance(String url) throws MalformedURLException, JSONException, IOException {
        aggregateAttendance(new URL(url));
    }

    public static void aggregateAttendance(URL url) throws IOException, JSONException {
        String contents = getURLcontents(url);
        Map<String, Integer> map = getStudentAttendanceMap(contents);
        map = sortByValues(map);
        int i = 0;
        for (Entry<String, Integer> entry : map.entrySet()) {
            i += 1;
            System.out.println(String.format("%d) %s - %s", i, entry.getKey(), entry.getValue()));
        }
        System.out.println();
    }

    public static void aggregateStudentsAttendingMoreCourses(String url) throws IOException, JSONException {
        aggregateStudentsAttendingMoreCourses(new URL(url));
    }

    public static void aggregateStudentsAttendingMoreCourses(URL url) throws IOException, JSONException {
        String contents = getURLcontents(url);
        List<String> students = getStudentsAttendingMoreCoursesList(new JSONArray(contents));
        int i = 0;
        for (String student : students) {
            i += 1;
            System.out.println(String.format("%d) %s", i, student));
        }
        System.out.println();
    }

    public static List<String> getStudentsAttendingMoreCoursesList(JSONArray array) throws JSONException {
        List<String> outputList = new LinkedList<String>();
        for (int i = 0; i < array.length(); i++) {
            JSONObject student = array.getJSONObject(i);
            int attendedCourses = student.getJSONArray("courses").length();
            if (attendedCourses > 1) {
                outputList.add(student.getString("name"));
            }
        }
        return outputList;
    }

    public static Map<String, Integer> getStudentAttendanceMap(String array) throws JSONException {
        return getStudentAttendanceMap(new JSONArray(array));
    }

    public static Map<String, Integer> getStudentAttendanceMap(JSONArray array) throws JSONException {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < array.length(); i++) {
            String studentName = array.getJSONObject(i).getString("student_name");
            int attendanceCount = 0;
            for (int j = 0; j < array.length(); j++) {
                String otherName = array.getJSONObject(j).getString("student_name");
                if (studentName.equals(otherName)) {
                    attendanceCount += 1;
                }
            }
            if (!map.containsKey(studentName)) {
                map.put(studentName, attendanceCount);
            }
        }
        return map;
    }

    public static <K, V extends Comparable<V>> Map<K, V> sortByValues(final Map<K, V> map) {
        Comparator<K> valueComparator = new Comparator<K>() {
            @Override
            public int compare(K k1, K k2) {
                int compare = map.get(k2).compareTo(map.get(k1));
                if (compare == 0) {
                    return 1;
                } else {
                    return compare;
                }
            }
        };
        Map<K, V> sortedByValues = new TreeMap<K, V>(valueComparator);
        sortedByValues.putAll(map);
        return sortedByValues;
    }

    public static String getURLcontents(URL url) throws IOException {
        URLConnection conn = url.openConnection();
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String contents = "";
        String line;
        while ((line = br.readLine()) != null) {
            contents += line + "\n";
        }
        br.close();
        return contents;
    }
}
