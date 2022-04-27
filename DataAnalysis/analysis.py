from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

'''
q = a + bi + cj + dk
# Unity stores the real component(a) to the last number in the quartet
# See https://docs.unity3d.com/ScriptReference/Quaternion.html for more
a = cos θ/2
b = v_x sin θ/2
c = v_y sin θ/2
d = v_z sin θ/2

where v is the rotation axis, and θ is the rotation angle

PLAN:
Use Beach Exploration data for 2D heat map plot in the x-y plane?
- First calibrate/center the datsets so 0,0 isthe heads starting position, as opposed to
the center of the Oculus play area generated for each participant. These starting measurements
were noted down on each trial
- Concatenate the datasets from all participants together, then plot


Use Museum Exploration data for Sphere plots
Use Beach guided motion data for histogram of azimuthal angle variation (convert to polar)
^ this is a measure of yaw exploration
Do the same with museum, maybe superimpose their histogram,s and quote statistics like mean,
median, range, gaussian-ness (Wilk test with p-value) and modality (bi/tri modal)

'''

column_names = ['x', 'y', 'z', 'b', 'c', 'd', 'a']
file_path1_noHap = './ParticipantDataClean/p1/beach/p1_1.txt'
file_path1_Hap = './ParticipantDataClean/p1/beach/p1_4.txt'
file_path2_noHap = './ParticipantDataClean/p2/beach/p2_1.txt'
file_path2_Hap = './ParticipantDataClean/p2/beach/p2_3.txt'
file_path3_noHap = './ParticipantDataClean/p3/beach/p3_1.txt'
file_path3_Hap = './ParticipantDataClean/p3/beach/p3_4.txt'
file_path4_noHap = './ParticipantDataClean/p4/beach/p4_1.txt'
file_path4_Hap = './ParticipantDataClean/p4/beach/p4_4.txt'

df1_noHap = pd.read_csv(file_path1_noHap, sep=',', names = column_names)
df1_noHap['Haptic Rendering'] = False
df1_Hap = pd.read_csv(file_path1_Hap, sep=',', names = column_names)
df1_Hap['Haptic Rendering'] = True
df1 = pd.concat([df1_noHap, df1_Hap], ignore_index=True, sort=False)
# Remove measured participant offset
df1['x'] = df1['x'] - 0.360
# df1['z'] = df1['z'] - 0.260
df1['z'] = df1['z'] - 0.260

df3_noHap = pd.read_csv(file_path3_noHap, sep=',', names = column_names)
df3_noHap['Haptic Rendering'] = False
df3_noHap['z'] = df3_noHap['z'] - 0.175
df3_Hap = pd.read_csv(file_path3_Hap, sep=',', names = column_names)
df3_Hap['Haptic Rendering'] = True
# df3_Hap['z'] = df3_Hap['z'] - 0.130
df3_Hap['z'] = df3_Hap['z'] - 0.115
# df3_Hap['z'] = 0
df3 = pd.concat([df3_noHap, df3_Hap], ignore_index=True, sort=False)
# Remove measured participant offset
df3['x'] = df3['x'] + 0.140

df4_noHap = pd.read_csv(file_path4_noHap, sep=',', names = column_names)
df4_noHap['Haptic Rendering'] = False
df4_Hap = pd.read_csv(file_path4_Hap, sep=',', names = column_names)
df4_Hap['Haptic Rendering'] = True
df4_Hap['z'] = df4_Hap['z'] - 0.03
df4 = pd.concat([df4_noHap, df4_Hap], ignore_index=True, sort=False)
# Remove measured participant offset
df4['x'] = df4['x'] + 0.200
df4['z'] = df4['z'] - 0.090
# df4['z'] = df4['z'] - 0.120

df_beach_exploration = pd.concat([df1, df3, df4], ignore_index=True, sort=False)

print(df3_noHap.head())
print(df3_Hap.head())
# Position Data - use this for beach exploration
Haptic_palette = {True:"dodgerblue",
                False:"firebrick"}
p = sns.jointplot(data=df_beach_exploration, x='x', y='z',kind='kde', shade=True,
                    hue='Haptic Rendering', alpha=0.5, palette=Haptic_palette,
                    labels={False:'Off', True:'On'})
# p.ax_marg_y.set_ylim(0.05, 0.25)
# p.fig.suptitle("Distribution of Head Motion in the x-z plane when exploring Tenerife")
p.ax_joint.set_xlabel('x [m]')
p.ax_joint.set_ylabel('z [m]')
p.fig.set_dpi(200)
# sns.jointplot(data=df3_Hap, x='x', y='z',kind='kde', cmap='Reds', shade=True, ax=ax2)
# # fig = plt.figure()
# # ax = fig.add_subplot(projection='3d')
# # ax.scatter(df3_noHap['x'], df3_noHap['y'], df3_noHap['z'])
# # ax.scatter(df3_Hap['x'], df3_Hap['y'], df3_Hap['z'])
# # ax.set_xlabel('$x$[m]', fontsize=20, rotation=150)
# # ax.set_ylabel('$y$[m]', fontsize=20,)
# # ax.set_zlabel('$z$[m]', fontsize=20, rotation=60)
# # plt.colorbar()
plt.savefig('./XZBeachSaved.png', dpi=300)
plt.show()
df_jp_hap = df_beach_exploration[df_beach_exploration['Haptic Rendering'] == True]
print('Haptic x, W = ', stats.shapiro(df_jp_hap['x']))
print('Haptic z, W = ', stats.shapiro(df_jp_hap['z']))
df_jp_nohap = df_beach_exploration[df_beach_exploration['Haptic Rendering'] == False]
print('Non Haptic x, W = ', stats.shapiro(df_jp_nohap['x']))
print('Non Haptic z, W = ', stats.shapiro(df_jp_nohap['z']))
print(stats.ttest_ind(df_jp_hap['x'], df_jp_nohap['x']))
print(stats.ttest_ind(df_jp_hap['z'], df_jp_nohap['z']))




