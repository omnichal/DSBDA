public class LogReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    private LongWritable maxDuration = new LongWritable();

    public void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        long totalDuration = 0;
        // Calculate total duration for the user
        for (LongWritable value : values) {
            totalDuration += value.get();
        }
        // Check if this user has the maximum duration so far
        if (totalDuration > maxDuration.get()) {
            maxDuration.set(totalDuration);
            // Clear previous results since we found a new maximum
            context.write(key, maxDuration);
        } else if (totalDuration == maxDuration.get()) {
            // If there are multiple users with the same maximum duration, append their IDs
            context.write(key, maxDuration);
        }
    }
}
