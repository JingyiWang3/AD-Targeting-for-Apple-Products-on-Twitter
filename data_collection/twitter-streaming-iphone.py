WORDS = ['iphone', '#iphone', 'iPhone', '#iPhone'] # remember to change the tag value
import json
import datetime
def preprocess_data(datajson, db):
    # Add More Information
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    post = datajson
    if str(post['user']['location']).split(', ')[-1] in states:
        device = ''
        if 'Android' in str(post['source']):
            device = 'Andriod'
        elif 'Web' in str(post['source']):
            device = 'Web'
        elif 'iPhone' in str(post['source']):
            device = 'iPhone'
        elif 'Buffer' in str(post['source']):
            device = 'Buffer'
        else:
            device = 'Others'
        # New DataFrame
        new_df = pd.DataFrame()
        new_df = new_df.append({'location' : str(post['user']['location']).split(', ')[-1], 
                                'time' : post['created_at'],
                                'tag' : 'iPhone',
                                'device' : device,
                                'total_donations': 1},
                                ignore_index=True)
        a = new_df['time'].apply(lambda x: str(x).split(' '))
        a = a.apply(lambda x:x[2]+'-'+x[1]+'-'+x[5] + ' ' + x[3].split(':')[0] + ':' + x[3].split(':')[1] + ':00')
        new_df['time'] = a.apply(lambda x:datetime.datetime.strptime(x,'%d-%b-%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') )
        ddf = new_df.rename(columns={'location': 'school_state',
                                     'time': 'date_posted',
                                     'tag': 'resource_type',
                                     'device': 'funding_status'})
        # Combine the jason
        datajsonn = ddf.to_dict('records')
        datajson.update(datajsonn[0])
        
        return datajson
            
    return None