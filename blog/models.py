from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# recipe model: Handles the recipe posts
class Recipe(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='recipe_posts')
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='recipes')
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES, default='draft')

    @property
    def number_of_ratings(self):
        return self.ratings.count()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
    # average rating method: Calculates the average rating of a recipe
    @property
    def average_rating(self):
        ratings = Rating.objects.filter(recipe=self)
        total_ratings = ratings.count()
        if total_ratings > 0:
            total_stars = sum([rating.stars for rating in ratings])
            return total_stars / total_ratings
        else:
            return 0
    
    
# rating model: Handles the ratings, ensures that a user can only rate a
# recipe once
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='ratings')
    STAR_CHOICES = [(i, i) for i in range(1, 6)]
    stars = models.IntegerField(choices=STAR_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'recipe']]

    def __str__(self):
        return f'{self.recipe.title} - {self.user.username} - {self.stars}'
    

# comment model
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    @property
    def like_count(self):
        return self.commentlike_set.count()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.recipe.title} - {self.user.username}'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'comment'),)


# favorite model
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorites')

    class Meta:
        unique_together = [['user', 'recipe']]

    def __str__(self):
        return f'{self.recipe.title} - {self.user.username}'


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name