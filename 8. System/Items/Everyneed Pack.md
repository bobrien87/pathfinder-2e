---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 20}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Constructed of green material and decorated with a white Glyph of the Open Road, an *everyneed pack* has a dozen or more small pockets lining the inside. The pack is enchanted so that each pocket contains common, mundane gear, each item worth no more than 1 gp, such as chalk, flint and steel, and string. It doesn't contain any armor, shields, weapons, or items made of precious material. Keep track of the exact value of the gear you retrieve from the pack. The pack becomes a mundane backpack after items of your choice with a combined value of 8 gp have been removed from it.

**Activate** 1 minute (manipulate)

**Frequency** once per hour

**Effect** You draw any number of pieces of mundane gear from the pack with a combined value of 1 gp or less.

**Source:** `= this.source` (`= this.source-type`)
