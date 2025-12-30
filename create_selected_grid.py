import matplotlib.pyplot as plt
import cv2
import os

# Seçilen karelerin dosya yolları
selected_frames = {
    'angry':   {'front': 'stimuli_figures/frames_for_selection/angry_front_frame57.png',
                'left':  'stimuli_figures/frames_for_selection/angry_left_frame53.png'},
    'happy':   {'front': 'stimuli_figures/frames_for_selection/happy_front_frame58.png',
                'left':  'stimuli_figures/frames_for_selection/happy_left_last_frame97.png'},
    'sad':     {'front': 'stimuli_figures/frames_for_selection/sad_front_frame63.png',
                'left':  'stimuli_figures/frames_for_selection/sad_left_frame64.png'},
    'surprise':{'front': 'stimuli_figures/frames_for_selection/surprise_front_frame51.png',
                'left':  'stimuli_figures/frames_for_selection/surprise_left_frame58.png'}
}

emotions = ['angry', 'happy', 'sad', 'surprise']
poses = ['front', 'left']

fig, axes = plt.subplots(len(emotions), len(poses), figsize=(8, 8))
for i, emotion in enumerate(emotions):
    for j, pose in enumerate(poses):
        frame_path = selected_frames[emotion][pose]
        if os.path.exists(frame_path):
            img = cv2.cvtColor(cv2.imread(frame_path), cv2.COLOR_BGR2RGB)
            axes[i, j].imshow(img)
        axes[i, j].set_xticks([])
        axes[i, j].set_yticks([])
        if j == 0:
            axes[i, j].set_ylabel(emotion.capitalize(), fontsize=14)
        if i == 0:
            axes[i, j].set_title(pose.capitalize(), fontsize=14)
plt.tight_layout()
plt.savefig('stimuli_figures/stimuli_grid_selected.png')
plt.close()
print('Seçilen karelerden grid oluşturuldu: stimuli_figures/stimuli_grid_selected.png')
