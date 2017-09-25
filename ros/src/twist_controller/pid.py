
MIN_NUM = float('-inf')
MAX_NUM = float('inf')


class PID(object):
    def __init__(self, kp, ki, kd, min=MIN_NUM, max=MAX_NUM):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.min = min
        self.max = max

        self.int_val = self.last_int_val = self.last_error = 0.

    def reset(self):
        self.int_val = 0.0
        self.last_int_val = 0.0

    def step(self, error, sample_time):
        self.last_int_val = self.int_val

        integral = self.int_val + error * sample_time;
        derivative = (error - self.last_error) / sample_time;

        val = self.kp * error + self.ki * self.int_val + self.kd * derivative;

        # TODO Implement anti-windup
        if val > self.max:
            val = self.max
        elif val < self.min:
            val = self.min
        else:
            self.int_val = integral

        self.last_error = error

        return val
