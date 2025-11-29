import csv

class student:

    @staticmethod
    def read():
        with open("studentDetails.csv", newline="") as f:
            reader = list(csv.DictReader(f))
            return reader

    def cal_avg_mask(self):
        reader = student.read()
        total = 0
        avg_mask=0
        for row in reader:
            total = total + int(row["Mask"])
        avg_mask = total/len(reader)
        with open("summary.txt", "w") as f:
            f.write("Average: {}".format(avg_mask))
            f.close()
        return avg_mask


s = student()
s.cal_avg_mask()
