---
marp: true
theme: base
size: 16:9
fontsize: 12px;
style: |
  section::after {
    content: 'Слайд ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
  }


  h1 {
    color: 	rgb(40, 190, 70);
  }
  
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  
  .columns3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }

  .small-text {
    font-size: 1.45rem;
  }
  .headerless {
        display: none;
    }

---

<style>
section {
  font-family: 'Roboto', 'Segoe UI', 'Liberation Sans', 'Helvetica', 'Arial', sans-serif !important;
  font-size: 1.55rem;
  padding: 3.5rem;
  justify-content: start;
}
</style>

![bg left](sectiongk.jpeg)

![w:520](logoclr.png)

<br>
<br>

# Python для задач химической технологии



## Лекция №3 - Введение в бибилиотеку NumPy
<br>
<br>
Вячеслав Алексеевич Чузлов

к.т.н., доцент ОХИ ИШПР ТПУ 

---

<style scoped>
  section {
    justify-content: center;
    font-size: 30px
  }
</style>

![bg](contentinteriorw.jpeg)

# Описание функций

<!-- _paginate: skip -->


---


<!-- paginate: true -->


# Написание кода функций

<pre><code>console.log(`Hello, highlight.js!`);
console.log(`Formatting Markdown code blocks!`);
const add = (a: number, b: number) => a + b
add(2, 3) // Returns 5
</code></pre>

<!-- Load highlight.js from a CDN -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>

<!-- Optionally load a template from a CDN -->
<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/atom-one-light.min.css" integrity="sha512-o5v54Kh5PH0dgnf9ei0L+vMRsbm5fvIvnR/XkrZZjN4mqdaeH7PW66tumBoQVIaKNVrLCZiBEfHzRY4JJSMK/Q==" crossorigin="anonymous" referrerpolicy="no-referrer" /> -->

<!-- Initialize highlight.js -->
<script>hljs.initHighlightingOnLoad();</script>

<mark> Hello there</mark>

^^more highlight^^

```c++
void main() {
    return 0
}
```



---

<style scoped>
  section {
    justify-content: center;
    font-size: 30px
  }
</style>

<!-- _paginate: skip -->
![bg right opacity:.3](sectiongk.jpeg)

![w:520](logoclr.png)

<br>
<br>

# Благодарю за внимание!

<br>
<br>

Вячеслав Алексеевич Чузлов
к.т.н., доцент ОХИ ИШПР
