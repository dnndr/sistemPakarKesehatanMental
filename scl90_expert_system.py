import tkinter as tk
from tkinter import messagebox, ttk

questions = {
    1: "Apakah Anda sering merasakan sakit kepala?",
    2: "Apakah Anda sering merasa gugup tanpa alasan?",
    3: "Apakah Anda sering mengalami kesulitan mengingat hal-hal?",
    4: "Apakah Anda sering merasa pusing atau ingin pingsan?",
    5: "Apakah Anda merasa tidak tertarik pada hal-hal yang biasanya menarik bagi Anda?",
    6: "Apakah Anda sering merasa takut?",
    7: "Apakah Anda merasa bahwa orang lain tidak bisa dipercaya?",
    8: "Apakah Anda merasa bahwa sesuatu yang buruk akan terjadi?",
    9: "Apakah Anda kesulitan membuat keputusan?",
    10: "Apakah Anda merasa takut di tempat umum atau ruang terbuka?",
    11: "Apakah Anda merasa bahwa orang-orang tidak menyukai Anda?",
    12: "Apakah Anda sering merasakan sakit di dada atau jantung?",
    13: "Apakah Anda merasa bahwa orang-orang mencoba menyakiti Anda?",
    14: "Apakah Anda merasa kesepian?",
    15: "Apakah Anda mudah menangis?",
    16: "Apakah Anda merasa bahwa orang-orang sedang membicarakan Anda?",
    17: "Apakah Anda merasa bahwa pikiran Anda sedang dikendalikan oleh kekuatan luar?",
    18: "Apakah Anda merasa tiba-tiba ketakutan tanpa alasan?",
    19: "Apakah Anda merasa bahwa seseorang mengamati Anda?",
    20: "Apakah Anda merasa sangat sedih?",
    21: "Apakah Anda merasa bahwa Anda tidak dapat percaya pada pikiran Anda sendiri?",
    22: "Apakah Anda merasa putus asa?",
    23: "Apakah Anda merasa tegang atau gelisah?",
    24: "Apakah Anda merasa bahwa orang-orang mengejek Anda?",
    25: "Apakah Anda merasa takut berbicara di depan orang?",
    26: "Apakah Anda sering menyalahkan diri sendiri?",
    27: "Apakah Anda merasa sesak napas?",
    28: "Apakah pikiran Anda tiba-tiba kosong?",
    29: "Apakah Anda merasa tidak berguna?",
    30: "Apakah Anda merasa terjebak atau tidak bisa keluar dari suatu situasi?",
    31: "Apakah Anda terlalu banyak khawatir terhadap banyak hal?",
    32: "Apakah Anda merasa lemah secara fisik?",
    33: "Apakah Anda merasa tegang tanpa alasan jelas?",
    34: "Apakah Anda merasa bahwa pikiran Anda sedang dibaca oleh orang lain?",
    35: "Apakah Anda merasa tidak dapat berkonsentrasi?",
    36: "Apakah Anda merasa bahwa orang lain berusaha mengendalikan Anda?",
    37: "Apakah Anda merasa bahwa Anda berbeda dari orang lain?",
    38: "Apakah Anda mengalami kesulitan berkonsentrasi?",
    39: "Apakah Anda merasa ketakutan?",
    40: "Apakah Anda mengalami mual atau sakit perut?",
    41: "Apakah Anda merasa malu di depan orang lain?",
    42: "Apakah Anda mengalami mati rasa atau kesemutan di bagian tubuh?",
    43: "Apakah Anda merasa bahwa dunia ini tidak nyata?",
    44: "Apakah Anda merasa bahwa tubuh Anda berubah bentuk?",
    45: "Apakah Anda memiliki pikiran yang tidak diinginkan berulang kali?",
    46: "Apakah Anda merasa terhambat dalam menyelesaikan tugas?",
    47: "Apakah Anda merasa sangat terganggu oleh suara-suara?",
    48: "Apakah Anda sering merasakan sakit di punggung bagian bawah?",
    49: "Apakah Anda merasa berat di lengan atau kaki?",
    50: "Apakah Anda merasa bahwa orang-orang berbicara tentang Anda?",
    51: "Apakah Anda harus memeriksa sesuatu berulang kali?",
    52: "Apakah Anda sering merasakan panas atau dingin yang tiba-tiba?",
    53: "Apakah Anda mengalami kesulitan tidur?",
    54: "Apakah Anda merasa putus asa tentang masa depan?",
    55: "Apakah Anda harus melakukan sesuatu dengan sangat lambat?",
    56: "Apakah Anda merasa jantung Anda berdetak sangat cepat atau keras?",
    57: "Apakah Anda merasa panik tanpa sebab yang jelas?",
    58: "Apakah Anda merasa bahwa orang-orang memanfaatkan Anda?",
    59: "Apakah Anda merasa malu atau bersalah?",
    60: "Apakah Anda memiliki pikiran aneh yang tidak bisa Anda kendalikan?",
    61: "Apakah Anda merasa bahwa Anda kehilangan kontrol atas diri Anda?",
    62: "Apakah Anda merasa sangat kesepian bahkan di antara orang lain?",
    63: "Apakah Anda merasa bahwa Anda memiliki kekuatan khusus?",
    64: "Apakah Anda merasa sangat mudah tersinggung?",
    65: "Apakah Anda kesulitan menyelesaikan pekerjaan yang telah Anda mulai?",
    66: "Apakah Anda merasa tidak mampu berbicara dengan orang lain?",
    67: "Apakah Anda merasa bahwa orang lain ingin menyakiti Anda?",
    68: "Apakah Anda merasa sangat sensitif terhadap kritik?",
    69: "Apakah Anda merasa bahwa orang-orang berbicara tentang Anda?",
    70: "Apakah Anda merasa tidak nyaman di lingkungan sosial?",
    71: "Apakah Anda merasa bahwa pikiran Anda tidak dapat dikendalikan?",
    72: "Apakah Anda merasa takut secara tiba-tiba tanpa alasan?",
    73: "Apakah Anda merasa tidak berdaya dalam menghadapi masalah sehari-hari?",
    74: "Apakah Anda merasa sulit untuk memulai aktivitas baru?",
    75: "Apakah Anda merasa bahwa hidup ini tidak berarti?",
    76: "Apakah Anda merasa bahwa sesuatu yang mengerikan akan terjadi?",
    77: "Apakah Anda merasa tidak memiliki kontrol atas emosi Anda?",
    78: "Apakah Anda merasa sangat tidak percaya diri?",
    79: "Apakah Anda merasa bahwa hidup Anda tidak berharga?",
    80: "Apakah Anda merasa bahwa Anda lebih buruk dari orang lain?",
    81: "Apakah Anda merasa bahwa orang-orang tidak menyukai kehadiran Anda?",
    82: "Apakah Anda merasa sangat mudah cemas atau gugup?",
    83: "Apakah Anda merasa tidak memiliki energi untuk melakukan hal-hal biasa?",
    84: "Apakah Anda merasa tidak nyaman dengan tubuh Anda sendiri?",
    85: "Apakah Anda merasa takut akan kehilangan kontrol atas diri Anda?",
    86: "Apakah Anda merasa sangat gugup atau cemas?",
    87: "Apakah Anda merasa tidak dapat berpikir jernih?",
    88: "Apakah Anda merasa bahwa semua orang menghakimi Anda?",
    89: "Apakah Anda merasa tidak aman di lingkungan sekitar Anda?",
    90: "Apakah Anda merasa bahwa Anda ingin menyakiti diri sendiri?"
}

