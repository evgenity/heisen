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
        <tr class="wrapper">
          <td class="content-right"><img class="u-max-full-width partner-logo" src="{{ p.logo | absolute_url }}"></td>
          <td class="content-left">{{p.description}}</td>
        </tr>
        {% endfor %}
      </table>
    </div>
  </div>
</div>