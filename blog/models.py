from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings

class Carousel(models.Model):
    """
    Carousel model for storing carousel images,headings, and captions(content)
    """
    image = CloudinaryField('carousel_image', default='placeholder')
    heading = models.CharField(max_length=250)
    caption = models.TextField()

    def __str__(self):
        """
        Return a string representation of the carousel model which includes the heading
        """
        return self.heading


class Recipe(models.Model):
    """
    Recipe model for creating, storing, and managing recipe posts. Includes information such as title, author, slug, created_date, updated_date, content, featured_image, excerpt, category, and status
    """
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
        """
        Returns the number of ratings a recipe has received
        """
        return self.ratings.count()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        """
        Returns a string representation of the recipe model which includes the title
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the url for a recipe detail page
        """
        return reverse('recipe_detail', kwargs={'slug': self.slug})
    
    
    @property
    def average_rating(self):
        """
        Calculate and return the average rating for a recipe
        """
        ratings = self.ratings.all()
        total_ratings = ratings.count()
        if total_ratings > 0:
            total_stars = sum([rating.stars for rating in ratings])
            return total_stars / total_ratings
        else:
            return 0
    
    

class Rating(models.Model):
    """
    Rating model for recrding a user's rating of a recipe. Ensures a user can only rate a recipe once
    """
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
        """
        Returns a string representation of the rating model which includes the recipe title, user, and rating
        """
        return f'{self.recipe.title} - {self.user.username} - {self.stars}'
    

# comment model
class Comment(models.Model):
    """
    Comment model for storing a user's comment on recipes. Includes information about the recipe, commenter's name, email, and the comment itself"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    
    @property
    def like_count(self):
        """
        Returns the number of likes a comment has received
        """
        return self.likes.count()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string representation of the comment model which includes the recipe title and commenter's user name.
        """
        return f'{self.recipe.title} - {self.user.username}'


class CommentLike(models.Model):
    """
    CommentLike model for storing a user's like on a comment. Ensures a user can only like a comment once"""
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'comment'),)


# favorite model
class Favorite(models.Model):
    """
    Model for tracking a user's favorite recipes.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorited_by')

    class Meta:
        unique_together = [['user', 'recipe']]

    def __str__(self):
        """
        Returns a string representation of the favorite model which includes the recipe title and user name of who favorited the recipe.
        """
        return f'{self.recipe.title} - {self.user.username}'


class Category(models.Model):
    """
    Category model for organizing recipes into various categories. Includes information such as name, slug, image, and description
    """
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically create a slug when a category is created
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the category model which is just its name"""
        return self.name