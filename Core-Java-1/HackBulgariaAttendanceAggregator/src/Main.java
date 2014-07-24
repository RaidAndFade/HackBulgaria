import java.io.IOException;

import org.codehaus.jettison.json.JSONException;

public class Main {
    public static void main(String[] args) {
        Console consoleIn = new Console();
        final String HACKBULGARIA_API_URL = "https://hackbulgaria.com/api/";
        String option;
        while (true) {
            option = consoleIn.readLine("1) Individual attendance\n2) Attending more courses\n> ").trim();
            try {
                if (option.equals("1")) {
                    AttendanceAggregator.aggregateAttendance(HACKBULGARIA_API_URL + "checkins/");
                } else if (option.equals("2")) {
                    AttendanceAggregator.aggregateStudentsAttendingMoreCourses(HACKBULGARIA_API_URL + "students/");
                } else {
                    System.out.println("Unknown option");
                }
            } catch (JSONException | IOException e) {
                System.out.println("Invalid URL");
            }
        }
    }
}
