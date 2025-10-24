from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from destinations.models import Region, Destination
import requests
from io import BytesIO


class Command(BaseCommand):
    help = '인도 여행지 초기 데이터 생성'

    def handle(self, *args, **options):
        self.stdout.write('인도 여행지 데이터 생성 시작...')

        # 지역 생성
        north_india, _ = Region.objects.get_or_create(
            name='north',
            defaults={'description': '북인도는 타지마할, 황금사원 등 역사적인 건축물과 히말라야 산맥의 아름다운 풍경을 자랑합니다.'}
        )
        south_india, _ = Region.objects.get_or_create(
            name='south',
            defaults={'description': '남인도는 열대 해변, 백워터, 고대 사원과 독특한 문화가 어우러진 매력적인 지역입니다.'}
        )

        # 북인도 여행지 데이터
        north_destinations = [
            {
                'name': '타지마할',
                'name_en': 'Taj Mahal',
                'description': '무굴 제국의 황제 샤 자한이 사랑하는 아내 뭄타즈 마할을 기리기 위해 건설한 대리석 묘. 인도 이슬람 건축의 정수로 평가받으며 유네스코 세계문화유산으로 지정되었습니다. 완공에 22년이 걸렸으며, 보름달이 뜨는 날을 기준으로 전후 2일간 야간 개장을 합니다.',
                'address': 'Agra, Uttar Pradesh',
                'latitude': 27.175015,
                'longitude': 78.042155,
                'image_url': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800'
            },
            {
                'name': '델리',
                'name_en': 'Delhi',
                'description': '인도의 수도로 인디아 게이트, 레드 포트, 쿠투브 미나르 등 역사적 명소가 가득합니다. 쿠투브 미나르는 인도에서 가장 오래된 이슬람 유적으로 유네스코 세계문화유산입니다. 현대와 전통이 공존하는 도시입니다.',
                'address': 'New Delhi, Delhi',
                'latitude': 28.613939,
                'longitude': 77.209021,
                'image_url': 'https://images.unsplash.com/photo-1597262975002-c5c3b14bbd62?w=800'
            },
            {
                'name': '자이푸르',
                'name_en': 'Jaipur',
                'description': '핑크시티로 불리는 라자스탄 주의 주도. 하와 마할(바람의 궁전)은 950개 이상의 작은 창문으로 유명하며, 궁중 여성들이 거리를 볼 수 있도록 설계되었습니다. 암베르 포트와 시티 팰리스 등 화려한 궁전들이 있습니다.',
                'address': 'Jaipur, Rajasthan',
                'latitude': 26.912434,
                'longitude': 75.787270,
                'image_url': 'https://images.unsplash.com/photo-1603262110160-6d042c9610b9?w=800'
            },
            {
                'name': '바라나시',
                'name_en': 'Varanasi',
                'description': '영혼의 도시로 불리는 힌두교의 성지. 갠지스 강변에서 매일 아침 일출과 함께 진행되는 푸자(예배) 의식을 볼 수 있습니다. 힌두교 신자들은 이곳에서 생을 마감하면 윤회에서 벗어날 수 있다고 믿습니다.',
                'address': 'Varanasi, Uttar Pradesh',
                'latitude': 25.317645,
                'longitude': 82.973914,
                'image_url': 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800'
            },
            {
                'name': '아그라 포트',
                'name_en': 'Agra Fort',
                'description': '아그라의 붉은 요새로 불리는 거대한 무굴제국의 성벽. 1566년 악바르 대제가 건설했으며 유네스코 세계문화유산입니다. 샤자한이 아들에게 권력을 빼앗기고 8년간 유폐되었던 곳으로, 이곳에서 타지마할을 바라보며 여생을 보냈습니다.',
                'address': 'Agra, Uttar Pradesh',
                'latitude': 27.179500,
                'longitude': 78.021400,
                'image_url': 'https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800'
            },
            {
                'name': '우다이푸르',
                'name_en': 'Udaipur',
                'description': '화이트 시티로 불리는 호수의 도시. 피촐라 호수 위에 떠 있는 레이크 팰리스는 세계에서 가장 로맨틱한 호텔 중 하나로 꼽힙니다. 시티 팰리스와 자그 만디르 등 아름다운 궁전들이 호수를 둘러싸고 있습니다.',
                'address': 'Udaipur, Rajasthan',
                'latitude': 24.585445,
                'longitude': 73.712479,
                'image_url': 'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800'
            },
        ]

        # 남인도 여행지 데이터
        south_destinations = [
            {
                'name': '마이소르 궁전',
                'name_en': 'Mysore Palace',
                'description': '카르나타카 주의 랜드마크로 매년 60만 명이 넘는 관광객이 방문하는 타지마할에 버금가는 명소입니다. 1912년 영국 식민지 시절 헨리 어윈에 의해 설계되었으며, 야간 조명으로 밤에 더욱 아름다운 야경을 자랑합니다.',
                'address': 'Mysore, Karnataka',
                'latitude': 12.305160,
                'longitude': 76.655197,
                'image_url': 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800'
            },
            {
                'name': '케랄라 알레피',
                'name_en': 'Alleppey Kerala',
                'description': '백워터 보트투어로 유명한 남인도의 베니스. 하우스보트를 타고 야자수와 논이 펼쳐진 수로를 따라 이동하며 시간대별로 변하는 물빛을 구경할 수 있습니다. 케랄라의 전통 생활을 경험할 수 있는 최고의 장소입니다.',
                'address': 'Alappuzha, Kerala',
                'latitude': 9.498066,
                'longitude': 76.338947,
                'image_url': 'https://images.unsplash.com/photo-1593693411515-c20261bcad6e?w=800'
            },
            {
                'name': '첸나이',
                'name_en': 'Chennai',
                'description': '남인도 최대 도시이자 타밀나두 주의 주도. 마리나 비치는 세계에서 두 번째로 긴 도시 해변입니다. 산토메 성당은 예수의 제자 도마가 순교한 성지로 알려져 있으며, 카팔리쉬와라 사원 등 드라비다 건축의 정수를 볼 수 있습니다.',
                'address': 'Chennai, Tamil Nadu',
                'latitude': 13.082680,
                'longitude': 80.270721,
                'image_url': 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800'
            },
            {
                'name': '고아',
                'name_en': 'Goa',
                'description': '인도의 대표적인 해변 휴양지. 포르투갈 식민지 유산으로 유럽풍 건축물과 성당이 많습니다. 바가 비치, 칼랑구트 비치 등 아름다운 해변과 함께 요가 리트리트, 스파이스 농장 투어 등 다양한 액티비티를 즐길 수 있습니다.',
                'address': 'Goa',
                'latitude': 15.299326,
                'longitude': 74.123996,
                'image_url': 'https://images.unsplash.com/photo-1559628376-f3fe5f782a2e?w=800'
            },
            {
                'name': '함피',
                'name_en': 'Hampi',
                'description': '14세기 비자야나가라 제국의 수도였던 유적지. 유네스코 세계문화유산으로 지정된 거대한 바위 언덕과 고대 사원 유적이 펼쳐져 있습니다. 비룹악샤 사원, 비탈라 사원의 돌 전차 등 놀라운 건축물들이 있습니다.',
                'address': 'Hampi, Karnataka',
                'latitude': 15.335000,
                'longitude': 76.460000,
                'image_url': 'https://images.unsplash.com/photo-1596402184320-417e7178b2cd?w=800'
            },
            {
                'name': '마하발리푸람',
                'name_en': 'Mahabalipuram',
                'description': '첸나이 근처의 고대 항구 도시로 유네스코 세계문화유산. 푸른 바다를 병풍 삼은 해안 사원(Shore Temple)과 거대한 바위에 조각된 아르주나의 고행 부조가 유명합니다. 7세기 팔라바 왕조의 걸작 석조 건축물들이 있습니다.',
                'address': 'Mahabalipuram, Tamil Nadu',
                'latitude': 12.616667,
                'longitude': 80.192778,
                'image_url': 'https://images.unsplash.com/photo-1596422846543-75c6fc197f07?w=800'
            },
        ]

        # 북인도 여행지 생성
        for data in north_destinations:
            image_url = data.pop('image_url')
            destination, created = Destination.objects.get_or_create(
                name=data['name'],
                region=north_india,
                defaults=data
            )

            if created:
                # 이미지 다운로드 및 저장 (실제 운영에서는 로컬 이미지 사용 권장)
                try:
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        image_content = ContentFile(response.content)
                        destination.image.save(f"{data['name_en']}.jpg", image_content, save=True)
                        self.stdout.write(self.style.SUCCESS(f'✓ {data["name"]} 생성 완료 (이미지 포함)'))
                    else:
                        self.stdout.write(self.style.WARNING(f'✓ {data["name"]} 생성 완료 (이미지 다운로드 실패)'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'✓ {data["name"]} 생성 완료 (이미지 오류: {str(e)})'))
            else:
                self.stdout.write(f'- {data["name"]} 이미 존재함')

        # 남인도 여행지 생성
        for data in south_destinations:
            image_url = data.pop('image_url')
            destination, created = Destination.objects.get_or_create(
                name=data['name'],
                region=south_india,
                defaults=data
            )

            if created:
                try:
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        image_content = ContentFile(response.content)
                        destination.image.save(f"{data['name_en']}.jpg", image_content, save=True)
                        self.stdout.write(self.style.SUCCESS(f'✓ {data["name"]} 생성 완료 (이미지 포함)'))
                    else:
                        self.stdout.write(self.style.WARNING(f'✓ {data["name"]} 생성 완료 (이미지 다운로드 실패)'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'✓ {data["name"]} 생성 완료 (이미지 오류: {str(e)})'))
            else:
                self.stdout.write(f'- {data["name"]} 이미 존재함')

        self.stdout.write(self.style.SUCCESS('\n인도 여행지 데이터 생성 완료!'))
        self.stdout.write(f'총 {Destination.objects.count()}개의 여행지가 생성되었습니다.')
