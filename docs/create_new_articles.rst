Create new articles
===================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample article list
-------------------

.. code-block:: console

    User = get_user_model()

    Article.objects.create(
        author = User.objects.first(),
        title = "Test Article 1",
        slug = "test-article-1",
        body = "This is a test from the shell",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="susan"),
        title = "Test Article 2",
        slug = "test-article-2",
        body = "This is a second test from the shell",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.first(),
        title = "Django REST framework is a powerful toolkit",
        slug = "django-rest-framework-is-a-powerful-toolkit",
        body = "Some reasons you might want to use REST framework:\r\n\r\n    The Web browsable API is a huge usability win for your developers.\r\n    Authentication policies including packages for OAuth1a and OAuth2.\r\n    Serialization that supports both ORM and non-ORM data sources.\r\n    Customizable all the way down - just use regular function-based views if you don't need the more powerful features.\r\n    Extensive documentation, and great community support.\r\n    Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="john"),
        title = "On this day in 1928",
        slug = "on-this-day-in-1928",
        body = "Indian physicist C. V. Raman and his colleagues discovered what is now known as Raman scattering, for which he later became the first Asian to win the Nobel Prize in Physics.\r\n Raman scattering or the Raman effect (/ˈrɑːmən/) is the inelastic scattering of photons by matter, meaning that there is both an exchange of energy and a change in the light's direction. Typically this effect involves vibrational energy being gained by a molecule as incident photons from a visible laser are shifted to lower energy.\r\n This is called normal Stokes Raman scattering.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="mary"),
        title = "On this day in 1897",
        slug = "on-this-day-in-1897",
        body = "Ranavalona III, the last sovereign ruler of the Kingdom of Madagascar, was deposed by French military forces. Ranavalona III (Malagasy pronunciation: [ranˈfalunə̥]; November 22, 1861 – May 23, 1917) was the last sovereign of the Kingdom of Madagascar. She ruled from July 30, 1883 to February 28, 1897 in a reign marked by ultimately futile efforts to resist the colonial designs of the government of France.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="susan"),
        title = "Natural philosopy",
        slug = "natural-philosophy",
        body = "Natural philosophy or philosophy of nature (from Latin philosophia naturalis) was the philosophical study of nature and the physical universe that was dominant before the development of modern science.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="david"),
        title = "On this day in 1865",
        slug = "on-this-day-in-1865",
        body = "US President Abraham Lincoln is shot dead in the head by John Wilkes Booth at Ford's Theater in Washington; he dies a day later.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="alice"),
        title = "Civilization and its Discontents",
        slug = "civilization-and-its-discontents",
        body = "The real problem of humanity is the following: We have Paleolithic emotions, medieval institutions and godlike technology. And it is terrifically dangerous, and it is now approaching a point of crisis overall.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="john"),
        title = "On this day in 1865",
        slug = "on-this-day-in-1865",
        body = "Steamboat 'SS Sultana' explodes in the Mississippi River, killing up to 1,800 of the 2,427 passengers in the greatest maritime disaster in United States history. Most were paroled Union POWs on their way home.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="mary"),
        title = "Positivity",
        slug = "positivity",
        body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="susan"),
        title = "Eric Dolphy",
        slug = "eric-dolphy",
        body = "Eric Dolphy was an American jazz alto saxophonist, bass clarinetist and flautist. Dolphy was one of several multi-instrumentalists to gain prominence in the same era. Dolphy extended the vocabulary and boundaries of the alto saxophone, and was among the earliest significant jazz flute soloists.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="david"),
        title = "PEP 673: Self Type Was Accepted",
        slug = "pep-673-self-type-was-accepted",
        body = "This PEP introduces a simple and intuitive way to annotate methods that return an instance of their class. This behaves the same as the TypeVar-based approach specified in PEP 484 but is more concise and easier to follow.",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="alice"),
        title = "Upcoming Python Feature PEPs",
        slug = "upcoming-python-feature-peps",
        body = "These PEPs are a great way of getting the freshest info about what might be included in the upcoming Python releases. So, in this article we will go over all the proposals that are going to bring some exciting new Python features in a near future!",
        status = "PB",
    )
    Article.objects.create(
        author = User.objects.get(username="kbowen"),
        title = "Positivity",
        slug = "positivity",
        body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
        status = "PB",
    )
