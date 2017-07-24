# github-license-recommender

There are lot of projects going on in various companies. These projects mainly use various manifest files for their respective projects. For example, pom.xml for maven ecosystem, requirement.txt for pypi ecosystem, package.json for npm ecosystem etc. 

Now at large scale, it is very difficult to identify the license of the project as various packages/libraries used inside it will have separate licenses. Some of them are compatible with each other and some are not. An approach is implemented here. 

This work mainly focuses on the GitHub standard licenses. It uses the networkx as the graph backbone for finding compatible and suitable licenses for a package level and manifest file level recommendation.

This work is highly influenced by David A. Wheeler (https://www.dwheeler.com/essays/floss-license-slide.html).


