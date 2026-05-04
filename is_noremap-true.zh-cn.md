Q: What is `noremap = true` in `vim.keymap.set`? Do I have to set it?

A(译): 在Vim中，`noremap`选项用于指定映射不应递归。当在`vim.keymap.set`函数中将`noremap = true`设置时，它会防止该映射调用可能具有相同按键序列的其他映射。

以下是选项的详细说明：

- **noremap**：如果设置为`true`，该映射将不会递归调用其他映射。这在您想确保映射行为一致且不受可能使用相同按键组合的其他映射影响时非常有用。

- 如果未设置`noremap`（或设置为`false`），则该映射可以是递归的。这意味着如果您创建一个有效调用另一个映射的映射，第二个映射也可能会被执行。

是否需要设置`noremap = true`取决于您的具体使用场景。如果您希望您的映射简单明了且不受其他映射的影响，您应使用`noremap = true`。如果您有一种情况希望该映射可以调用其他映射，则可以省略此设置或将其设置为`false`。

例如：

```lua
-- 非递归映射：
vim.keymap.set('n', '<leader>e', ':e<CR>', { noremap = true })

-- 递归映射；如果不小心可能会引发问题：
vim.keymap.set('n', '<leader>e', ':e<CR>', { noremap = false })
```

总之，虽然您并不一定要设置`noremap = true`，但通常建议这样做，以避免由于递归映射引起的意外行为。

[GPT-4o mini]