# Museum Exploration Head tracking to Sphere plotsf
file_path1_noHap = './ParticipantDataClean/p1/museum/p1_2.txt'
file_path1_Hap = './ParticipantDataClean/p1/museum/p1_3.txt'
file_path2_noHap = './ParticipantDataClean/p2/museum/p2_2.txt'
file_path2_Hap = './ParticipantDataClean/p2/museum/p2_3.txt'
file_path3_noHap = './ParticipantDataClean/p3/museum/p3_2.txt'
file_path3_Hap = './ParticipantDataClean/p3/museum/p3_3.txt'
file_path4_noHap = './ParticipantDataClean/p4/museum/p4_2.txt'
file_path4_Hap = './ParticipantDataClean/p4/museum/p4_3.txt'

df1_noHap = pd.read_csv(file_path1_noHap, sep=',', names = column_names)
df1_noHap['Haptic Rendering'] = False
df1_Hap = pd.read_csv(file_path1_Hap, sep=',', names = column_names)
df1_Hap['Haptic Rendering'] = True
df1 = pd.concat([df1_noHap, df1_Hap], ignore_index=True, sort=False)


df3_noHap = pd.read_csv(file_path3_noHap, sep=',', names = column_names)
df3_noHap['Haptic Rendering'] = False
df3_Hap = pd.read_csv(file_path3_Hap, sep=',', names = column_names)
df3_Hap['Haptic Rendering'] = True
df3 = pd.concat([df3_noHap, df3_Hap], ignore_index=True, sort=False)

df4_noHap = pd.read_csv(file_path4_noHap, sep=',', names = column_names)
df4_noHap['Haptic Rendering'] = False
df4_Hap = pd.read_csv(file_path4_Hap, sep=',', names = column_names)
df4_Hap['Haptic Rendering'] = True
df4 = pd.concat([df4_noHap, df4_Hap], ignore_index=True, sort=False)


df_museum_exploration = pd.concat([df1, df3, df4], ignore_index=True, sort=False)

# Convert Orientation Data Quaternions -> Axis Angle Representation
df4_Hap = df1_Hap
df4_noHap = df1_noHap
df= df4_noHap
df['v_x'] = df['b']/np.sqrt(1-df['a']**2)
df['v_y'] = df['c']/np.sqrt(1-df['a']**2)
df['v_z'] = df['d']/np.sqrt(1-df['a']**2)
# Normalise to lie on a Unit Sphere
df['v_x'] = df['v_x']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
df['v_y'] = df['v_y']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
df['v_z'] = df['v_z']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)


## SPHERE HEAD MOVEMENT PLOT
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.set_aspect((1,1,1))

# Convert Orientation Data Quaternions -> Axis Angle Representation
df4_noHap['v_x'] = df4_noHap['b']/np.sqrt(1-df['a']**2)
df4_noHap['v_y'] = df4_noHap['c']/np.sqrt(1-df['a']**2)
df4_noHap['v_z'] = df4_noHap['d']/np.sqrt(1-df['a']**2)
# Normalise to lie on a Unit Sphere
df4_noHap['v_x'] = df4_noHap['v_x']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
df4_noHap['v_y'] = df4_noHap['v_y']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
df4_noHap['v_z'] = df4_noHap['v_z']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)


# draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="k", alpha=0.2)


df= df4_Hap
df4_Hap['v_x'] = df4_Hap['b']/np.sqrt(1-df['a']**2)
df4_Hap['v_y'] = df4_Hap['c']/np.sqrt(1-df['a']**2)
df4_Hap['v_z'] = df4_Hap['d']/np.sqrt(1-df['a']**2)
# Normalise to lie on a Unit Sphere
df4_Hap['v_x'] = df4_Hap['v_x']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
df4_Hap['v_y'] = df4_Hap['v_y']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
df4_Hap['v_z'] = df4_Hap['v_z']/np.sqrt(df['v_x']**2 + df['v_y']**2 + df['v_z']**2)
ax.plot(df4_Hap['v_x'], df4_Hap['v_y'], df4_Hap['v_z'], label='On', alpha=0.8, color='dodgerblue')
ax.plot(df4_noHap['v_x'], df4_noHap['v_y'], df4_noHap['v_z'], label='Off', alpha=0.8, color='firebrick')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.zaxis.set_rotate_label(False)
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_zticks([-1, -0.5, 0, 0.5, 1])
plt.legend(title="Haptic Rendering")

plt.show()

def toSpherical(x, y,z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r) * 180 / np.pi
    phi = np.arctan2(y, x) * 180 / np.pi # Azimuthal angle
    return r, theta, phi

_, _, df4_noHap['azi'] = toSpherical(df4_noHap['v_x'], df4_noHap['v_y'], df4_noHap['v_z'])
_, _, df4_Hap['azi'] = toSpherical(df4_Hap['v_x'], df4_Hap['v_y'], df4_Hap['v_z'])

h1 = sns.histplot(data=df4_noHap, x='azi', label='No Haptic', color='firebrick', stat='proportion', bins=20, fill=False, element="step")
h2 = sns.histplot(data=df4_Hap, x='azi', label='Haptic', color='dodgerblue', stat='proportion', bins=20, fill=False, element="step")
print(stats.shapiro(df4_noHap['azi']))
print(stats.shapiro(df4_Hap['azi']))
h2.set_xlabel('Yaw Angle [$^{\circ}$]')
h2.set_ylabel('Proportion of total trial time')
plt.legend()

plt.show()
