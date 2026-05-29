from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def programs(request):
    return render(request, 'website/programs.html')   # you can create placeholder later

def about(request):
    return render(request, 'website/about.html')

def events(request):
    return render(request, 'website/events.html')

def impact(request):
    return render(request, 'website/impact.html')

def contact(request):
    return render(request, 'website/contact.html')

def get_involved(request):
    return render(request, 'website/get_involved.html')


def application(request):
    if request.method == 'POST':
        # Process the form data here (save to database, send email, etc.)
        # For now, just redirect to a thank‑you page or show a success message
        return render(request, 'website/application_success.html')  # optional
    return render(request, 'website/application.html')



def volunteer(request):
    if request.method == 'POST':
        # Process volunteer data here
        return render(request, 'website/application_success.html')  # or a dedicated success page
    return render(request, 'website/volunteer.html')




def partner(request):
    if request.method == 'POST':
        # Process partnership enquiry (save to DB, send email, etc.)
        return render(request, 'website/partner_success.html')  # or a success message
    return render(request, 'website/partner.html')



def sponsor(request):
    if request.method == 'POST':
        # Process sponsorship enquiry
        return render(request, 'website/sponsor_success.html')
    return render(request, 'website/sponsor.html')



def conference(request):
    return render(request, 'website/conference.html')


def leadership(request):
    return render(request, 'website/leadership.html')


def peacebuilding(request):
    return render(request, 'website/peacebuilding.html')


def protocol(request):
    return render(request, 'website/protocol.html')


def gender(request):
    return render(request, 'website/gender.html')


def mentorship(request):
    return render(request, 'website/mentorship.html')



def programs(request):
    return render(request, 'website/programs.html')





