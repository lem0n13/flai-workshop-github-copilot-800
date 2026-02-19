"""
Management command to update team member counts based on actual user data
"""
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User


class Command(BaseCommand):
    help = 'Update team member counts based on actual user data'

    def handle(self, *args, **kwargs):
        teams = Team.objects.all()
        
        for team in teams:
            # Count actual users in this team
            member_count = User.objects.filter(team=team._id).count()
            team.member_count = member_count
            team.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Updated {team.name}: {member_count} members'
                )
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully updated all team member counts'))
