public class LogMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    private Text user = new Text();
    private LongWritable duration = new LongWritable();

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        // Parse the log line to extract user ID, login timestamp, and logout timestamp
        String[] parts = line.split("\\s+");
        String userId = parts[0];
        long loginTime = Long.parseLong(parts[1]);
        long logoutTime = Long.parseLong(parts[2]);

        // Calculate the duration of the session
        long sessionDuration = logoutTime - loginTime;

        // Emit user ID and session duration
        user.set(userId);
        duration.set(sessionDuration);
        context.write(user, duration);
    }
}
