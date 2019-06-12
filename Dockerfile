FROM jekyll/jekyll:3


WORKDIR /site
EXPOSE 4000

COPY ["Gemfile*", "/site/"]

RUN bundle install

CMD [ "/bin/bash" ]