def event_detail(request, event_slug):
    # Event data dictionary - you can move this to a database later
    events = {
        'annual-conference-2026': {
            'event_title': 'Annual Dream MUN Conference 2026',
            'event_subtitle': 'Three days of immersive diplomatic simulations, policy drafting, and networking with over 300 youth delegates from 20+ African countries.',
            'event_description': 'The flagship Annual Dream MUN Conference returns for its most ambitious edition yet.',
            'event_description_full': 'The Annual Dream MUN Conference is the highlight of our calendar — a three‑day immersive experience where young people step into the shoes of diplomats, represent countries, debate global issues, and draft resolutions that mirror real United Nations processes. Participants are assigned to committees such as the Security Council, General Assembly, ECOWAS, or specialised agencies. They research, negotiate, build coalitions, and present formal policy documents.',
            'event_image': 'img/youth-delegation.webp',
            'event_image_2': 'img/hero-conference.webp',
            'event_days': '3',
            'event_date': '12–14 June 2026',
            'event_location': 'Freetown, Sierra Leone',
            'event_badge': 'Flagship Conference',
            'event_heading': 'Where diplomacy meets youth action',
            'event_year': '2026',
            'event_features': [
                '6 UN committees including Security Council & General Assembly',
                '300+ delegates from 20+ African countries',
                'Professional diplomatic training & protocol workshops',
                'Cultural night & networking dinner',
                'Awards ceremony & certification',
                'Post-conference mentorship opportunities'
            ],
            'event_expect_title': 'Three days that transform you',
            'event_highlights': [
                {'icon': '🏛️', 'title': 'Real UN Simulations', 'description': 'Participate in authentic committee sessions using official rules of procedure. Draft resolutions, deliver speeches, and negotiate with delegates from across Africa.'},
                {'icon': '🎤', 'title': 'Public Speaking & Debate', 'description': 'Sharpen your ability to articulate ideas clearly, think on your feet, and persuade an audience — skills that serve you in any career.'},
                {'icon': '📜', 'title': 'Policy Writing', 'description': 'Learn to research and write formal position papers and resolutions. Receive feedback from experienced chairs and mentors.'},
                {'icon': '🤝', 'title': 'Networking', 'description': 'Connect with 300+ motivated young leaders, diplomats, academics, and partner organisations.'},
                {'icon': '🏆', 'title': 'Awards & Recognition', 'description': 'Outstanding delegates and delegations are recognised with certificates, awards, and opportunities for international events.'},
                {'icon': '🎓', 'title': 'Mentorship Access', 'description': 'Access to our Mentorship Network connecting you with diplomats, policy experts, and professionals.'},
            ],
            'event_schedule': [
                {'day': 'Day 1', 'title': 'Opening Ceremony & Training', 'description': 'Keynote address, diplomatic protocol workshop, committee orientation, and ice‑breaker sessions. Delegates receive country assignments and research briefs.'},
                {'day': 'Day 2', 'title': 'Committee Sessions & Negotiations', 'description': 'Full‑day committee sessions. Delegates present position papers, form blocs, debate topics, and begin drafting resolutions.'},
                {'day': 'Day 3', 'title': 'Final Debate & Closing Ceremony', 'description': 'Committees vote on resolutions, awards are announced, and the conference closes with a networking dinner and cultural night.'},
            ],
            'event_attendees': [
                {'icon': '🎓', 'title': 'University Students', 'description': 'Undergraduate and graduate students interested in international relations, political science, law, or diplomacy.'},
                {'icon': '🏫', 'title': 'High School Students', 'description': 'Secondary school students aged 16+ who want to explore global issues and develop leadership skills early.'},
                {'icon': '💼', 'title': 'Young Professionals', 'description': 'Early-career professionals in policy, development, journalism, or related fields seeking to expand their networks and skills.'},
            ],
            'event_cta_text': 'Whether you\'re a first‑time delegate or a seasoned MUN participant, the Annual Dream MUN Conference offers an experience that will stretch your abilities and expand your horizons.',
        },
        'diplomatic-bootcamp-2026': {
            'event_title': 'Diplomatic Protocol & Public Speaking Bootcamp',
            'event_subtitle': 'Intensive two‑day masterclass covering diplomatic etiquette, speech writing, negotiation tactics, and formal debate procedures.',
            'event_description': 'Master the art of professional diplomacy in this intensive bootcamp.',
            'event_description_full': 'This intensive two‑day bootcamp is designed for youth who want to master the formal skills of diplomacy. From writing position papers to delivering powerful speeches, participants learn by doing — with real‑time feedback from experienced diplomats and trainers. The bootcamp covers everything from UN rules of procedure to cross‑cultural communication.',
            'event_image': 'img/un-chamber.webp',
            'event_image_2': 'img/hero-conference.webp',
            'event_days': '2',
            'event_date': '24–25 August 2026',
            'event_location': 'Virtual',
            'event_badge': 'Training Bootcamp',
            'event_heading': 'Speak, write, and negotiate like a diplomat',
            'event_year': '2026',
            'event_features': [
                'UN rules of procedure & formal debate protocols',
                'Speech writing & delivery techniques',
                'Negotiation & consensus building strategies',
                'Diplomatic etiquette & professional conduct',
                'Cross‑cultural communication skills',
                'Certificate of completion'
            ],
            'event_expect_title': 'Skills that set you apart',
            'event_highlights': [
                {'icon': '📜', 'title': 'Rules of Procedure', 'description': 'Learn formal debate protocols, points of order, motions, and voting procedures used in real UN sessions.'},
                {'icon': '🎤', 'title': 'Public Speaking', 'description': 'Master the art of delivering persuasive speeches with clarity and confidence.'},
                {'icon': '✍️', 'title': 'Policy Writing', 'description': 'Learn to draft position papers and resolutions that meet professional diplomatic standards.'},
                {'icon': '🤝', 'title': 'Negotiation', 'description': 'Develop techniques for effective negotiation and finding common ground among diverse stakeholders.'},
                {'icon': '👔', 'title': 'Diplomatic Etiquette', 'description': 'Understand formal dress codes, seating arrangements, titles, and cultural protocols.'},
                {'icon': '🌍', 'title': 'Cultural Intelligence', 'description': 'Learn to navigate cross‑cultural communication with respect and adaptability.'},
            ],
            'event_schedule': [
                {'day': 'Day 1', 'title': 'Protocol & Procedure', 'description': 'Deep dive into UN rules of procedure, formal debate formats, and diplomatic correspondence. Practice sessions with feedback.'},
                {'day': 'Day 2', 'title': 'Speaking & Negotiation', 'description': 'Speech writing workshop, impromptu speaking drills, negotiation simulations, and closing ceremony with certificates.'},
            ],
            'event_attendees': [
                {'icon': '🎓', 'title': 'Aspiring Diplomats', 'description': 'Youth who want to pursue careers in foreign service, international organisations, or global governance.'},
                {'icon': '🗣️', 'title': 'Public Speakers', 'description': 'Anyone who wants to improve their confidence and effectiveness in public speaking and formal presentations.'},
                {'icon': '🌐', 'title': 'Global Citizens', 'description': 'Young people interested in understanding how international diplomacy works and how to engage effectively.'},
            ],
            'event_cta_text': 'Join this intensive bootcamp and gain the professional skills that will set you apart in any career — from diplomacy to business to civil society.',
        },
        'leadership-sdg-summit-2026': {
            'event_title': 'African Youth Leadership & SDG Summit',
            'event_subtitle': 'A collaborative summit bringing together youth leaders, policy makers, and innovators to design actionable SDG roadmaps for the continent.',
            'event_description': 'Shape Africa\'s sustainable development future at this landmark summit.',
            'event_description_full': 'The African Youth Leadership & SDG Summit is a collaborative gathering that brings together young leaders, policy makers, and innovators from across the continent. Over two days, participants will engage in workshops, panel discussions, and design labs focused on creating actionable roadmaps for achieving the Sustainable Development Goals in Africa. The summit emphasises youth-led solutions and cross‑border collaboration.',
            'event_image': 'img/hero-conference.webp',
            'event_image_2': 'img/global-youth-assembly.webp',
            'event_days': '2',
            'event_date': '5–6 October 2026',
            'event_location': 'Nairobi, Kenya',
            'event_badge': 'Summit',
            'event_heading': 'Youth designing Africa\'s sustainable future',
            'event_year': '2026',
            'event_features': [
                'Keynote addresses from African leaders & policy makers',
                'Interactive SDG design labs & workshops',
                'Policy brief development & presentation',
                'Cross‑border networking with 500+ delegates',
                'Innovation showcase & project funding opportunities',
                'Post‑summit mentorship & implementation support'
            ],
            'event_expect_title': 'Two days of action and collaboration',
            'event_highlights': [
                {'icon': '🌍', 'title': 'SDG Workshops', 'description': 'Deep dive into specific SDGs with experts, developing actionable strategies for local implementation.'},
                {'icon': '💡', 'title': 'Innovation Labs', 'description': 'Design thinking sessions where you create solutions to real development challenges.'},
                {'icon': '📋', 'title': 'Policy Drafting', 'description': 'Work with peers to draft policy briefs that will be shared with decision‑makers.'},
                {'icon': '🤝', 'title': 'Networking', 'description': 'Connect with 500+ youth leaders, innovators, and policy makers from across Africa.'},
                {'icon': '🎤', 'title': 'Speaking Opportunities', 'description': 'Present your ideas on stage and get feedback from experienced leaders.'},
                {'icon': '🌱', 'title': 'Project Funding', 'description': 'Top projects receive seed funding and mentorship to turn ideas into reality.'},
            ],
            'event_schedule': [
                {'day': 'Day 1', 'title': 'Keynotes & SDG Labs', 'description': 'Opening ceremony, keynote speeches from African leaders, SDG deep‑dive workshops, and innovation lab sessions.'},
                {'day': 'Day 2', 'title': 'Policy Design & Closing', 'description': 'Policy brief drafting, project presentations, funding announcements, and closing ceremony with cultural celebration.'},
            ],
            'event_attendees': [
                {'icon': '🌍', 'title': 'Youth Activists', 'description': 'Young people already working on SDG-related projects in their communities who want to scale their impact.'},
                {'icon': '💼', 'title': 'Social Entrepreneurs', 'description': 'Innovators and entrepreneurs developing solutions aligned with the SDGs.'},
                {'icon': '🏛️', 'title': 'Policy Enthusiasts', 'description': 'Students and professionals interested in understanding how policy can drive sustainable development.'},
            ],
            'event_cta_text': 'Be part of Africa\'s most ambitious youth-led summit on sustainable development. Your ideas can shape the continent\'s future.',
        },
    }
    
    event = events.get(event_slug)
    if not event:
        # If event not found, you could return a 404 or redirect to events page
        from django.http import Http404
        raise Http404("Event not found")
    
    return render(request, 'website/event_detail.html', event)




