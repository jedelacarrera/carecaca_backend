# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_fixed_times 1'] = {
    'image_url': 'http://www.clubconecta.cl/images.ashx?cmd=get&id=8',
    'options': [
        {
            'description': 'Reservar',
            'token': 'f71c1ed1cedb14327ab1a16c00bb1fd5930a89302d86b5a61bc1289ed71b25d36f5368fca7319b2c23d960d02d6e2515'
        }
    ],
    'title': 'Pádel 3 12:00 13:30'
}

snapshots['test_get_schedule 1'] = {
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

snapshots['test_get_availability 1'] = {
    'image_url': 'http://padeloriente.cl/images.ashx?cmd=get&id=6',
    'options': [
        {
            'description': "60' Defecto",
            'token': 'e7e81ed9881919a99516881ccb8f99ace4b6398d9ba174475a294c07f7ce2422bab15dcfac0a87a3181dae383d104e99'
        },
        {
            'description': "90' Defecto",
            'token': 'e7e81ed9881919a99516881ccb8f99ace4b6398d9ba174475a294c07f7ce24223d8cddd22b2619de3becf7208f7f69f3'
        },
        {
            'description': "120' Defecto",
            'token': 'e7e81ed9881919a99516881ccb8f99ace4b6398d9ba174475a294c07f7ce242226f30ab2f62bc44b15afeec2746e1b39'
        }
    ],
    'title': 'Cancha 1 28/11/2020 13:30'
}
