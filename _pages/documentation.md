---
layout: page
title: Documentation
description: Guide to update the material on the website.
permalink: /documentation/
---

# Table of contents

* [How to create or edit a blog post?](#edit_post)
* [How to deploy my edits to the website?](#commit_changes)
* [How to add images or videos to the posts?](#image_guideline)
* [How to add links and citations?](#citation)
* [How to add people to the lab?](#add_people)
* [How to edit and preview the content in Linux?](#command_line)



<a id="edit_post"></a>

## How to create or edit a blog post?

Creating/editing pages can be done directly on the GitHub webpage if you are not familiar with command line tools. If you are familiar with Linux command line, you may follow [these steps](#command_line) instead.


1. You need to have a [GitHub](https://github.com/) account.

1. Navigate to the [website repository](https://github.com/csb5-page/csb5-page.github.io) and click `fork` on the top right corner.

   ![](/images/misc/documentation/GitHub_page.png)
   *On the top right there are 3 buttons. Click "fork" to create a copy.*

   The fork only needs to be done once, and you may use your forked repository for future commits.

1. Navigate to your **forked repository**. You can find it in your list of repositories (click your profile picture on the top right, and select `Repositories`).

   Before you commit, check if the message `This branch is up to date with csb5-page/csb5-page.github.io:main.` appears at the top of your page. If your branch is behind the main branch, click the `Sync fork` button.

1. Go to the `_posts` folder, click `Add file` on the top right to create a new post or an existing file to edit one.

   ![](/images/misc/documentation/post_page.png)
   *You should see something like this.*

   If you are adding a new file, make sure its name is in the form of `YYYY-MM-DD-your-post-title.markdown`.

1. Every markdown should start with a metadata section. See [this](https://github.com/csb5-page/csb5-page.github.io/blob/main/_posts/2024-12-02-sequencing-non-canonical-bases.markdown?plain=1) file for an example. It contains the following fields. The order of the fields doesn't matter.

   ```yaml
---
layout: post
title: [preferably short project title]
description: [short one- or two-sentence summary of the project]
image: [a pretty image that is going to be the thumbnail of your post]
image_caption: (optional) [caption (or source) of the thumbnail image]
date: (optional) [date of the publication or start of the project in the form of YYYY-MM-DD]
tags: (optional) [list of topics]
preprint: (optional) [link to the published preprint]
paper: (optional) [link to the published paper]
publication: (optional, must define the paper field) [Name of the conference/journal]
code: (optional) [link to the code repository]
author: [one or a list of authors]
featured: false
---
   ```

   The list of authors should take the form `[mauricio, nok, rafael, niranjan]`, where each entry is the `username` defined in the [author page](https://github.com/csb5-page/csb5-page.github.io/blob/main/_authors/1.md?plain=1).

1. Add the content of the post below the metadata. Refer to [this guideline](#image_guideline) for adding images.

1. Commit your changes to the website with [these steps](#commit_changes).

<a id="commit_changes"></a>

## How to deploy my edits to the website?

1. After you finished editing, commit your changes (the green button on top right).

   ![](/images/misc/documentation/commit.png)

1. Once you've done all the commits, navigate again to the main page of your fored repository. You may notice a message that says `This branch is x commit ahead of csb5-page/csb5-page.github.io:main`. Click on `Contribute` and open a pull request (PR)!

   

1. You may see your PR in the `Pull request` tab of the main website repository. A build test will run automatically to check whether your we can build the website successfully with your edits.

   ![](/images/misc/documentation/pr_ready.png)
   *If the build test succeeds (ignore the deployment test), you are good to go!*

1. Ask one of the website maintainer (or become one!) to merge your PR, and soon your edits will appear on the website!

<a id="image_guideline"></a>

## How to add images or videos to the posts?

You can either add images from other websites by copying the image links (not recommended, as the image links will become invalid if the website that contains it gets deleted or edited), or adding the image directly to the repository.

Under `images/posts/`, create a separate folder with the same name as the blog post markdown file, and store all images & videos used in the blog post there.

Find out how to use different styles for fonts, images, and videos in your blog posts in [this demo](https://csb5-page.github.io/elements/) and its [source code](https://github.com/csb5-page/csb5-page.github.io/blob/main/_pages/elements.md?plain=1).


<a id="citation"></a>

## How to add links and citations?

In the markdown file, you can include hyperlinks using the format `[Text](Link)`, 

**Example**:

```markdown
[Preprint](https://www.biorxiv.org/content/10.1101/2025.04.24.650393v1)
```

**Demo**: [Preprint](https://www.biorxiv.org/content/10.1101/2025.04.24.650393v1)

You can also include links that let you jump to another position in the page. The link would look like `[Text](#target_id)`, and the position you would jump to should be labeled with `<a id="target_id"></a>`. **Example**:

```
Here is our preprint [[1](#preprint)].

### References

<a id="preprint">[1]</a> Li, C., Ravikrishnan, A., Wijaya, I., Naim, A. N. M., Gounot, J. S., Wearne, S., ... & Nagarajan, N. (2025). Large-scale skin metagenomics reveals extensive prevalence, coordination, and functional adaptation of skin microbiome dermotypes across body sites. bioRxiv, 2025-04.
```

**Demo**: Here is our preprint [[1](#preprint)].

### References

<a id="preprint">[1]</a> Li, C., Ravikrishnan, A., Wijaya, I., Naim, A. N. M., Gounot, J. S., Wearne, S., ... & Nagarajan, N. (2025). Large-scale skin metagenomics reveals extensive prevalence, coordination, and functional adaptation of skin microbiome dermotypes across body sites. bioRxiv, 2025-04.



<a id="add_people"></a>

## How to add people to the lab?

1. Create a fork of the website repository using the first three steps in [this guide](#edit_post), if you haven't done so already.

1. Under `_authors` folder, create a new markdown file for the person you want to add. The name of the file should be the same as the name of the person.

1. Create the metadata section for the person's info. See [this](https://github.com/csb5-page/csb5-page.github.io/blob/main/_authors/mauricio.md?plain=1) file for an example. It contains the following fields. The order of the fields doesn't matter.

   ```yaml
---
username: [A short phrase, usually the person's first name]
name: [The person's full name]
nick_name: [The person's nick name]
image: [Link to the person's photo]
image_fun: (optional) [Link to the person's photo]
email: (optional) [Email address]
website: (optional) [Personal webpage]
scholar: (optional) [Google scholar profile]
research_gate: (optional) [Research gate profile]
orcid: (optional) [ORCID profile]
github: (optional) [GitHub profile]
X: (optional) [X page]
bluesky: (optional) [bluesky page]
linkedin: (optional) [LinkedIn profile]
position: [The person's position in the lab]
next_position: (optional) [If the person has left the lab, specify the next position]
---
   ```

   If the `next_position` field is defined, the person would be moved to the "Alumni" page.

1. Add the person's qualification and (optional) self introduction below the metadata.

<a id="command_line"></a>

## How to edit and preview the content in Linux?

The following steps needs a linux command line.

1. Refer to [this documentation](https://jekyllrb.com/docs/) (first 2 steps) to install all the prerequisites.

1. Clone your **forked repository** to your computer. Navigate to the folder.

   ```bash
cd csb5-page.github.io/
   ```

1. Build the website using

   ```bash
bundle exec jekyll serve
   ```

1. Open your favourite web browser and enter

   ```bash
http://localhost:4000
   ```

   to view the built webpage.

1. After you update a file, click Ctrl+S to save the file, and refresh to see the updated webpage.
1. Use `git commit` to save your edits, and

   ```bash
git push origin main
   ```

   to push your edits to your forked branch. Create a pull request in the GitHub webpage, so that your edits are deployed.