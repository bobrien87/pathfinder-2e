---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 20}"
usage: "affixed-to-firearm"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a firearm

**Activate** a (concentrate)

**Requirements** You're trained in Intimidation.

This wide strip of treated lizard hide is wrapped around the grip or stock of the affixed weapon, augmenting the unease that your gunshot creates. When you activate it, you fire your gun into the air with the effects of [[Warning Shot]]. If you already have the Warning Shot feat, the target doesn't become temporarily immune to your Demoralize, potentially allowing you to Demoralize them again.

**Source:** `= this.source` (`= this.source-type`)
