# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_info_from_court 1'] = {
    'bookings': [
        {
            'end_time': '10:30',
            'end_time_float': 10.5,
            'initial_time': '09:00',
            'initial_time_float': 9,
            'total_time': 90
        },
        {
            'end_time': '19:30',
            'end_time_float': 19.5,
            'initial_time': '18:00',
            'initial_time_float': 18,
            'total_time': 90
        },
        {
            'end_time': '21:00',
            'end_time_float': 21,
            'initial_time': '19:30',
            'initial_time_float': 19.5,
            'total_time': 90
        },
        {
            'end_time': '22:00',
            'end_time_float': 22,
            'initial_time': '21:00',
            'initial_time_float': 21,
            'total_time': 60
        }
    ],
    'end_time': '23:00',
    'end_time_float': 23,
    'fixed_times': [
        {
            'end_time': '12:00',
            'end_time_float': 12,
            'id': 621,
            'initial_time': '10:30',
            'initial_time_float': 10.5,
            'price': '',
            'total_time': 90,
            'valid': True
        },
        {
            'end_time': '13:30',
            'end_time_float': 13.5,
            'id': 622,
            'initial_time': '12:00',
            'initial_time_float': 12,
            'price': '',
            'total_time': 90,
            'valid': True
        },
        {
            'end_time': '15:00',
            'end_time_float': 15,
            'id': 623,
            'initial_time': '13:30',
            'initial_time_float': 13.5,
            'price': '',
            'total_time': 90,
            'valid': True
        },
        {
            'end_time': '16:30',
            'end_time_float': 16.5,
            'id': 624,
            'initial_time': '15:00',
            'initial_time_float': 15,
            'price': '',
            'total_time': 90,
            'valid': True
        },
        {
            'end_time': '18:00',
            'end_time_float': 18,
            'id': 625,
            'initial_time': '16:30',
            'initial_time_float': 16.5,
            'price': '',
            'total_time': 90,
            'valid': True
        }
    ],
    'id': '13',
    'initial_time': '09:00',
    'initial_time_float': 9,
    'name': 'Pádel 1',
    'provider': 'Conecta'
}

