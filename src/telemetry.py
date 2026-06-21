import pandas as pd

def analyze_telemetry(file_path):
    df = pd.read_csv(file_path)

    total_distance = df['distance'].max()

    s1_end = total_distance / 3
    s2_end = 2 * total_distance / 3

    # Get closest time when crossing sector boundaries
    s1_cross = df.iloc[(df['distance'] - s1_end).abs().argsort()[:1]]
    s2_cross = df.iloc[(df['distance'] - s2_end).abs().argsort()[:1]]

    start_time = df['time'].min()
    end_time = df['time'].max()

    s1_time = float(s1_cross['time'].values[0] - start_time)
    s2_time = float(s2_cross['time'].values[0] - s1_cross['time'].values[0])
    s3_time = float(end_time - s2_cross['time'].values[0])

    lap_time = float(end_time - start_time)

    sectors = {
        "s1": s1_time,
        "s2": s2_time,
        "s3": s3_time
    }

    performance = analyze_performance(sectors)

    return {
        "lap_time": lap_time,
        "sectors": sectors,
        "performance": performance
    }



def analyze_performance(sectors):
    s1 = sectors["s1"]
    s2 = sectors["s2"]
    s3 = sectors["s3"]

    # find best time
    best_sector = min(sectors, key=sectors.get)
    worst_sector = max(sectors, key=sectors.get)

    # time loss (difference from best to worst)
    time_loss ={
        "s1_loss": float(s1-sectors[best_sector]),
        "s2_loss": float(s2-sectors[best_sector]),
        "s3_loss": float(s3-sectors[best_sector])
    }

    return{
        "best_sector": best_sector,
        "worst_sector": worst_sector,
        "time_loss": time_loss
    }




#     df = pd.read_csv(file_path)

#     total_distance = df['distance'].max()

#     #defing sectors
#     s1_end = total_distance/3
#     s2_end = 2*total_distance/3

#     #sector distace split
#     s1 = df[df['distance']<= s1_end]
#     s2 = df[(df['distance']>s1_end) & (df['distance']<=s2_end)]
#     s3 = df[df['distance'] > s2_end]

#     # calculateing sector time
#     s1_time = s1['time'].max()-s1['time'].min()
#     s2_time = s2['time'].max()-s2['time'].min()
#     s3_time = s3['time'].max()-s3['time'].min()

#     # total lap time
#     lap_time = df['time'].max() - df['time'].min()
#     return{
#         "lap_time": float(lap_time),
#         "sectors": {
#             "s1": float(s1_time),
#             "s2": float(s2_time),
#             "s3": float(s3_time)
#         }
    # }


    # # Basic analysis
    # avg_speed = df['speed'].mean()
    # max_speed = df['speed'].max()
    # min_speed = df['speed'].min()

    # return {
    #     "avg_speed": float(round(avg_speed, 2)),
    #     "max_speed": int (max_speed),
    #     "min_speed": int(min_speed)
    # }

