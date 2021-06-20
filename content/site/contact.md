---
title: "お問い合わせ"
date: 2020-06-06T14:00:09+09:00
draft: false
tags: ["その他"]
description : "お問い合わせのページです"
card : "summary_large_image"
card : "summary_large_image"
imgUrl : "/images/default.JPG"
imgUrlWebP : "/images/default.webp"
---
<style>
main #blog_main form[name="contact"] p {margin: 5px 0 1px 0;}
main #blog_main form[name="contact"] input,
main #blog_main form[name="contact"] textarea {
    width: calc(100% - 4px);
    padding: 2px;
    font-size: 1.2rem;
    border: solid 1.5px #afafaf;
    border-radius: 2px;
}
main #blog_main form[name="contact"] textarea {resize: vertical; height: 100px;}
main #blog_main form[name="contact"] button {width: 100px; border: solid 1px #121212; background-color: transparent; display: block; margin: 0 auto; padding: 5px 15px; border-radius: 10px; font-size: 1.1rem;}
</style>
お問い合わせは以下のフォームまたはcontact[at]shiga-info.netまたはページ下部の専門メールアドレスまでお願いします。  
(ご連絡の際は[at]を@に置き換えてご利用ください。)

## フォーム

<form name="contact" netlify>
  <input type="hidden" name="form-name" value="contact">
  <p>お名前</p>
  <input type="text" name="name" required>
  <p>返信用メール</p>
  <input type="email" name="email" required>
  <p>お問い合わせ内容</p>
  <textarea name="message" required></textarea>
  <div></div>
  <button type="submit">Send</button>
</form>

## その他専門メールアドレス

|担当|アドレス|
|--------|---------|
|お問い合わせ全般|contact[at]shiga-info.net|
|広報に関するお問い合わせ|pr[at]shiga-info.net|
|滋賀Free広告に関するお問い合わせ|ads[at]shiga-info.net|
|開発に関するご相談|dev[at]shiga-info.net|
|記事や内容に関するお問い合わせ|support[at]shiga-info.net|

(ご連絡の際は[at]を@に置き換えてご利用ください。)