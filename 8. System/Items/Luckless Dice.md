---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Cursed]]", "[[Magical]]", "[[Misfortune]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved of bone, luckless dice appear to be a set of loaded dice. If unsuccessfully identified as cursed, luckless dice seem to hold a minor enchantment that improves your luck. However, they fuse to you when you use them, cursing you with ill fortune. Luckless dice don't grant a bonus on Games Lore checks. Instead, when you use them to gamble, the GM rolls secretly, granting you the lower result. Once you realize the dice are cursed, the GM can instead allow you to roll twice and take the lower result.

**Source:** `= this.source` (`= this.source-type`)
