from django.db import models
from datetime import datetime
import re
import markdown
from pypinyin import lazy_pinyin
# Create your models here.

class Tag(models.Model):

    name = models.CharField("名称",max_length=255)
    slug = models.SlugField(unique=True, max_length=100, editable=False)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        ordering = ['name', 'id']

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        title = self.name.replace(' ', '_').lower()
        title = re.sub(r'\W+', '', title)
        name_pinyin = lazy_pinyin(title)
        self.slug = '_'.join(name_pinyin)[:100]
        super(Tag, self).save(*args, **kwargs)

    def get_post_count(self):
        return self.post_set.prefetch_related().count()

class Category(models.Model):

    name = models.CharField("名称",max_length=255)
    slug = models.SlugField(unique=True, max_length=100, editable=False)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name
        ordering = ['name', 'id']

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        title = self.name.replace(' ', '_').lower()
        title = re.sub(r'\W+', '', title)
        name_pinyin = lazy_pinyin(title)
        self.slug = '_'.join(name_pinyin)[:100]
        super(Category, self).save(*args, **kwargs)

    def get_post_count(self):
        return self.post_set.select_related().count()

class Post(models.Model):

    md = markdown.Markdown(output_format='html5', extensions=['fenced_code', 'codehilite', 'tables'],
                           extension_configs={
                               'codehilite': {
                                    'linenums': False,      # 行号在github-markdown-css下显示效果不太好
                                    'guess_lang': False     # 代码猜测不够准确
                                }
                           })
    owner = ((True, '原创'), (False, '转载'))
    publish = ((True, '发布'), (False, '草稿'))

    title = models.CharField("标题",max_length=255)
    content = models.TextField("内容")
    slug = models.SlugField(unique=True, max_length=100, editable=False)
    timestamp = models.DateTimeField('时间戳', default=datetime.now, db_index=True)
    tags = models.ManyToManyField(Tag,verbose_name="标签")
    category = models.ForeignKey(Category,null=True,verbose_name="类别",on_delete=models.CASCADE)
    read_num = models.IntegerField('阅读次数', default=0, editable=False)
    own = models.BooleanField('属性', choices=owner, default=True)
    published = models.BooleanField('状态', choices=publish, default=False)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-timestamp', 'id']
        unique_together = ('title', 'category')

    def get_tags(self):
        return ','.join([str(t) for t in self.tags.all()])

    def get_tags_slug(self):
        slugs = []
        for t in self.tags.all():
            for s in self.tags.filter(name=t).values('slug'):
                slugs.append(s['slug'])
        return ','.join(slugs)

    def __str__(self):
        return '%s' % self.title

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(self,*args,**kwargs)

    def save(self, *args, **kwargs):
        """
        自动生成拼音slug
        """
        # 空格转下划线
        title = self.title.replace(' ', '_').lower()
        # 去除转载等标识
        type_index = title.find(']')
        if type_index > 0:
            title = title[type_index + 1:]
        # 删除非单词字符
        title = re.sub(r'\W+', '', title)
        # 汉字转拼音
        name_pinyin = lazy_pinyin(title)
        self.slug = '_'.join(name_pinyin)[:100]
        super(Post, self).save(*args, **kwargs)

    def get_html_content(self):
        return self.md.reset().convert(self.content)

    def get_synopsis(self):
        """
        生成文章摘要
        """
        synopsis = []
        word_num = 0
        code_area = False
        for line in self.content.splitlines(keepends=True):
            if line.startswith('```'):      # 跳过代码段
                code_area = not code_area
            if code_area:
                continue

            if re.match(r'\w+', line):
                synopsis.append(line)
                word_num += len(re.findall(r'[A-Za-z0-9:/.]+|[\u4e00-\u9fa5]', line))  # 计数，网址等算为一个字
            if word_num > 30 or len(synopsis) > 3:  # 30字以上或4个段落
                break

        synopsis = ''.join(synopsis)

        return self.md.reset().convert(synopsis)
