---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 85}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

This wooden whistle is stuffed with cotton and carved with images of bellowing stags, howling wolves, and chirping birds. You can blow on this whistle to use it as a catalyst when casting an [[Animal Form]] spell. When you do, you retain the ability to speak.

Once during the spell's duration, you can cast either a spell of 4th-rank or lower or a cantrip of any level, ignoring the inability to cast spells while in your battle form.

**Source:** `= this.source` (`= this.source-type`)
