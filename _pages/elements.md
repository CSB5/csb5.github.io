---
layout: page
title: Elements
description: List of styles that can be used in a blog post.
permalink: /elements/
---

**Refer to [this source file](https://github.com/csb5-page/csb5-page.github.io/blob/main/_pages/elements.md?plain=1) to see how to use those styles in a markdown file.**

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in sem imperdiet, semper lectus nec, pharetra nibh. Vestibulum volutpat fringilla leo, nec mollis ante gravida eu. Duis et tortor a dui tristique rhoncus. Nullam vitae commodo orci. Curabitur sed nibh quis quam condimentum volutpat. Morbi orci ex, ullamcorper et consequat vitae, volutpat nec ante. Pellentesque ultricies ligula porttitor lorem aliquet suscipit. Maecenas hendrerit metus ac suscipit viverra. Duis sed fermentum lorem, ac egestas massa. Donec quis orci placerat, blandit lacus quis, ornare dolor. Morbi et luctus velit. Proin tincidunt magna a nisi ultrices fermentum. Nam dictum iaculis orci, sed ultricies nibh aliquet in. Donec eget quam dolor. Aliquam quis metus et urna finibus ultricies.

***

## Headings by default:

# H1 Default styles for headings
## H2 Default styles for headings
### H3 Default styles for headings
#### H4 Default styles for headings
##### H5 Default styles for headings
###### H6 Default styles for headings

***

## Lists

### Ordered list example:

1. Poutine drinking vinegar bitters.
2. Coloring book distillery fanny pack.
3. Venmo biodiesel gentrify enamel pin meditation.
4. Jean shorts shaman listicle pickled portland.
5. Salvia mumblecore brunch iPhone migas.

***

### Unordered list example:

* Bitters semiotics vice thundercats synth.
* Literally cred narwhal bitters wayfarers.
* Kale chips chartreuse paleo tbh street art marfa.
* Mlkshk polaroid sriracha brooklyn.
* Pug you probably haven't heard of them air plant man bun.

***

## Table

<div class="table-container">
  <table>
    <tr><th>Header 1</th><th>Header 2</th><th>Header 3</th><th>Header 4</th><th>Header 5</th></tr>
    <tr><td>Row:1 Cell:1</td><td>Row:1 Cell:2</td><td>Row:1 Cell:3</td><td>Row:1 Cell:4</td><td>Row:1 Cell:5</td></tr>
    <tr><td>Row:2 Cell:1</td><td>Row:2 Cell:2</td><td>Row:2 Cell:3</td><td>Row:2 Cell:4</td><td>Row:2 Cell:5</td></tr>
    <tr><td>Row:3 Cell:1</td><td>Row:3 Cell:2</td><td>Row:3 Cell:3</td><td>Row:3 Cell:4</td><td>Row:3 Cell:5</td></tr>
    <tr><td>Row:4 Cell:1</td><td>Row:4 Cell:2</td><td>Row:4 Cell:3</td><td>Row:4 Cell:4</td><td>Row:4 Cell:5</td></tr>
    <tr><td>Row:5 Cell:1</td><td>Row:5 Cell:2</td><td>Row:5 Cell:3</td><td>Row:5 Cell:4</td><td>Row:5 Cell:5</td></tr>
    <tr><td>Row:6 Cell:1</td><td>Row:6 Cell:2</td><td>Row:6 Cell:3</td><td>Row:6 Cell:4</td><td>Row:6 Cell:5</td></tr>
  </table>
</div>

***

## Quotes

#### A quote looks like this:

> The longer I live, the more I realize that I am never wrong about anything, and that all the pains I have so humbly taken to verify my notions have only wasted my time!
>
> <cite>George Bernard Shaw</cite>

***

## Syntax Highlighter

{% highlight css %}
body {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #1c2021;
}

li {
  width: 200px;
  min-height: 250px;
  border: 1px solid #000;
  display: inline-block;
  vertical-align: top;
  margin: 5px;
}
{% endhighlight %}

{% highlight js %}
  $('.top').click(function () {
    $('html, body').stop().animate({ scrollTop: 0 }, 'slow', 'swing');
  });
  $(window).scroll(function () {
    if ($(this).scrollTop() > $(window).height()) {
      $('.top').addClass("top-active");
    } else {
      $('.top').removeClass("top-active");
    };
  });
{% endhighlight %}

***

## Images

![](/images/activities/2025-04-25-barbecue/group_photo.jpg)
*A regular image.*

![](/images/activities/2025-04-25-barbecue/group_photo.jpg#wide)
*A large image.*

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/resting_dough.jpg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/making_pasta.jpg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/pasta_machine.jpg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/aarthi.jpg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/zhenhao.jpg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/seeusi.jpg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/making_pasta_everyone.jpeg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/making_pasta_smiling.jpeg" loading="lazy">
    <img src="/images/activities/2025-07-17-pasta-making-durian-tasting/pasta_shapes.jpg" loading="lazy">
  </div>
  <em>A grid of many images.</em>
</div>

***

## Youtube Embed

<p><iframe src="https://www.youtube.com/embed/7VoGbMaiaI8" loading="lazy" frameborder="0" allowfullscreen></iframe></p>

***

## Video Embed

<video width="100%" controls>
  <source src="/images/activities/2025-07-17-pasta-making-durian-tasting/pasta_out.mp4" type="video/mp4">
</video>