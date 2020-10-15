import numpy as np

np.random.seed(0)


class SSQ:
    def __init__(self):

        self.input_value = input("press 1 for FIFO \n      2 for LIFO\n      3 for SJF\n input: ")

        # self.interarrivals= [0.4,1.2,0.5,1.7,0.2,1.6,0.2,1.4,1.9]  #exponential distribution mean 1/3
        # self.interarrivals= [0.8,1.6,0.5,2.2,1.3,0.7,0.5,1.9,1.8]
        # self.service_times= [2.2,0.5,0.3,1.1,3.5,0.6,0.9,1.5,1.2]  #exponential distribution mean 1/4

        #self.interarrivals = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9, 0.7]
        # 0.4, 1.6, 2.1, 3.8, 4.0, 5.6, 5.8, 7.2, 10.1, 10.8
        #self.service_times = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6, 0.9, 1.5, 1.2, 0.7]

        self.interarrivals = list(np.random.exponential(1 / 3.0, 101))
        self.service_times = list(np.random.exponential(1 / 4.0, 101))
        print(self.interarrivals)
        print(self.service_times)
        self.clock = 0.0

        self.next_arrival = self.interarrivals.pop(0)
        self.next_departure1 = float('inf')
        self.next_departure2 = float('inf')

        self.num_in_queue = 0
        self.times_of_arrivalqueue = []  # store times of arrivals who are waiting in the queue
        self.service_times_in_queue = []  # store service times of waiting customers in the queue

        self.total_delay = 0.0
        self.num_of_delays = 0.0
        self.area_under_q = 0.0
        self.area_under_b = 0.0

        self.server1_status = 0  # server 1  # 0 for IDLE , 1 for BUSY
        self.server2_status = 0  # server 2
        self.last_event_time = 0.0  # we will need to store last event clock time

        self.Q_t = 0
        self.B_t_server1 = 0
        self.B_t_server2 = 0

    def start(self):
        while self.num_of_delays < 100:
            self.timing()

        avg_delay = self.total_delay / self.num_of_delays
        print("Average delay =", avg_delay)

        expected_num_of_customer_in_queue = self.Q_t / self.clock
        print("Expected number of customers in queue =", expected_num_of_customer_in_queue)

        expected_utilization_of_server1 = self.B_t_server1 / self.clock
        print("Expected utilization of the server 1 =", expected_utilization_of_server1)

        expected_utilization_of_server2 = self.B_t_server2 / self.clock
        print("Expected utilization of the server 2 =", expected_utilization_of_server2)

    def timing(self):

        self.clock = min(self.next_arrival, self.next_departure1, self.next_departure2)
        self.update_register()

        if self.next_arrival < self.next_departure1 and self.next_arrival < self.next_departure2:
            print("Arrival at Clock:" + str(self.clock))
            self.arrival()

        else:
            if self.next_departure1 < self.next_departure2:
                print("Departure from server1 at Clock:" + str(self.clock))
                self.departure(1)
            else:
                print("Departure from server2 at Clock:" + str(self.clock))
                self.departure(2)

        print("Server 1 Status:" + str(self.server1_status))
        print("Server 2 Status:" + str(self.server2_status))
        print("Times of arrivals in Queue: " + str(self.times_of_arrivalqueue))
        print("Service times in Queue: " + str(self.service_times_in_queue))
        print("Number of Delays: " + str(self.num_of_delays))
        print("Total Delay:" + str(self.total_delay))
        print("Next Arrival Time: " + str(self.next_arrival))
        print("Next Departure from server 1 Time: " + str(self.next_departure1))
        print("Next Departure from server 2 Time: " + str(self.next_departure2))
        print("area under Q(t):", self.Q_t)
        print("area under B(t) for server1:", self.B_t_server1)
        print("area under B(t) for server2:", self.B_t_server2)
        print(" ")

    def arrival(self):
        self.next_arrival += self.interarrivals.pop(0)  # Schedule next arrival time = arrival + next interarrival time
        if self.server1_status == 0:  # Server IDLE
            self.server1_status = 1  # make server BUSY
            delay = 0.0  # so delay is zero
            self.total_delay += delay
            self.num_of_delays += 1  # increase the number of customers delayed
            # schedule next departure, pop the first element of service_times list to get service time of this customer
            self.next_departure1 = self.clock + self.service_times.pop(0)  # schedule departure of this customer

        elif self.server2_status == 0:  # Server IDLE
            self.server2_status = 1  # make server BUSY
            delay = 0.0  # so delay is zero
            self.total_delay += delay
            self.num_of_delays += 1  # increase the number of customers delayed
            # schedule next departure, pop the first element of service_times list to get service time of this customer
            self.next_departure2 = self.clock + self.service_times.pop(0)  # schedule departure of this customer

        else:
            # increase queue length, this customer will have to wait in the queue
            self.num_in_queue += 1

            # store the arrival time and service time of this customer in seperate lists

            self.times_of_arrivalqueue.append(self.clock)   # it will be used for next arrival delay count
            self.service_times_in_queue.append(self.service_times.pop(0))  # for sjf

    def departure(self, s):
        # check number of customers in the queue
        if self.num_in_queue == 0:  # if no customer in the queue, queue empty
            if s == 1:
                # make server IDLE
                self.server1_status = 0
                # schedule next departure= infinity
                self.next_departure1 = float('infinity')

            else:
                # make server IDLE
                self.server2_status = 0
                # schedule next departure= infinity
                self.next_departure2 = float('infinity')
        else:
            # if queue not empty, pop one customer, decrease queue length
            self.num_in_queue -= 1
            self.num_of_delays += 1
            # AS FIFO, pop first arrival and service time from the queue. IF LIFO we have to pop last arrival and service time
            # For SJF, find the index of minimum service time from  service_times_in_queue list.
            # Then pop the arrival of that index from times_of_arrivalqueue for delay count and others.

            if int(self.input_value) == 1:

                arrival = self.times_of_arrivalqueue.pop(0)

                delay = self.clock - arrival
                self.total_delay += delay
                if s == 1:
                    self.next_departure1 = self.clock + self.service_times_in_queue.pop(0)
                else:
                    self.next_departure2 = self.clock + self.service_times_in_queue.pop(0)

            elif int(self.input_value) == 2:
                arrival = self.times_of_arrivalqueue.pop()

                delay = self.clock - arrival
                self.total_delay += delay
                if s == 1:
                    self.next_departure1 = self.clock + self.service_times_in_queue.pop()
                else:
                    self.next_departure2 = self.clock + self.service_times_in_queue.pop()

            elif int(self.input_value) == 3:
                index_of_shortest_service_in_queue = self.service_times_in_queue.index(min(self.service_times_in_queue))
                arrival = self.times_of_arrivalqueue.pop(index_of_shortest_service_in_queue)

                delay = self.clock - arrival
                self.total_delay += delay
                if s == 1:
                    self.next_departure1 = self.clock + self.service_times_in_queue.pop(index_of_shortest_service_in_queue)
                else:
                    self.next_departure2 = self.clock + self.service_times_in_queue.pop(index_of_shortest_service_in_queue)

    def update_register(self):
        time_difference = self.clock - self.last_event_time

        self.last_event_time = self.clock
        #
        self.Q_t += time_difference * self.num_in_queue
        self.B_t_server1 += time_difference * self.server1_status
        self.B_t_server2 += time_difference * self.server2_status


model = SSQ()  # create SSQ object; __init__ is called
model.start()


