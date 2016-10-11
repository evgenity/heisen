---
layout: home
title: About
permalink: /team/
---

<div class="block-3 team">
	<div class="container">
		<div class="row">
			<div class="twelve columns block-header">
				<h4>Наша команда</h4>
			</div>
		</div>
		<div class="row names-team">
			{% for a in site.teamates %}
			<div class="two columns member">
				<img class="u-max-full-width avatar" src="{{ a.avatar }}">
				<p class=""> {{ a.display}}</p>
			</div>
			{% endfor %}
		</div>
	</div>
</div>