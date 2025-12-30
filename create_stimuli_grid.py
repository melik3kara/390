import cv2
import matplotlib.pyplot as plt
import os
import random

# Duygular ve pozlar
emotions = ['angry', 'happy', 'sad', 'surprise']
poses = ['front', 'left']

# Video dosyalarının bulunduğu klasör
data_dir = 'videos/StudyVideos'

# Her duygunun ve pozun videosunu bul
video_dict = {}
for emotion in emotions:
    video_dict[emotion] = {}
    for pose in poses:
        # Dosya adında hem duygu hem poz geçen ilk videoyu bul
        for fname in os.listdir(data_dir):
            if fname.startswith(f'{emotion}') and f'_{pose}_' in fname and fname.endswith('.mp4'):
                video_dict[emotion][pose] = os.path.join(data_dir, fname)
                break

def get_first_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    return None

def get_random_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count > 0:
        idx = random.randint(0, frame_count - 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        cap.release()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            return frame
    cap.release()
    return None

def create_grid(get_frame_func, out_path):
    fig, axes = plt.subplots(len(emotions), len(poses), figsize=(8, 8))
    for i, emotion in enumerate(emotions):
        for j, pose in enumerate(poses):
            video_path = video_dict[emotion].get(pose)
            if video_path:
                frame = get_frame_func(video_path)
                if frame is not None:
                    axes[i, j].imshow(frame)
                axes[i, j].set_xticks([])
                axes[i, j].set_yticks([])
                if j == 0:
                    axes[i, j].set_ylabel(emotion.capitalize(), fontsize=14)
                if i == 0:
                    axes[i, j].set_title(pose.capitalize(), fontsize=14)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

if __name__ == '__main__':
    os.makedirs('stimuli_figures', exist_ok=True)
    # İlk karelerden grid
    create_grid(get_first_frame, 'stimuli_figures/stimuli_grid_first.png')
    # Rastgele karelerden grid
    create_grid(get_random_frame, 'stimuli_figures/stimuli_grid_random.png')
    print('Görseller kaydedildi: stimuli_figures/stimuli_grid_first.png ve stimuli_figures/stimuli_grid_random.png')
