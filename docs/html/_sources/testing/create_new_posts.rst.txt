Create new posts
================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample post list
----------------

.. code-block:: console

    User = get_user_model()

    Post.objects.create(
        author = User.objects.first(),
        title = "Test Post 1",
        slug = "test-post-1",
        body = "This is a test from the shell",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="susan"),
        title = "Test Post 2",
        slug = "test-post-2",
        body = "This is a second test from the shell",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.first(),
        title = "Django REST framework is a powerful toolkit",
        slug = "django-rest-framework-is-a-powerful-toolkit",
        body = "Some reasons you might want to use REST framework:\r\n\r\n    The Web browsable API is a huge usability win for your developers.\r\n    Authentication policies including packages for OAuth1a and OAuth2.\r\n    Serialization that supports both ORM and non-ORM data sources.\r\n    Customizable all the way down - just use regular function-based views if you don't need the more powerful features.\r\n    Extensive documentation, and great community support.\r\n    Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="john"),
        title = "Meet Django",
        slug = "meet-django",
        body = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="mary"),
        title = "Django is ridiculously fast",
        slug = "django-is-ridiculously-fast",
        body = "Django was designed to help developers take applications from concept to completion as quickly as possible.",
    )
    Post.objects.create(
        author = User.objects.get(username="susan"),
        title = "Django is reassuringly secure",
        slug = "django-is-reassuringly-secure",
        body = "Django takes security seriously and helps developers avoid many common security mistakes.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="david"),
        title = "Django is exceedingly scalable",
        slug = "django-is-exceedingly-scalable",
        body = "Some of the busiest sites on the web leverage Django\u2019s ability to quickly and flexibly scale.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="alice"),
        title = "Civilization and its Discontents",
        slug = "civilization-and-its-discontents",
        body = "The real problem of humanity is the following: We have Paleolithic emotions, medieval institutions and godlike technology. And it is terrifically dangerous, and it is now approaching a point of crisis overall.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="john"),
        title = "A painter's credo of service to State and Church",
        slug = "a-painters-credo-of-service-to-state-and-church",
        body = "And I have belief As I kneel now and light a candle, sensing A fitted silence in the weight of things. I am a man bound by indentures, agreements. All things dilate On the glory of empires, the prelates' zeal, The Saviour's great goodness in all His forms.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="mary"),
        title = "Positivity",
        slug = "positivity",
        body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="susan"),
        title = "Who was Eric Dolphy?",
        slug = "who-was-eric-dolphy",
        body = "Eric Dolphy was an American jazz alto saxophonist, bass clarinetist and flautist. Dolphy was one of several multi-instrumentalists to gain prominence in the same era. Dolphy extended the vocabulary and boundaries of the alto saxophone, and was among the earliest significant jazz flute soloists.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="david"),
        title = "PEP 673: Self Type Was Accepted",
        slug = "pep-673-self-type-was-accepted",
        body = "This PEP introduces a simple and intuitive way to annotate methods that return an instance of their class. This behaves the same as the TypeVar-based approach specified in PEP 484 but is more concise and easier to follow.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="alice"),
        title = "Upcoming Python Feature PEPs",
        slug = "upcoming-python-feature-peps",
        body = "These PEPs are a great way of getting the freshest info about what might be included in the upcoming Python releases. So, in this article we will go over all the proposals that are going to bring some exciting new Python features in a near future!",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="kbowen"),
        title = "Positivity",
        slug = "positivity2",
        body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="susan"),
        title  = "Who was Django Reinhardt?",
        slug   = "who-was-django-reinhardt",
        body   = "Jean Reinhardt (23 January 1910 – 16 May 1953), known by his Romani nickname Django (French: [dʒãŋɡo ʁɛjnaʁt] or [dʒɑ̃ɡo ʁenɑʁt]), was a Romani-Belgian jazz guitarist and composer. He was one of the first major jazz talents to emerge in Europe and has been hailed as one of its most significant exponents.\r\n\nWith violinist Stéphane Grappelli,[2] Reinhardt formed the Paris-based Quintette du Hot Club de France in 1934. The group was among the first to play jazz that featured the guitar as a lead instrument.[5] Reinhardt recorded in France with many visiting American musicians, including Coleman Hawkins and Benny Carter, and briefly toured the United States with Duke Ellington's orchestra in 1946. He died suddenly of a stroke in 1953 at the age of 43.",
        status = "PB",
    )
    Post.objects.create(
        author = User.objects.get(username="david"),
        title  = "Who was Charlie Christian?",
        slug   = "who-was-charlie-christian",
        body   = "Charles Henry Christian (July 29, 1916 – March 2, 1942) was an American swing and jazz guitarist. He was among the first electric guitarists and was a key figure in the development of bebop and cool jazz. He gained national exposure as a member of the Benny Goodman Sextet and Orchestra from August 1939 to June 1941. His single-string technique, combined with amplification, helped bring the guitar out of the rhythm section and into the forefront as a solo instrument. For this, he is often credited with leading to the development of the lead guitar role in musical ensembles and bands.",
        status = "PB",
    )
