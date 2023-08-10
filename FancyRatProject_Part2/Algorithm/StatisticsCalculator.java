import java.util.List;

public class StatisticsCalculator {

    public static class Statistics {
        private double mean;
        private double variance;
        private double standardDeviation;

        public Statistics(double mean, double variance, double standardDeviation) {
            this.mean = mean;
            this.variance = variance;
            this.standardDeviation = standardDeviation;
        }

        public double getMean() {
            return mean;
        }

        public double getVariance() {
            return variance;
        }

        public double getStandardDeviation() {
            return standardDeviation;
        }
    }

    public static Statistics calculateStatistics(List<Double> numbers) {
        int n = numbers.size();
        if (n == 0) {
            throw new IllegalArgumentException("Input list cannot be empty");
        }

        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        double mean = sum / n;

        double sumSquaredDiff = 0;
        for (double num : numbers) {
            double diff = num - mean;
            sumSquaredDiff += diff * diff;
        }
        double variance = sumSquaredDiff / n;
        double standardDeviation = Math.sqrt(variance);

        return new Statistics(mean, variance, standardDeviation);
    }

    public static void main(String[] args) {
        List<Double> numbers = List.of(2.5, 3.7, 1.2, 5.4, 6.8, 7.3);
        Statistics statistics = calculateStatistics(numbers);

        System.out.println("Mean: " + statistics.getMean());
        System.out.println("Variance: " + statistics.getVariance());
        System.out.println("Standard Deviation: " + statistics.getStandardDeviation());
    }
}
