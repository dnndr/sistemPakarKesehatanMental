import tkinter as tk
from tkinter import messagebox, ttk

questions = {
    1: "Apakah Anda sering mengalami rasa sakit di bagian tubuh seperti kepala, punggung, atau dada?",
    2: "Apakah Anda merasa gugup, cemas, atau tegang tanpa sebab yang jelas?",
    3: "Apakah Anda sering mengalami pikiran yang tidak bisa dihilangkan atau keinginan melakukan sesuatu berulang kali?",
    4: "Apakah Anda sering merasa pusing atau mau pingsan?",
    5: "Apakah Anda merasa sedih atau putus asa tanpa alasan jelas?",
    6: "Apakah Anda merasa takut atau cemas dalam situasi sosial?",
    7: "Apakah Anda takut terhadap hal-hal tertentu seperti tempat terbuka atau keramaian?",
    8: "Apakah Anda merasa khawatir sesuatu yang buruk akan terjadi?",
    9: "Apakah Anda kesulitan membuat keputusan sehari-hari?",
    10: "Apakah Anda sering merasa takut berbicara di depan umum?",
    11: "Apakah Anda mudah marah atau merasa kesal terhadap orang lain?",
    12: "Apakah Anda merasakan nyeri atau ketidaknyamanan di dada?",
    13: "Apakah Anda merasa bahwa orang lain ingin menyakiti Anda?",
    14: "Apakah Anda merasa kesepian atau terisolasi?",
    15: "Apakah Anda mudah menangis atau merasa sedih?",
    16: "Apakah Anda merasa bahwa orang lain mengejek atau menolak Anda?",
    17: "Apakah Anda pernah merasa pikiran Anda dikendalikan oleh kekuatan luar?",
    18: "Apakah Anda tiba-tiba merasa sangat takut tanpa alasan?",
    19: "Apakah Anda merasa diawasi atau dikejar oleh orang lain?",
    20: "Apakah Anda merasa sangat sedih atau kehilangan minat pada aktivitas sehari-hari?",
    21: "Apakah Anda merasa sulit mempercayai pikiran sendiri?",
    22: "Apakah Anda merasa putus asa tentang masa depan?",
    23: "Apakah Anda sering merasa gelisah atau tegang?",
    24: "Apakah Anda merasa bahwa orang lain menertawakan Anda?",
    25: "Apakah Anda takut berbicara atau tampil di depan orang banyak?",
    26: "Apakah Anda sering menyalahkan diri sendiri?",
    27: "Apakah Anda merasa sesak napas atau sulit bernapas?",
    28: "Apakah Anda merasa pikiran Anda tiba-tiba kosong atau sulit berkonsentrasi?",
    29: "Apakah Anda merasa tidak berharga atau tidak berguna?",
    30: "Apakah Anda merasa terjebak dalam situasi tanpa jalan keluar?",
    31: "Apakah Anda sering merasa khawatir berlebihan terhadap banyak hal?",
    32: "Apakah Anda merasa lemah secara fisik atau mudah lelah?",
    33: "Apakah Anda merasa tegang tanpa alasan jelas?",
    34: "Apakah Anda merasa pikiran Anda dibaca oleh orang lain?",
    35: "Apakah Anda merasa sulit fokus atau berkonsentrasi?",
    36: "Apakah Anda merasa dikendalikan atau dimanipulasi oleh orang lain?",
    37: "Apakah Anda merasa berbeda atau terasing dari orang lain?",
    38: "Apakah Anda mengalami kesulitan berkonsentrasi pada tugas tertentu?",
    39: "Apakah Anda sering merasa takut tanpa sebab yang jelas?",
    40: "Apakah Anda mengalami mual, sakit perut, atau gangguan pencernaan?",
    41: "Apakah Anda merasa malu atau canggung di depan orang lain?",
    42: "Apakah Anda merasakan mati rasa atau kesemutan di bagian tubuh tertentu?",
    43: "Apakah Anda merasa bahwa dunia ini tidak nyata atau aneh?",
    44: "Apakah Anda merasa bahwa tubuh Anda berubah bentuk atau aneh?",
    45: "Apakah Anda memiliki pikiran berulang yang tidak diinginkan?",
    46: "Apakah Anda merasa terhambat atau sulit menyelesaikan pekerjaan?",
    47: "Apakah Anda terganggu oleh suara-suara atau hal-hal aneh di sekitar Anda?",
    48: "Apakah Anda sering merasakan sakit di punggung bawah?",
    49: "Apakah Anda merasa berat atau lemas di lengan atau kaki?",
    50: "Apakah Anda merasa bahwa orang berbicara tentang Anda?",
    51: "Apakah Anda merasa perlu memeriksa sesuatu berulang kali?",
    52: "Apakah Anda merasa panas dingin secara tiba-tiba?",
    53: "Apakah Anda mengalami kesulitan tidur atau tidur tidak nyenyak?",
    54: "Apakah Anda merasa putus asa tentang masa depan?",
    55: "Apakah Anda melakukan sesuatu dengan sangat lambat atau berhati-hati berlebihan?",
    56: "Apakah Anda merasakan jantung berdetak sangat cepat atau keras?",
    57: "Apakah Anda merasa panik tanpa sebab jelas?",
    58: "Apakah Anda merasa dimanfaatkan atau diperlakukan tidak adil oleh orang lain?",
    59: "Apakah Anda merasa malu atau bersalah secara berlebihan?",
    60: "Apakah Anda memiliki pikiran aneh yang tidak dapat dikendalikan?",
    61: "Apakah Anda merasa kehilangan kontrol atas diri sendiri?",
    62: "Apakah Anda merasa sangat kesepian meskipun ada orang di sekitar?",
    63: "Apakah Anda merasa memiliki kekuatan atau kemampuan khusus?",
    64: "Apakah Anda mudah tersinggung atau marah?",
    65: "Apakah Anda kesulitan menyelesaikan pekerjaan yang sudah dimulai?",
    66: "Apakah Anda merasa tidak nyaman atau sulit berbicara dengan orang lain?",
    67: "Apakah Anda merasa bahwa orang lain ingin menyakiti Anda?",
    68: "Apakah Anda sangat sensitif terhadap kritik?",
    69: "Apakah Anda merasa bahwa orang berbicara tentang Anda secara negatif?",
    70: "Apakah Anda merasa tidak nyaman dalam situasi sosial?",
    71: "Apakah Anda merasa pikiran Anda sulit dikendalikan?",
    72: "Apakah Anda merasa takut secara tiba-tiba tanpa alasan jelas?",
    73: "Apakah Anda merasa tidak berdaya menghadapi masalah sehari-hari?",
    74: "Apakah Anda sulit memulai aktivitas baru?",
    75: "Apakah Anda merasa hidup ini tidak berarti?",
    76: "Apakah Anda khawatir sesuatu yang mengerikan akan terjadi?",
    77: "Apakah Anda merasa kehilangan kontrol atas emosi Anda?",
    78: "Apakah Anda merasa tidak percaya diri?",
    79: "Apakah Anda merasa hidup Anda tidak berharga?",
    80: "Apakah Anda merasa lebih buruk dari orang lain?",
    81: "Apakah Anda merasa tidak disukai oleh orang lain?",
    82: "Apakah Anda mudah cemas atau gugup?",
    83: "Apakah Anda merasa tidak punya energi untuk melakukan aktivitas sehari-hari?",
    84: "Apakah Anda merasa tidak nyaman dengan tubuh Anda?",
    85: "Apakah Anda takut kehilangan kontrol atas diri Anda?",
    86: "Apakah Anda merasa sangat cemas atau gugup?",
    87: "Apakah Anda merasa sulit berpikir jernih?",
    88: "Apakah Anda merasa semua orang menghakimi Anda?",
    89: "Apakah Anda merasa tidak aman di lingkungan sekitar?",
    90: "Apakah Anda merasa ingin menyakiti diri sendiri?"
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
