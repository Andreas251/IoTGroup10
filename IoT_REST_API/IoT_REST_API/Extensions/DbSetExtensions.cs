using System;
using System.Collections.Generic;
using System.Linq;
using IoT_REST_API.Interfaces;

namespace IoT_REST_API.Extensions
{
    public static class DbSetExtensions
    {
        public static IEnumerable<T> ReadingsWithinRange<T>(this IQueryable<T> t, Guid? sensorId, DateTime start, DateTime end) where T : Reading
        {
            if (sensorId == null)
            {
                var readingsWithinRange = t.AsEnumerable().Where(p => p.Timestamp.DateTime >= start && p.Timestamp.DateTime <= end);
                return readingsWithinRange;
            }
            else
            {
                var readingsForSensor = t.Where(p => p.SensorId == sensorId).AsEnumerable();
                var readingsWithinRange = readingsForSensor.Where(p => p.Timestamp.DateTime >= start && p.Timestamp.DateTime <= end);
                return readingsWithinRange;
            }
        }

        public static T LatestReading<T>(this IQueryable<T> t, Guid? sensorId) where T : Reading
        {
            if(sensorId == null)
            {
                return t.OrderByDescending(p => p.Timestamp).FirstOrDefault();
            }
            else
            {
                return t.Where(p => p.SensorId == sensorId).OrderByDescending(p => p.Timestamp).FirstOrDefault();
            }
        }
    }
}
