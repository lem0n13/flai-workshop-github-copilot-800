from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        
        self.stdout.write(self.style.SUCCESS('Connected to MongoDB...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        
        # Create unique index on email field
        self.stdout.write('Creating unique index on email field...')
        db.users.create_index([("email", 1)], unique=True)
        
        # Create Teams
        self.stdout.write('Creating teams...')
        teams_data = [
            {
                "_id": "team_marvel",
                "name": "Team Marvel",
                "description": "Avengers Assemble! The mightiest heroes of Earth.",
                "created_at": datetime.now().isoformat(),
                "member_count": 0
            },
            {
                "_id": "team_dc",
                "name": "Team DC",
                "description": "Justice League - Defending truth and justice.",
                "created_at": datetime.now().isoformat(),
                "member_count": 0
            }
        ]
        db.teams.insert_many(teams_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(teams_data)} teams'))
        
        # Create Users (Superheroes)
        self.stdout.write('Creating superhero users...')
        users_data = [
            # Team Marvel
            {
                "name": "Tony Stark",
                "email": "ironman@marvel.com",
                "team": "team_marvel",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Steve Rogers",
                "email": "captainamerica@marvel.com",
                "team": "team_marvel",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Thor Odinson",
                "email": "thor@marvel.com",
                "team": "team_marvel",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Natasha Romanoff",
                "email": "blackwidow@marvel.com",
                "team": "team_marvel",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Bruce Banner",
                "email": "hulk@marvel.com",
                "team": "team_marvel",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            # Team DC
            {
                "name": "Clark Kent",
                "email": "superman@dc.com",
                "team": "team_dc",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Bruce Wayne",
                "email": "batman@dc.com",
                "team": "team_dc",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Diana Prince",
                "email": "wonderwoman@dc.com",
                "team": "team_dc",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Barry Allen",
                "email": "flash@dc.com",
                "team": "team_dc",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "Arthur Curry",
                "email": "aquaman@dc.com",
                "team": "team_dc",
                "role": "member",
                "points": 0,
                "created_at": datetime.now().isoformat()
            }
        ]
        result = db.users.insert_many(users_data)
        user_ids = result.inserted_ids
        self.stdout.write(self.style.SUCCESS(f'Created {len(users_data)} superhero users'))
        
        # Update team member counts
        db.teams.update_one({"_id": "team_marvel"}, {"$set": {"member_count": 5}})
        db.teams.update_one({"_id": "team_dc"}, {"$set": {"member_count": 5}})
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts_data = [
            {
                "name": "Super Soldier Strength",
                "description": "Captain America's training routine for peak performance",
                "category": "strength",
                "duration_minutes": 45,
                "difficulty": "advanced",
                "exercises": [
                    {"name": "Bench Press", "sets": 4, "reps": 10},
                    {"name": "Squats", "sets": 4, "reps": 12},
                    {"name": "Deadlifts", "sets": 3, "reps": 8}
                ]
            },
            {
                "name": "Stark Cardio Blast",
                "description": "High-intensity cardio to keep up with Iron Man's suit",
                "category": "cardio",
                "duration_minutes": 30,
                "difficulty": "intermediate",
                "exercises": [
                    {"name": "Running", "duration": "15 minutes"},
                    {"name": "Jumping Jacks", "sets": 3, "reps": 50},
                    {"name": "Burpees", "sets": 3, "reps": 20}
                ]
            },
            {
                "name": "Asgardian Warrior Training",
                "description": "Thor's legendary hammer-wielding workout",
                "category": "strength",
                "duration_minutes": 60,
                "difficulty": "advanced",
                "exercises": [
                    {"name": "Hammer Swings", "sets": 5, "reps": 15},
                    {"name": "Battle Ropes", "sets": 4, "duration": "45 seconds"},
                    {"name": "Overhead Press", "sets": 4, "reps": 10}
                ]
            },
            {
                "name": "Speedster Sprint",
                "description": "Flash-inspired speed and agility training",
                "category": "cardio",
                "duration_minutes": 25,
                "difficulty": "intermediate",
                "exercises": [
                    {"name": "Sprint Intervals", "sets": 6, "duration": "30 seconds"},
                    {"name": "Agility Ladder", "sets": 5, "reps": 3},
                    {"name": "Box Jumps", "sets": 3, "reps": 15}
                ]
            },
            {
                "name": "Bat-Cave Flexibility",
                "description": "Batman's stealth and flexibility routine",
                "category": "flexibility",
                "duration_minutes": 20,
                "difficulty": "beginner",
                "exercises": [
                    {"name": "Yoga Flow", "duration": "10 minutes"},
                    {"name": "Dynamic Stretching", "duration": "10 minutes"}
                ]
            }
        ]
        result = db.workouts.insert_many(workouts_data)
        workout_ids = result.inserted_ids
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts_data)} workout suggestions'))
        
        # Create Activities
        self.stdout.write('Creating activity logs...')
        activities_data = []
        activity_types = ["running", "cycling", "swimming", "strength training", "yoga", "boxing"]
        
        for i, user_id in enumerate(user_ids):
            # Each user gets 3-5 random activities
            num_activities = random.randint(3, 5)
            user_email = users_data[i]["email"]
            user_name = users_data[i]["name"]
            
            for j in range(num_activities):
                days_ago = random.randint(1, 30)
                date = datetime.now() - timedelta(days=days_ago)
                duration = random.randint(20, 90)
                points = random.randint(10, 50)
                
                activity = {
                    "user_id": user_id,
                    "user_email": user_email,
                    "user_name": user_name,
                    "activity_type": random.choice(activity_types),
                    "duration_minutes": duration,
                    "distance_km": round(random.uniform(2.0, 15.0), 2) if random.random() > 0.5 else None,
                    "calories": duration * random.randint(6, 12),
                    "points": points,
                    "date": date.isoformat(),
                    "notes": f"Great workout session on {date.strftime('%Y-%m-%d')}"
                }
                activities_data.append(activity)
                
                # Update user points
                db.users.update_one(
                    {"_id": user_id},
                    {"$inc": {"points": points}}
                )
        
        db.activities.insert_many(activities_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(activities_data)} activities'))
        
        # Create Leaderboard
        self.stdout.write('Creating leaderboard...')
        
        # Get updated user data with points
        users_with_points = list(db.users.find().sort("points", -1))
        
        leaderboard_data = []
        for rank, user in enumerate(users_with_points, 1):
            leaderboard_entry = {
                "user_id": user["_id"],
                "user_name": user["name"],
                "user_email": user["email"],
                "team": user["team"],
                "points": user["points"],
                "rank": rank,
                "activities_count": len([a for a in activities_data if a["user_id"] == user["_id"]]),
                "last_updated": datetime.now().isoformat()
            }
            leaderboard_data.append(leaderboard_entry)
        
        db.leaderboard.insert_many(leaderboard_data)
        self.stdout.write(self.style.SUCCESS(f'Created leaderboard with {len(leaderboard_data)} entries'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {db.teams.count_documents({})}')
        self.stdout.write(f'Users: {db.users.count_documents({})}')
        self.stdout.write(f'Activities: {db.activities.count_documents({})}')
        self.stdout.write(f'Workouts: {db.workouts.count_documents({})}')
        self.stdout.write(f'Leaderboard: {db.leaderboard.count_documents({})}')
        self.stdout.write(self.style.SUCCESS('===================================\n'))
        
        client.close()
