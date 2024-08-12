<div align="center">

  # ✨ .dotfiles

  <sub>My current dotfiles. I only really use this to sync my config files and share wallpapers atm.</sub>

  <img src="./desktop_showcase_2.png">

  <br>

</div>

Hi this is Goldy and this is where I store my Linux dotfiles. Nothing really special here though, just some configs and wallpapers I like carrying around different systems but my dotfiles are public just in case anyone wants anything from it.

I've designed the repo in such a way you can just pick and choose what you wanna add to your existing system. I recommend [GNU stow](https://www.gnu.org/software/stow/) to achieve this. 

For example, you want my fastfetch and kitty config? CD into my repo and symlink them with `stow`:
```sh
stow kitty fastfetch
```

<img width="600px" src="./terminal_showcase.png">

Then if you want to remove them, run this:
```sh
stow -D kitty fastfetch
```

and etc etc...

## Wallpapers
<img width="800px" src="./wallpaper_example.jpg">

```sh
git submodule init && git submodule update
stow wallpapers
```
> They should be in your ~/Pictures folder now.

If I add new wallpapers at [my wallpapers repo](https://github.com/THEGOLDENPRO/wallpapers) and you would also like them just update the submodule like so:
```sh
git submodule update --remote
```