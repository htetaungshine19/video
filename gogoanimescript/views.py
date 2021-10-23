from django.shortcuts import render
from django.http import HttpResponse
from .script import get_video_stream_url


def test(request):
    return HttpResponse(get_video_stream_url(
        "https://gogoanime.pe/dragon-quest-dai-no-daibouken-2020-episode-54"))


