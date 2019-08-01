from django.core.management import BaseCommand

from apps.staff.models import Team, Role, Staff
from apps.content.models import Event


class Command(BaseCommand):
    help = '''
        team_csv format:
            team.persian_name, team.english_name, team.position_from_top

        role_csv format:
            role.persian_name, role.english_name, role.team.english_name

        data_csv format:
            staff.persian_name, staff,english_name, staff.role.english_name, staff.head_title (empty means they're not head)

        event_id:
            event's id!
    '''

    def add_arguments(self, parser):
        parser.add_argument('team_csv', type=str)
        parser.add_argument('role_csv', type=str)
        parser.add_argument('data_csv', type=str)
        parser.add_argument('event_id', type=str)

    def handle(self, *args, **options):
        try:
            team_csv = options['team_csv']
            role_csv = options['role_csv']
            data_csv = options['data_csv']
            event_id = int(options['event_id'])
        except:
            print("I don't know what but exiting.")
            exit(1)

        if Event.objects.filter(pk=event_id).count() != 1:
            print("Event with id {} not found. exiting.")
            exit(1)
        event = Event.objects.filter(pk=event_id).get()

        Team.objects.filter(event=event).delete()

        with open(team_csv) as f:
            for l in f:
                w = [ll.strip() for ll in l.split(',')]
                if len(w) != 3:
                    print("Broken line at team_csv: {}. exiting.".format(w))
                    exit(1)
                persian_name = w[0]
                english_name = w[1]
                pos_from_top = int(w[2])

                if Team.objects.filter(position_from_top=pos_from_top, event=event).count() != 0:
                    print("Repetetive team position from top at line {}. exiting".format(w))
                    exit(1)

                Team.objects.create(persian_name=persian_name,
                        english_name=english_name,
                        position_from_top=pos_from_top,
                        event=event)

        with open(role_csv) as f:
            for l in f:
                w = [ll.strip() for ll in l.split(',')]
                if len(w) != 3:
                    print("Broken line at role_csv: {}. exiting.".format(w))
                    exit(1)
                persian_name = w[0]
                english_name = w[1]
                team_english_name = w[2]

                team_filter = Team.objects.filter(english_name=team_english_name, event=event)
                if team_filter.count() != 1:
                    print("No\More than one Team with english name: {} found. exiting.".format(team_english_name))
                    exit(1)

                Role.objects.create(persian_name=persian_name,
                        english_name=english_name,
                        team=team_filter.get())

        with open(data_csv) as f:
            for l in f:
                w = [ll.strip() for ll in l.split(',')]
                if len(w) != 4:
                    print("Broken line at data_csv: {}. exiting.".format(w))
                    exit(1)

                persian_name = w[0]
                english_name = w[1]
                role_english_name = w[2]
                head_title = w[3]

                role_filter = Role.objects.filter(english_name=role_english_name)
                if role_filter.count() != 1:
                    print("No\More than one role with english name: {} found. exiting.".format(role_english_name))
                    exit(1)

                Staff.objects.create(persian_name=persian_name, english_name=english_name, role=role_filter.get(), head_title=head_title)


