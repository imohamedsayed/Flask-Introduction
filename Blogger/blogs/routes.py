from flask import Blueprint, redirect, url_for, render_template, flash, request, abort
from flask_login import current_user, login_required
from Blogger.blogs.forms import BlogForm, UpdateBlogForm
from Blogger.models import Blog
from Blogger import db

blogs = Blueprint("blogs", __name__)


@blogs.route("/blog/add", methods=["GET", "POST"])
@login_required
def addBlog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(
            title=form.title.data, content=form.content.data, user_id=current_user.id
        )
        db.session.add(blog)
        db.session.commit()
        flash(f"Blog added successfully", "success")
        return redirect(url_for("blogs.get_blogs"))
    return render_template("add_blog.html", title="Add Blog", form=form)


@blogs.route("/blogs", methods=["GET"])
@login_required
def get_blogs():
    blogs_res = current_user.blogs

    return render_template("blogs.html", title="Blogs", blogs=blogs_res)


@blogs.route("/blog/<int:blogId>/update", methods=["GET", "POST"])
@login_required
def updateBlog(blogId):
    form = UpdateBlogForm()
    blog = Blog.query.get_or_404(blogId)
    if blog.author != current_user:
        abort(403)

    if request.method == "GET":
        form.title.data = blog.title
        form.content.data = blog.content

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash(f"Blog updated successfully", "success")
        return redirect(url_for("blogs.get_blogs"))

    return render_template(
        "update_blog.html", title="Update Blog", blog=blog, form=form
    )


@blogs.route("/blog/<int:blogId>/delete", methods=["GET"])
def deleteBlog(blogId):
    blog = Blog.query.get_or_404(blogId)
    if blog.author != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash(f"blog {blog.title} deleted successfully ", "success")
    return redirect(url_for("blogs.get_blogs"))
