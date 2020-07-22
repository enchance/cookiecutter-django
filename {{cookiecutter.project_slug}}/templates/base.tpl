{% load static i18n coretags corefilters %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- <meta property="og:url" content="">
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="">
    <meta property="og:title" content="">
    <meta property="og:description" content="">
    <meta property="og:image" content="">
    <meta property="og:image:width" content="">
    <meta property="og:image:height" content="">

    <meta name="googlebot" content="index,follow">
    <meta name="google" content="notranslate">
    <meta name="robots" content="index,follow">
    <meta name="theme-color" content="#D4E7FF">
    <link rel="publisher" href=""> -->

    {% block meta %}{% endblock %}

    {#    <link rel="shortcut icon" type="image/png" href="{% static '' %}" />#}

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
    <![endif]-->

    <link rel="stylesheet" type="text/css" href="{% static 'css/style.min.css' %}">

    <title>{% block title %}{{ title }}{% endblock %} | {{ sitename }}</title>

    {% block css %}{% endblock %}

</head>
<body class="starter-theme {{ body_class }} {% block body_class %}{% endblock %}">


{% block content %}
    <p>Use this document as a way to quick start any new project.</p>
{% endblock %}


<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>

{% if settings.DEBUG %}
    <link rel="stylesheet" type="text/css" href="{% static 'fontawesome/css/all.min.css' %}">
{% else %}
    <script defer src="https://kit.fontawesome.com/32259de65d.js" crossorigin="anonymous"></script>
{% endif %}

<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

<script src="{% static 'js/init.js' %}" defer></script>
<script src="{% static 'js/autosize.min.js' %}" defer></script>
<script>
    $(function() {
        // Disable the submit button to prevent multiple submissions
        $('form').submit(function() {
            $(this).find('input[type="submit"]').addClass('disabled')
        })

        // Autogrow textarea
        autosize($('textarea'));
    })
</script>

{% block js %}{% endblock %}

</body>
</html>


