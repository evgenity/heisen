---
layout: home
title: About
permalink: /partners/
---

<div class="block-3">
  <div class="container projects">
    <div class="row">
      <div class="twelve columns block-header">
        <h4>Партнёры</h4>
      </div>
    </div>
    <div class="container">
      <table class="u-full-width">
        {% for p in site.partners %}
        <tr>
          <td><img class="u-max-full-width partner-logo" src="{{ p.logo | absolute_url }}"></td>
        </tr>
        {% endfor %}
      </table>
    </div>
  </div>
</div>