snapshots['test_get_conecta_schedule 1'] = {
    'courts': [
        {
            'bookings': [
                {
                    'end_time': '10:30',
                    'end_time_float': 10.5,
                    'initial_time': '09:00',
                    'initial_time_float': 9,
                    'total_time': 90
                },
                {
                    'end_time': '19:30',
                    'end_time_float': 19.5,
                    'initial_time': '18:00',
                    'initial_time_float': 18,
                    'total_time': 90
                },
                {
                    'end_time': '21:00',
                    'end_time_float': 21,
                    'initial_time': '19:30',
                    'initial_time_float': 19.5,
                    'total_time': 90
                },
                {
                    'end_time': '22:00',
                    'end_time_float': 22,
                    'initial_time': '21:00',
                    'initial_time_float': 21,
                    'total_time': 60
                }
            ],
            'end_time': '23:00',
            'end_time_float': 23,
            'fixed_times': [
                {
                    'end_time': '12:00',
                    'end_time_float': 12,
                    'id': 621,
                    'initial_time': '10:30',
                    'initial_time_float': 10.5,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '13:30',
                    'end_time_float': 13.5,
                    'id': 622,
                    'initial_time': '12:00',
                    'initial_time_float': 12,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '15:00',
                    'end_time_float': 15,
                    'id': 623,
                    'initial_time': '13:30',
                    'initial_time_float': 13.5,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '16:30',
                    'end_time_float': 16.5,
                    'id': 624,
                    'initial_time': '15:00',
                    'initial_time_float': 15,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '18:00',
                    'end_time_float': 18,
                    'id': 625,
                    'initial_time': '16:30',
                    'initial_time_float': 16.5,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                }
            ],
            'id': '13',
            'initial_time': '09:00',
            'initial_time_float': 9,
            'name': 'Pádel 1',
            'provider': 'Conecta'
        },
        {
            'bookings': [
                {
                    'end_time': '20:00',
                    'end_time_float': 20,
                    'initial_time': '09:30',
                    'initial_time_float': 9.5,
                    'total_time': 630
                }
            ],
            'end_time': '23:00',
            'end_time_float': 23,
            'fixed_times': [
                {
                    'end_time': '11:00',
                    'end_time_float': 11,
                    'id': 849,
                    'initial_time': '09:30',
                    'initial_time_float': 9.5,
                    'price': '$ 20.000',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '12:30',
                    'end_time_float': 12.5,
                    'id': 850,
                    'initial_time': '11:00',
                    'initial_time_float': 11,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '14:00',
                    'end_time_float': 14,
                    'id': 851,
                    'initial_time': '12:30',
                    'initial_time_float': 12.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '15:30',
                    'end_time_float': 15.5,
                    'id': 852,
                    'initial_time': '14:00',
                    'initial_time_float': 14,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '17:00',
                    'end_time_float': 17,
                    'id': 853,
                    'initial_time': '15:30',
                    'initial_time_float': 15.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '18:30',
                    'end_time_float': 18.5,
                    'id': 854,
                    'initial_time': '17:00',
                    'initial_time_float': 17,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '20:00',
                    'end_time_float': 20,
                    'id': 855,
                    'initial_time': '18:30',
                    'initial_time_float': 18.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                }
            ],
            'id': '14',
            'initial_time': '09:00',
            'initial_time_float': 9,
            'name': 'Pádel 2',
            'provider': 'Conecta'
        },
        {
            'bookings': [
                {
                    'end_time': '10:30',
                    'end_time_float': 10.5,
                    'initial_time': '09:00',
                    'initial_time_float': 9,
                    'total_time': 90
                },
                {
                    'end_time': '21:00',
                    'end_time_float': 21,
                    'initial_time': '19:30',
                    'initial_time_float': 19.5,
                    'total_time': 90
                },
                {
                    'end_time': '22:00',
                    'end_time_float': 22,
                    'initial_time': '21:00',
                    'initial_time_float': 21,
                    'total_time': 60
                }
            ],
            'end_time': '23:00',
            'end_time_float': 23,
            'fixed_times': [
                {
                    'end_time': '12:00',
                    'end_time_float': 12,
                    'id': 621,
                    'initial_time': '10:30',
                    'initial_time_float': 10.5,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '13:30',
                    'end_time_float': 13.5,
                    'id': 622,
                    'initial_time': '12:00',
                    'initial_time_float': 12,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '15:00',
                    'end_time_float': 15,
                    'id': 623,
                    'initial_time': '13:30',
                    'initial_time_float': 13.5,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '16:30',
                    'end_time_float': 16.5,
                    'id': 624,
                    'initial_time': '15:00',
                    'initial_time_float': 15,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '18:00',
                    'end_time_float': 18,
                    'id': 625,
                    'initial_time': '16:30',
                    'initial_time_float': 16.5,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                },
                {
                    'end_time': '19:30',
                    'end_time_float': 19.5,
                    'id': 626,
                    'initial_time': '18:00',
                    'initial_time_float': 18,
                    'price': '',
                    'total_time': 90,
                    'valid': True
                }
            ],
            'id': '15',
            'initial_time': '09:00',
            'initial_time_float': 9,
            'name': 'Pádel 3',
            'provider': 'Conecta'
        },
        {
            'bookings': [
                {
                    'end_time': '20:00',
                    'end_time_float': 20,
                    'initial_time': '09:30',
                    'initial_time_float': 9.5,
                    'total_time': 630
                }
            ],
            'end_time': '23:00',
            'end_time_float': 23,
            'fixed_times': [
                {
                    'end_time': '11:00',
                    'end_time_float': 11,
                    'id': 849,
                    'initial_time': '09:30',
                    'initial_time_float': 9.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '12:30',
                    'end_time_float': 12.5,
                    'id': 850,
                    'initial_time': '11:00',
                    'initial_time_float': 11,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '14:00',
                    'end_time_float': 14,
                    'id': 851,
                    'initial_time': '12:30',
                    'initial_time_float': 12.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '15:30',
                    'end_time_float': 15.5,
                    'id': 852,
                    'initial_time': '14:00',
                    'initial_time_float': 14,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '17:00',
                    'end_time_float': 17,
                    'id': 853,
                    'initial_time': '15:30',
                    'initial_time_float': 15.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '18:30',
                    'end_time_float': 18.5,
                    'id': 854,
                    'initial_time': '17:00',
                    'initial_time_float': 17,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '20:00',
                    'end_time_float': 20,
                    'id': 855,
                    'initial_time': '18:30',
                    'initial_time_float': 18.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                }
            ],
            'id': '16',
            'initial_time': '09:00',
            'initial_time_float': 9,
            'name': 'Pádel 4',
            'provider': 'Conecta'
        },
        {
            'bookings': [
                {
                    'end_time': '10:00',
                    'end_time_float': 10,
                    'initial_time': '09:00',
                    'initial_time_float': 9,
                    'total_time': 60
                },
                {
                    'end_time': '14:00',
                    'end_time_float': 14,
                    'initial_time': '10:00',
                    'initial_time_float': 10,
                    'total_time': 240
                },
                {
                    'end_time': '15:00',
                    'end_time_float': 15,
                    'initial_time': '14:00',
                    'initial_time_float': 14,
                    'total_time': 60
                },
                {
                    'end_time': '23:00',
                    'end_time_float': 23,
                    'initial_time': '15:00',
                    'initial_time_float': 15,
                    'total_time': 480
                }
            ],
            'end_time': '23:00',
            'end_time_float': 23,
            'fixed_times': [
                {
                    'end_time': '10:30',
                    'end_time_float': 10.5,
                    'id': 620,
                    'initial_time': '09:00',
                    'initial_time_float': 9,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '12:00',
                    'end_time_float': 12,
                    'id': 621,
                    'initial_time': '10:30',
                    'initial_time_float': 10.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '13:30',
                    'end_time_float': 13.5,
                    'id': 622,
                    'initial_time': '12:00',
                    'initial_time_float': 12,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '15:00',
                    'end_time_float': 15,
                    'id': 623,
                    'initial_time': '13:30',
                    'initial_time_float': 13.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '16:30',
                    'end_time_float': 16.5,
                    'id': 624,
                    'initial_time': '15:00',
                    'initial_time_float': 15,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '18:00',
                    'end_time_float': 18,
                    'id': 625,
                    'initial_time': '16:30',
                    'initial_time_float': 16.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '19:30',
                    'end_time_float': 19.5,
                    'id': 626,
                    'initial_time': '18:00',
                    'initial_time_float': 18,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '21:00',
                    'end_time_float': 21,
                    'id': 627,
                    'initial_time': '19:30',
                    'initial_time_float': 19.5,
                    'price': '',
                    'total_time': 90,
                    'valid': False
                },
                {
                    'end_time': '22:00',
                    'end_time_float': 22,
                    'id': 898,
                    'initial_time': '21:00',
                    'initial_time_float': 21,
                    'price': '',
                    'total_time': 60,
                    'valid': False
                }
            ],
            'id': '17',
            'initial_time': '09:00',
            'initial_time_float': 9,
            'name': 'Pádel 5',
            'provider': 'Conecta'
        }
    ],
    'end_time': '23:00',
    'end_time_float': 23,
    'initial_time': '09:00',
    'initial_time_float': 9,
    'name': 'Conecta'
}