subscales = {
    "Somatisasi": [1, 4, 12, 27, 40, 42, 48, 49, 52],
    "Obsesi-Kompulsi": [3, 9, 10, 28, 38, 45, 46, 51, 55],
    "Sensitivitas Interpersonal": [6, 21, 34, 36, 37, 41, 61, 69, 70],
    "Depresi": [5, 14, 15, 20, 22, 26, 29, 30, 31, 54, 71, 75, 79],
    "Kecemasan": [2, 17, 23, 33, 39, 57, 72, 77, 86],
    "Hostilitas": [11, 16, 47, 50, 64, 66, 68],
    "Phobia": [7, 8, 18, 24, 25, 43, 56, 73, 76],
    "Paranoia": [13, 19, 32, 35, 58, 60, 62, 67, 74, 80],
    "Psikotik": [44, 53, 59, 63, 65, 78, 81, 82, 83, 84, 85, 87, 88, 89, 90]
}

certaintyFactor = {}

class SCL90App:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistem Pakar SCL-90")

        try:
            self.master.state('zoomed')
        except:
            self.master.attributes('-zoomed', True)

        self.question_vars = {}

        self.canvas = tk.Canvas(master)
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        title_label = tk.Label(self.scrollable_frame, text="Sistem Pakar Deteksi Diri Gangguan Kesehatan Mental Berbasis SCL-90", font=("Arial", 24, "bold"), pady=20)
        title_label.pack()

        for q_num, q_text in questions.items():
            frame = ttk.Frame(self.scrollable_frame, padding=30)
            frame.pack(fill="x", padx=5, pady=2)
            tk.Label(frame, text=f"{q_num}. {q_text}", wraplength=1000, anchor="center", justify="center").pack()

            var = tk.IntVar()
            self.question_vars[q_num] = var

            options = ["(Tidak sama sekali)", "(Sedikit saja)", "(Cukup)", "(Lumayan sering)", "(Sangat sering)"]
            for idx, text in enumerate(options):
                tk.Radiobutton(frame, text=text, variable=var, value=idx).pack(side="left", expand=True)

        self.submit_btn = tk.Button(self.scrollable_frame, text="Submit", command=self.submit)
        self.submit_btn.pack(pady=20)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def submit(self):
        certainty_mapping = [0.0, 0.25, 0.5, 0.75, 1.0]

        for q_num, var in self.question_vars.items():
            certaintyFactor[q_num] = certainty_mapping[var.get()]

        hasil_cf = self.hitung_cf_subskala()
        interpretasi = self.interpretasi_cf(hasil_cf)

        result_window = tk.Toplevel(self.master)
        result_window.title("Hasil Evaluasi")
        tk.Label(result_window, text="Ringkasan Hasil Evaluasi:", font=("Arial", 14, "bold")).pack(pady=10)
        for subscale, score in hasil_cf.items():
            status = interpretasi[subscale]
            tk.Label(result_window, text=f"{subscale}: CF = {score:.2f} → {status}", font=("Arial", 11)).pack(anchor="w")

        suggestion = tk.Label(result_window, text="\nSaran: Jika Anda memiliki CF sedang hingga tinggi pada salah satu kategori, disarankan untuk berkonsultasi dengan profesional kesehatan mental.", wraplength=500, fg="darkred")
        suggestion.pack(pady=20)

        tk.Button(result_window, text="Tutup", command=result_window.destroy).pack()

    def hitung_cf_subskala(self):
        hasil = {}
        for kategori, daftar_pertanyaan in subscales.items():
            nilai_cf = [certaintyFactor[i] for i in daftar_pertanyaan if i in certaintyFactor]
            hasil[kategori] = sum(nilai_cf) / len(nilai_cf) if nilai_cf else 0
        return hasil

    def interpretasi_cf(self, hasil_cf):
        interpretasi = {}
        for subscale, cf_score in hasil_cf.items():
            if cf_score >= 0.75:
                interpretasi[subscale] = "Tingkat gejala tinggi"
            elif cf_score >= 0.5:
                interpretasi[subscale] = "Tingkat gejala sedang"
            else:
                interpretasi[subscale] = "Tingkat gejala rendah"
        return interpretasi


if __name__ == "__main__":
    root = tk.Tk()
    app = SCL90App(root)
    root.mainloop()